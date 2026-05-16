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


import os
import sys
import platform
import logging
import time
import json
import base64
import socket
from typing import TYPE_CHECKING


from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

if eval(os.getenv("PRISM_DEBUG", "False")):
    try:
        del sys.modules["widget_import_scenedata"]
    except:
        pass

from PrismUtils.Decorators import err_catcher as err_catcher


PLUGINROOT = os.path.dirname(os.path.dirname(__file__))
SETTINGS_FILE_NAME = "Prism_Gimp_Settings.json"
THUMB_TILE_SIZE = 12
THUMB_COLOR_LIGHT = QColor(150, 150, 150)
THUMB_COLOR_DARK = QColor(75, 75, 75)


if TYPE_CHECKING:
    from PrismCore import PrismCore
    from ProjectBrowser import ProjectBrowser
    from PrismSettings import UserSettings
    from StateManager import StateManager


logger = logging.getLogger(__name__)


class Prism_Gimp_Functions(object):
    def __init__(self, core:"PrismCore", plugin):
        self.core = core
        self.plugin = plugin
        self.noImagePopupTime = 0.0
        self.pendingBridgeImageId = None
        self.saveCommentBridgeImageId = None
        self.pendingThumbnailBridgeImageId = None
        self.stateManagerBridgeImageId = None
        self.lastResolvedImageKey = None
        self.suppressStateSaveUntil = 0.0

        try:
            self.loadSettings()
        except Exception:
            pass

        #  CALLBACKS
        self.core.registerCallback("onProjectBrowserStartup", self.onProjectBrowserStartup, plugin=self.plugin, priority=20)
        self.core.registerCallback("onUserSettingsOpen", self.onUserSettingsOpen, plugin=self.plugin, priority=20)
        self.core.registerCallback("onUserSettingsSave", self.onUserSettingsSave, plugin=self.plugin, priority=20)
        self.core.registerCallback("onStateManagerOpen", self.onStateManagerOpen, plugin=self.plugin, priority=20)
        self.core.registerCallback("onStateManagerShow", self.onStateManagerShow, plugin=self.plugin, priority=20)
        self.core.registerCallback("onStateManagerClose", self.onStateManagerClose, plugin=self.plugin, priority=20)


    @err_catcher(name=__name__)
    def startup(self, origin:"PrismCore"):
        if platform.system() == "Linux":
            origin.timer.stop()

            if "prism_project" in os.environ and os.path.exists(os.environ["prism_project"]):
                curPrj = os.environ["prism_project"]

            else:
                curPrj = self.core.getConfig("globals", "current project")

            if curPrj != "":
                self.core.changeProject(curPrj)
            return False

        styleSheet = self.core.setActiveStyleSheet("Gimp")

        qapp = QApplication.instance()

        if qapp:
            for w in qapp.topLevelWidgets():
                w.setStyleSheet(styleSheet["css"])
                w.update()

        appIcon = QIcon(os.path.join(self.core.prismRoot, "Scripts", "UserInterfacesPrism", "p_tray.png"))
        qapp.setWindowIcon(appIcon)

        origin.timer.stop()
        origin.startAutosaveTimer()


    #   Load from Prism User Settings    
    @err_catcher(name=__name__)
    def loadSettings(self):
        sharedSettings = self.loadSharedSettings()
        coreSettings = self.core.getConfig("Gimp")
        self.gimpSettings = {}

        if isinstance(coreSettings, dict):
            self.gimpSettings.update(coreSettings)

        if isinstance(sharedSettings, dict):
            self.gimpSettings.update(sharedSettings)

        if not self.gimpSettings:
            logger.debug("Gimp settings not found.")
            self.gimpSettings = self.createDefaultSettings()

        logger.debug("Loaded Gimp Settings")


    #   Return Settings File Path
    @err_catcher(name=__name__)
    def getSharedSettingsPath(self) -> str:
        overridePath = os.environ.get("PRISM_GIMP_SETTINGS_PATH")
        if overridePath:
            return overridePath

        return os.path.join(PLUGINROOT, SETTINGS_FILE_NAME)


    #   Read Settings Json File
    @err_catcher(name=__name__)
    def loadSharedSettings(self) -> dict:
        settingsPath = self.getSharedSettingsPath()

        try:
            with open(settingsPath, "r", encoding="utf-8") as handle:
                settingsData = json.load(handle)
        except Exception:
            return {}

        if not isinstance(settingsData, dict):
            return {}

        return settingsData


    #   Get Defaults from Variables and Save to User Settings (Prism.json)    
    @err_catcher(name=__name__)
    def createDefaultSettings(self):
        sData = {}
        #   Get Defaults from Variables
        sData["Gimp"] = self.gimpDefaults

        #   Save to User Settings
        self.core.setConfig(data=sData)

        logger.debug("Created new Gimp settings.")
        return self.gimpDefaults



    #######################################
    ##             Helpers               ##   
    #######################################

    #   Return Current Image Context from Active Gimp Image
    @err_catcher(name=__name__)
    def resolveCurrentImageContext(self) -> dict:
        #   Send Request to Gimp Bridge
        response = self.sendCmdToGimp(
            action="get-current-file-name",
            payload={},
            timeout=2.0,
        )

        #   Return Empty Dict if No Response or Error from Bridge
        if not response or not response.get("ok"):
            return {
                "key": "none",
                "path": "",
                "name": "",
                "imageId": None,
            }

        data = response.get("data") or {}
        path = str(data.get("path") or "").strip()
        name = str(data.get("name") or "").strip()

        #   Build Context Key from Available Data
        raw_image_id = data.get("imageId")
        try:
            image_id = int(raw_image_id) if raw_image_id is not None else None
        except Exception:
            image_id = None

        #   Get Key from: Image Id, or Path, or Name, or None
        if path:
            key = f"path:{path.lower()}"
        elif image_id is not None:
            key = f"id:{image_id}"
        elif name:
            key = f"name:{name}"
        else:
            key = "none"

        context = {
            "key": key,
            "path": path,
            "name": name,
            "imageId": image_id,
        }

        #   Log when the Active Image Context Changed Between Requests
        if key != self.lastResolvedImageKey:
            self.lastResolvedImageKey = key
            logger.debug(
                "Active image context changed",
                extra={
                    "image_id": image_id,
                    "path": path,
                    "name": name,
                },
            )

        return context


    #   Build Payload from Current Active Image Id
    @err_catcher(name=__name__)
    def getCurrentImagePayload(self) -> dict:
        context = self.resolveCurrentImageContext()
        image_id = context.get("imageId")

        if image_id is None:
            return {}

        return {"image_id": image_id}


    #   If State Manager has an Active Image Id or Fall Back to Current Active Image
    @err_catcher(name=__name__)
    def getStateManagerImagePayload(self) -> dict:
        if self.stateManagerBridgeImageId is not None:
            return {"image_id": self.stateManagerBridgeImageId}

        return self.getCurrentImagePayload()
    

    #   Store Requested Image Id for Next Bridge Action
    @err_catcher(name=__name__)
    def setPendingBridgeImageFromRequest(self, requestData):
        image_id = None

        if isinstance(requestData, dict):
            raw_image_id = requestData.get("image_id")
            if raw_image_id is not None:
                try:
                    image_id = int(raw_image_id)

                except Exception:
                    image_id = None

        self.pendingBridgeImageId = image_id


    #   Merge Extra Payload with Active Bridge Image Id
    @err_catcher(name=__name__)
    def getBridgeImagePayload(self, extraPayload:dict=None) -> dict:
        payload = dict(extraPayload or {})

        image_id = None

        if self.pendingBridgeImageId is not None:
            image_id = self.pendingBridgeImageId

        elif self.pendingThumbnailBridgeImageId is not None:
            image_id = self.pendingThumbnailBridgeImageId

        elif self.saveCommentBridgeImageId is not None:
            image_id = self.saveCommentBridgeImageId

        if image_id is not None:
            payload["image_id"] = image_id

        return payload


    #   Extract Error Message from a Bridge Response
    def _responseError(self, response) -> str:
        if isinstance(response, dict):
            return response.get("error") or "Unknown bridge error"

        return "Unknown bridge error"


    #   Return True if Error Means No Active Image
    @err_catcher(name=__name__)
    def isNoActiveImageError(self, errorMsg:str) -> bool:
        normalized = str(errorMsg or "").strip().lower()
        return "no active image" in normalized


    #   Show Popup When No Active Image Exists
    @err_catcher(name=__name__)
    def popupNoActiveImage(self) -> None:
        #   Limit Duplicate Popups from Repeated Bridge Calls.
        now = time.monotonic()
        if (now - self.noImagePopupTime) < 1.0:
            return

        self.noImagePopupTime = now

        try:
            self.core.popup(
                "Cannot create a new version from current because there is no active GIMP image.\n\n"
                "Create or open an image first, then try again.",
                title="Prism - GIMP",
            )
        except Exception:
            pass


    #   Pause State Saves for a Short Time
    @err_catcher(name=__name__)
    def suppressStateSaves(self, seconds:float=8.0) -> None:
        self.suppressStateSaveUntil = max(self.suppressStateSaveUntil, time.monotonic() + max(0.0, seconds))


    #   Marks the Gimp Scenefile Dirty to Prompt Save on Exit
    @err_catcher(name=__name__)
    def markSceneDirty(self, origin=None, force=False):
        payload = {
            "force": bool(force),
            **self.getStateManagerImagePayload(),
        }

        logger.debug(
            "Mark scene dirty request",
            extra={
                "image_id": payload.get("image_id"),
                "force": bool(force),
            },
        )

        response = self.sendCmdToGimp(
            action="mark-scene-dirty",
            payload=payload,
            timeout=5.0,
        )

        if not response or not response.get("ok"):
            logger.warning(f"ERROR: Failed to mark scene dirty via bridge: {self._responseError(response)}")
            return False

        return True


    #   Query Current Image Specs from Gimp Bridge
    @err_catcher(name=__name__)
    def getImageSpecs(self) -> dict:
        response = None

        for attempt in range(5):
            response = self.sendCmdToGimp(
                action="get-image-specs",
                payload={},
                timeout=3.0,
            )

            if response and response.get("ok"):
                break

            if attempt < 4:
                time.sleep(0.1)

        if not response or not response.get("ok"):
            return {}

        data = response.get("data") or {}
        specs = data.get("imageSpecs") or {}
        return specs if isinstance(specs, dict) else {}



    #######################################
    ##             CALLBACKS             ##
    #######################################

    @err_catcher(name=__name__)
    def onProjectBrowserStartup(self, origin:"ProjectBrowser"):
        origin.setWindowIcon(QIcon(self.appIcon))


    @err_catcher(name=__name__)
    def onUserSettingsOpen(self, origin:"UserSettings"):
        origin.setWindowIcon(QIcon(self.appIcon))


    @err_catcher(name=__name__)
    def onUserSettingsSave(self, origin:"UserSettings"):
        self.loadSettings()


    @err_catcher(name=__name__)
    def onStateManagerOpen(self, origin:"StateManager"):
        origin.setWindowIcon(QIcon(self.appIcon))

        #   Resizes the StateManager Window
        if hasattr(origin, 'resize'):
            try:
                origin.resize(900, 900)
            except:
                pass

        #	Remove Native Buttons
        origin.b_createImport.deleteLater()
        origin.b_shotCam.deleteLater()
        origin.b_createExport.deleteLater()
        origin.b_createPlayblast.deleteLater()

        #	Create Import Image Button
        origin.b_importLayer = QPushButton(origin.w_CreateImports)
        origin.b_importLayer.setObjectName("b_importLayer")
        origin.b_importLayer.setText("Import Layer")
        #	Add to the Beginning of the Layout
        origin.horizontalLayout_3.insertWidget(0, origin.b_importLayer)
        #	Add State Connection to Button
        origin.b_importLayer.clicked.connect(lambda: self.addGimpImportState(origin))

        #   Set Styling for Gimp
        origin.b_showImportStates.setStyleSheet("padding-left: 1px;padding-right: 1px;")
        origin.b_showExportStates.setStyleSheet("padding-left: 1px;padding-right: 1px;")
        origin.b_createImport.setMinimumWidth(70 * self.core.uiScaleFactor)
        origin.b_createImport.setMaximumWidth(70 * self.core.uiScaleFactor)
        origin.b_createImport.setMinimumHeight(0)
        origin.b_createImport.setMaximumHeight(500 * self.core.uiScaleFactor)
        origin.b_shotCam.setMinimumHeight(0)
        origin.b_shotCam.setMaximumHeight(50 * self.core.uiScaleFactor)
        origin.b_showImportStates.setMinimumWidth(30 * self.core.uiScaleFactor)
        origin.b_showImportStates.setMaximumWidth(30 * self.core.uiScaleFactor)
        origin.b_showExportStates.setMinimumWidth(30 * self.core.uiScaleFactor)
        origin.b_showExportStates.setMaximumWidth(30 * self.core.uiScaleFactor)
        origin.b_createExport.setMinimumWidth(70 * self.core.uiScaleFactor)
        origin.b_createExport.setMaximumWidth(70 * self.core.uiScaleFactor)
        origin.b_createRender.setMinimumWidth(70 * self.core.uiScaleFactor)
        origin.b_createRender.setMaximumWidth(70 * self.core.uiScaleFactor)
        origin.b_createPlayblast.setMinimumWidth(80 * self.core.uiScaleFactor)
        origin.b_createPlayblast.setMaximumWidth(80 * self.core.uiScaleFactor)
        origin.b_description.setMinimumWidth(35 * self.core.uiScaleFactor)
        origin.b_description.setMaximumWidth(35 * self.core.uiScaleFactor)
        origin.b_preview.setMinimumWidth(35 * self.core.uiScaleFactor)
        origin.b_preview.setMaximumWidth(35 * self.core.uiScaleFactor)

        origin.b_importLayer.setMinimumWidth(70 * self.core.uiScaleFactor)
        origin.b_importLayer.setMinimumHeight(0)
        origin.b_importLayer.setMaximumHeight(500 * self.core.uiScaleFactor)

        #   Remove Unused States Except for gimpStates
        for state in list(origin.stateTypes.keys()):
            if state not in self.gimpStates:
                try:
                    del origin.stateTypes[state]
                except Exception:
                    logger.debug(f"Unable to remove default state: {state}")


    #   Creates the Gimp Import state from the StateManager Import button
    @err_catcher(name=__name__)
    def addGimpImportState(self, origin:"StateManager"):
        logger.debug("Gimp Import button clicked; creating Gimp Import state")

        parent = None

        #   Add into the Selected Import Folder
        try:
            curSel = origin.getCurrentItem(origin.activeList)
            if (
                origin.activeList == origin.tw_import
                and curSel is not None
                and getattr(getattr(curSel, "ui", None), "className", None) == "Folder"
            ):
                parent = curSel
        except Exception:
            parent = None

        importStates = []
        for stateKey in list(origin.stateTypes.keys()):
            stateType = origin.stateTypes.get(stateKey)
            categories = getattr(stateType, "stateCategories", {})
            importStates += categories.get("Import2d", [])

        if not importStates:
            logger.warning("No Import2d states available to create from the Import button")
            return

        selectedState = None
        for stateDef in importStates:
            if str(stateDef.get("stateType") or "") == "Gimp Import":
                selectedState = stateDef
                break

        if selectedState is None:
            selectedState = importStates[0]

        origin.createState(
            selectedState["stateType"],
            parent=parent,
            setActive=True,
            **selectedState.get("kwargs", {}),
        )

        origin.activeList.setFocus()


    @err_catcher(name=__name__)
    def onStateManagerClose(self, origin:"StateManager"):
        self.stateManagerBridgeImageId = None


    @err_catcher(name=__name__)
    def onStateManagerShow(self, origin:"StateManager"):
        #   Display Import List (Prism closes the list by default)
        origin.gb_import.setChecked(True)

        if self.stateManagerBridgeImageId is None:
            context = self.resolveCurrentImageContext()
            self.stateManagerBridgeImageId = context.get("imageId")

        logger.debug(
            "SM show bound image context",
            extra={"image_id": self.stateManagerBridgeImageId},
        )


    # @err_catcher(name=__name__)
    # def prePublish(self, origin:"StateManager"):
    #     origin.showMinimized()


    # @err_catcher(name=__name__)
    # def postPublish(self, origin:"StateManager", pubType, result={}):
    #     origin.showNormal()



    ###################################################
    ##          Called From Gimp Prism Tools         ##   
    ###################################################

    @err_catcher(name=__name__)
    def saveVersion(self, requestData=None):
        self.saveCommentBridgeImageId = None
        self.pendingThumbnailBridgeImageId = None

        #   Store Requested Image Id for Next Bridge Action
        self.setPendingBridgeImageFromRequest(requestData)

        #   If No Image Context, Show Popup and Clear Pending Ids
        context = self.resolveCurrentImageContext()
        if context.get("imageId") is None:
            self.popupNoActiveImage()
            self.pendingBridgeImageId = None
            return False

        try:
            self.core.saveScene()
        finally:
            self.pendingBridgeImageId = None


    @err_catcher(name=__name__)
    def saveComment(self, requestData=None):
        #   Store Requested Image Id for Next Bridge Action
        self.setPendingBridgeImageFromRequest(requestData)
        self.saveCommentBridgeImageId = self.pendingBridgeImageId

        #   If No Image Context, Show Popup and Clear Pending Ids
        context = self.resolveCurrentImageContext()
        if context.get("imageId") is None:
            self.popupNoActiveImage()
            self.pendingBridgeImageId = None
            self.saveCommentBridgeImageId = None
            return False

        try:
            self.core.saveWithComment()
        finally:
            self.pendingBridgeImageId = None


    @err_catcher(name=__name__)
    def open_ProjectBrowser(self):
        self.core.projectBrowser()


    @err_catcher(name=__name__)
    def open_StateManager(self, requestData=None):
        #   Store Requested Image Id for Next Bridge Action
        self.setPendingBridgeImageFromRequest(requestData)
        try:
            #   Open State Manager with Pending Image Id
            payload = {}
            if self.pendingBridgeImageId is not None:
                payload["image_id"] = self.pendingBridgeImageId

            #   Send Request to Gimp Bridge
            response = self.sendCmdToGimp(
                action="get-current-file-name",
                payload=payload,
                timeout=2.0,
            )

            #   If No Response or Error from Bridge, Show Popup and Clear Pending Ids
            scenePath = ""
            if response and response.get("ok"):
                data = response.get("data") or {}
                scenePath = str(data.get("path") or "")

            #   If Scene Path Not in Pipeline, Show Warning and Clear Pending Ids
            if not self.core.fileInPipeline(scenePath, validateFilename=False):
                self.core.showFileNotInProjectWarning()
                self.stateManagerBridgeImageId = None
                return

            #   Open State Manager Window
            self.stateManagerBridgeImageId = self.pendingBridgeImageId
            if self.stateManagerBridgeImageId is None:
                context = self.resolveCurrentImageContext()
                self.stateManagerBridgeImageId = context.get("imageId")

            logger.debug(
                "SM open bound image context",
                extra={
                    "request_image_id": self.pendingBridgeImageId,
                    "bound_image_id": self.stateManagerBridgeImageId,
                    "scene_path": scenePath,
                },
            )

            #   Force StateManager Refresh so Prism Reloads Image States
            self.core.stateManager(reload_module=True)
        finally:
            self.pendingBridgeImageId = None


    @err_catcher(name=__name__)
    def open_PrismSettings(self):
        self.core.prismSettings()



    ###################################################
    ##                COMMUNICATIONS                 ##
    ###################################################


    #   Sends a Blocking Request to the In-Gimp Bridge Service
    @err_catcher(name=__name__)
    def sendCmdToGimp(self, action:str, payload:dict=None, timeout:float=10.0) -> dict | None:
        bridgePort = int(self.gimpSettings.get("bridgePort_in", 50601))
        packet = {
            "action": action,
            "data": payload or {},
        }

        try:
            #   Connect to Bridge and Send Request
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                client.settimeout(timeout)
                client.connect(("127.0.0.1", bridgePort))
                client.sendall(json.dumps(packet).encode("utf-8"))
                chunks = []

                while True:
                    try:
                        #   Use Socket Timeout to Break When No More Data is Being Sent by Bridge
                        chunk = client.recv(65536)
                    except socket.timeout:
                        #   If Some Data Already Arrived, or Treat as No Response
                        if chunks:
                            break
                        return None

                    if not chunk:
                        break

                    chunks.append(chunk)

                #   Combine Received Chunks and Parse as JSON
                rawResponse = b"".join(chunks)

            if not rawResponse:
                return None

            return json.loads(rawResponse.decode("utf-8"))

        except Exception as exc:
            logger.warning(f"ERROR: Bridge request failed for action '{action}': {exc}")
            return None



    ###########################################
    ##                THUMBNAIL              ##   
    ###########################################


    #   Captures Thumbnail from Gimp
    @err_catcher(name=__name__)
    def captureViewportThumbnail(self) -> QPixmap | None:
        #   If Pending Thumbnail Image Id Exists, Use for this Request and Clear After
        consumeDelayedThumbnailImage = (
            self.pendingBridgeImageId is None
            and self.pendingThumbnailBridgeImageId is not None
        )

        try:
            #   Get Thumbnail Size from Settings or Use Defaults
            preview_width = int(getattr(self.core, "scenePreviewWidth", 512) or 512)
            preview_height = int(getattr(self.core, "scenePreviewHeight", 256) or 256)

            #   Send Request to Gimp Bridge
            response = self.sendCmdToGimp(
                action="get-thumbnail",
                payload=self.getBridgeImagePayload({
                    "width": max(1, preview_width),
                    "height": max(1, preview_height),
                }),
                timeout=10.0,
            )

            if not response or not response.get("ok"):
                logger.warning(f"ERROR: Unable to capture thumbnail via bridge: {self._responseError(response)}")

                #   If No Thumbnail from Bridge, Attempt to Load Current Scene File as Fallback Thumbnail
                current_path = self.getCurrentFileName(origin=None, path=True)
                if current_path and os.path.isfile(current_path):
                    fallback_pixmap = QPixmap(current_path)
                    if not fallback_pixmap.isNull():
                        return fallback_pixmap

                return None

            data = response.get("data") or {}

            width = int(data.get("width") or 0)
            height = int(data.get("height") or 0)
            bpp = int(data.get("bpp") or 0)
            pixels_b64 = data.get("pixels") or ""

            #   Validate Thumbnail Data from Bridge
            if width <= 0 or height <= 0 or bpp not in (3, 4) or not pixels_b64:
                logger.warning("ERROR: Thumbnail generation failed: Invalid bridge thumbnail payload")
                return None

            try:
                #   Decode Base64 Pixel Data from Bridge
                pixel_bytes = base64.b64decode(pixels_b64)

            except Exception as exc:
                logger.warning(f"ERROR: Thumbnail generation failed: Base64 decode failed: {exc}")
                return None

            #   Check that Decoded Pixel Data Size Matches Expected Size from Thumbnail Specs
            expected_size = width * height * bpp
            if expected_size <= 0 or len(pixel_bytes) < expected_size:
                logger.warning("ERROR: Thumbnail generation failed: Pixel buffer smaller than expected")
                return None

            #   Create QImage from Raw Pixel Data and Convert to QPixmap
            bytesPerLine = width * bpp
            image_format = QImage.Format_RGBA8888 if bpp == 4 else QImage.Format_RGB888

            image = QImage(pixel_bytes[:expected_size], width, height, bytesPerLine, image_format).copy()

            #   If RGBA, Composite Thumbnail onto Checkerboard Background
            if bpp == 4:
                pixmap = self.compThumbnailOnChecker(image)
            else:
                pixmap = QPixmap.fromImage(image)

            if pixmap.isNull():
                logger.warning("ERROR: Thumbnail generation failed: QPixmap is null")
                return None

            return pixmap

        except Exception as exc:
            logger.warning(f"ERROR: Unable to capture thumbnail: {exc}")
            return None
        
        finally:
            if consumeDelayedThumbnailImage:
                #   Use delayed Save Comment Image Binding after First Thumbnail Request.
                self.pendingThumbnailBridgeImageId = None
                self.saveCommentBridgeImageId = None


    #   Composites an RGBA Thumbnail onto Generated Checkerboard Background.
    @err_catcher(name=__name__)
    def compThumbnailOnChecker(self, source_image:QImage) -> QPixmap:
        width = source_image.width()
        height = source_image.height()

        #   Create Thumbnail-Sized BG
        canvas = QImage(width, height, QImage.Format_RGB32)
        painter = QPainter(canvas)

        #   Fill BG with Checkerboard Pattern
        for y in range(0, height, THUMB_TILE_SIZE):
            row_index = y // THUMB_TILE_SIZE
            for x in range(0, width, THUMB_TILE_SIZE):
                col_index = x // THUMB_TILE_SIZE
                color = THUMB_COLOR_LIGHT if (row_index + col_index) % 2 == 0 else THUMB_COLOR_DARK
                painter.fillRect(x, y, THUMB_TILE_SIZE, THUMB_TILE_SIZE, color)

        #   Composite Thumbnail onto BG and Convert to QPixmap
        painter.drawImage(0, 0, source_image)
        painter.end()

        return QPixmap.fromImage(canvas)



    ###################################################
    ##                  GIMP Stuff                   ##
    ###################################################

    @err_catcher(name=__name__)
    def getSceneExtension(self, origin):
        return self.sceneFormats[0]


    #   Query Gimp Application Version from Bridge
    @err_catcher(name=__name__)
    def getAppVersion(self, origin:"PrismCore") -> str:
        response = self.sendCmdToGimp(
            action="get-app-version",
            payload={},
            timeout=2.0,
        )

        if not response or not response.get("ok"):
            logger.warning("ERROR: Unable to query Gimp version from bridge")
            return ""

        data = response.get("data") or {}
        version = data.get("version")

        if version is None:
            return ""

        return str(version)


    #   Return Current Scene File Path or File Name
    @err_catcher(name=__name__)
    def getCurrentFileName(self, origin=None, path=True, attempts:int=10, delay:float=0.2) -> str:
        response = None
        filePath = None

        #   Retry Loop to Handle While Gimp is Still Initializing
        for attempt in range(attempts):
            response = self.sendCmdToGimp(
                action="get-current-file-name",
                payload={},
                timeout=2.0,
            )

            if response and response.get("ok"):
                data = response.get("data") or {}
                filePath = data.get("path")
                break

            if attempt < attempts - 1:
                time.sleep(delay)

        if not response or not response.get("ok"):
            logger.warning("ERROR: Unable to query current Gimp filename from bridge")
            return ""

        if path:
            return filePath or ""

        if not filePath:
            return ""

        return os.path.basename(filePath)


    #   Open a Scene File in Gimp Through Bridge
    @err_catcher(name=__name__)
    def openScene(self, origin, filepath, force=False):
        if not filepath:
            return False

        if not filepath.lower().endswith(".xcf"):
            return False
        
        filepath = os.path.normpath(filepath)

        if not os.path.isfile(filepath):
            logger.warning(f"ERROR: Scenefile does not exist: {filepath}")
            return False

        try:
            response = self.sendCmdToGimp(
                action="open-scene",
                payload={
                    "path": filepath,
                    "force": bool(force),
                },
                timeout=20.0,
            )

            if not response or not response.get("ok"):
                logger.warning(f"ERROR: Unable to open Scenefile via bridge: {filepath} ({self._responseError(response)})")
                return False

            logger.debug(f"Opened Scene: {filepath}")
            return True
        
        except Exception as e:
            logger.warning(f"ERROR:  Unable to open Scenefile: {filepath}\n{e}")
            return False
            

    #   Saves .XCF to New Passed Filepath
    @err_catcher(name=__name__)
    def saveScene(self, origin=None, filepath=None, details={}):
        #   To Keep Image Bound for Post-Save Thumbnail Capture in Save Comment Flow
        delayedComment_ImageId = self.saveCommentBridgeImageId

        try:
            if filepath:
                if not filepath.lower().endswith(".xcf"):
                    return False

                filepath = os.path.normpath(filepath)

                parent_dir = os.path.dirname(filepath)
                if parent_dir and not os.path.isdir(parent_dir):
                    logger.warning(f"ERROR: Save folder does not exist: {parent_dir}")
                    return False

            payload = {
                "path": filepath,
                "details": details or {},
            }

            #   If Delayed Comment Image Id Exists and No Pending Bridge Image Id, Use Delayed Comment Image Id for this Save Request
            if delayedComment_ImageId is not None and self.pendingBridgeImageId is None:
                payload["image_id"] = delayedComment_ImageId
                #   Keep image binding for post-save thumbnail capture in async Save Comment flow.
                self.pendingThumbnailBridgeImageId = delayedComment_ImageId

            #   Send Request to Gimp Bridge
            response = self.sendCmdToGimp(
                action="save-scene",
                payload=self.getBridgeImagePayload(payload),
                timeout=30.0,
            )

            #   Clear Delayed Comment Image Id After Save Request is Sent to Bridge
            if not response or not response.get("ok"):
                errorMsg = self._responseError(response)
                if self.isNoActiveImageError(errorMsg):
                    self.suppressStateSaves()
                    self.popupNoActiveImage()
                    return False

                logger.warning(f"ERROR: Unable to save the .xcf via bridge: {errorMsg}")
                return False

            return True
        
        except Exception as e:
            logger.warning(f"ERROR: Unable to save the .xcf: {e}")
            return False



    ##########################################
    ##            IMAGE IMPORT              ##
    ##########################################

    #   Called to Import Filepath as a New Layer
    @err_catcher(name=__name__)
    def importImage(self, state, basefile, versionData):
        try:
            payload = {
                "path": basefile,
                "versionData": versionData,
            }

            #   Send Request to Gimp Bridge
            response = self.sendCmdToGimp(
                action="import-image",
                payload=payload,
                timeout=30.0,
            )

            if not response or not response.get("ok"):
                logger.warning(f"ERROR: Unable to import image via bridge: {self._responseError(response)}")
                return False

            #   Get Layer Name and Layer Tattoo
            layer_name = (response.get("data") or {}).get("layerName") if isinstance(response, dict) else None
            layer_tattoo = (response.get("data") or {}).get("layerTattoo") if isinstance(response, dict) else None

            logger.debug(f"Imported Image: {basefile}")

            return {
                "layerName": layer_name or "",
                "layerTattoo": layer_tattoo,
            } if (layer_name or layer_tattoo) else True
        
        except Exception as e:
            logger.warning(f"ERROR:  Unable to Import Image:\n\n{e}")
            return False


    #   Returns the Name of a Layer from its Tattoo
    @err_catcher(name=__name__)
    def getLayerName(self, state, layerTattoo=None):
        try:
            payload = {
                "layerTattoo": layerTattoo,
                **self.getStateManagerImagePayload(),
            }

            response = self.sendCmdToGimp(
                action="get-layer-name",
                payload=payload,
                timeout=10.0,
            )

            if not response or not response.get("ok"):
                logger.warning(f"ERROR: Unable to get layer name via bridge: {self._responseError(response)}")
                return None

            return (response.get("data") or {}).get("layerName")

        except Exception as e:
            logger.warning(f"ERROR:  Unable to get layer name:\n\n{e}")
            return None


    #   Renames a Layer in Gimp and Returns the New Name
    @err_catcher(name=__name__)
    def renameLayer(self, state, newName, layerTattoo=None):
        try:
            payload = {
                "layerTattoo": layerTattoo,
                "newName": newName,
                **self.getStateManagerImagePayload(),
            }

            response = self.sendCmdToGimp(
                action="rename-layer",
                payload=payload,
                timeout=10.0,
            )

            if not response or not response.get("ok"):
                logger.warning(f"ERROR: Unable to rename layer via bridge: {self._responseError(response)}")
                return None

            confirmed_name = (response.get("data") or {}).get("layerName")
            logger.debug(f"Renamed layer to: {confirmed_name}")
            return confirmed_name

        except Exception as e:
            logger.warning(f"ERROR:  Unable to rename layer:\n\n{e}")
            return None


    #   Deletes a Layer in Gimp by its Tattoo
    @err_catcher(name=__name__)
    def deleteLayer(self, state, layerName=None, versionData=None, layerTattoo=None):
        try:
            payload = {
                "layerName": layerName,
                "layerTattoo": layerTattoo,
                "versionData": versionData or {},
                **self.getStateManagerImagePayload(),
            }

            #   Send Request to Gimp Bridge
            response = self.sendCmdToGimp(
                action="delete-image-layer",
                payload=payload,
                timeout=10.0,
            )

            if not response or not response.get("ok"):
                logger.warning(f"ERROR: Unable to delete image layer via bridge: {self._responseError(response)}")
                return False

            removed = bool((response.get("data") or {}).get("deleted"))
            if removed:
                logger.debug("Deleted imported image layer from Gimp image")
            else:
                logger.debug("Import layer not found in Gimp image; nothing deleted")

            return True

        except Exception as e:
            logger.warning(f"ERROR:  Unable to delete image layer:\n\n{e}")
            return False
        



    ##########################################
    ##                RENDER                ##
    ##########################################

    @err_catcher(name=__name__)
    def sm_render_startup(self, origin):
        return None


    @err_catcher(name=__name__)
    def sm_render_preExecute(self, origin):
        return []


    @err_catcher(name=__name__)
    def sm_render_preSubmit(self, origin, settings):
        return None


    @err_catcher(name=__name__)
    def sm_render_undoRenderSettings(self, origin, settings):
        return None


    @err_catcher(name=__name__)
    def sm_render_startLocalRender(self, origin, outputName, settings):
        payload = {
            "path": outputName,
            "settings": settings or {},
            **self.getStateManagerImagePayload(),
        }

        logger.debug(
            "SM render export request",
            extra={
                "image_id": payload.get("image_id"),
                "path": outputName,
            },
        )

        #   Send Request to Gimp Bridge
        response = self.sendCmdToGimp(
            action="export-image",
            payload=payload,
            timeout=120.0,
        )

        if response and response.get("ok"):
            return "Result=Success"

        return f"Export failed: {self._responseError(response)}"




    ###################################################
    ##         State Manager States Handling         ##   
    ###################################################
    ##   The Plugin uses Gimp's Parasite System to   ##
    ##   Store State Data within the .XCF Scenefile  ##


    #   Save State Manager Data into Scene Metadata
    @err_catcher(name=__name__)
    def sm_saveStates(self, origin, buf):
        #   If State Saves are Temporarily Suppressed, Skip Saving and Return Early
        if time.monotonic() < self.suppressStateSaveUntil:
            logger.debug("Skipping State save because save flow was aborted after no-image error")
            return

        if isinstance(buf, str):
            stateData = buf
        else:
            stateData = json.dumps(buf)

        #   If No Active Image Context, Show Popup and Skip Saving
        context = self.resolveCurrentImageContext()
        if context.get("imageId") is None:
            logger.debug("Skipping State save because no active image exists")
            return

        logger.debug(
            "SM saveStates request",
            extra={
                "image_id": context.get("imageId"),
                "state_bytes": len(stateData.encode("utf-8", errors="replace")),
            },
        )

        #   Send Request to Gimp Bridge
        response = self.sendCmdToGimp(
            action="save-states",
            payload={
                "stateData": stateData,
                **self.getStateManagerImagePayload(),
            },
            timeout=10.0,
        )

        #   If No Response or Error from Bridge, Show Popup and Skip Saving
        if not response or not response.get("ok"):
            errorMsg = self._responseError(response)
            if self.isNoActiveImageError(errorMsg):
                logger.debug("Skipping State save because no active image exists")
                return

            logger.warning(f"ERROR: Failed to save states via bridge: {errorMsg}")


    #   Read State Manager Data from Scene Metadata
    @err_catcher(name=__name__)
    def sm_readStates(self, origin):
        #   Default Empty State
        emptyState = json.dumps({
            "states": [
                {"statename": "publish", "comment": "", "description": ""}
            ]
        })

        try:
            #   If No Active Image Context, Show Popup and Return Empty State
            context = self.resolveCurrentImageContext()
            logger.debug(
                "SM readStates request",
                extra={
                    "image_id": context.get("imageId"),
                },
            )

            #   Send Request to Gimp Bridge
            response = self.sendCmdToGimp(
                action="get-states",
                payload=self.getStateManagerImagePayload(),
                timeout=5.0,
            )

            if not response or not response.get("ok"):
                return emptyState

            #   Extract State Data from Bridge Response
            data = response.get("data") or {}
            stateData = data.get("stateData") or ""
            logger.debug(
                "SM readStates response",
                extra={
                    "image_id": data.get("imageId"),
                    "command_image_id": data.get("commandImageId"),
                },
            )

            if not stateData:
                return emptyState

            if isinstance(stateData, (dict, list)):
                return json.dumps(stateData)

            if not isinstance(stateData, str):
                return emptyState

            normalized = stateData.strip()
            if not normalized:
                return emptyState

            try:
                parsed = json.loads(normalized)
            except Exception:
                return emptyState

            if isinstance(parsed, str):
                try:
                    reparsed = json.loads(parsed)
                except Exception:
                    return emptyState

                if isinstance(reparsed, dict) and "states" in reparsed:
                    return json.dumps(reparsed)
                return emptyState

            if isinstance(parsed, dict) and "states" in parsed:
                return json.dumps(parsed)

            return emptyState

        except Exception as e:
            logger.warning(f"Failed to read states: {e}")
            return emptyState


    #   Reset Scene States to Default Publish State
    @err_catcher(name=__name__)
    def sm_deleteStates(self, origin):
        self.sm_saveStates(origin, {
            "states": [
                {"statename": "publish", "comment": "", "description": ""}
            ]
        })
