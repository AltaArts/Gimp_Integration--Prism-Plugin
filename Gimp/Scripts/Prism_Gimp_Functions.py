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
        self.Gimp = None
        self.noImagePopupTime = 0.0

        try:
            self.loadSettings()
        except Exception:
            pass

        ##  CALLBACKS
        # self.core.registerCallback("postInitialize", self.setupPrismMenu, plugin=self.plugin)
        self.core.registerCallback("onStateManagerOpen", self.onStateManagerOpen, plugin=self.plugin, priority=20)
        # self.core.registerCallback("onStateManagerShow", self.onStateManagerShow, plugin=self.plugin, priority=20)
        # self.core.registerCallback("onProjectBrowserStartup", self.onProjectBrowserStartup, plugin=self.plugin)
        # self.core.registerCallback("onUserSettingsOpen", self.onUserSettingsOpen, plugin=self.plugin)
        # self.core.registerCallback("onUserSettingsSave", self.onUserSettingsSave, plugin=self.plugin,)
        # self.core.registerCallback("prePublish", self.prePublish, plugin=self.plugin)
        # self.core.registerCallback("postPublish", self.postPublish, plugin=self.plugin)


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


    def getSharedSettingsPath(self) -> str:
        overridePath = os.environ.get("PRISM_GIMP_SETTINGS_PATH")
        if overridePath:
            return overridePath

        return os.path.join(PLUGINROOT, SETTINGS_FILE_NAME)


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


    def isNoActiveImageError(self, errorMsg:str) -> bool:
        normalized = str(errorMsg or "").strip().lower()
        return "no active image" in normalized


    def popupNoActiveImage(self) -> None:
        #   Throttle to avoid duplicate popups from tightly grouped bridge calls.
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
    

    #   Marks the Gimp Scenefile Dirty to Prompt Save on Exit
    @err_catcher(name=__name__)
    def markSceneDirty(self, origin=None, force=False):
        response = self.sendCmdToGimp(
            action="mark-scene-dirty",
            payload={"force": bool(force)},
            timeout=5.0,
        )

        if not response or not response.get("ok"):
            errorMsg = "Unknown bridge error"
            if isinstance(response, dict):
                errorMsg = response.get("error") or errorMsg
            logger.warning(f"ERROR: Failed to mark scene dirty via bridge: {errorMsg}")
            return False

        return True


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
        origin.setWindowIcon(QIcon(self.prismAppIcon))
        ss = self.core.getActiveStyleSheet()
        origin.setStyleSheet(ss["css"])


    @err_catcher(name=__name__)
    def onUserSettingsOpen(self, origin:"UserSettings"):
        origin.setWindowIcon(QIcon(self.prismAppIcon))
        ss = self.core.getActiveStyleSheet()
        origin.setStyleSheet(ss["css"])


    @err_catcher(name=__name__)
    def onUserSettingsSave(self, origin:"UserSettings"):
        self.loadSettings()


    @err_catcher(name=__name__)
    def onStateManagerOpen(self, origin:"StateManager"):
        origin.setWindowIcon(QIcon(self.prismAppIcon))
        ss = self.core.getActiveStyleSheet()
        origin.setStyleSheet(ss["css"])

		#   Resizes the StateManager Window
        if hasattr(origin, 'resize'):
            try:
                origin.resize(900, 900)
            except:
                pass

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

        #	Remove Native Buttons
        # origin.b_createImport.deleteLater()
        origin.b_shotCam.deleteLater()
        origin.b_createExport.deleteLater()
        origin.b_createPlayblast.deleteLater()

        #	Create New Scene Button
        # origin.b_createShot = QPushButton(origin.w_CreateImports)
        # origin.b_createShot.setObjectName("b_createShot")
        # origin.b_createShot.setText("New Scene")
        # origin.horizontalLayout_3.insertWidget(0, origin.b_createShot)
        # origin.b_createShot.clicked.connect(lambda: self.addShot(origin, "scene"))

        #   Add Shot Button
        # origin.b_addShot = QPushButton(origin.w_CreateImports)
        # origin.b_addShot.setObjectName("b_addShot")
        # origin.b_addShot.setText("Add Shot")
        # origin.horizontalLayout_3.insertWidget(1, origin.b_addShot)
        # origin.b_addShot.clicked.connect(lambda: self.addShot(origin, "shot"))

        #   Add Survey Button
        # origin.b_addSurvey = QPushButton(origin.w_CreateImports)
        # origin.b_addSurvey.setObjectName("b_addSurvey")
        # origin.b_addSurvey.setText("Survey Shot")
        # origin.horizontalLayout_3.insertWidget(2, origin.b_addSurvey)
        # origin.b_addSurvey.clicked.connect(lambda: self.addShot(origin, "survey"))

        #   Add Mesh Button
        # origin.b_addMesh = QPushButton(origin.w_CreateImports)
        # origin.b_addMesh.setObjectName("b_addMesh")
        # origin.b_addMesh.setText("Mesh")
        # origin.horizontalLayout_3.insertWidget(3, origin.b_addMesh)
        # origin.b_addMesh.clicked.connect(lambda: origin.createState("ImportMesh"))

        # Export Scene Button
        # origin.b_exportScene = QPushButton(origin.w_CreateExports)
        # origin.b_exportScene.setObjectName("b_exportScene")
        # origin.b_exportScene.setText("Export Scene")
        # origin.b_exportScene.setMaximumSize(QSize(150, 16777215))
        # sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        # origin.b_exportScene.setSizePolicy(sizePolicy)
        # origin.horizontalLayout_4.insertWidget(0, origin.b_exportScene)
        # origin.b_exportScene.clicked.connect(lambda: origin.createState("SceneExport"))

        # tip = ("Create New Gimp Scene.\n\n"
        #        "This will start an entirely new scene and import the images(s)\n"
        #        "This is the same as the 'New' button in the Gimp UI.\n\n"
        #        "Please note this will overwrite any shots in the existing scene.")
        # origin.b_createShot.setToolTip(tip)

        # tip = ("This will add an additional Shot and Camera to the existing Scene.\n\n"
        #        "This is the same as the 'Add Shot' button in Gimp.")
        # origin.b_addShot.setToolTip(tip)

        # tip = ("This will add a Survey Shot and Camera to the existing Scene.\n\n"
        #        "This is the same as the 'Add Survey Shot' button in Gimp.")
        # origin.b_addSurvey.setToolTip(tip)

        # tip = "Import a 3D Mesh object into the Scene."
        # origin.b_addMesh.setToolTip(tip)

        # tip = "Export the Gimp Scene to the desired format."
        # origin.b_exportScene.setToolTip(tip)

        # tip = ("Create the Desired Render State:\n\n"
        #        "ImageRender - Same as Gimp 'Save Sequence'\n"
        #        "STMap Render - Same as Gimp 'Write Distortion Maps")
        # origin.b_createRender.setToolTip(tip)

        # tip = ("Creates a Playblast State.\n\n"
        #        "This uses the Gimp 'Preview Movie' from\n"
        #        "the Perspective View.")
        # origin.b_createPlayblast.setToolTip(tip)

        #   Remove Unused States Except for gimpStates
        for state in list(origin.stateTypes.keys()):
            if state not in self.gimpStates:
                try:
                    del origin.stateTypes[state]
                except Exception:
                    logger.debug(f"Unable to remove default state: {state}")


    @err_catcher(name=__name__)
    def onStateManagerShow(self, origin:"StateManager"):
        #   Display Import List (Prism closes the list by default)
        origin.gb_import.setChecked(True)


    @err_catcher(name=__name__)
    def prePublish(self, origin:"StateManager"):
        origin.showMinimized()


    @err_catcher(name=__name__)
    def postPublish(self, origin:"StateManager", pubType, result={}):
        origin.showNormal()



    ###################################################
    ##          Called From Gimp Prism Tools         ##   
    ###################################################

    @err_catcher(name=__name__)
    def saveVersion(self):
        self.core.saveScene()

    @err_catcher(name=__name__)
    def saveComment(self):
        self.core.saveWithComment()

    @err_catcher(name=__name__)
    def open_ProjectBrowser(self):
        self.core.projectBrowser()

    @err_catcher(name=__name__)
    def open_StateManager(self):
        self.core.stateManager()

    @err_catcher(name=__name__)
    def open_PrismSettings(self):
        self.core.prismSettings()



    ###################################################
    ##                COMMUNICATIONS                 ##
    ###################################################


    #   Sends a Blocking Request to the In-Gimp Bridge Service
    def sendCmdToGimp(self, action:str, payload:dict=None, timeout:float=10.0) -> dict | None:
        bridgePort = int(self.gimpSettings.get("bridgePort_in", 50601))
        packet = {
            "action": action,
            "data": payload or {},
        }

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                client.settimeout(timeout)
                client.connect(("127.0.0.1", bridgePort))
                client.sendall(json.dumps(packet).encode("utf-8"))
                chunks = []

                while True:
                    try:
                        chunk = client.recv(65536)
                    except socket.timeout:
                        #   If some data already arrived, use it. Otherwise treat as no response.
                        if chunks:
                            break
                        return None

                    if not chunk:
                        break

                    chunks.append(chunk)

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
        try:
            preview_width = int(getattr(self.core, "scenePreviewWidth", 512) or 512)
            preview_height = int(getattr(self.core, "scenePreviewHeight", 256) or 256)

            response = self.sendCmdToGimp(
                action="get-thumbnail",
                payload={
                    "width": max(1, preview_width),
                    "height": max(1, preview_height),
                },
                timeout=10.0,
            )

            if not response or not response.get("ok"):
                errorMsg = "Unknown bridge error"
                if isinstance(response, dict):
                    errorMsg = response.get("error") or errorMsg

                logger.warning(f"ERROR: Unable to capture thumbnail via bridge: {errorMsg}")

                #   Fallback for builds without thumbnail bridge APIs: load the current saved scene file.
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

            if width <= 0 or height <= 0 or bpp not in (3, 4) or not pixels_b64:
                logger.warning("ERROR: Thumbnail generation failed: Invalid bridge thumbnail payload")
                return None

            try:
                pixel_bytes = base64.b64decode(pixels_b64)

            except Exception as exc:
                logger.warning(f"ERROR: Thumbnail generation failed: Base64 decode failed: {exc}")
                return None

            expected_size = width * height * bpp
            if expected_size <= 0 or len(pixel_bytes) < expected_size:
                logger.warning("ERROR: Thumbnail generation failed: Pixel buffer smaller than expected")
                return None

            bytesPerLine = width * bpp
            image_format = QImage.Format_RGBA8888 if bpp == 4 else QImage.Format_RGB888

            image = QImage(pixel_bytes[:expected_size], width, height, bytesPerLine, image_format).copy()
            if bpp == 4:
                pixmap = self.compositeThumbnailOnChecker(image)
            else:
                pixmap = QPixmap.fromImage(image)

            if pixmap.isNull():
                logger.warning("ERROR: Thumbnail generation failed: QPixmap is null")
                return None

            return pixmap

        except Exception as exc:
            logger.warning(f"ERROR: Unable to capture thumbnail: {exc}")
            return None


    #   Composites an RGBA thumbnail onto Generated Checkerboard Background.
    def compositeThumbnailOnChecker(self, source_image:QImage) -> QPixmap:
        width = source_image.width()
        height = source_image.height()

        canvas = QImage(width, height, QImage.Format_RGB32)
        painter = QPainter(canvas)

        for y in range(0, height, THUMB_TILE_SIZE):
            row_index = y // THUMB_TILE_SIZE
            for x in range(0, width, THUMB_TILE_SIZE):
                col_index = x // THUMB_TILE_SIZE
                color = THUMB_COLOR_LIGHT if (row_index + col_index) % 2 == 0 else THUMB_COLOR_DARK
                painter.fillRect(x, y, THUMB_TILE_SIZE, THUMB_TILE_SIZE, color)

        painter.drawImage(0, 0, source_image)
        painter.end()

        return QPixmap.fromImage(canvas)



    ###################################################
    ##                  GIMP Stuff                   ##
    ###################################################



    @err_catcher(name=__name__)
    def getSceneExtension(self, origin):
        return self.sceneFormats[0]



    #   Returns Gimp Version
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


    #   Returns Current Gimp File Name/Path (retries multiple times for potential startup timing issues)
    @err_catcher(name=__name__)
    def getCurrentFileName(self, origin=None, path=True, attempts:int=10, delay:float=0.2) -> str:
        response = None
        filePath = None

        for attempt in range(attempts):
            response = self.sendCmdToGimp(
                action="get-current-file-name",
                payload={},
                timeout=2.0,
            )

            if response and response.get("ok"):
                data = response.get("data") or {}
                filePath = data.get("path")

                if filePath:
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
                errorMsg = "Unknown bridge error"
                if isinstance(response, dict):
                    errorMsg = response.get("error") or errorMsg

                logger.warning(f"ERROR: Unable to open Scenefile via bridge: {filepath} ({errorMsg})")
                return False

            logger.debug(f"Opened Scene: {filepath}")
            return True
        
        except Exception as e:
            logger.warning(f"ERROR:  Unable to open Scenefile: {filepath}\n{e}")
            return False
            

    #   Saves .XCF to New Passed Filepath
    @err_catcher(name=__name__)
    def saveScene(self, origin=None, filepath=None, details={}):
        try:
            if filepath:
                if not filepath.lower().endswith(".xcf"):
                    return False

                filepath = os.path.normpath(filepath)

                parent_dir = os.path.dirname(filepath)
                if parent_dir and not os.path.isdir(parent_dir):
                    logger.warning(f"ERROR: Save folder does not exist: {parent_dir}")
                    return False

            response = self.sendCmdToGimp(
                action="save-scene",
                payload={
                    "path": filepath,
                    "details": details or {},
                },
                timeout=30.0,
            )

            if not response or not response.get("ok"):
                errorMsg = "Unknown bridge error"
                if isinstance(response, dict):
                    errorMsg = response.get("error") or errorMsg

                if self.isNoActiveImageError(errorMsg):
                    self.popupNoActiveImage()
                    return False

                logger.warning(f"ERROR: Unable to save the .xcf via bridge: {errorMsg}")
                return False

            return True
        
        except Exception as e:
            logger.warning(f"ERROR: Unable to save the .xcf: {e}")
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
        response = self.sendCmdToGimp(
            action="export-image",
            payload={
                "path": outputName,
                "settings": settings or {},
            },
            timeout=120.0,
        )

        if response and response.get("ok"):
            return "Result=Success"

        errorMsg = "Unknown bridge error"
        if isinstance(response, dict):
            errorMsg = response.get("error") or errorMsg

        return f"Export failed: {errorMsg}"




    ###################################################
    ##         State Manager States Handling         ##   
    ###################################################
    ##   The Plugin uses Gimp's Parasite System to   ##
    ##   Store State Data within the .XCF Scenefile  ##


    @err_catcher(name=__name__)
    def sm_saveStates(self, origin, buf):
        if isinstance(buf, str):
            stateData = buf
        else:
            stateData = json.dumps(buf)

        response = self.sendCmdToGimp(
            action="save-states",
            payload={"stateData": stateData},
            timeout=10.0,
        )

        if not response or not response.get("ok"):
            errorMsg = "Unknown bridge error"
            if isinstance(response, dict):
                errorMsg = response.get("error") or errorMsg

            if self.isNoActiveImageError(errorMsg):
                logger.debug("Skipping State save because no active image exists")
                return

            logger.warning(f"ERROR: Failed to save states via bridge: {errorMsg}")


    @err_catcher(name=__name__)
    def sm_readStates(self, origin):
        emptyState = json.dumps({
            "states": [
                {"statename": "publish", "comment": "", "description": ""}
            ]
        })

        try:
            response = self.sendCmdToGimp(
                action="get-states",
                payload={},
                timeout=5.0,
            )

            if not response or not response.get("ok"):
                return emptyState

            data = response.get("data") or {}
            stateData = data.get("stateData") or ""

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


    @err_catcher(name=__name__)
    def sm_deleteStates(self, origin):
        self.sm_saveStates(origin, {
            "states": [
                {"statename": "publish", "comment": "", "description": ""}
            ]
        })
