#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
####################################################
#
# PRISM - Pipeline for animation and VFX projects
#
# www.prism-pipeline.com
#
# contact: contact@prism-pipeline.com
#
####################################################
#
#
# Copyright (C) 2016-2023 Richard Frangenberg
# Copyright (C) 2023 Prism Software GmbH
#
# Licensed under GNU LGPL-3.0-or-later
#
# This file is part of Prism.
#
# Prism is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Prism is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Prism.  If not, see <https://www.gnu.org/licenses/>.
###########################################################################
###########################################################################
#
#                    Gimp Integration for Prism2
#
#       https://github.com/AltaArts/Gimp_Integration--Prism-Plugin
#
#
#                           Joshua Breckeen
#                              Alta Arts
#                          josh@alta-arts.com
#
###########################################################################

###########################################################################
#
#   GIMP Bridge plugin for Prism integration.
#
#   Runs as a GIMP 3 persistent procedure. Responsibilities:
#     - Registers Prism menu procedures visible inside GIMP
#     - Hosts a socket server (PrismGimpBridgeService) that receives
#       commands from the external Prism host process
#     - Dispatches GIMP API calls on the main thread: open/save scene,
#       thumbnail capture, image export, state parasites, dirty marking
#     - Launches and monitors Prism_Host.py (the external Qt/PrismCore
#       process) on demand
#



import json
import os
import socket
import sys
import threading
import time
import subprocess
import traceback
import base64
from typing import Any


import gi

gi.require_version("Gimp", "3.0")

from gi.repository import Gimp, GLib, Gio

import Prism_Helper as Helper


PRISM_ROOT = r"@PRISMROOTREPLACE@"
MENU_ROOT = "<Image>/Prism"
HOST_SCRIPT_NAME = "Prism_Host.py"


#   Conversion dict for Gimp Image Codes
COLORMODEDATA = {
    100: {"display": "8-bit Integer", "gamma": "Linear"},
    150: {"display": "8-bit Integer", "gamma": "sRGB"},
    200: {"display": "16-bit Integer", "gamma": "Linear"},
    250: {"display": "16-bit Integer", "gamma": "sRGB"},
    300: {"display": "32-bit Integer", "gamma": "Linear"},
    350: {"display": "32-bit Integer", "gamma": "sRGB"},
    500: {"display": "16-bit Half Float", "gamma": "Linear"},
    550: {"display": "16-bit Half Float", "gamma": "sRGB"},
    600: {"display": "32-bit Float", "gamma": "Linear"},
    650: {"display": "32-bit Float", "gamma": "sRGB"},
}



######################################################
#   Shared Runtime for the in-Gimp Bridge Service    #
######################################################
class PrismGimpBridgeServiceRuntime:
    def __init__(self):
        self.loadSettings()
        self.bridgeHost = "127.0.0.1"
        self.logLock = threading.Lock()
        self.logComponent = "BRIDGE"
        Helper.rotateLog(self.settings, self.logLock)


    def loadSettings(self) -> None:
        self.settings = Helper.loadSettings()
        self.bridgePort_in = self.settings["bridgePort_in"]
        self.log_maxBytes = self.settings["log_maxBytes"]


    #   Summarizes a Bridge Request for Logging
    def summarizeRequest(self, request) -> dict:
        if not isinstance(request, dict):
            return {"request_type": type(request).__name__}

        return {
            "action": request.get("action") or request.get("command"),
            "keys": sorted(request.keys()),
        }


    #   Gets Bridge Incoming Port, Allowing Environment Override
    def getBridgePort_in(self) -> int:
        try:
            return int(os.environ.get("PRISM_GIMP_BRIDGE_PORT_IN", self.bridgePort_in))
        except Exception:
            return self.bridgePort_in


    #   Adds a Line to the Shared Log  (pass component="GIMP" for Gimp-internal messages)
    def addToLog(self, message:str, component:str=None, **fields) -> None:
        with self.logLock:
            with open(Helper.getLogPath(), "a", encoding="utf-8") as handle:
                handle.write(Helper.formatLogLine(message, component or self.logComponent, **fields))


    #   Writes a Header for a New Gimp Session
    def writeSessionHeader(self, procedureName:str) -> None:
        try:
            with self.logLock:
                with open(Helper.getLogPath(), "a", encoding="utf-8") as handle:
                    handle.write("\n\n")
                    handle.write(
                        Helper.formatLogLine(
                            "===== New GIMP Session Started =====",
                            self.logComponent,
                            procedure=procedureName,
                        )
                    )
        except Exception:
            pass



######################################################
#   Persistent Bridge Service Running Inside Gimp    #
######################################################
class PrismGimpBridgeService:
    def __init__(self, procedure, ensurePrismHostRunning=None):
        self.runtime = BRIDGE_RUNTIME

        self.procedure = procedure
        self.plugIn = procedure.get_plug_in()

        self.ensurePrismHostRunning = ensurePrismHostRunning

        self.host = "127.0.0.1"
        self.port = self.runtime.getBridgePort_in()
        self.serverSocket = None

        self.serverThread = None

        self.mainLoop = GLib.MainLoop()
        self.shutdownEvent = threading.Event()

        self.started = False

        self.sceneDirtyFallbackByImageId = {}

        self.runtime.writeSessionHeader(self.procedure.get_name())
        self.addToLog("Initialized Prism Bridge service", host=self.host, port=self.port, procedure=self.procedure.get_name())


    ##############################
    ##        LOGGING           ##
    ##############################

    #   Adds a Line to the Log Using Shared Bridge Runtime
    def addToLog(self, message, component=None, **fields):
        try:
            self.runtime.addToLog(message, component=component, **fields)
        except Exception:
            pass


    #   Emits a Warning to both Gimp's Message Console and Prism log
    def emitGimpWarning(self, message, **fields):
        warning_text = str(message)

        gimpMessenger = getattr(Gimp, "message", None)
        if callable(gimpMessenger):
            try:
                gimpMessenger(f"PRISM BRIDGE: {warning_text}")

            except Exception:
                pass

        self.addToLog(warning_text, component="GIMP", level="warning", **fields)


    ###################################################
    ##        GIMP BRIDGE COMMAND LISTENER           ##
    ###################################################

    #   Starts the Bridge Socket Server
    def start(self):
        if self.started:
            self.addToLog("Bridge start requested but service is already running")
            return

        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serverSocket.bind((self.host, self.port))
        self.serverSocket.listen(5)
        self.serverSocket.settimeout(0.5)

        self.serverThread = threading.Thread(target=self.runServer, name="PrismGimpBridge", daemon=True)
        self.serverThread.start()
        self.started = True

        self.addToLog("Bridge socket server listening", host=self.host, port=self.port, thread_name=self.serverThread.name)

        if self.ensurePrismHostRunning:
            try:
                self.ensurePrismHostRunning()
            except Exception as exc:
                self.addToLog("Prism Host startup failed during Bridge startup", error=str(exc))


    #   Stops the Bridge Service
    def stop(self):
        self.addToLog("Stopping Bridge service")
        self.shutdownEvent.set()

        if self.serverSocket:
            try:
                self.serverSocket.close()
            except Exception:
                pass
            self.serverSocket = None

        if self.mainLoop.is_running():
            self.mainLoop.quit()

        self.addToLog("Bridge service stopped")
        return False


    #   Runs the Bridge Service Main Loop
    def run(self):
        self.start()
        self.procedure.persistent_ready()
        self.plugIn.persistent_enable()

        self.mainLoop.run()
        self.addToLog("Bridge main loop exited")


    #   Server Loop Accepting Incoming Host Requests
    def runServer(self):
        while not self.shutdownEvent.is_set():
            try:
                client, _address = self.serverSocket.accept()
            except socket.timeout:
                continue
            except OSError:
                self.addToLog("Bridge server socket closed or errored during accept")
                break

            with client:
                client.settimeout(1)

                try:
                    rawData = client.recv(65536)
                    if not rawData:
                        continue

                    request = json.loads(rawData.decode("utf-8"))
                    response = self.dispatchRequest(request)

                except Exception as exc:
                    self.addToLog("Bridge request handling failed before dispatch", error=str(exc))
                    response = {
                        "ok": False,
                        "error": str(exc),
                        "traceback": traceback.format_exc(),
                    }

                try:
                    client.sendall(json.dumps(response).encode("utf-8"))
                    if not response.get("ok"):
                        request_action = None
                        if isinstance(request, dict):
                            request_action = request.get("action") or request.get("command")

                        self.addToLog(
                            "Bridge response reported failure",
                            action=request_action,
                            error=response.get("error"),
                        )
                except Exception:
                    self.addToLog("Failed to send Bridge response")

        self.addToLog("Bridge Server thread exiting")


    ###################################################
    ##                COMMUNICATIONS                 ##
    ###################################################

    #   Dispatches a Bridge Request on Gimp Main Thread and Waits for Completion
    def dispatchRequest(self, request):
        completed = threading.Event()
        responseHolder = {}

        def executeRequest():
            try:
                responseHolder["response"] = self.handleRequest(request)
            except Exception as exc:
                responseHolder["response"] = {
                    "ok": False,
                    "error": str(exc),
                    "traceback": traceback.format_exc(),
                }
            finally:
                completed.set()

            return False

        GLib.idle_add(executeRequest)
        completed.wait()

        response = responseHolder.get("response") or {}
        if not response.get("ok"):
            self.addToLog(
                "Bridge request failed",
                **self.runtime.summarizeRequest(request),
                error=response.get("error"),
            )

        return responseHolder["response"]


    #   Handles a Single Parsed Bridge Request
    def handleRequest(self, request):
        action = request.get("action") or request.get("command")
        requestData = request.get("data") if isinstance(request.get("data"), dict) else {}

        match action:

            case "ping":
                return {
                    "ok": True,
                    "data": {
                        "bridge": "gimp",
                        "host": self.host,
                        "port": self.port,
                    },
                }

            case "get-bridge-status":
                return {
                    "ok": True,
                    "data": {
                        "bridge": "gimp",
                        "autoStarted": True,
                        "host": self.host,
                        "port": self.port,
                        "procedure": self.procedure.get_name(),
                    },
                }

            case "shutdown-bridge":
                self.addToLog("Received bridge shutdown request")
                GLib.idle_add(self.stop)
                return {"ok": True}

            case "get-current-file-name":
                return self.getCurrentFile()

            case "get-app-version":
                return self.getAppVersion()

            case "open-scene":
                return self.openScene(requestData)

            case "save-scene":
                return self.saveScene(requestData)

            case "get-thumbnail":
                return self.getThumbnail(requestData)

            case "get-image-specs":
                return self.getImageSpecs()

            case "export-image":
                return self.exportImage(requestData)

            case "save-states":
                return self.saveStates(requestData)

            case "mark-scene-dirty":
                return self.markSceneDirty(requestData)

            case "get-states":
                return self.getStates()

            case _:
                self.addToLog("Received unknown Bridge action", action=action)
                return {
                    "ok": False,
                    "error": "Unknown bridge action: %s" % action,
                }



    ###########################################
    ##               GIMP API                ##
    ###########################################

    #   Returns the Gimp Version for Host Queries
    def getAppVersion(self):
        version_value = None

        #   Direct API first.
        version_getter = getattr(Gimp, "version", None)
        if callable(version_getter):
            try:
                version_value = version_getter()
            except Exception:
                version_value = None

        #   PDB fallback when direct API is unavailable.
        if version_value is None:
            get_pdb = getattr(Gimp, "get_pdb", None)
            if callable(get_pdb):
                try:
                    pdb = get_pdb()
                except Exception:
                    pdb = None

                if pdb is not None:
                    lookup = getattr(pdb, "lookup_procedure", None)
                    if callable(lookup):
                        try:
                            proc = lookup("gimp-version")
                        except Exception:
                            proc = None

                        if proc:
                            try:
                                cfg = proc.create_config()
                                result = proc.run(cfg)
                                version_value = str(result)
                            except Exception:
                                version_value = None

        if version_value is None:
            return {"ok": True, "data": {"version": None}}

        return {"ok": True, "data": {"version": str(version_value)}}


    #   Converts a filesystem path to Gio.File
    def getGioFile(self, filePath:str) -> object | None:
        try:
            return Gio.File.new_for_path(filePath)
        except Exception:
            return None


    #   Returns a PDB Procedure by Name
    def getPdbProcedure(self, procedureName:str) -> object | None:
        get_pdb = getattr(Gimp, "get_pdb", None)
        if not callable(get_pdb):
            return None

        try:
            pdb = get_pdb()
        except Exception:
            return None

        if pdb is None:
            return None

        lookup = getattr(pdb, "lookup_procedure", None)
        if not callable(lookup):
            return None

        try:
            return lookup(procedureName)
        except Exception:
            return None


    #   Sets a PDB Config Property
    def setConfigValue(self, config:object, key:Any, value:Any) -> None:
        if value is None:
            return

        try:
            config.set_property(key, value)
        except Exception:
            pass


    #   Tries a Callable with Several Arg Signatures
    def callWithSignatures(self, func, signatures):
        errors = []

        for args in signatures:
            try:
                return func(*args), None
            except Exception as exc:
                errors.append(f"args={args}: {exc}")

        return None, "; ".join(errors)


    #   Runs a PDB Procedure with Config Key/Value Pairs
    def runPdbProcedure(self, procedureName, values):
        procedure = self.getPdbProcedure(procedureName)
        if not procedure:
            return None, f"Procedure not found: {procedureName}"

        try:
            config = procedure.create_config()
            for key, value in (values or {}).items():
                self.setConfigValue(config, key, value)

            result = procedure.run(config)
            values_flat = Helper.flattenValues(result)

            status_text = ""
            if values_flat:
                try:
                    status_text = str(values_flat[0])
                except Exception:
                    status_text = ""

            status_upper = status_text.upper()
            result_message = ""

            for value in values_flat[1:]:
                if isinstance(value, str) and value.strip():
                    result_message = value.strip()
                    break

            if result_message:
                self.emitGimpWarning(
                    f"PDB message from {procedureName}: {result_message}",
                    procedure=procedureName,
                    status=status_text or None,
                )

            if any(flag in status_upper for flag in ["CALLING_ERROR", "EXECUTION_ERROR", "CANCEL"]):
                details = result_message or status_text or "PDB call failed"
                return result, f"{procedureName} failed: {details}"

            return result, None
        except Exception as exc:
            return None, str(exc)


    ###################################################
    ##              GIMP RESULT PARSERS             ##
    ###################################################

    #   Extracts First Layer Object from GI/PDB Values
    def extractLayerFromResult(self, rawResult:Any) -> object | None:
        for value in Helper.flattenValues(rawResult):
            if value is None:
                continue

            has_name = callable(getattr(value, "get_name", None))
            has_alpha = callable(getattr(value, "has_alpha", None))
            has_mode = callable(getattr(value, "get_mode", None))
            if has_name and (has_alpha or has_mode):
                return value

        return None
    

    #   Extracts First Image-like Object from GI/PDB Values
    def extractImageFromResult(self, raw_result):
        for value in Helper.flattenValues(raw_result):
            if value is None:
                continue

            has_width = callable(getattr(value, "get_width", None))
            has_height = callable(getattr(value, "get_height", None))
            has_layers = callable(getattr(value, "get_layers", None))
            if (has_width and has_height) or has_layers:
                return value

        return None


    ##########################################
    ##              SCENE FILE              ##
    ##########################################

    #   Returns Active/Open Gimp Document Path/Name for Host Queries
    def getCurrentFile(self):
        image, _image_source = self.getCurrentImage()
        if image is None:
            return {
                "ok": True,
                "data": {
                    "path": None,
                    "name": None,
                },
            }

        file_path = self.getImageFilePath(image)
        file_name = None

        name_getter = getattr(image, "get_name", None)
        if callable(name_getter):
            try:
                name_value = name_getter()
                if name_value:
                    file_name = str(name_value)
            except Exception:
                pass

        if file_path and not file_name:
            file_name = os.path.basename(file_path)

        return {
            "ok": True,
            "data": {
                "path": file_path,
                "name": file_name,
            },
        }


    #   Opens an XCF Scene File in Gimp
    def openScene(self, request_data):
        file_path = request_data.get("path") if isinstance(request_data, dict) else None

        if not file_path:
            return {"ok": False, "error": "Missing file path"}

        file_path = os.path.normpath(str(file_path))
        gio_file = self.getGioFile(file_path)
        run_mode = getattr(Gimp.RunMode, "NONINTERACTIVE", None)

        procedure_name = "gimp-file-load"
        procedure = self.getPdbProcedure(procedure_name)

        if not procedure:
            return {"ok": False, "error": f"Required procedure not found: {procedure_name}"}

        try:
            config = procedure.create_config()
            self.setConfigValue(config, "run-mode", run_mode)
            self.setConfigValue(config, "file", gio_file)
            procedure.run(config)

            #   A newly opened scene should be treated as clean until edited.
            self.sceneDirtyFallbackByImageId.clear()

            self.addToLog("Opened scene in Gimp", path=file_path, procedure=procedure_name)
            return {"ok": True, "data": {"opened": True, "path": file_path, "procedure": procedure_name}}

        except Exception as exc:
            self.addToLog("Failed to open scene in Gimp", path=file_path, error=str(exc), procedure=procedure_name)
            return {"ok": False, "error": str(exc), "data": {"path": file_path, "procedure": procedure_name}}


    #   Saves the Current Gimp Image to an XCF Scene File
    def saveScene(self, request_data):
        image, _ = self.getCurrentImage()
        if image is None:
            return {"ok": False, "error": "No active image to save"}

        file_path = request_data.get("path") if isinstance(request_data, dict) else None
        if file_path:
            file_path = os.path.normpath(str(file_path))
        else:
            file_path = self.getImageFilePath(image)

        if not file_path:
            return {"ok": False, "error": "Missing file path"}

        active_drawable = None
        drawable_getter = getattr(image, "get_active_drawable", None)
        if callable(drawable_getter):
            try:
                active_drawable = drawable_getter()
            except Exception:
                active_drawable = None

        gio_file = self.getGioFile(file_path)
        run_mode = getattr(Gimp.RunMode, "NONINTERACTIVE", None)

        procedure_name = "gimp-file-save"
        procedure = self.getPdbProcedure(procedure_name)

        if not procedure:
            return {"ok": False, "error": f"Required procedure not found: {procedure_name}"}

        try:
            config = procedure.create_config()
            self.setConfigValue(config, "run-mode", run_mode)
            self.setConfigValue(config, "image", image)
            self.setConfigValue(config, "drawable", active_drawable)
            self.setConfigValue(config, "file", gio_file)
            procedure.run(config)

            #   Saving clears dirty state; clear fallback marker for this image.
            image_id = self.getImageId(image)
            if image_id in self.sceneDirtyFallbackByImageId:
                del self.sceneDirtyFallbackByImageId[image_id]

            self.addToLog("Saved scene in Gimp", path=file_path, procedure=procedure_name)
            return {"ok": True, "data": {"saved": True, "path": file_path, "procedure": procedure_name}}

        except Exception as exc:
            self.addToLog("Failed to save scene in Gimp", path=file_path, error=str(exc), procedure=procedure_name)
            return {"ok": False, "error": str(exc), "data": {"path": file_path, "procedure": procedure_name}}


    ##########################################
    ##               GIMP IMAGE             ##
    ##########################################

    #   Returns the Currently Active Image
    def getCurrentImage(self) -> tuple[object, str]:
        for getter_name in ["get_images", "list_images", "image_list"]:
            getter = getattr(Gimp, getter_name, None)
            if not callable(getter):
                continue

            try:
                images = Helper.normalizeGimpItems(getter())
            except Exception:
                images = []

            if images:
                return images[0], f"gimp.{getter_name}"

        for display_getter_name in ["get_displays", "list_displays", "display_list"]:
            display_getter = getattr(Gimp, display_getter_name, None)
            if not callable(display_getter):
                continue

            try:
                displays = Helper.normalizeGimpItems(display_getter())
            except Exception:
                displays = []

            for display in displays:
                image_getter = getattr(display, "get_image", None)
                if not callable(image_getter):
                    continue

                try:
                    display_image = image_getter()
                except Exception:
                    display_image = None

                if display_image:
                    return display_image, "gimp.display"

        return None, "none"


    #   Returns a Per-process ID for a Gimp Image Object
    def getImageId(self, image:object) -> int | None:
        if image is None:
            return None

        image_id_getter = getattr(image, "get_id", None)
        if callable(image_id_getter):
            try:
                image_id = int(image_id_getter())
                if image_id > 0:
                    return image_id
            except Exception:
                pass

        return id(image)


    #   Returns Gimp Image Dirty State
    def isImageDirty(self, image:object) -> bool | None:
        if image is None:
            return None

        for getter_name in ["is_dirty", "get_dirty"]:
            getter = getattr(image, getter_name, None)
            if callable(getter):
                try:
                    return bool(getter())
                except Exception:
                    continue

        dirty_value = getattr(image, "dirty", None)
        if isinstance(dirty_value, bool):
            return dirty_value

        return None


    #   Marks the Current Scene Dirty Once and Skips Work if Already Dirty
    def markSceneDirty(self, request_data=None):
        image, _ = self.getCurrentImage()
        if image is None:
            return {"ok": False, "error": "No active image to mark dirty"}

        force_mark = bool((request_data or {}).get("force")) if isinstance(request_data, dict) else False
        image_id = self.getImageId(image)

        if not force_mark:
            dirty_state = self.isImageDirty(image)
            if dirty_state is True:
                return {"ok": True, "data": {"dirtyMarked": False, "alreadyDirty": True, "reason": "image-api"}}

            if dirty_state is None and self.sceneDirtyFallbackByImageId.get(image_id):
                return {"ok": True, "data": {"dirtyMarked": False, "alreadyDirty": True, "reason": "fallback-cache"}}

        result = self._markSceneDirtyInternal(image)
        if result.get("ok"):
            if image_id is not None:
                self.sceneDirtyFallbackByImageId[image_id] = True
            result["data"] = {"dirtyMarked": True, "alreadyDirty": False}

        return result


    #   Performs a Tiny No-op Layer Add/Remove so Gimp Marks the Image Modified
    def _markSceneDirtyInternal(self, image):

        w, h = self.getImageSize(image)
        width = max(1, w) if w > 0 else 1
        height = max(1, h) if h > 0 else 1

        layer = None
        created_with_pdb = False
        inserted = False

        try:
            image_type_enum = getattr(getattr(Gimp, "ImageType", None), "RGBA_IMAGE", None)
            layer_mode_enum = getattr(getattr(Gimp, "LayerMode", None), "NORMAL", None)

            layer_new = getattr(getattr(Gimp, "Layer", None), "new", None)
            if callable(layer_new):
                signature_options = []

                if image_type_enum is not None and layer_mode_enum is not None:
                    signature_options.append((image, width, height, image_type_enum, "__PrismDirty__", 0.0, layer_mode_enum))

                signature_options.extend([
                    (image, width, height, 0, "__PrismDirty__", 0.0, 0),
                    (image, width, height, "RGBA", "__PrismDirty__", 0.0, "NORMAL"),
                ])

                layer, _ = self.callWithSignatures(layer_new, signature_options)

            if layer is None:
                pdb_values = {
                    "image": image,
                    "width": width,
                    "height": height,
                    "name": "__PrismDirty__",
                    "opacity": 0.0,
                }

                if image_type_enum is not None:
                    pdb_values["type"] = image_type_enum
                if layer_mode_enum is not None:
                    pdb_values["mode"] = layer_mode_enum

                result, error = self.runPdbProcedure("gimp-layer-new", pdb_values)
                if error:
                    return {"ok": False, "error": f"Failed to create temp layer: {error}"}

                layer = self.extractLayerFromResult(result)
                if layer is None:
                    return {"ok": False, "error": "Failed to parse temp layer from PDB result"}

                created_with_pdb = True

            undo_group_start = getattr(image, "undo_group_start", None)
            undo_group_end = getattr(image, "undo_group_end", None)
            undo_started = False

            if callable(undo_group_start) and callable(undo_group_end):
                try:
                    undo_group_start()
                    undo_started = True
                except Exception:
                    undo_started = False

            try:
                insert_layer = getattr(image, "insert_layer", None) or getattr(image, "add_layer", None)

                if callable(insert_layer):
                    _, insert_error = self.callWithSignatures(insert_layer, [
                        (layer, None, 0),
                        (layer, 0),
                        (layer,),
                    ])
                    if insert_error:
                        return {"ok": False, "error": f"Failed to insert temp layer: {insert_error}"}
                else:
                    _result, error = self.runPdbProcedure("gimp-image-insert-layer", {
                        "image": image,
                        "layer": layer,
                        "parent": None,
                        "position": 0,
                    })
                    if error:
                        return {"ok": False, "error": f"Failed to insert temp layer: {error}"}

                inserted = True

                remove_layer = getattr(image, "remove_layer", None)
                if callable(remove_layer):
                    _, remove_error = self.callWithSignatures(remove_layer, [
                        (layer,),
                    ])
                    if remove_error:
                        return {"ok": False, "error": f"Failed to remove temp layer: {remove_error}"}
                else:
                    _result, error = self.runPdbProcedure("gimp-image-remove-layer", {
                        "image": image,
                        "layer": layer,
                    })
                    if error:
                        return {"ok": False, "error": f"Failed to remove temp layer: {error}"}

                inserted = False
            finally:
                if undo_started:
                    try:
                        undo_group_end()
                    except Exception:
                        pass

            self.addToLog("Marked Gimp scenefile dirty")
            return {"ok": True}

        except Exception as exc:
            return {"ok": False, "error": str(exc)}

        finally:
            if inserted and layer is not None:
                try:
                    remove_layer = getattr(image, "remove_layer", None)
                    if callable(remove_layer):
                        remove_layer(layer)
                    else:
                        self.runPdbProcedure("gimp-image-remove-layer", {
                            "image": image,
                            "layer": layer,
                        })
                except Exception:
                    pass

            if created_with_pdb and layer is not None:
                try:
                    delete_layer = getattr(layer, "delete", None)
                    if callable(delete_layer):
                        delete_layer()
                except Exception:
                    pass


    #   Reads the Filesystem Path from an Image Object
    def getImageFilePath(self, image:object) -> str | None:
        if not image:
            return None

        file_getter = getattr(image, "get_file", None)
        if not callable(file_getter):
            return None

        try:
            file_obj = file_getter()
        except Exception:
            file_obj = None

        if not file_obj:
            return None

        path_getter = getattr(file_obj, "get_path", None)
        if not callable(path_getter):
            return None

        try:
            filePath = path_getter()
        except Exception:
            filePath = None

        if not filePath:
            return None

        return str(filePath)


    #   Returns Active Image Specs Needed by the Gimp_Export State UI
    def getImageSpecs(self):
        image, _ = self.getCurrentImage()
        if image is None:
            return {"ok": True, "data": {"imageSpecs": {}}}

        specs = {
            "xRez": 0,
            "yRez": 0,
            "colorMode": "Unknown",
            "bitDepth": "Unknown",
            "gamma": "Unknown",
            "hasAlpha": False,
        }

        specs["xRez"], specs["yRez"] = self.getImageSize(image)

        base_type = self.getImageBaseType(image)
        if base_type:
            specs["colorMode"] = {"GRAY": "Grayscale"}.get(base_type, base_type)

        precision_getter = getattr(image, "get_precision", None)
        if callable(precision_getter):
            try:
                precision_raw = precision_getter()
                precision_str = str(precision_raw)

                precision_int = None
                try:
                    precision_int = int(precision_raw)
                except Exception:
                    precision_int = None

                if precision_int in COLORMODEDATA:
                    specs["bitDepth"] = COLORMODEDATA[precision_int]["display"]
                    specs["gamma"] = COLORMODEDATA[precision_int]["gamma"]
                else:
                    precision_upper = precision_str.upper()
                    if "U8" in precision_upper:
                        specs["bitDepth"] = "8-bit Integer"
                    elif "U16" in precision_upper:
                        specs["bitDepth"] = "16-bit Integer"
                    elif "U32" in precision_upper:
                        specs["bitDepth"] = "32-bit Integer"
                    elif "HALF" in precision_upper or "F16" in precision_upper:
                        specs["bitDepth"] = "16-bit Half Float"
                    elif "FLOAT" in precision_upper or "F32" in precision_upper:
                        specs["bitDepth"] = "32-bit Float"
                    else:
                        specs["bitDepth"] = precision_str

                    specs["gamma"] = "Linear" if "LINEAR" in precision_upper else "sRGB"
            except Exception:
                pass

        specs["hasAlpha"] = self.imageHasAlpha(image)

        return {"ok": True, "data": {"imageSpecs": specs}}


    ###################################
    ##            THUMBNAIL          ##
    ###################################

    #   Captures a Thumbnail from the Active Gimp Image and Returns Raw Pixel Data
    def getThumbnail(self, request_data):
        image, _ = self.getCurrentImage()
        if image is None:
            return {"ok": False, "error": "No active image for thumbnail capture"}

        width = request_data.get("width") if isinstance(request_data, dict) else None
        height = request_data.get("height") if isinstance(request_data, dict) else None

        try:
            width = int(width) if width is not None else 512
        except Exception:
            width = 512

        try:
            height = int(height) if height is not None else 512
        except Exception:
            height = 512

        width = max(1, min(width, 4096))
        height = max(1, min(height, 4096))

        method_attempt_errors = []

        method_candidates = [
            ("get_thumbnail_data", [(width, height), (width, height, 4), (width, height, 3)]),
            ("get_thumbnail", [(width, height), (width, height, 0), (width, height, 1), (width, height, 2)]),
        ]

        for method_name, signatures in method_candidates:
            method = getattr(image, method_name, None)
            if not callable(method):
                continue

            raw_result, call_error = self.callWithSignatures(method, signatures)
            if raw_result is None:
                if call_error:
                    method_attempt_errors.append(f"{method_name}: {call_error}")
                continue

            parsed = self.parseThumbnailPayload(raw_result, width, height)
            if not parsed:
                parsed = self.parsePixbufPayload(raw_result)

            if parsed:
                self.addToLog("Captured thumbnail via image method", method=method_name, width=parsed["width"], height=parsed["height"], bpp=parsed["bpp"])
                return {
                    "ok": True,
                    "data": {
                        "width": parsed["width"],
                        "height": parsed["height"],
                        "bpp": parsed["bpp"],
                        "pixels": base64.b64encode(parsed["pixels"]).decode("ascii"),
                    },
                }

            method_attempt_errors.append(f"{method_name}: returned unrecognized payload")

        procedure_candidates = [
            "gimp-image-thumbnail",
            "gimp-image-get-thumbnail",
            "gimp-image-get-thumbnail-data",
        ]

        for procedure_name in procedure_candidates:
            procedure = self.getPdbProcedure(procedure_name)
            if not procedure:
                continue

            try:
                config = procedure.create_config()
                self.setConfigValue(config, "image", image)
                self.setConfigValue(config, "width", width)
                self.setConfigValue(config, "height", height)
                self.setConfigValue(config, "max-width", width)
                self.setConfigValue(config, "max-height", height)
                self.setConfigValue(config, "max_width", width)
                self.setConfigValue(config, "max_height", height)

                raw_result = procedure.run(config)
                parsed = self.parseThumbnailPayload(raw_result, width, height)
                if not parsed:
                    parsed = self.parsePixbufPayload(raw_result)

                if not parsed:
                    method_attempt_errors.append(f"{procedure_name}: returned unrecognized payload")
                    continue

                self.addToLog("Captured thumbnail via PDB", procedure=procedure_name, width=parsed["width"], height=parsed["height"], bpp=parsed["bpp"])
                return {
                    "ok": True,
                    "data": {
                        "width": parsed["width"],
                        "height": parsed["height"],
                        "bpp": parsed["bpp"],
                        "pixels": base64.b64encode(parsed["pixels"]).decode("ascii"),
                    },
                }

            except Exception as exc:
                method_attempt_errors.append(f"{procedure_name}: {exc}")

        # Return a detailed error so host can decide on fallback behavior.
        details = "; ".join(method_attempt_errors) if method_attempt_errors else "No compatible thumbnail APIs found"
        return {"ok": False, "error": f"Thumbnail APIs unavailable: {details}"}


    #   Parses Thumbnail API/PDB Return Payload into Width/Height/BPP/Bytes
    def parseThumbnailPayload(self, raw_result:object, fallback_width:int=0, fallback_height:int=0) -> dict | None:
        values = Helper.flattenValues(raw_result)

        ints = []
        pixel_bytes = b""

        for value in values:
            if value is None:
                continue

            if isinstance(value, bool):
                continue

            if isinstance(value, int):
                ints.append(value)
                continue

            converted = Helper.toBytes(value)
            if converted and not pixel_bytes:
                pixel_bytes = converted

        if not pixel_bytes:
            return None

        width = int(fallback_width or 0)
        height = int(fallback_height or 0)
        bpp = 0

        if len(ints) >= 3:
            width = max(width, int(ints[0]))
            height = max(height, int(ints[1]))
            bpp = int(ints[2])

        if bpp not in (3, 4):
            if width > 0 and height > 0:
                pixel_count = width * height
                if pixel_count > 0:
                    derived_bpp = len(pixel_bytes) // pixel_count
                    if derived_bpp in (3, 4):
                        bpp = derived_bpp

        if width <= 0 or height <= 0:
            if bpp in (3, 4) and fallback_width and fallback_height:
                expected = int(fallback_width) * int(fallback_height) * bpp
                if expected == len(pixel_bytes):
                    width = int(fallback_width)
                    height = int(fallback_height)

        if width <= 0 or height <= 0 or bpp not in (3, 4):
            return None

        expected_size = width * height * bpp
        if expected_size <= 0 or len(pixel_bytes) < expected_size:
            return None

        return {
            "width": width,
            "height": height,
            "bpp": bpp,
            "pixels": pixel_bytes[:expected_size],
        }


    #   Parses Pixbuf Thumbnail to Width/Height/BPP/Bytes
    def parsePixbufPayload(self, raw_result:object) -> dict | None:
        value = Helper.unpackValue(raw_result)

        if isinstance(value, (list, tuple)):
            for item in value:
                parsed = self.parsePixbufPayload(item)
                if parsed:
                    return parsed
            return None

        if value is None:
            return None

        width_getter = getattr(value, "get_width", None)
        height_getter = getattr(value, "get_height", None)
        channels_getter = getattr(value, "get_n_channels", None)
        rowstride_getter = getattr(value, "get_rowstride", None)
        pixels_getter = getattr(value, "get_pixels", None)

        if not (callable(width_getter) and callable(height_getter) and callable(channels_getter) and callable(pixels_getter)):
            return None

        try:
            width = int(width_getter())
            height = int(height_getter())
            bpp = int(channels_getter())
            rowstride = int(rowstride_getter()) if callable(rowstride_getter) else width * bpp
            raw_pixels = Helper.toBytes(pixels_getter())
        except Exception:
            return None

        if width <= 0 or height <= 0 or bpp not in (3, 4) or rowstride <= 0:
            return None

        tight_stride = width * bpp
        expected_row_data = rowstride * height
        if len(raw_pixels) < expected_row_data:
            return None

        if rowstride == tight_stride:
            pixels = raw_pixels[: tight_stride * height]
        else:
            rows = []
            for row_index in range(height):
                start = row_index * rowstride
                end = start + tight_stride
                rows.append(raw_pixels[start:end])
            pixels = b"".join(rows)

        return {
            "width": width,
            "height": height,
            "bpp": bpp,
            "pixels": pixels,
        }


    ##############################################
    ##              IMAGE OPERATIONS            ##
    ##############################################

    #   Duplicates an Image for Non-destructive Export Processing
    def duplicateImage(self, image):
        method = getattr(image, "duplicate", None)
        if callable(method):
            try:
                duplicated = method()
                if duplicated:
                    return duplicated, None
            except Exception:
                pass

        result, error = self.runPdbProcedure("gimp-image-duplicate", {"image": image})
        if error:
            return None, error

        duplicated = self.extractImageFromResult(result)
        if duplicated is None:
            return None, "Could not parse duplicated image result"

        return duplicated, None


    #   Deletes a Temporary Duplicated Image
    def deleteImage(self, image):
        if not image:
            return

        method = getattr(image, "delete", None)
        if callable(method):
            try:
                method()
                return
            except Exception:
                pass

        self.runPdbProcedure("gimp-image-delete", {"image": image})


    #   Returns Active Drawable for an Image
    def getActiveDrawable(self, image):
        drawable_getter = getattr(image, "get_active_drawable", None)
        if not callable(drawable_getter):
            return None

        try:
            return drawable_getter()
        except Exception:
            return None


    #   Returns Whether a Drawable Has Alpha Support
    def drawableHasAlpha(self, drawable):
        if drawable is None:
            return False

        for getter_name in ["has_alpha", "get_has_alpha"]:
            getter = getattr(drawable, getter_name, None)
            if callable(getter):
                try:
                    return bool(getter())
                except Exception:
                    continue

        return False


    #   Returns Whether Active Drawable Has Alpha
    def imageHasAlpha(self, image):
        #   Prefer active drawable first.
        if self.drawableHasAlpha(self.getActiveDrawable(image)):
            return True

        #   Fall back to scanning all layers/drawables in the image.
        for layers_getter_name in ["get_layers", "list_layers", "layers"]:
            layers_getter = getattr(image, layers_getter_name, None)
            if not callable(layers_getter):
                continue

            try:
                layers = Helper.normalizeGimpItems(layers_getter())

            except Exception:
                layers = []

            for layer in layers:
                if self.drawableHasAlpha(layer):
                    return True

        return False


    #   Returns Normalized Image Base Type for Color Conversion Checks
    def getImageBaseType(self, image):
        base_type_getter = getattr(image, "get_base_type", None)
        if not callable(base_type_getter):
            return None

        try:
            base_type_raw = base_type_getter()
        except Exception:
            return None

        base_type_str = str(base_type_raw).upper()

        base_type_int = None
        try:
            base_type_int = int(base_type_raw)
        except Exception:
            base_type_int = None

        if "RGB" in base_type_str or base_type_int == 0:
            return "RGB"
        if "GRAY" in base_type_str or base_type_int == 1:
            return "GRAY"
        if "INDEX" in base_type_str or base_type_int == 2:
            return "INDEXED"

        return base_type_str


    #   Returns Image Width and Height, Trying Multiple Getter Names
    def getImageSize(self, image) -> tuple[int, int]:
        w, h = 0, 0
        for attr in ["get_width", "width"]:
            getter = getattr(image, attr, None)
            if callable(getter):
                try:
                    w = int(getter())
                    break
                except Exception:
                    pass
        for attr in ["get_height", "height"]:
            getter = getattr(image, attr, None)
            if callable(getter):
                try:
                    h = int(getter())
                    break
                except Exception:
                    pass
        return w, h


    #   Converts Image Base Type to Match Requested Export Color Mode
    def convertImageColorMode(self, image, output_color_mode):
        requested_mode = str(output_color_mode or "").upper()
        if requested_mode in ("GRAY", "GRAYA"):
            target_base = "GRAY"
        elif requested_mode in ("RGB", "RGBA"):
            target_base = "RGB"
        else:
            return True, None

        current_base = self.getImageBaseType(image)
        if current_base == target_base:
            return True, None

        enum_container = getattr(Gimp, "ImageBaseType", None)
        target_enum = getattr(enum_container, target_base, None) if enum_container else None

        method_errors = []
        for method_name in ["convert_type", "convert_base_type", "convert"]:
            method = getattr(image, method_name, None)
            if not callable(method):
                continue

            arg_sets = []
            if target_enum is not None:
                arg_sets.append((target_enum,))
            arg_sets.append((target_base,))

            for args in arg_sets:
                try:
                    method(*args)
                    return True, None
                except Exception as exc:
                    method_errors.append(f"{method_name}{args}: {exc}")

        if target_base == "GRAY":
            proc_names = ["gimp-image-convert-grayscale", "gimp-image-convert-base-type"]
        else:
            proc_names = ["gimp-image-convert-rgb", "gimp-image-convert-base-type"]

        proc_errors = []
        for proc_name in proc_names:
            values = {"image": image}

            if proc_name == "gimp-image-convert-base-type":
                values.update(
                    {
                        "base-type": target_enum,
                        "base_type": target_enum,
                        "new-type": target_enum,
                        "new_type": target_enum,
                        "type": target_enum,
                    }
                )

            _result, error = self.runPdbProcedure(proc_name, values)
            if error is None:
                return True, None

            proc_errors.append(f"{proc_name}: {error}")

        all_errors = "; ".join(method_errors + proc_errors) if (method_errors or proc_errors) else "No compatible conversion API found"
        return False, all_errors


    #   Scales Image Dimensions by Percentage
    def scaleImagePercent(self, image, scale_percent):
        if scale_percent == 100:
            return True, None

        width, height = self.getImageSize(image)

        if width <= 0 or height <= 0:
            return False, "Could not resolve image dimensions for scaling"

        new_width = max(1, int(round(width * (scale_percent / 100.0))))
        new_height = max(1, int(round(height * (scale_percent / 100.0))))
        scale_method = getattr(image, "scale", None)
        if callable(scale_method):
            for args in [(new_width, new_height), (new_width, new_height, 0)]:
                try:
                    scale_method(*args)
                    return True, None
                except Exception:
                    continue

        proc_names = ["gimp-image-scale", "gimp-image-scale-full"]
        for proc_name in proc_names:
            _result, error = self.runPdbProcedure(proc_name, {
                "image": image,
                "new-width": new_width,
                "new-height": new_height,
                "new_width": new_width,
                "new_height": new_height,
                "width": new_width,
                "height": new_height,
                "interpolation": getattr(Gimp.InterpolationType, "CUBIC", None),
            })
            if error is None:
                return True, None

        return False, "No compatible image scale API available"


    ###############################
    ##           RENDER          ##
    ###############################

    #   Exports the Active Image to a Target Path Using Gimp File-save
    def exportImage(self, request_data):
        image, _ = self.getCurrentImage()
        if image is None:
            return {"ok": False, "error": "No active image to export"}

        file_path = request_data.get("path") if isinstance(request_data, dict) else None
        if not file_path:
            return {"ok": False, "error": "Missing export file path"}

        file_path = os.path.normpath(str(file_path))
        settings = request_data.get("settings") if isinstance(request_data, dict) else {}
        if not isinstance(settings, dict):
            settings = {}

        try:
            scale_percent = int(settings.get("exportScale") or 100)
        except Exception:
            scale_percent = 100

        scale_percent = max(1, min(scale_percent, 1000))

        output_color_mode = str(settings.get("colorMode") or "").upper()
        supports_color_mode = output_color_mode in ("RGB", "RGBA", "GRAY", "GRAYA")

        export_image = image
        used_temp_image = False

        if scale_percent != 100 or supports_color_mode:
            temp_image, duplicate_error = self.duplicateImage(image)
            if temp_image is not None:
                export_image = temp_image
                used_temp_image = True
            else:
                self.addToLog("Could not duplicate image for export preprocessing", error=str(duplicate_error))

        if (scale_percent != 100 or supports_color_mode) and not used_temp_image:
            message = "Failed to prepare temporary image for export preprocessing"
            return {
                "ok": False,
                "error": message,
                "data": {
                    "scale": scale_percent,
                    "color_mode": output_color_mode if supports_color_mode else None,
                },
            }

        if scale_percent != 100 and used_temp_image:
            ok, scale_error = self.scaleImagePercent(export_image, scale_percent)
            if not ok:
                self.addToLog("Scale preprocessing failed", scale=scale_percent, error=str(scale_error))
                return {
                    "ok": False,
                    "error": f"Export scale failed: {scale_error}",
                    "data": {"scale": scale_percent},
                }
        if supports_color_mode and used_temp_image:
            ok, color_error = self.convertImageColorMode(export_image, output_color_mode)
            if not ok:
                self.emitGimpWarning(
                    "Color mode preprocessing failed",
                    color_mode=output_color_mode,
                    error=str(color_error),
                )
                return {
                    "ok": False,
                    "error": f"Color mode conversion failed: {color_error}",
                    "data": {"color_mode": output_color_mode},
                }

        gio_file = self.getGioFile(file_path)
        run_mode = getattr(Gimp.RunMode, "NONINTERACTIVE", None)
        active_drawable = self.getActiveDrawable(export_image)

        procedure_name = "gimp-file-save"
        result, save_error = self.runPdbProcedure(
            procedure_name,
            {
                "run-mode": run_mode,
                "image": export_image,
                "drawable": active_drawable,
                "file": gio_file,
            },
        )

        try:
            if save_error is None:
                self.addToLog(
                    "Exported image from Gimp",
                    path=file_path,
                    procedure=procedure_name,
                    scale=scale_percent,
                    color_mode=output_color_mode if supports_color_mode else None,
                )
                return {"ok": True, "data": {"exported": True, "path": file_path, "procedure": procedure_name}}

            self.emitGimpWarning(
                "Failed to export image from Gimp",
                path=file_path,
                procedure=procedure_name,
                error=str(save_error),
            )
            return {
                "ok": False,
                "error": str(save_error),
                "data": {
                    "path": file_path,
                    "procedure": procedure_name,
                    "scale": scale_percent,
                    "color_mode": output_color_mode if supports_color_mode else None,
                    "result": str(result) if result is not None else None,
                },
            }

        finally:
            if used_temp_image:
                self.deleteImage(export_image)


    #################################################
    ##              SM STATE HANDLING              ##
    #################################################

    #   Saves Prism StateManager State JSON as a Parasite on the Active Image
    def saveStates(self, request_data):
        image, _ = self.getCurrentImage()
        if image is None:
            return {"ok": False, "error": "No active image to save states on"}

        state_data = request_data.get("stateData") if isinstance(request_data, dict) else None
        if state_data is None:
            return {"ok": False, "error": "Missing stateData in request"}

        try:
            data_bytes = state_data.encode("utf-8") if isinstance(state_data, str) else bytes(state_data)

            parasite = Gimp.Parasite.new("PrismStates", 1, data_bytes)

            attach = getattr(image, "attach_parasite", None) or getattr(image, "parasite_attach", None)
            if not callable(attach):
                return {"ok": False, "error": "No parasite attach method available on image"}

            attach(parasite)
            self.addToLog("Saved Prism states to Gimp scenefile")
            return {"ok": True}

        except Exception as exc:
            self.addToLog("Failed to save Prism states Gimp scenefile", error=str(exc))
            return {"ok": False, "error": str(exc)}


    #   Reads Prism StateManager State JSON from a Parasite on the Active Image
    def getStates(self):
        image, _ = self.getCurrentImage()
        if image is None:
            return {"ok": True, "data": {"stateData": ""}}

        try:
            find = getattr(image, "get_parasite", None) or getattr(image, "parasite_find", None)
            if not callable(find):
                return {"ok": True, "data": {"stateData": ""}}

            parasite = find("PrismStates")
            if not parasite:
                return {"ok": True, "data": {"stateData": ""}}

            get_data = getattr(parasite, "get_data", None)
            if callable(get_data):
                raw = get_data()
            else:
                raw = getattr(parasite, "data", None)

            if raw is None:
                return {"ok": True, "data": {"stateData": ""}}

            raw_bytes = b""
            if isinstance(raw, tuple):
                for item in raw:
                    raw_bytes = Helper.toBytes(item)
                    if raw_bytes:
                        break
            else:
                raw_bytes = Helper.toBytes(raw)

            if raw_bytes:
                state_data = raw_bytes.decode("utf-8", errors="replace")
            elif isinstance(raw, str):
                state_data = raw
            else:
                state_data = ""

            return {"ok": True, "data": {"stateData": state_data}}

        except Exception as exc:
            self.addToLog("Failed to read Prism states parasite", error=str(exc))
            return {"ok": False, "error": str(exc)}




#####################################################
#   Main Runtime of the Prism Gimp Bridge Plugin    #
#####################################################
class PrismGimpBridgeRuntime:

    #   Define Gimp Procedures (Menu Items)
    PROCEDURES = {
        "prism-save-version": {
            "menu_label": "1 - Save Version",
            "command": "saveVersion",
            "blurb": "Run Prism Save Version.",
            "help": "Sends a command from GIMP to Prism to save a new version.",
        },
        "prism-save-comment": {
            "menu_label": "2 - Save Comment",
            "command": "saveComment",
            "blurb": "Run Prism Save Comment.",
            "help": "Sends a command from GIMP to Prism to save with a comment.",
        },
        "prism-open-project-browser": {
            "menu_label": "3 - Open Project Browser",
            "command": "open_ProjectBrowser",
            "blurb": "Open the Prism Project Browser.",
            "help": "Sends a command from GIMP to Prism to open the Project Browser.",
        },
        "prism-open-state-manager": {
            "menu_label": "4 - Open State Manager",
            "command": "open_StateManager",
            "blurb": "Open the Prism State Manager.",
            "help": "Sends a command from GIMP to Prism to open the State Manager.",
        },
        "prism-open-settings": {
            "menu_label": "5 - Open Prism Settings",
            "command": "open_PrismSettings",
            "blurb": "Open Prism Settings.",
            "help": "Sends a command from GIMP to Prism to open Prism Settings.",
        },
        "reset-prism": {
            "menu_label": "6 - Reset Prism",
            "command": "resetPrism",
            "blurb": "Resets the Prism Core.",
            "help": "Will restart the Prism core inside Gimp.",
        },
    }


    def __init__(self):
        self.bridgeService = None
        self.logLock = threading.Lock()

        self.loadSettings()

    #   Load Settings from json File
    def loadSettings(self):
        self.settings = Helper.loadSettings()
        self.bridgePort_out = self.settings["bridgePort_out"]
        self.bridgePort_in = self.settings["bridgePort_in"]
        self.hostStartTimeout = self.settings["hostStartTimeout"]
        self.log_fileName = self.settings["log_fileName"]
        self.log_maxBytes = self.settings["log_maxBytes"]
        self.attribution = self.settings["attribution"]


    #   Adds Log Line to Custom Gimp Logger
    def addToLog(self, message:str, **fields) -> None:
        line = Helper.formatLogLine(message, "GIMP", **fields)

        with self.logLock:
            with open(Helper.getLogPath(), "a", encoding="utf-8") as handle:
                handle.write(line)


    #   Launches the Prism Host Process if Not Already Running, or Force it
    def launchPrismHost(self, force:bool=False) -> None:
        if not force and self.isPrismHostResponsive():
            return

        if not force and Helper.canConnectToPrism(self.bridgePort_out):
            self.addToLog("Detected unresponsive Prism Host socket, attempting recovery")
            self.recoverUnresponsiveHost()

        hostScript = Helper.getHostScriptPath()
        deadline = time.time() + self.hostStartTimeout

        for python_command in Helper.getHostPythonCommands():
            if not force and self.isPrismHostResponsive():
                return

            self.addToLog("Launching Prism Host", python_command=" ".join(python_command), forced=force)

            process = self.startPrismHost(python_command, hostScript)
            attempt_deadline = min(deadline, time.time() + 3.0)
            launch_time = time.time()

            while time.time() < attempt_deadline:
                if not force and self.isPrismHostResponsive():
                    return

                if process.poll() is not None:
                    self.addToLog("Host process exited", return_code=process.returncode)
                    Helper.removeHostPidState(process.pid, addToLog=self.addToLog)
                    break

                if force and time.time() - launch_time >= 0.5:
                    self.addToLog("Host process started", process_id=process.pid)
                    return

                time.sleep(0.1)

            if not force and process.poll() is None:
                self.addToLog("Host process still initializing, waiting for command server", process_id=process.pid)

                while time.time() < deadline:
                    if self.isPrismHostResponsive():
                        return

                    if process.poll() is not None:
                        self.addToLog("Host process exited", return_code=process.returncode)
                        Helper.removeHostPidState(process.pid, addToLog=self.addToLog)
                        break

                    time.sleep(0.1)

                if process.poll() is None:
                    break

        while time.time() < deadline:
            if not force and self.isPrismHostResponsive():
                return
            time.sleep(0.1)

        raise TimeoutError(f"Prism Host did not start within {self.hostStartTimeout} seconds")
    

    #   Starts the Prism Host Sub-Process
    def startPrismHost(self, python_command:list, host_script_path:str) -> subprocess.Popen:
        if not os.path.isfile(host_script_path):
            raise RuntimeError(f"Prism Host script not found: {host_script_path}")

        parent_pid = self.getHostParentPid()

        launch_args = list(python_command) + [
            host_script_path,
            "--parent-pid",
            str(parent_pid),
            "--prism-root",
            PRISM_ROOT,
        ]

        launch_env = os.environ.copy()
        launch_env["PRISM_GIMP_LOG_PATH"] = Helper.getLogPath()
        launch_env["PRISM_GIMP_LOG_BACKUP_PATH"] = Helper.getBackupLogPath()
        launch_env["PRISM_GIMP_log_maxBytes"] = str(self.log_maxBytes)

        popen_kwargs = {
            "cwd": os.path.dirname(host_script_path),
            "env": launch_env,
        }

        if os.name == "nt":
            creationflags = 0
            creationflags |= getattr(subprocess, "DETACHED_PROCESS", 0)
            creationflags |= getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0)
            creationflags |= getattr(subprocess, "CREATE_NO_WINDOW", 0)
            popen_kwargs["creationflags"] = creationflags
            popen_kwargs["close_fds"] = True
            popen_kwargs["stdout"] = subprocess.DEVNULL
            popen_kwargs["stderr"] = subprocess.DEVNULL

        else:
            popen_kwargs["start_new_session"] = True
            popen_kwargs["stdout"] = subprocess.DEVNULL
            popen_kwargs["stderr"] = subprocess.DEVNULL

        return subprocess.Popen(launch_args, **popen_kwargs)


    #   Resolves the PID used by Prism Host for parent-process monitoring
    def getHostParentPid(self) -> int:
        try:
            bridge_pid = Helper.readSettingsData().get("BRIDGE_PID")
            if bridge_pid not in [None, ""]:
                bridge_pid = int(bridge_pid)
                if Helper.isProcessRunning(bridge_pid):
                    return bridge_pid
                self.addToLog("Recorded bridge pid is stale; disabling host parent monitor", bridge_pid=bridge_pid)
        except Exception:
            pass

        #   Fallback: disable parent monitor instead of using transient menu callback pids.
        return 0


    #   Resets the Prism Host by Terminating the Process and Restarting it
    def resetPrismHost(self) -> None:
        self.addToLog("Reset Prism requested")
        host_pid = Helper.readHostPid()

        if host_pid:
            self.addToLog("Stopping Prism Host", process_id=host_pid)
            Helper.terminateProcess(host_pid)

            shutdown_deadline = time.time() + self.hostStartTimeout
            while time.time() < shutdown_deadline:
                if not Helper.isProcessRunning(host_pid):
                    break
                time.sleep(0.1)

            if Helper.isProcessRunning(host_pid):
                raise TimeoutError(f"Prism Host did not stop within {self.hostStartTimeout} seconds")

            Helper.removeHostPidState(host_pid, addToLog=self.addToLog)

        else:
            self.addToLog("Reset Prism continuing without host pid state")

        disconnect_deadline = time.time() + 2.0
        while time.time() < disconnect_deadline:
            if not Helper.canConnectToPrism(self.bridgePort_out):
                break
            time.sleep(0.1)

        self.launchPrismHost(force=True)
        self.addToLog("Reset Prism completed")


    #   Ensures the Prism Host is Running, Launch if Not
    def ensurePrismHostRunning(self):
        #   Persist the persistent bridge pid so host parent monitoring stays stable across callbacks.
        Helper.updateSettingState(BRIDGE_PID=os.getpid())
        self.launchPrismHost(force=False)


    #   Sends a Raw Request to the Prism Host and Returns Parsed JSON Response
    def sendPacketToHost(self, message:dict, timeout:float=1.0) -> dict:
        return Helper.sendJsonRequest(self.bridgePort_out, message, timeout=timeout)


    #   Verifies Host Health by Requiring a Valid Ping Response
    def isPrismHostResponsive(self, timeout:float=0.75) -> bool:
        try:
            response = self.sendPacketToHost({"command": "ping", "data": {}}, timeout=timeout)
            return bool(response.get("ok"))
        except Exception:
            return False


    #   Attempts to Terminate a Stale Host Process if Socket is Up but Host is Unresponsive
    def recoverUnresponsiveHost(self) -> None:
        host_pid = Helper.readHostPid()

        if not host_pid:
            self.addToLog("Unable to recover unresponsive host: no host pid state")
            return

        if not Helper.isProcessRunning(host_pid):
            Helper.removeHostPidState(host_pid, addToLog=self.addToLog)
            return

        self.addToLog("Terminating unresponsive Prism Host", process_id=host_pid)
        Helper.terminateProcess(host_pid)

        shutdown_deadline = time.time() + self.hostStartTimeout
        while time.time() < shutdown_deadline:
            if not Helper.isProcessRunning(host_pid):
                break
            time.sleep(0.1)

        if Helper.isProcessRunning(host_pid):
            raise TimeoutError(f"Unresponsive Prism Host did not stop within {self.hostStartTimeout} seconds")

        Helper.removeHostPidState(host_pid, addToLog=self.addToLog)


    #   Sends a Command to the Prism Host
    def sendToPrism(self, command, payload=None):
        message = {"command": command, "data": payload or {}}

        #   Checks Comms Connection
        if not self.isPrismHostResponsive():
            self.addToLog("Prism Host is not responsive; command ignored", command=command)
            return False

        #   Sends Command to Comms Method
        response = self.sendPacketToHost(message, timeout=3.0)

        if not response.get("ok"):
            self.addToLog("Prism host command failed", command=command, error=response.get("error"))
            return False

        return True


    #   Gimp Procedure Callback to Run a Prism Command
    def runPrismCommand(self, procedure, run_mode, image, drawables, config, data=None):
        procedure_data = self.PROCEDURES.get(procedure.get_name())

        if not procedure_data:
            return procedure.new_return_values(Gimp.PDBStatusType.CALLING_ERROR, None)

        try:
            if procedure_data["command"] == "resetPrism":
                self.addToLog("Running Prism command", command=procedure_data["command"])
                self.resetPrismHost()

            else:
                self.addToLog("Running Prism command", command=procedure_data["command"])
                command_ok = self.sendToPrism(procedure_data["command"])

                if not command_ok:
                    raise RuntimeError("Prism host command failed: %s" % procedure_data["command"])
                
            return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, None)
        
        except Exception as e:
            print(f"[Prism] Failed to send command to Prism: {e}")
            self.addToLog("Failed to send command to Prism", error=str(e))

            return procedure.new_return_values(Gimp.PDBStatusType.EXECUTION_ERROR, None)


    #   Gimp Procedure Callback to Start the Prism Bridge Service
    def runPrismBridge(self, procedure, config, data=None):
        try:
            if self.bridgeService is None:
                self.bridgeService = PrismGimpBridgeService(procedure, ensurePrismHostRunning=self.ensurePrismHostRunning)

            self.bridgeService.run()
            return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, None)
        except Exception as e:
            print(f"[Prism] Failed to start Gimp bridge: {e}")
            self.addToLog("Failed to start Gimp bridge", error=str(e))
            return procedure.new_return_values(Gimp.PDBStatusType.EXECUTION_ERROR, None)


    #   Gimp Plugin Callbacks to Query and Create Procedures
    def queryProcedures(self):
        return ["extension-prism-gimp-bridge"] + list(self.PROCEDURES.keys())


    #    Creates Gimp Procedures for the Bridge and Command Menu Items
    def createProcedure(self, plugin, name):
        if name == "extension-prism-gimp-bridge":
            procedure = Gimp.Procedure.new(
                plugin,
                name,
                Gimp.PDBProcType.PERSISTENT,
                runPrismBridge,
            )
            procedure.set_documentation(
                "Auto-start Prism Gimp bridge.",
                "Starts the persistent Prism bridge process inside Gimp and auto-launches the external Prism Host.",
                None,
            )
            procedure.set_attribution(*self.attribution)
            return procedure

        procedure_data = self.PROCEDURES.get(name)

        if not procedure_data:
            return None

        procedure = Gimp.ImageProcedure.new(
            plugin,
            name,
            Gimp.PDBProcType.PLUGIN,
            runPrismCommand,
        )
        procedure.set_sensitivity_mask(Gimp.ProcedureSensitivityMask.ALWAYS)
        procedure.set_image_types("*")
        procedure.set_menu_label(procedure_data["menu_label"])
        procedure.add_menu_path(MENU_ROOT)
        procedure.set_documentation(
            procedure_data["blurb"],
            procedure_data["help"],
            None,
        )
        procedure.set_attribution(*self.attribution)
        return procedure


#   Shared Bridge Runtime Instance
BRIDGE_RUNTIME = PrismGimpBridgeServiceRuntime()

#   Define the Main Entry Point for the Gimp Bridge Plugin
RUNTIME = PrismGimpBridgeRuntime()


#   Used as Callbacks for Gimp Procedures
def runPrismCommand(procedure, run_mode, image, drawables, config, data=None):
    return RUNTIME.runPrismCommand(procedure, run_mode, image, drawables, config, data)


#   Used as Callback for the Bridge Procedure
def runPrismBridge(procedure, config, data=None):
    return RUNTIME.runPrismBridge(procedure, config, data)



#   Main Gimp Bridge Plugin Class
class PrismGimpBridgePlugin(Gimp.PlugIn):
    def do_set_i18n(self, procedure_name):
        return False, None, None

    def do_query_procedures(self):
        return RUNTIME.queryProcedures()

    def do_create_procedure(self, name):
        return RUNTIME.createProcedure(self, name)


#   Gimp Call to Run Plugin
Gimp.main(PrismGimpBridgePlugin.__gtype__, sys.argv)


