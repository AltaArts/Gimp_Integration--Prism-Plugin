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
#     - Registers Prism menu procedures in Gimp
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
import re


import gi

gi.require_version("Gimp", "3.0")

from gi.repository import Gimp, GLib, Gio

import Prism_Helper as Helper

PRISM_ROOT = r"@PRISMROOTREPLACE@"
GIMP_PLUGIN_ROOT = r"@GIMPPLUINREPLACE@"
MENU_ROOT = "<Image>/Prism"
HOST_SCRIPT_NAME = "Prism_Host.py"

SCRIPTS_DIR = os.path.join(GIMP_PLUGIN_ROOT, "Scripts")
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)

from GimpMapping import (
    IMAGEPRECISIONDATA,
    EXPORTER_PROCEDURE_MAP,
    PNG_FORMAT_MAP,
    JPEG_SUBSAMPLING_MAP,
    TIFF_COMPRESSION_MAP,
    )


######################################################
#   Shared Runtime for the in-Gimp Bridge Service    #
######################################################
class PrismGimpBridgeServiceRuntime:
    def __init__(self):
        self.loadSettings()
        self.logLock = threading.Lock()
        self.logComponent = "BRIDGE"
        self.imageHintLock = threading.Lock()
        self.imageHintId = None
        self.imageHintTime = 0.0
        Helper.rotateLog(self.settings, self.logLock)


    def loadSettings(self) -> None:
        self.settings = Helper.loadSettings()
        self.bridgePort_in = self.settings["bridgePort_in"]
        self.log_maxBytes = self.settings["log_maxBytes"]


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


    #   Stores Image ID Hint for the Active Image
    def setImageHint(self, imageId:int | None) -> None:
        with self.imageHintLock:
            self.imageHintId = imageId
            self.imageHintTime = time.time()


    #   Returns Recent Hinted Image ID, or None if Stale/Missing
    def getImageHint(self, maxAgeSeconds:float=8.0) -> int | None:
        with self.imageHintLock:
            if self.imageHintId is None:
                return None

            if (time.time() - self.imageHintTime) > maxAgeSeconds:
                return None

            return self.imageHintId



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
        self.lastActiveImageLogKey = None

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

        try:
            Gimp.message(f"PRISM BRIDGE: {warning_text}")
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
        #   Start the Server Thread
        self.start()
        #   Enable the Persistent Host Procedure to Keep the Plugin Alive
        self.procedure.persistent_ready()
        self.plugIn.persistent_enable()

        #   Run the Server Loop to Process Requests Received from the Host
        self.mainLoop.run()

        self.addToLog("Bridge main loop exited")


    #   Server Loop Accepting Incoming Host Requests
    def runServer(self):
        while not self.shutdownEvent.is_set():
            try:
                #   Accept Connection with Timeout to allow Shutdown Check
                client, _address = self.serverSocket.accept()

            except socket.timeout:
                continue

            except OSError:
                self.addToLog("Bridge server socket closed or errored during accept")
                break

            with client:
                client.settimeout(1)

                try:
                    #   Receive Command from Host and Parse as JSON
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
                    #   Send Response as JSON Back to Host
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

        #   Helper to Send the Request to the Main Thread
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

        #   Schedule the Request to be Executed on the Main Gimp Thread and Wait for Completion
        GLib.idle_add(executeRequest)
        completed.wait()

        response = responseHolder.get("response") or {}
        if not response.get("ok"):
            self.addToLog(
                "Bridge request failed",
                **Helper.summarizeRequest(request),
                error=response.get("error"),
            )

        return responseHolder["response"]


    #   Handles a Received Bridge Request
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
                return self.getCurrentFile(requestData)

            case "get-app-version":
                return self.getAppVersion()

            case "open-scene":
                return self.openScene(requestData)

            case "save-scene":
                return self.saveScene(requestData)

            case "get-thumbnail":
                return self.getThumbnail(requestData)

            case "mark-scene-dirty":
                return self.markSceneDirty(requestData)
            
            case "get-image-specs":
                return self.getImageSpecs()
            
            case "import-image":
                return self.importImage(requestData)

            case "delete-image-layer":
                return self.deleteImageLayer(requestData)

            case "get-layer-name":
                return self.getTrackedLayerName(requestData)

            case "rename-layer":
                return self.renameImageLayer(requestData)

            case "replace-layer-image":
                return self.replaceLayerImage(requestData)

            case "export-image":
                return self.exportImage(requestData)

            case "save-states":
                return self.saveStates(requestData)

            case "get-states":
                return self.getStates(requestData)

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

        #   Direct API first
        try:
            version_value = Gimp.version()
        except Exception:
            version_value = None

        #   PDB fallback
        if version_value is None:
            try:
                pdb = Gimp.get_pdb()
                proc = pdb.lookup_procedure("gimp-version")
                version_value = str(proc.run(proc.create_config()))
            except Exception:
                pass

        if version_value is None:
            return {"ok": True, "data": {"version": None}}

        return {"ok": True, "data": {"version": str(version_value)}}


    #   Converts a File Path to Gio.File
    def getGioFile(self, filePath:str) -> object | None:
        try:
            return Gio.File.new_for_path(filePath)
        
        except Exception:
            return None


    #   Returns a PDB Procedure by Name
    def getPdbProcedure(self, procedureName:str) -> object | None:
        try:
            pdb = Gimp.get_pdb()
            if pdb is None:
                return None

            return pdb.lookup_procedure(procedureName)
        
        except Exception:
            return None


    #   Runs a PDB Procedure with Config Key/Value Pairs
    def runPdbProcedure(self, procedureName, values):
        #   Get the Procedure by Name
        procedure = self.getPdbProcedure(procedureName)
        if not procedure:
            return None, f"Procedure not found: {procedureName}"

        try:
            #   Create Proc Config and Set Values
            config = procedure.create_config()
            unsupported_keys = []
            for key, value in (values or {}).items():
                if not Helper.setConfigValue(config, key, value):
                    unsupported_keys.append(str(key))

            if unsupported_keys:
                self.addToLog(
                    "PDB config ignored unsupported keys",
                    procedure=procedureName,
                    keys=unsupported_keys,
                )

            #   Run the Procedure and Flatten Results
            result = procedure.run(config)
            values_flat = Helper.flattenValues(result)

            statusText = ""
            if values_flat:
                try:
                    statusText = str(values_flat[0])
                except Exception:
                    statusText = ""

            status_upper = statusText.upper()
            resultMsg = ""

            for value in values_flat[1:]:
                if isinstance(value, str) and value.strip():
                    resultMsg = value.strip()
                    break

            #   Emit Result as Gimp Warnings and Log
            if resultMsg:
                self.emitGimpWarning(
                    f"PDB message from {procedureName}: {resultMsg}",
                    procedure=procedureName,
                    status=statusText or None,
                )

            if any(flag in status_upper for flag in ["CALLING_ERROR", "EXECUTION_ERROR", "CANCEL"]):
                details = resultMsg or statusText or "PDB call failed"
                return result, f"{procedureName} failed: {details}"

            return result, None
        
        except Exception as exc:
            return None, str(exc)


    #   Checks if a Procedure Config accepts specific keys on this Gimp build
    def procedureConfigSupportsKeys(self, procedureName, keyValues):
        procedure = self.getPdbProcedure(procedureName)
        if not procedure:
            return False, [str(k) for k in (keyValues or {}).keys()]

        try:
            config = procedure.create_config()
        except Exception:
            return False, [str(k) for k in (keyValues or {}).keys()]

        unsupported = []
        for key, value in (keyValues or {}).items():
            if not Helper.setConfigValue(config, key, value):
                unsupported.append(str(key))

        return len(unsupported) == 0, unsupported

    
    #   Gets a Layer Property Using Multiple Possible Getter Methods or Attributes
    def getLayerProp(self, layer, getters, attrs=None, default=None):
        for getter_name in getters or []:
            getter = getattr(layer, getter_name, None)
            if callable(getter):
                value, error = Helper.callWithSignatures(getter, [(), (layer,)])
                if error is None:
                    return value

        for attr in attrs or []:
            try:
                return getattr(layer, attr)
            except Exception:
                continue

        return default
    

    #   Sets a Layer Property Using Multiple Possible Setter Methods or Attributes
    def setLayerProp(self, layer, setters, value, attrs=None):
        if value is None:
            return False

        for setter_name in setters or []:
            setter = getattr(layer, setter_name, None)
            if callable(setter):
                _result, error = Helper.callWithSignatures(setter, [(value,), (layer, value)])
                if error is None:
                    return True

        for attr_name in attrs or []:
            try:
                setattr(layer, attr_name, value)
                return True
            except Exception:
                continue

        return False


    ##########################################
    ##              SCENE FILE              ##
    ##########################################

    #   Returns Active/Open Gimp Document Path/Name for Host Queries
    def getCurrentFile(self, rData=None):
        #   Resolve the Active Image
        image = self.getActiveImage(rData)

        #   Return Empty Data if No Image
        if image is None:
            return {
                "ok": True,
                "data": {
                    "imageId": None,
                    "path": None,
                    "name": None,
                },
            }

        #   Attempt to Get File Path and Name
        filePath = Helper.getImageFilePath(image)
        fileName = None

        try:
            fileName = str(image.get_name()) or None
        except Exception:
            pass

        if filePath and not fileName:
            fileName = os.path.basename(filePath)

        #   Get the Image ID for Logging and Context Change Detection
        image_id = Helper.getImageId(image)

        context_key = f"{image_id}|{filePath or ''}|{fileName or ''}"
        if context_key != self.lastActiveImageLogKey:
            self.lastActiveImageLogKey = context_key
            self.addToLog(
                "Detected active image context",
                image_id=image_id,
                path=filePath,
                name=fileName,
            )

        return {
            "ok": True,
            "data": {
                "imageId": image_id,
                "path": filePath,
                "name": fileName,
            },
        }


    #   Opens an XCF Scene File in Gimp
    def openScene(self, rData):
        #   Resolve the File Path from the Request Data
        filePath = rData.get("path") if isinstance(rData, dict) else None

        if not filePath:
            return {"ok": False, "error": "Missing file path"}

        #   Normalize the File Path and Convert to Gio.File
        filePath = os.path.normpath(str(filePath))
        gio_file = self.getGioFile(filePath)
        runMode = getattr(Gimp.RunMode, "NONINTERACTIVE", None)

        #   Get the PDB Procedure for File Loading
        procedure_name = "gimp-file-load"
        procedure = self.getPdbProcedure(procedure_name)

        if not procedure:
            return {"ok": False, "error": f"Required procedure not found: {procedure_name}"}

        try:
            #   Create Proc Config Values and Run
            config = procedure.create_config()
            Helper.setConfigValue(config, "run-mode", runMode)
            Helper.setConfigValue(config, "file", gio_file)
            procedure.run(config)

            #   Reset Scene Dirty
            self.sceneDirtyFallbackByImageId.clear()

            self.addToLog("Opened scene in Gimp", path=filePath, procedure=procedure_name)

            return {"ok": True, "data": {"opened": True, "path": filePath, "procedure": procedure_name}}

        except Exception as exc:
            self.addToLog("Failed to open scene in Gimp", path=filePath, error=str(exc), procedure=procedure_name)
            return {"ok": False, "error": str(exc), "data": {"path": filePath, "procedure": procedure_name}}


    #   Saves the Current Gimp Image to an XCF Scene File
    def saveScene(self, rData):
        #   Resolve the Active Image to Save
        image = self.getActiveImage(rData)
        if image is None:
            return {"ok": False, "error": "No active image to save"}

        #   Attempt to Get the Image Name for Logging
        image_name = None
        try:
            image_name = str(image.get_name()) or None
        except Exception:
            pass

        #   Get the Image ID for Logging and Context Change Detection
        imageID = Helper.getImageId(image)

        filePath = rData.get("path") if isinstance(rData, dict) else None
        if filePath:
            filePath = os.path.normpath(str(filePath))
        else:
            filePath = Helper.getImageFilePath(image)

        if not filePath:
            return {"ok": False, "error": "Missing file path"}

        #   Resolve the Active Drawable from Gimp
        active_drawable = None
        try:
            active_drawable = image.get_active_drawable()
        except Exception:
            active_drawable = None

        #   Normalize the File Path and Convert to Gio.File
        gio_file = self.getGioFile(filePath)
        run_mode = getattr(Gimp.RunMode, "NONINTERACTIVE", None)

        #   Get the PDB Procedure for File Saving
        procedure_name = "gimp-file-save"
        procedure = self.getPdbProcedure(procedure_name)

        if not procedure:
            return {"ok": False, "error": f"Required procedure not found: {procedure_name}"}

        try:
            #   Create Proc Config Values and Run
            config = procedure.create_config()
            Helper.setConfigValue(config, "run-mode", run_mode)
            Helper.setConfigValue(config, "image", image)
            Helper.setConfigValue(config, "drawable", active_drawable)
            Helper.setConfigValue(config, "file", gio_file)
            procedure.run(config)

            #   Clear Scene Dirty
            if imageID in self.sceneDirtyFallbackByImageId:
                del self.sceneDirtyFallbackByImageId[imageID]

            self.addToLog(
                "Saved scene in Gimp",
                path=filePath,
                procedure=procedure_name,
                image_id=imageID,
                image_name=image_name,
                command_image_id=(rData.get("image_id") if isinstance(rData, dict) else None),
            )
            return {"ok": True, "data": {"saved": True, "path": filePath, "procedure": procedure_name}}

        except Exception as exc:
            self.addToLog(
                "Failed to save scene in Gimp",
                path=filePath,
                error=str(exc),
                procedure=procedure_name,
                image_id=imageID,
                image_name=image_name,
                command_image_id=(rData.get("image_id") if isinstance(rData, dict) else None),
            )
            return {"ok": False, "error": str(exc), "data": {"path": filePath, "procedure": procedure_name}}


    ##########################################
    ##               GIMP IMAGE             ##
    ##########################################

    #   Returns the Active Image (Currently Viewed in Gimp)
    def getActiveImage(self, rData:dict | None=None) -> object | None:
        if isinstance(rData, dict):
            #   Resolve by Image ID Passed in the Request Data (if any)
            raw_imageID = rData.get("image_id")
            if raw_imageID is not None:
                try:
                    request_imageID = int(raw_imageID)

                except Exception:
                    request_imageID = None

                #   Get the Image Object by ID
                if request_imageID is not None:
                    request_image = self.getImageById(request_imageID)
                    if request_image is not None:
                        return request_image

        #   Check for a Hinted Image ID Set by Recent Operations (if any)
        hinted_imageID = self.runtime.getImageHint()

        #   Get the Image Object by the Hinted ID
        if hinted_imageID is not None:
            hinted_image = self.getImageById(hinted_imageID)
            if hinted_image is not None:
                return hinted_image

        #   Attempt to Get the Active Image from Gimp API
        for getter_name in ["get_images", "list_images", "image_list"]:
            getter = getattr(Gimp, getter_name, None)
            if not callable(getter):
                continue

            try:
                images = Helper.normalizeGimpItems(getter())
            except Exception:
                images = []

            if images:
                return images[0]

        return None


    #   Resolves an Image Object by Image ID
    def getImageById(self, imageId:int) -> object | None:
        if not imageId:
            return None

        #   Attempt Direct API if Available
        try:
            image = Gimp.Image.get_by_id(int(imageId))
            if image:
                return image
        except Exception:
            pass

        #   Fallback to Iterating All Images and Matching IDs
        for getter_name in ["get_images", "list_images", "image_list"]:
            getter = getattr(Gimp, getter_name, None)
            if not callable(getter):
                continue

            try:
                images = Helper.normalizeGimpItems(getter())
            except Exception:
                images = []

            for image in images:
                try:
                    if int(image.get_id()) == int(imageId):
                        return image

                except Exception:
                    continue

        return None


    #   Marks the Current Image Dirty Once and Skips if Already Dirty
    def markSceneDirty(self, rData=None):
        image = self.getActiveImage(rData)
        if image is None:
            return {"ok": False, "error": "No active image to mark dirty"}

        image_id = Helper.getImageId(image)
        command_image_id = rData.get("image_id") if isinstance(rData, dict) else None
        force_mark = bool((rData or {}).get("force")) if isinstance(rData, dict) else False

        if not force_mark:
            dirty_state = Helper.isImageDirty(image)
            cached_dirty_mark = bool(self.sceneDirtyFallbackByImageId.get(image_id))
            already_dirty = (dirty_state is True) or (dirty_state is None and cached_dirty_mark)
            if already_dirty:
                reason = "image-api" if dirty_state is True else "fallback-cache"
                self.addToLog(
                    "Skipping dirty mark; image already dirty",
                    image_id=image_id,
                    command_image_id=command_image_id,
                    reason=reason,
                    cached_dirty_mark=cached_dirty_mark,
                )
                return {"ok": True, "data": {"dirtyMarked": False, "alreadyDirty": True, "reason": reason}}

        result = self._markSceneDirtyInternal(image)
        if result.get("ok"):
            if image_id is not None:
                self.sceneDirtyFallbackByImageId[image_id] = True
            result["data"] = {"dirtyMarked": True, "alreadyDirty": False}
            self.addToLog("Marked scene dirty", image_id=image_id, command_image_id=command_image_id)

        return result


    #   Performs a Tiny No-op Layer Add/Remove so Gimp Marks the Image Modified
    def _markSceneDirtyInternal(self, image):

        w, h = Helper.getImageSize(image)
        width = max(1, w) if w > 0 else 1
        height = max(1, h) if h > 0 else 1

        layer = None
        created_with_pdb = False
        inserted = False

        try:
            image_type_enum = getattr(getattr(Gimp, "ImageType", None), "RGBA_IMAGE", None)
            layer_mode_enum = getattr(getattr(Gimp, "LayerMode", None), "NORMAL", None)

            try:
                layer_new = Gimp.Layer.new
                signature_options = []

                if image_type_enum is not None and layer_mode_enum is not None:
                    signature_options.append((image, width, height, image_type_enum, "__PrismDirty__", 0.0, layer_mode_enum))

                signature_options.extend([
                    (image, width, height, 0, "__PrismDirty__", 0.0, 0),
                    (image, width, height, "RGBA", "__PrismDirty__", 0.0, "NORMAL"),
                ])

                layer, _ = Helper.callWithSignatures(layer_new, signature_options)
            except Exception:
                layer = None

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

                layer = Helper.extractLayerFromResult(result)
                if layer is None:
                    return {"ok": False, "error": "Failed to parse temp layer from PDB result"}

                created_with_pdb = True

            undo_started = False
            try:
                image.undo_group_start()
                undo_started = True

            except Exception:
                pass

            try:
                try:
                    _, insert_error = Helper.callWithSignatures(image.insert_layer, [
                        (layer, None, 0),
                        (layer, 0),
                        (layer,),
                    ])
                    if insert_error:
                        raise RuntimeError(str(insert_error))
                except Exception:

                    try:
                        _, insert_error = Helper.callWithSignatures(image.add_layer, [
                            (layer, 0),
                            (layer,),
                        ])
                        if insert_error:
                            raise RuntimeError(str(insert_error))
                    except Exception:
                        _result, error = self.runPdbProcedure("gimp-image-insert-layer", {
                            "image": image,
                            "layer": layer,
                            "parent": None,
                            "position": 0,
                        })
                        if error:
                            return {"ok": False, "error": f"Failed to insert temp layer: {error}"}

                inserted = True

                try:
                    _, remove_error = Helper.callWithSignatures(image.remove_layer, [
                        (layer,),
                    ])
                    if remove_error:
                        raise RuntimeError(str(remove_error))
                    
                except Exception:
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
                        image.undo_group_end()
                    except Exception:
                        pass

            self.addToLog("Marked Gimp scenefile dirty")
            return {"ok": True}

        except Exception as exc:
            return {"ok": False, "error": str(exc)}

        finally:
            if inserted and layer is not None:
                try:
                    try:
                        image.remove_layer(layer)
                    except Exception:
                        self.runPdbProcedure("gimp-image-remove-layer", {
                            "image": image,
                            "layer": layer,
                        })
                except Exception:
                    pass

            if created_with_pdb and layer is not None:
                try:
                    layer.delete()
                except Exception:
                    pass



    #   Returns Active Image Specs Needed by the Gimp_Export State UI
    def getImageSpecs(self):
        image = self.getActiveImage()
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

        specs["xRez"], specs["yRez"] = Helper.getImageSize(image)

        base_type = self.getImageBaseType(image)
        if base_type:
            specs["colorMode"] = {"GRAY": "Grayscale"}.get(base_type, base_type)

        try:
            precision_raw = image.get_precision()
            precision_str = str(precision_raw)

            precision_int = None
            try:
                precision_int = int(precision_raw)

            except Exception:
                precision_int = None

            if precision_int in IMAGEPRECISIONDATA:
                specs["bitDepth"] = IMAGEPRECISIONDATA[precision_int]["display"]
                specs["gamma"] = IMAGEPRECISIONDATA[precision_int]["gamma"]

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


    #   Duplicates an Image for Non-destructive Export Processing
    def duplicateImage(self, image):
        try:
            duplicated = image.duplicate()
            if duplicated:
                return duplicated, None
        except Exception:
            pass

        result, error = self.runPdbProcedure("gimp-image-duplicate", {"image": image})
        if error:
            return None, error

        duplicated = Helper.extractImageFromResult(result)
        if duplicated is None:
            return None, "Could not parse duplicated image result"

        return duplicated, None


    #   Deletes a Temporary Duplicated Image
    def deleteImage(self, image):
        if not image:
            return

        try:
            image.delete()
            return
        except Exception:
            pass

        self.runPdbProcedure("gimp-image-delete", {"image": image})


    #   Returns Active Drawable for an Image
    def getActiveDrawable(self, image):
        try:
            return image.get_active_drawable()
        except Exception:
            return None


    #   Returns Image Layers using the First Compatible Getter
    def getImageLayers(self, image):
        for layers_getter_name in ["get_layers", "list_layers", "layers"]:
            layers_getter = getattr(image, layers_getter_name, None)
            if not callable(layers_getter):
                continue

            try:
                layers = Helper.normalizeGimpItems(layers_getter())
            except Exception:
                layers = []

            if layers:
                return layers

        return []


    #   Returns all Drawables/Layers in an Image
    def getImageDrawables(self, image):
        layers = self.getImageLayers(image)
        if layers:
            return layers

        active = self.getActiveDrawable(image)
        return [active] if active else []


    #   Returns Whether a Drawable Has Alpha
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
        #   Prefer Active Drawable First
        if self.drawableHasAlpha(self.getActiveDrawable(image)):
            return True

        #   Fall back to Scanning all Layers/Drawables
        for layer in self.getImageLayers(image):
            if self.drawableHasAlpha(layer):
                return True

        return False


    #   Returns Normalized Image Base Type for Color Conversion Checks
    def getImageBaseType(self, image):
        try:
            base_type_raw = image.get_base_type()
            
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


    #   Refreshes Display(s) for an Image to Force UI Update
    def refreshImageDisplay(self, image:object) -> None:
        if not image:
            return

        #   Try Direct API First.
        try:
            image.flush()
            return
        except Exception:
            pass

        #   Try get_displays() API for GIMP 3+.
        try:
            displays = Helper.normalizeGimpItems(Gimp.get_displays(image))
            for display in displays:
                try:
                    display.flush()
                except Exception:
                    pass
            return
        except Exception:
            pass

        #   Fall back to PDB gimp-displays-flush
        try:
            self.runPdbProcedure("gimp-displays-flush", {})
        except Exception:
            pass


    #   Converts Image Base Type to Match Requested Export Color Mode
    def convertImageColorMode(self, image, output_color_mode):
        #  Determine the Target Base Type from the Requested Color Mode
        requested_mode = str(output_color_mode or "").upper()
        if requested_mode in ("GRAY", "GRAYA"):
            target_base = "GRAY"
        elif requested_mode in ("RGB", "RGBA"):
            target_base = "RGB"
        else:
            return True, None

        #   Get the Current Base Type of the Image and Check if Conversion is Needed
        current_base = self.getImageBaseType(image)
        if current_base == target_base:
            return True, None

        #   Attempt to Use Direct Image Method for Base Type Conversion if Available
        enum_container = getattr(Gimp, "ImageBaseType", None)
        target_enum = getattr(enum_container, target_base, None) if enum_container else None

        #   Try Multiple Method Signatures for Compatibility with Different Gimp Versions
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

        #   If Direct Methods Failed, Fall Back to PDB Procedures for Base Type Conversion
        if target_base == "GRAY":
            proc_names = ["gimp-image-convert-grayscale", "gimp-image-convert-base-type"]
        else:
            proc_names = ["gimp-image-convert-rgb", "gimp-image-convert-base-type"]

        #   Try Multiple Procedures for Compatibility with Different Gimp Versions
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
        #   If Scale is 100%, No Scaling Needed
        if scale_percent == 100:
            return True, None

        width, height = Helper.getImageSize(image)

        if width <= 0 or height <= 0:
            return False, "Could not resolve image dimensions for scaling"

        #   Calculate the New Dimensions Based on the Scale Percentage
        new_width = max(1, int(round(width * (scale_percent / 100.0))))
        new_height = max(1, int(round(height * (scale_percent / 100.0))))

        #   Try Multiple Method Signatures for Compatibility with Different Gimp Versions
        for args in [(new_width, new_height), (new_width, new_height, 0)]:
            try:
                image.scale(*args)
                return True, None
            except Exception:
                continue

        #   If Direct Methods Failed, Fall Back to PDB Procedures for Image Scaling
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


    #   Resolves a Gimp Layer Object by its Persistent Tattoo
    def getLayerByTattoo(self, image:object, layerTattoo:int) -> object | None:
        if image is None or layerTattoo is None:
            return None

        try:
            target_tattoo = int(layerTattoo)
        except Exception:
            return None

        for layer in self.getImageDrawables(image):
            if Helper.getLayerTattoo(layer) == target_tattoo:
                return layer

        return None



    ###################################
    ##            THUMBNAIL          ##
    ###################################

    #   Captures a Thumbnail from the Active Gimp Image and Returns Raw Pixel Data
    def getThumbnail(self, rData):
        #   Resolve the Active Image from Gimp
        image = self.getActiveImage(rData)
        if image is None:
            return {"ok": False, "error": "No active image for thumbnail capture"}

        #   Get the Command Image ID for Logging Context (if any)
        command_image_id = rData.get("image_id") if isinstance(rData, dict) else None

        #   Resolve the Desired Thumbnail Size from the Request Data (with Defaults and Clamping)
        width = rData.get("width") if isinstance(rData, dict) else None
        height = rData.get("height") if isinstance(rData, dict) else None

        try:
            width = int(width) if width is not None else 512
        except Exception:
            width = 512

        try:
            height = int(height) if height is not None else 512
        except Exception:
            height = 512

        width = max(1, min(width, 2048))
        height = max(1, min(height, 2048))

        fallback_reasons = []

        #   Attempt to Get Thumbnail Data from the Image Object Directly
        method_name = "get_thumbnail_data"
        try:
            method = getattr(image, method_name)
            raw_result, call_error = Helper.callWithSignatures(method, [(width, height), (width, height, 4), (width, height, 3)])

            #   Parse and Return if Valid
            if raw_result is not None:
                parsed = Helper.parseThumbnailResult(raw_result, width, height)
                if parsed:
                    self.addToLog(
                        "Captured thumbnail",
                        method=method_name,
                        width=parsed["width"],
                        height=parsed["height"],
                        bpp=parsed["bpp"],
                        command_image_id=command_image_id,
                    )
                    return {
                        "ok": True,
                        "data": {
                            "width": parsed["width"],
                            "height": parsed["height"],
                            "bpp": parsed["bpp"],
                            "pixels": base64.b64encode(parsed["pixels"]).decode("ascii"),
                        },
                    }
                fallback_reasons.append(f"{method_name}: returned unrecognized payload")

            else:
                #   If Call Failed, Capture the Error for Logging
                details = str(call_error) if call_error else "No return value"
                fallback_reasons.append(f"{method_name}: {details}")
        except Exception:
            #   If Method Not Available, Capture for Logging
            fallback_reasons.append(f"{method_name}: unavailable")

        #   If Direct Method Failed, Use the Older get_thumbnail Method
        method_name = "get_thumbnail"
        try:
            method = getattr(image, method_name)
            #   Try Multiple Signatures for Compatibility with Different Gimp Versions
            raw_result, call_error = Helper.callWithSignatures(method, [(width, height), (width, height, 0), (width, height, 1), (width, height, 2)])
            if raw_result is not None:
                #   Parse and Return if Valid
                parsed = Helper.parseThumbnailResult(raw_result, width, height)
                if parsed:
                    self.addToLog(
                        "Captured thumbnail",
                        method=method_name,
                        width=parsed["width"],
                        height=parsed["height"],
                        bpp=parsed["bpp"],
                        command_image_id=command_image_id,
                    )
                    return {
                        "ok": True,
                        "data": {
                            "width": parsed["width"],
                            "height": parsed["height"],
                            "bpp": parsed["bpp"],
                            "pixels": base64.b64encode(parsed["pixels"]).decode("ascii"),
                        },
                    }
                fallback_reasons.append(f"{method_name}: returned unrecognized payload")

            else:
                #   If Call Failed, Capture the Error for Logging
                details = str(call_error) if call_error else "No return value"
                fallback_reasons.append(f"{method_name}: {details}")
        except Exception:
            #   If Method Not Available, Capture for Logging
            fallback_reasons.append(f"{method_name}: unavailable")

        fallback_reason = "; ".join(fallback_reasons)

        self.addToLog(
            "Using black thumbnail fallback",
            reason=fallback_reason,
            width=width,
            height=height,
            bpp=4,
            command_image_id=command_image_id,
        )

        return {
            "ok": True,
            "data": {
                "width": width,
                "height": height,
                "bpp": 4,
                "pixels": base64.b64encode(bytes(width * height * 4)).decode("ascii"),
            },
        }



    ##############################################
    ##                IMPORTING                 ##
    ##############################################

    def importImage(self, rData):
        #   Resolve the Target Image from Request Payload
        image = self.getActiveImage(rData)
        if image is None:
            return {"ok": False, "error": "No active image to import into"}

        #   Get Image Filepath from Request Data
        filePath = rData.get("path") if isinstance(rData, dict) else None
        if not filePath:
            return {"ok": False, "error": "Missing import path"}

        filePath = os.path.normpath(str(filePath))
        if not os.path.exists(filePath):
            return {"ok": False, "error": f"Import file does not exist: {filePath}"}

        #   Get Version Data from Request for Layer Naming
        version_data = rData.get("versionData") if isinstance(rData, dict) else {}
        command_image_id = rData.get("image_id") if isinstance(rData, dict) else None

        identifier_value = None
        version_value = None

        if isinstance(version_data, dict):
            identifier_value = version_data.get("identifier")
            version_value = version_data.get("version")

        if identifier_value in [None, ""] and isinstance(rData, dict):
            identifier_value = rData.get("identifier")

        if version_value in [None, ""] and isinstance(rData, dict):
            version_value = rData.get("version")

        desired_layer_name = None
        if identifier_value not in [None, ""] and version_value not in [None, ""]:
            desired_layer_name = f"{identifier_value}_{version_value}"

        #   Try the Known GIMP Layer-load Procedures
        procedure_names = ["gimp-file-load-layer", "file-open-as-layer"]
        procedure = None
        procedure_name = None
        for candidate in procedure_names:
            procedure = self.getPdbProcedure(candidate)
            if procedure:
                procedure_name = candidate
                break

        if not procedure:
            return {"ok": False, "error": "No compatible GIMP layer import procedure found"}

        #   Create a GIO File Object for the Import Path
        gio_file = self.getGioFile(filePath)
        if gio_file is None:
            return {"ok": False, "error": f"Could not create GIO file for: {filePath}"}

        try:
            #   Set up the Procedure Configuration
            config = procedure.create_config()
            run_mode = getattr(Gimp.RunMode, "NONINTERACTIVE", None)
            Helper.setConfigValue(config, "run-mode", run_mode)
            Helper.setConfigValue(config, "image", image)
            Helper.setConfigValue(config, "file", gio_file)

            #   Run the Procedure to Import the Image as a Layer
            result = procedure.run(config)
            layer = Helper.extractLayerFromResult(result)

            if layer is None:
                return {"ok": False, "error": f"Import procedure did not return a layer: {procedure_name}"}

            #   Get Insert Method for the Image and Insert the New Layer
            insert_layer = None
            for method_name in ["insert_layer", "add_layer"]:
                method = getattr(image, method_name, None)
                if callable(method):
                    insert_layer = method
                    break

            if insert_layer is None:
                return {"ok": False, "error": "Active image does not support layer insertion"}

            _, insert_error = Helper.callWithSignatures(
                insert_layer,
                [
                    (layer, None, 0),
                    (layer, 0),
                    (layer,),
                ],
            )
            if insert_error:
                return {"ok": False, "error": f"Failed to insert imported layer: {insert_error}"}

            #   Attempt to Set the Desired Layer Name Based on Version Data
            if desired_layer_name:
                try:
                    layer.set_name(str(desired_layer_name))
                except Exception:
                    try:
                        layer.name = str(desired_layer_name)
                    except Exception:
                        pass

            layer_name = None
            try:
                layer_name = layer.get_name()
            except Exception:
                layer_name = None

            self.addToLog(
                "Imported image as new layer",
                path=filePath,
                procedure=procedure_name,
                image_id=Helper.getImageId(image),
                command_image_id=command_image_id,
                layer_name=layer_name,
                version_identifier=(version_data.get("identifier") if isinstance(version_data, dict) else None),
            )

            #   Capture the Tattoo
            layer_tattoo = Helper.getLayerTattoo(layer)

            #   Refresh the Display to Show the New Layer
            self.refreshImageDisplay(image)

            return {
                "ok": True,
                "data": {
                    "imported": True,
                    "path": filePath,
                    "procedure": procedure_name,
                    "layerName": layer_name,
                    "layerTattoo": layer_tattoo,
                },
            }

        except Exception as exc:
            self.addToLog(
                "Failed to import image as layer",
                path=filePath,
                error=str(exc),
                procedure=procedure_name,
                command_image_id=command_image_id,
            )
            return {"ok": False, "error": str(exc), "data": {"path": filePath, "procedure": procedure_name}}


    #   Returns the Current Name of a Tracked Layer
    def getTrackedLayerName(self, rData):
        #   Resolve the Active Image from Gimp
        image = self.getActiveImage(rData)
        if image is None:
            return {"ok": False, "error": "No active image"}

        #   Resolve the Tracked Layer from the Request Data
        layer = self.resolveTrackedLayer(image, rData)
        if layer is None:
            return {"ok": True, "data": {"layerName": None, "found": False}}

        #   Attempt to Get the Layer Name
        layer_name = None
        try:
            layer_name = layer.get_name()
        except Exception:
            layer_name = None

        return {"ok": True, "data": {"layerName": layer_name, "found": True}}


    #   Renames a Tracked Layer in the Active Image
    def renameImageLayer(self, rData):
        #   Resolve the Active Image from Gimp
        image = self.getActiveImage(rData)
        if image is None:
            return {"ok": False, "error": "No active image"}

        #   Resolve the Tracked Layer and New Name from the Request Data
        layer_tattoo = rData.get("layerTattoo") if isinstance(rData, dict) else None
        new_name = rData.get("newName") if isinstance(rData, dict) else None
        command_image_id = rData.get("image_id") if isinstance(rData, dict) else None

        if layer_tattoo is None:
            return {"ok": False, "error": "Missing layerTattoo"}
        if not new_name:
            return {"ok": False, "error": "Missing newName"}

        #   Resolve the Tracked Layer from the Request Data
        layer = self.resolveTrackedLayer(image, rData)
        if layer is None:
            return {"ok": False, "error": f"Tracked layer {layer_tattoo} not found in active image"}

        #   Attempt to Set the New Layer Name
        try:
            layer.set_name(str(new_name))
        except Exception:
            try:
                layer.name = str(new_name)
            except Exception as exc:
                return {"ok": False, "error": f"Failed to rename layer: {exc}"}

        #   Read Back the Confirmed Name
        confirmed_name = None
        try:
            confirmed_name = layer.get_name()
        except Exception:
            confirmed_name = new_name

        self.addToLog(
            "Renamed imported image layer",
            image_id=Helper.getImageId(image),
            command_image_id=command_image_id,
            layer_tattoo=Helper.getLayerTattoo(layer),
            new_name=confirmed_name,
        )

        self.refreshImageDisplay(image)

        return {
            "ok": True,
            "data": {
                "layerName": confirmed_name,
                "layerTattoo": Helper.getLayerTattoo(layer),
            },
        }


    #   Resolves a Tracked Layer by Persistent Tattoo
    def resolveTrackedLayer(self, image:object, rData:dict | None) -> object | None:
        #   Get the Tracked Layer Tattoo from the Request Data
        layer_tattoo = rData.get("layerTattoo") if isinstance(rData, dict) else None
        if layer_tattoo is not None:
            layer = self.getLayerByTattoo(image, layer_tattoo)
            if layer is not None:
                return layer

            #   Debug Lookup Failures
            if image is not None:
                layer_snapshot = []
                for layer_item in (self.getImageDrawables(image) or []):
                    try:
                        get_name = getattr(layer_item, "get_name", None)
                        layer_name = get_name() if callable(get_name) else getattr(layer_item, "name", None)
                    except Exception:
                        layer_name = None

                    layer_snapshot.append({
                        "name": str(layer_name or ""),
                        "tattoo": Helper.getLayerTattoo(layer_item),
                    })

                self.addToLog(
                    "Tracked layer tattoo was not found in active image",
                    requested_layer_tattoo=layer_tattoo,
                    requested_layer_name=(rData.get("layerName") if isinstance(rData, dict) else None),
                    requested_desired_layer_name=(rData.get("desiredLayerName") if isinstance(rData, dict) else None),
                    available_layers=layer_snapshot,
                )

        return None


    #   Deletes a Named Imported Layer from the Active Image if it Exists
    def deleteImageLayer(self, rData):
        #   Resolve the Active Image from Gimp
        image = self.getActiveImage(rData)
        if image is None:
            return {"ok": False, "error": "No active image to delete layer from"}

        #   Attempt to Resolve the Tracked Layer from the Request Data
        target_layer = self.resolveTrackedLayer(image, rData)
        layer_name = rData.get("layerName") if isinstance(rData, dict) else None
        version_data = rData.get("versionData") if isinstance(rData, dict) else {}
        command_image_id = rData.get("image_id") if isinstance(rData, dict) else None

        #   If Layer Name Not Provided, Attempt to Derive from Version Data or Target Layer
        if layer_name in [None, ""]:
            identifier_value = None
            version_value = None

            if isinstance(version_data, dict):
                identifier_value = version_data.get("identifier")
                version_value = version_data.get("version")

            if identifier_value in [None, ""] and isinstance(rData, dict):
                identifier_value = rData.get("identifier")

            if version_value in [None, ""] and isinstance(rData, dict):
                version_value = rData.get("version")

            if identifier_value not in [None, ""] and version_value not in [None, ""]:
                layer_name = f"{identifier_value}_{version_value}"

        #   If Layer Name Still Not Provided and Target Layer Found, Attempt to Get Name from Target Layer
        if layer_name in [None, ""] and target_layer is None:
            return {
                "ok": True,
                "data": {
                    "deleted": False,
                    "reason": "missing-layer-name",
                },
            }

        #   If Target Layer Not Found but Layer Name Provided, Attempt to Find a Matching Layer by Name
        if target_layer is not None and layer_name in [None, ""]:
            try:
                layer_name = target_layer.get_name()
            except Exception:
                layer_name = None

        #   If Target Layer Still Not Found, Attempt to Find a Matching Layer by Name
        if target_layer is None:
            for layer in self.getImageDrawables(image):
                if layer is None:
                    continue

                current_name = None
                try:
                    current_name = layer.get_name()
                except Exception:
                    current_name = None

                if str(current_name or "") == str(layer_name):
                    target_layer = layer
                    break

        #   If Target Layer Still Not Found, Log and Return Success (Nothing to Delete)
        if target_layer is None:
            self.addToLog(
                "Import layer not found for deletion",
                image_id=Helper.getImageId(image),
                command_image_id=command_image_id,
                layer_name=layer_name,
            )
            return {
                "ok": True,
                "data": {
                    "deleted": False,
                    "layerName": layer_name,
                },
            }

        #   Attempt to  Remove the Layer from the Image
        try:
            _, remove_error = Helper.callWithSignatures(image.remove_layer, [(target_layer,)])
            if remove_error:
                raise RuntimeError(str(remove_error))
        except Exception:
            _result, error = self.runPdbProcedure(
                "gimp-image-remove-layer",
                {
                    "image": image,
                    "layer": target_layer,
                },
            )
            if error:
                return {"ok": False, "error": f"Failed to remove layer: {error}"}

        self.addToLog(
            "Deleted imported image layer",
            image_id=Helper.getImageId(image),
            command_image_id=command_image_id,
            layer_tattoo=Helper.getLayerTattoo(target_layer),
            layer_name=layer_name,
        )

        #   Refresh the Display to Update the Layer List
        self.refreshImageDisplay(image)

        return {"ok": True, "data": {"deleted": True, "layerName": layer_name}}


    #   Replaces the Image Content of a Tracked Layer with a New File
    def replaceLayerImage(self, rData):
        #   Resolve the Active Image from Gimp
        image = self.getActiveImage(rData)
        if image is None:
            return {"ok": False, "error": "No active image to replace layer in"}

        #   Get Replacement Image
        filePath = rData.get("path") if isinstance(rData, dict) else None
        if not filePath:
            return {"ok": False, "error": "Missing file path for replacement"}

        #   Normalize the File Path and Check if it Exists
        filePath = os.path.normpath(str(filePath))
        if not os.path.exists(filePath):
            return {"ok": False, "error": f"Replacement file does not exist: {filePath}"}

        #   Attempt to Resolve the Tracked Layer from the Request Data
        target_layer = self.resolveTrackedLayer(image, rData)
        if target_layer is None:
            self.addToLog(
                "replaceLayerImage could not resolve tracked layer",
                path=filePath,
                requested_layer_tattoo=(rData.get("layerTattoo") if isinstance(rData, dict) else None),
                requested_layer_name=(rData.get("layerName") if isinstance(rData, dict) else None),
                requested_desired_layer_name=(rData.get("desiredLayerName") if isinstance(rData, dict) else None),
            )
            return {"ok": False, "error": "Tracked layer not found in active image"}

        #   Get Command Image ID and Version Data for Logging Context
        command_image_id = rData.get("image_id") if isinstance(rData, dict) else None
        version_data = rData.get("versionData") if isinstance(rData, dict) else {}
        desired_layer_name = rData.get("desiredLayerName") if isinstance(rData, dict) else None
        if desired_layer_name is not None:
            desired_layer_name = str(desired_layer_name).strip() or None

        new_layer = None

        try:
            ##   Store Target Layer Properties

            #   Name
            target_name = self.getLayerProp(target_layer, ["get_name"], ["name"], default="")
            if desired_layer_name is not None:
                target_name = desired_layer_name

            #   Opacity
            target_opacity = self.getLayerProp(target_layer, ["get_opacity"], ["opacity"], default=None)

            #   Visibility
            target_visible = self.getLayerProp(target_layer, ["get_visible"], ["visible"], default=True)

            #   Blending/Composite Mode
            target_mode = self.getLayerProp(target_layer, ["get_mode"], ["mode"], default=None)
            target_blend_mode = self.getLayerProp(target_layer, ["get_blend_mode"], ["blend_mode"], default=None)
            target_blend_space = self.getLayerProp(target_layer, ["get_blend_space"], ["blend_space"], default=None)
            target_composite_mode = self.getLayerProp(target_layer, ["get_composite_mode"], ["composite_mode"], default=None)
            target_composite_space = self.getLayerProp(target_layer, ["get_composite_space"], ["composite_space"], default=None)

            #   Alpha Lock
            target_lock_alpha = self.getLayerProp(target_layer, ["get_lock_alpha"], ["lock_alpha"], default=None)

            #   Offsets (X/Y Position)
            target_offsets = self.getLayerProp(target_layer, ["get_offsets"], ["offsets"], default=None)

            #   Geometric Transform
            target_transform = self.getLayerProp(
                target_layer,
                ["get_transform", "get_transform_matrix", "get_matrix"],
                ["transform", "transform_matrix", "matrix"],
                default=None,
            )

            #   Parent Layer/Group and Position in Layer Stack
            target_parent = None
            try:
                target_parent, _parent_error = Helper.callWithSignatures(target_layer.get_parent, [(), (target_layer,)])
            except Exception:
                target_parent = None

            target_position = None
            try:
                all_layers = self.getImageDrawables(image)
                if target_layer in all_layers:
                    target_position = all_layers.index(target_layer)
            except Exception:
                target_position = None

            #   Dimensions
            target_width = self.getLayerProp(target_layer, ["get_width"], ["width"], default=None)
            target_height = self.getLayerProp(target_layer, ["get_height"], ["height"], default=None)

            self.addToLog(
                "replaceLayerImage resolved target layer",
                target_layer_tattoo=Helper.getLayerTattoo(target_layer),
                target_layer_name=target_name,
                target_width=target_width,
                target_height=target_height,
                requested_layer_tattoo=(rData.get("layerTattoo") if isinstance(rData, dict) else None),
            )

            #   Load Replacement Layer
            before_layers = list(self.getImageDrawables(image) or [])
            file_obj = self.getGioFile(filePath)

            result, load_error = self.runPdbProcedure(
                "gimp-file-load-layer",
                {
                    "image": image,
                    "file": file_obj,
                },
            )
            if load_error:
                result, load_error = self.runPdbProcedure(
                    "file-open-as-layer",
                    {
                        "image": image,
                        "file": file_obj,
                    },
                )

            if load_error:
                return {"ok": False, "error": f"Failed to load replacement image: {load_error}"}

            #   Ensure a Layer Object was Returned from the Load Procedure
            new_layer = Helper.extractLayerFromResult(result)
            if new_layer is None:
                after_layers = list(self.getImageDrawables(image) or [])
                for layer in after_layers:
                    if layer not in before_layers:
                        new_layer = layer
                        break

            if new_layer is None:
                return {"ok": False, "error": "Replacement layer load returned no layer"}

            #   Ensure Replacement Layer is Inserted
            current_layers = list(self.getImageDrawables(image) or [])
            if new_layer not in current_layers:
                insert_layer = getattr(image, "insert_layer", None) or getattr(image, "add_layer", None)
                if not callable(insert_layer):
                    return {"ok": False, "error": "Active image does not support layer insertion"}

                _insert_result, insert_error = Helper.callWithSignatures(
                    insert_layer,
                    [
                        (new_layer, target_parent, int(target_position or 0)),
                        (new_layer, None, int(target_position or 0)),
                        (new_layer, int(target_position or 0)),
                        (new_layer,),
                    ],
                )
                if insert_error:
                    return {"ok": False, "error": f"Failed to insert replacement layer: {insert_error}"}

                current_layers = list(self.getImageDrawables(image) or [])
                if new_layer not in current_layers:
                    return {"ok": False, "error": "Replacement layer was not added to image after insertion"}

            #   Attempt to Match the Replacement Layer's Dimensions to the Target Layer
            new_width = self.getLayerProp(new_layer, ["get_width"], ["width"], default=None)
            new_height = self.getLayerProp(new_layer, ["get_height"], ["height"], default=None)
            if target_width and target_height and new_width and new_height:
                if int(target_width) != int(new_width) or int(target_height) != int(new_height):
                    scale_error = None
                    scaled_ok = False

                    try:
                        _scaled, direct_error = Helper.callWithSignatures(
                            new_layer.scale,
                            [
                                (int(target_width), int(target_height), False),
                                (int(target_width), int(target_height)),
                            ],
                        )
                        if direct_error is None:
                            scaled_ok = True
                        else:
                            scale_error = direct_error
                    except Exception:
                        pass

                    #   Fallback to known PDB procedures.
                    if not scaled_ok:
                        proc_values = {
                            "item": new_layer,
                            "drawable": new_layer,
                            "new-width": int(target_width),
                            "new_height": int(target_height),
                            "new-height": int(target_height),
                            "new_width": int(target_width),
                            "width": int(target_width),
                            "height": int(target_height),
                        }

                        for scale_proc_name in ["gimp-item-scale", "gimp-layer-scale", "gimp-drawable-scale"]:
                            _scale_result, proc_error = self.runPdbProcedure(scale_proc_name, proc_values)
                            if proc_error is None:
                                scaled_ok = True
                                scale_error = None
                                break

                            scale_error = proc_error

                    if not scaled_ok:
                        raise RuntimeError(f"Failed to scale replacement layer: {scale_error or 'No compatible scale API available'}")

            #   Match the Replacement Layer's Properties to the Target Layer
            current_opacity = self.getLayerProp(new_layer, ["get_opacity"], ["opacity"], default=None)
            current_visible = self.getLayerProp(new_layer, ["get_visible"], ["visible"], default=None)
            current_mode = self.getLayerProp(new_layer, ["get_mode"], ["mode"], default=None)
            current_blend_mode = self.getLayerProp(new_layer, ["get_blend_mode"], ["blend_mode"], default=None)
            current_blend_space = self.getLayerProp(new_layer, ["get_blend_space"], ["blend_space"], default=None)
            current_composite_mode = self.getLayerProp(new_layer, ["get_composite_mode"], ["composite_mode"], default=None)
            current_composite_space = self.getLayerProp(new_layer, ["get_composite_space"], ["composite_space"], default=None)
            current_lock_alpha = self.getLayerProp(new_layer, ["get_lock_alpha"], ["lock_alpha"], default=None)
            current_offsets = self.getLayerProp(new_layer, ["get_offsets"], ["offsets"], default=None)
            current_transform = self.getLayerProp(
                new_layer,
                ["get_transform", "get_transform_matrix", "get_matrix"],
                ["transform", "transform_matrix", "matrix"],
                default=None,
            )

            #   Only Set Properties that Differ from the Target Layer
            if target_opacity is not None and current_opacity is not None and float(current_opacity) != float(target_opacity):
                self.setLayerProp(new_layer, ["set_opacity"], float(target_opacity), ["opacity"])

            if current_visible is None or bool(current_visible) != bool(target_visible):
                self.setLayerProp(new_layer, ["set_visible"], bool(target_visible), ["visible"])

            if target_mode is not None and current_mode != target_mode:
                self.setLayerProp(new_layer, ["set_mode"], target_mode, ["mode"])

            if target_blend_mode is not None and current_blend_mode != target_blend_mode:
                self.setLayerProp(new_layer, ["set_blend_mode"], target_blend_mode, ["blend_mode"])

            if target_blend_space is not None and current_blend_space != target_blend_space:
                self.setLayerProp(new_layer, ["set_blend_space"], target_blend_space, ["blend_space"])

            if target_composite_mode is not None and current_composite_mode != target_composite_mode:
                self.setLayerProp(new_layer, ["set_composite_mode"], target_composite_mode, ["composite_mode"])

            if target_composite_space is not None and current_composite_space != target_composite_space:
                self.setLayerProp(new_layer, ["set_composite_space"], target_composite_space, ["composite_space"])

            if target_lock_alpha is not None and current_lock_alpha != target_lock_alpha:
                self.setLayerProp(new_layer, ["set_lock_alpha"], target_lock_alpha, ["lock_alpha"])

            if target_transform is not None and current_transform != target_transform:
                transform_applied = self.setLayerProp(
                    new_layer,
                    ["set_transform", "set_transform_matrix", "set_matrix"],
                    target_transform,
                    ["transform", "transform_matrix", "matrix"],
                )
                if not transform_applied:
                    self.addToLog(
                        "Replacement layer transform could not be applied on this Gimp build",
                        layer_name=target_name,
                    )

            if isinstance(target_offsets, (tuple, list)) and len(target_offsets) >= 2:
                offsets_match = False
                if isinstance(current_offsets, (tuple, list)) and len(current_offsets) >= 2:
                    offsets_match = (
                        int(current_offsets[0]) == int(target_offsets[0])
                        and int(current_offsets[1]) == int(target_offsets[1])
                    )

                if not offsets_match:
                    try:
                        Helper.callWithSignatures(
                            new_layer.set_offsets,
                            [
                                (int(target_offsets[0]), int(target_offsets[1])),
                                (new_layer, int(target_offsets[0]), int(target_offsets[1])),
                            ],
                        )
                    except Exception:
                        pass

            #   Move the Replacement Layer to the Target Layer's Position in the Layer Stack if Needed
            if target_position is not None:
                current_parent = None
                try:
                    current_parent, _parent_error = Helper.callWithSignatures(new_layer.get_parent, [(), (new_layer,)])
                except Exception:
                    current_parent = None

                current_position = None
                try:
                    current_layers = list(self.getImageDrawables(image) or [])
                    if new_layer in current_layers:
                        current_position = current_layers.index(new_layer)
                except Exception:
                    current_position = None

                if current_parent != target_parent or current_position != int(target_position):
                    _move_result, move_error = self.runPdbProcedure(
                        "gimp-image-reorder-item",
                        {
                            "image": image,
                            "item": new_layer,
                            "new-parent": target_parent,
                            "new-position": int(target_position),
                        },
                    )
                    if move_error:
                        self.addToLog("Could not reorder replacement layer", error=str(move_error))

            try:
                _result, remove_error = Helper.callWithSignatures(image.remove_layer, [(target_layer,)])
                if remove_error:
                    raise RuntimeError(f"Failed to remove original layer: {remove_error}")
            except Exception:
                _result, remove_error = self.runPdbProcedure(
                    "gimp-image-remove-layer",
                    {
                        "image": image,
                        "layer": target_layer,
                    },
                )
                if remove_error:
                    raise RuntimeError(f"Failed to remove original layer: {remove_error}")

            #   Rename After Old Layer Deletion to Avoid Gimp Auto-appending "#1"
            if target_name:
                self.setLayerProp(new_layer, ["set_name"], target_name, ["name"])

            new_layer_name = self.getLayerProp(new_layer, ["get_name"], ["name"], default=target_name)
            if target_name and new_layer_name != target_name:
                if re.search(r"\s#\d+$", str(new_layer_name or "")):
                    temp_name = f"__prism_replace_tmp__{int(time.time() * 1000)}"
                    self.setLayerProp(new_layer, ["set_name"], temp_name, ["name"])

                    try:
                        Gimp.displays_flush()
                    except Exception:
                        pass

                    self.setLayerProp(new_layer, ["set_name"], target_name, ["name"])
                    new_layer_name = self.getLayerProp(new_layer, ["get_name"], ["name"], default=target_name)

                self.addToLog(
                    "Replacement layer name differs after collision-avoid rename",
                    desired_layer_name=target_name,
                    actual_layer_name=new_layer_name,
                )

            new_layer_tattoo = Helper.getLayerTattoo(new_layer)

            #   Refresh Image
            try:
                Gimp.displays_flush()
            except Exception:
                pass

            self.addToLog(
                "Updated layer image to new version",
                path=filePath,
                image_id=Helper.getImageId(image),
                command_image_id=command_image_id,
                previous_layer_tattoo=Helper.getLayerTattoo(target_layer),
                layer_tattoo=new_layer_tattoo,
                layer_name=new_layer_name,
                version_identifier=(version_data.get("identifier") if isinstance(version_data, dict) else None),
            )

            self.refreshImageDisplay(image)

            return {
                "ok": True,
                "data": {
                    "replaced": True,
                    "path": filePath,
                    "layerName": new_layer_name,
                    "layerTattoo": new_layer_tattoo,
                },
            }

        except Exception as exc:
            if new_layer is not None:
                try:
                    if new_layer in list(self.getImageDrawables(image) or []):
                        try:
                            Helper.callWithSignatures(image.remove_layer, [(new_layer,)])
                        except Exception:
                            self.runPdbProcedure(
                                "gimp-image-remove-layer",
                                {
                                    "image": image,
                                    "layer": new_layer,
                                },
                            )
                except Exception:
                    pass

            self.addToLog(
                "Failed to replace layer image",
                path=filePath,
                error=str(exc),
                command_image_id=command_image_id,
            )
            return {"ok": False, "error": str(exc), "data": {"path": filePath}}


    ###############################
    ##           RENDER          ##
    ###############################

    #   Exports the Active Image to a Target Path Using Gimp File-save
    def exportImage(self, rData):
        #   Resolve the Active Image from Gimp
        image = self.getActiveImage(rData)
        if image is None:
            return {"ok": False, "error": "No active image to export"}

        #   Get the Image ID for Logging and Context Change Detection
        image_id = Helper.getImageId(image)
        command_image_id = rData.get("image_id") if isinstance(rData, dict) else None

        #   Resolve the Export File Path from the Request Data
        filePath = rData.get("path") if isinstance(rData, dict) else None
        if not filePath:
            return {"ok": False, "error": "Missing export file path"}

        filePath = os.path.normpath(str(filePath))
        file_ext = os.path.splitext(filePath)[1].lower()

        #   Get Config Settings
        settings = rData.get("settings") if isinstance(rData, dict) else {}
        if not isinstance(settings, dict):
            settings = {}

        #   Handle TIF Export Settings
        is_tiff_export = file_ext in [".tif", ".tiff"]
        tiff_save_layers_enabled = Helper.bitToBool(settings.get("tiff_SaveLayers"), True)
        requires_flat_tiff = False

        if is_tiff_export and not tiff_save_layers_enabled:
            supports_tiff_layer_keys, unsupported_tiff_layer_keys = self.procedureConfigSupportsKeys(
                "file-tiff-export",
                {
                    "save-layers": False,
                    "crop-layers": True,
                },
            )

            if not supports_tiff_layer_keys:
                requires_flat_tiff = True
                self.addToLog(
                    "TIFF save-layers unsupported; using compatibility preprocessing",
                    unsupported_keys=unsupported_tiff_layer_keys,
                    requested_save_layers=False,
                    image_id=image_id,
                )

        #   Get the Export Scale and Color Mode
        try:
            scale_percent = int(settings.get("exportScale") or 100)
        except Exception:
            scale_percent = 100

        scale_percent = max(1, min(scale_percent, 1000))

        output_color_mode = str(settings.get("colorMode") or "").upper()
        supports_color_mode = output_color_mode in ("RGB", "RGBA", "GRAY", "GRAYA")

        #   Create Temp Duplicated Image if any Preprocessing is Needed
        export_image = image
        used_temp_image = False

        if scale_percent != 100 or supports_color_mode or requires_flat_tiff:
            temp_image, duplicate_error = self.duplicateImage(image)
            if temp_image is not None:
                export_image = temp_image
                used_temp_image = True
            else:
                self.addToLog("Could not duplicate image for export preprocessing", error=str(duplicate_error))

        if (scale_percent != 100 or supports_color_mode or requires_flat_tiff) and not used_temp_image:
            message = "Failed to prepare temporary image for export preprocessing"
            return {
                "ok": False,
                "error": message,
                "data": {
                    "scale": scale_percent,
                    "color_mode": output_color_mode if supports_color_mode else None,
                    "flat_tiff": requires_flat_tiff,
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
        
        #   Convert Color Mode if Needed
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

        if requires_flat_tiff and used_temp_image:
            ok, flatten_error = self.mergeVisibleLayersForExport(export_image)
            if not ok:
                return {
                    "ok": False,
                    "error": f"TIFF compatibility preprocessing failed: {flatten_error}",
                    "data": {"flat_tiff": True},
                }

        #   Convert the File Path to a GIO File Object
        gio_file = self.getGioFile(filePath)
        run_mode = getattr(Gimp.RunMode, "NONINTERACTIVE", None)
        active_drawable = self.getActiveDrawable(export_image)

        proc_values = {
            "run-mode": run_mode,
            "image": export_image,
            "file": gio_file,
        }

        #   Get Export Proc Name
        procedure_name = self.getExporterProcedureName(filePath)

        if procedure_name == "gimp-file-save":
            proc_values["drawable"] = active_drawable
        else:
            proc_values.update(self.getExporterConfigValues(procedure_name, settings))

        result, save_error = self.runPdbProcedure(procedure_name, proc_values)

        try:
            if save_error is None:
                self.addToLog(
                    "Exported image from Gimp",
                    path=filePath,
                    procedure=procedure_name,
                    image_id=image_id,
                    command_image_id=command_image_id,
                    scale=scale_percent,
                    color_mode=output_color_mode if supports_color_mode else None,
                    tiff_save_layers=(tiff_save_layers_enabled if procedure_name == "file-tiff-export" else None),
                    tiff_flatten_compat=(requires_flat_tiff if procedure_name == "file-tiff-export" else None),
                )
                return {"ok": True, "data": {"exported": True, "path": filePath, "procedure": procedure_name}}

            self.emitGimpWarning(
                "Failed to export image from Gimp",
                path=filePath,
                procedure=procedure_name,
                error=str(save_error),
                image_id=image_id,
                command_image_id=command_image_id,
            )
            return {
                "ok": False,
                "error": str(save_error),
                "data": {
                    "path": filePath,
                    "procedure": procedure_name,
                    "scale": scale_percent,
                    "color_mode": output_color_mode if supports_color_mode else None,
                    "result": str(result) if result is not None else None,
                },
            }

        finally:
            if used_temp_image:
                self.deleteImage(export_image)


    #   Merges Visible Layers into one Layer for Flat Export Fallback
    def mergeVisibleLayersForExport(self, image):
        if image is None:
            return False, "No image provided"

        try:
            #   Try to merge visible layers using the available method
            try:
                merged_layer = image.merge_visible_layers()
                if merged_layer is not None:
                    self.addToLog("TIFF compatibility merged visible layers")
                    return True, None
            except Exception:
                pass

            #   Fall back to PDB procedure - use CLIP_TO_IMAGE mode (value 1)
            _result, error = self.runPdbProcedure(
                "gimp-image-merge-visible-layers", 
                {"image": image, "merge-type": 1}  # CLIP_TO_IMAGE = 1
            )
            if error is None:
                self.addToLog("TIFF compatibility merged visible layers via PDB")
                return True, None

            #   If merge-type fails, try without it
            _result, error = self.runPdbProcedure(
                "gimp-image-merge-visible-layers", 
                {"image": image}
            )
            if error is None:
                self.addToLog("TIFF compatibility merged visible layers via PDB (no merge-type)")
                return True, None

            return False, f"Could not merge visible layers: {error}"
        
        except Exception as exc:
            return False, f"Export merge preprocessing failed: {str(exc)}"


    #   Converts Image Precision (Bit Depth / Gamma) to the Target Value
    def convertImagePrecision(self, image, target_precision_int):
        #   Attempt to Resolve the Gimp.Precision Enum Value for the Target
        precision_enum = None
        precision_type = getattr(Gimp, "Precision", None)
        if precision_type is not None:
            for attr in dir(precision_type):
                try:
                    val = getattr(precision_type, attr)
                    if int(val) == target_precision_int:
                        precision_enum = val
                        break
                except Exception:
                    continue

        target_value = precision_enum if precision_enum is not None else target_precision_int

        #   Try Direct Image Method First
        try:
            image.convert_precision(target_value)
            return True, None
        except Exception:
            pass

        #   Fall Back to PDB Procedure
        _result, error = self.runPdbProcedure(
            "gimp-image-convert-precision",
            {"image": image, "precision": target_value},
        )
        if error is None:
            return True, None

        return False, error


    #   Resolves Target Precision ID from Format, Bit Depth, Gamma using IMAGEPRECISIONDATA
    def getTargetPrecisionForExport(self, filePath, bit_depth, output_gamma):
        ext = os.path.splitext(str(filePath or ""))[1].lower()
        bit_depth_str = str(bit_depth or "").strip()
        gamma_label = "Linear" if str(output_gamma or "").strip().lower() == "linear" else "sRGB"

        if bit_depth_str not in ["8", "16", "32"]:
            return None

        if bit_depth_str == "8":
            display_label = "8-bit Integer"
        elif bit_depth_str == "16":
            #   EXR 16-bit is half-float; other supported formats use 16-bit integer.
            display_label = "16-bit Half Float" if ext == ".exr" else "16-bit Integer"
        else:
            #   EXR/PSD 32-bit workflows are float-based.
            display_label = "32-bit Float" if ext in [".exr", ".psd"] else "32-bit Integer"

        for precision_id, meta in IMAGEPRECISIONDATA.items():
            if meta.get("display") == display_label and meta.get("gamma") == gamma_label:
                return precision_id

        return None


    #   Maps Output Extension to Exporter Procedure
    def getExporterProcedureName(self, filePath):
        ext = os.path.splitext(str(filePath or ""))[1].lower()
        return EXPORTER_PROCEDURE_MAP.get(ext, "gimp-file-save")


    #   Maps UI colorMode/bitDepth to PNG Export 
    def getPngFormatChoice(self, settings):
        color_mode = str(settings.get("colorMode") or "").upper()
        bit_depth = str(settings.get("png_BitDepth") or "").strip()
        if bit_depth not in ["8", "16"]:
            return "auto"
        return PNG_FORMAT_MAP.get((color_mode, bit_depth), "auto")


    #   Builds Exporter-specific Config Values from Prism Render Settings
    def getExporterConfigValues(self, procedure_name, settings):
        values = {}

        if procedure_name == "file-png-export":
            try:
                compression = int(settings.get("png_Compress") or 10) - 1
            except Exception:
                compression = 9

            compression = max(0, min(compression, 9))

            values.update(
                {
                    "interlaced": Helper.bitToBool(settings.get("png_Interlaced"), False),
                    "compression": compression,
                    "bkgd": Helper.bitToBool(settings.get("png_BgColor"), False),
                    "offs": Helper.bitToBool(settings.get("png_LayerOffset"), False),
                    "phys": Helper.bitToBool(settings.get("png_Rez"), True),
                    "save-transparent": Helper.bitToBool(settings.get("png_AlphaColor"), False),
                    "format": self.getPngFormatChoice(settings),
                }
            )

        elif procedure_name == "file-jpeg-export":
            try:
                quality = float(settings.get("jpg_Quality") or 0.9)
            except Exception:
                quality = 0.9

            try:
                smoothing = float(settings.get("jpg_Smoothing") or 0.0)
            except Exception:
                smoothing = 0.0

            values.update(
                {
                    "quality": max(0.0, min(quality, 1.0)),
                    "smoothing": max(0.0, min(smoothing, 1.0)),
                    "optimize": Helper.bitToBool(settings.get("jpg_Optimize"), True),
                    "progressive": Helper.bitToBool(settings.get("jpg_Progressive"), False),
                    "baseline": Helper.bitToBool(settings.get("jpg_Baseline"), True),
                    "sub-sampling": JPEG_SUBSAMPLING_MAP.get(str(settings.get("jpg_SubSample") or "4:2:2"), "sub-sampling-2x1"),
                }
            )

        elif procedure_name == "file-tiff-export":
            tiff_save_layers = Helper.bitToBool(settings.get("tiff_SaveLayers"), True)
            values.update(
                {
                    "save-layers": tiff_save_layers,
                    "crop-layers": True,
                    "bigtiff": Helper.bitToBool(settings.get("tiff_useBigTiff"), False),
                    "compression": TIFF_COMPRESSION_MAP.get(settings.get("tiff_Compression"), "none"),
                    "save-transparent-pixels": Helper.bitToBool(settings.get("tiff_SaveTransPx"), True),
                }
            )

        elif procedure_name == "file-pdf-export":
            values.update(
                {
                    "ignore-hidden": Helper.bitToBool(settings.get("pdf_OmitHidden"), True),
                    "vectorize": Helper.bitToBool(settings.get("pdf_ConvertToVector"), True),
                    "apply-masks": Helper.bitToBool(settings.get("pdf_ApplyLayers"), True),
                }
            )

        elif procedure_name == "file-psd-export":
            values.update(
                {
                    "cmyk": False,
                    "duotone": False,
                }
            )

        return values



    #################################################
    ##              SM STATE HANDLING              ##
    #################################################

    #   Saves Prism StateManager State JSON as a Parasite on the Active Image
    def saveStates(self, rData):
        #   Resolve the Active Image from Gimp
        image = self.getActiveImage(rData)
        if image is None:
            return {"ok": False, "error": "No active image to save states on"}

        #   Get the Image ID for Logging and Context Change Detection
        image_id = Helper.getImageId(image)
        command_image_id = rData.get("image_id") if isinstance(rData, dict) else None

        #   Resolve the State Data from the Request
        state_data = rData.get("stateData") if isinstance(rData, dict) else None
        if state_data is None:
            return {"ok": False, "error": "Missing stateData in request"}

        try:
            #   Convert the State Data to Bytes if it's a String
            data_bytes = state_data.encode("utf-8") if isinstance(state_data, str) else bytes(state_data)

            state_count = None
            try:
                #   Attempt to Parse the State Data as JSON to Count the Number of States for Logging
                parsed_state = json.loads(state_data) if isinstance(state_data, str) else None
                if isinstance(parsed_state, dict) and isinstance(parsed_state.get("states"), list):
                    state_count = len(parsed_state.get("states"))

            except Exception:
                state_count = None

            #   Create a New Parasite with the State Data
            parasite = Gimp.Parasite.new("PrismStates", 1, data_bytes)

            #   Attach the Parasite to the Image
            attach = getattr(image, "attach_parasite", None) or getattr(image, "parasite_attach", None)
            if not callable(attach):
                return {"ok": False, "error": "No parasite attach method available on image"}

            attach(parasite)
            self.addToLog(
                "Saved Prism states to Gimp scenefile",
                image_id=image_id,
                command_image_id=command_image_id,
                state_bytes=len(data_bytes),
                state_count=state_count,
            )
            return {"ok": True}

        except Exception as exc:
            self.addToLog(
                "Failed to save Prism states Gimp scenefile",
                error=str(exc),
                image_id=image_id,
                command_image_id=command_image_id,
            )
            return {"ok": False, "error": str(exc)}


    #   Reads Prism StateManager State JSON from a Parasite on the Active Image
    def getStates(self, rData=None):
        #   Resolve the Active Image from Gimp
        image = self.getActiveImage(rData)
        command_image_id = rData.get("image_id") if isinstance(rData, dict) else None
        if image is None:
            return {"ok": True, "data": {"stateData": ""}}

        #   Get the Image ID for Logging and Context Change Detection
        image_id = Helper.getImageId(image)

        try:
            #   Attempt to Find the Parasite Containing the Prism State Data
            find = getattr(image, "get_parasite", None) or getattr(image, "parasite_find", None)
            if not callable(find):
                return {"ok": True, "data": {"stateData": ""}}

            parasite = find("PrismStates")
            if not parasite:
                return {"ok": True, "data": {"stateData": ""}}

            #   Get the Raw State Data from the Parasite
            try:
                raw = parasite.get_data()
            except AttributeError:
                raw = getattr(parasite, "data", None)

            if raw is None:
                return {"ok": True, "data": {"stateData": ""}}

            #   Convert the Raw State Data to a String if it's in Bytes
            raw_bytes = b""
            if isinstance(raw, tuple):
                for item in raw:
                    raw_bytes = Helper.toBytes(item)
                    if raw_bytes:
                        break
            else:
                raw_bytes = Helper.toBytes(raw)

            #   Decode the Raw Bytes as UTF-8
            if raw_bytes:
                state_data = raw_bytes.decode("utf-8", errors="replace")
            elif isinstance(raw, str):
                state_data = raw
            else:
                state_data = ""

            state_count = None
            try:
                #    Parse the State Data as JSON to Count the Number of States for Logging
                parsed_state = json.loads(state_data) if isinstance(state_data, str) and state_data else None
                if isinstance(parsed_state, dict) and isinstance(parsed_state.get("states"), list):
                    state_count = len(parsed_state.get("states"))

            except Exception:
                state_count = None

            self.addToLog(
                "Read Prism states from Gimp scenefile",
                image_id=image_id,
                command_image_id=command_image_id,
                state_bytes=(len(state_data.encode("utf-8", errors="replace")) if isinstance(state_data, str) else 0),
                state_count=state_count,
            )

            return {
                "ok": True,
                "data": {
                    "stateData": state_data,
                    "imageId": image_id,
                    "commandImageId": command_image_id,
                },
            }

        except Exception as exc:
            self.addToLog(
                "Failed to read Prism states parasite",
                error=str(exc),
                image_id=image_id,
                command_image_id=command_image_id,
            )
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
        #   If Not Forcing Launch and Host is Responsive, No Action Needed
        if not force and self.isPrismHostResponsive():
            return

        #   If Not Forcing Launch but Host Socket is Unresponsive, Attempt Recovery Before Launching
        if not force and Helper.canConnectToPrism(self.bridgePort_out):
            self.addToLog("Detected unresponsive Prism Host socket, attempting recovery")
            self.recoverUnresponsiveHost()

        hostScript = Helper.getHostScriptPath()
        deadline = time.time() + self.hostStartTimeout

        #   Try to Launch Host with Each Python Until Responsive or Deadline Exceeded
        for python_command in Helper.getHostPythonCommands():
            if not force and self.isPrismHostResponsive():
                return

            self.addToLog("Launching Prism Host", python_command=" ".join(python_command), forced=force)

            process = self.startPrismHost(python_command, hostScript)
            attempt_deadline = min(deadline, time.time() + 3.0)
            launch_time = time.time()

            #   Wait for the Process to Start and Host to Become Responsive, or Process to Exit, or Deadline to Pass
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

            # If Not Forcing Launch, Wait for Host to Become Responsive if Process is Still Running
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

        #   Get the Parent PID for Host Monitoring
        parent_pid = self.getHostParentPid()

        #   Construct the Command Line Args and Enviro Vars for the Host Process
        launch_args = list(python_command) + [
            host_script_path,
            "--parent-pid",
            str(parent_pid),
            "--prism-root",
            PRISM_ROOT,
        ]

        #   Set Up Environment Variables for the Host Process, Including Log Paths and Settings
        launch_env = os.environ.copy()
        launch_env["PRISM_GIMP_LOG_PATH"] = Helper.getLogPath()
        launch_env["PRISM_GIMP_LOG_BACKUP_PATH"] = Helper.getBackupLogPath()
        launch_env["PRISM_GIMP_log_maxBytes"] = str(self.log_maxBytes)

        popen_kwargs = {
            "cwd": os.path.dirname(host_script_path),
            "env": launch_env,
        }

        #   On Windows, Use Creation Flags to Detach the Process and Suppress Console Window
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

        #   Fallback: Disable Parent Monitor
        return 0


    #   Resets the Prism Host by Terminating the Process and Restarting it
    def resetPrismHost(self) -> None:
        self.addToLog("Reset Prism requested")

        #   Attempt to Read the Host PID from State
        host_pid = Helper.readHostPid()

        #   Terminate the Process and Wait for it to Exit Before Launching a New Instance
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
        #   Look up the Command Data for this Procedure
        procedure_data = self.PROCEDURES.get(procedure.get_name())

        if not procedure_data:
            return procedure.new_return_values(Gimp.PDBStatusType.CALLING_ERROR, None)

        try:
            #   Get the Image ID and Pass it as a Hint to the Host
            hinted_image_id = None
            if image is not None:
                try:
                    hinted_image_id = int(image.get_id())
                except Exception:
                    hinted_image_id = None

            #   Set the Image ID Hint in the Bridge Runtime for the Host to Use in Context-Aware Commands
            BRIDGE_RUNTIME.setImageHint(hinted_image_id)

            #   Handle Reset Directly in the Bridge Runtime Instead of Sending to Host
            if procedure_data["command"] == "resetPrism":
                self.addToLog("Running Prism command", command=procedure_data["command"])
                self.resetPrismHost()

            else:
                command_payload = {}
                if hinted_image_id is not None:
                    command_payload["image_id"] = hinted_image_id

                self.addToLog(
                    "Running Prism command",
                    command=procedure_data["command"],
                    image_hint_id=hinted_image_id,
                )
                command_ok = self.sendToPrism(procedure_data["command"], payload=command_payload)

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
        #   Create the Persistent Bridge Procedure that Auto-Starts the Prism Host and Bridge Service When Gimp Loads
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

        #   Create a Procedure for the Prism Menu Item
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



