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
#                       Gimp2 Plugin for Prism2
#
#                           Joshua Breckeen
#                              Alta Arts
#                          josh@alta-arts.com
#
###########################################################################


import os
import sys
import re
import logging
from typing import TYPE_CHECKING


from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from PrismUtils.Decorators import err_catcher
from StateUserInterfaces import Gimp_ImportImage_ui

SCRIPT_ROOT = os.path.dirname(os.path.dirname(__file__))
if SCRIPT_ROOT not in sys.path:
    sys.path.insert(0, SCRIPT_ROOT)


logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from PrismCore import PrismCore
    from StateManager import StateManager
    from Prism_Gimp_Functions import Prism_Gimp_Functions

#   Global Colors
COLOR_GREEN = QColor(0, 130, 0)
COLOR_YELLOW = QColor(200, 150, 0)
COLOR_ORANGE = QColor(150, 100, 0)
COLOR_RED = QColor(130, 0, 0)
COLOR_BLACK = QColor(0, 0, 0, 0)
COLOR_WHITE = QColor(255, 255, 255, 255)

#   Icon to be used for State
scriptDir = os.path.dirname(os.path.dirname(__file__))
STATE_ICON = os.path.join(scriptDir, "Icons", "Image.png")



class Gimp_ImportImageClass(object):
    className = "Gimp Import"
    listType = "Import"
    stateCategories = {"Import2d": [{"label": className, "stateType": className}]}


    @err_catcher(name=__name__)
    def setup(
        self,
        state:QTreeWidgetItem,
        core: "PrismCore",
        stateManager: "StateManager",
        importPath:str = None,
        stateData:dict = None,
        settings:dict = None,
    ):

        #   Checks if the ATTR Already Exists and Assigns if Not
        self.core = getattr(self, "core", core)
        self.state = getattr(self, "state", state)
        self.stateManager = getattr(self, "stateManager", stateManager)
        self.gimpFuncts: "Prism_Gimp_Functions" = getattr(self, "gimpFuncts", self.core.appPlugin)

        if not hasattr(self, "mediaChooser"):
            self.mediaChooser = ReadMediaDialog(self, self.core)

        self.stateMode = "AddShot"
        self.taskName = ""
        self.setName = ""
        self.stateStatus = None
        self.trackedLayerName = None

        #   State name stuff
        stateNameTemplate = "{entity}_{version}"
        self.stateNameTemplate = self.core.getConfig(
            "globals",
            "defaultImportStateName",
            configPath=self.core.prismIni,
        ) or stateNameTemplate
        self.e_name.setText(self.stateNameTemplate)

        self.b_browse.setContextMenuPolicy(Qt.CustomContextMenu)
        
        #   Hide unused UI elements
        self.l_name.setVisible(False)
        self.e_name.setVisible(True)
        self.l_class.setVisible(True)
        self.w_autoUpdate.setVisible(False)

        #   Sets colors
        self.oldPalette = self.b_importLatest.palette()
        self.updatePalette = QPalette()
        self.updatePalette.setColor(QPalette.Button, COLOR_ORANGE)
        self.updatePalette.setColor(QPalette.ButtonText, COLOR_WHITE)

        #   Make Version labels Bold
        font = self.l_curVersion.font()
        font.setBold(True)
        self.l_curVersion.setFont(font)

        font = self.l_latestVersion.font()
        font.setBold(True)
        self.l_latestVersion.setFont(font)


    ####   Do one of the following:     ####

        ##   1. Load State from Saved Data
        if stateData is not None:
            self.loadData(stateData)
            logger.debug("Loaded State from Saved Data")

            self.nameChanged()
            self.updateUi()

        ##   2. Opens Media Popup to Select Import
        elif (
            importPath is None
            and stateData is None
            and not settings
            and not self.stateManager.standalone
            ):

            #   Open MediaChooser to Get Import
            requestResult = self.callMediaWindow()

            if requestResult == "Cancelled":
                logger.debug("Media Import cancelled")
                return False
            
            if requestResult == "Empty":
                return False
            
            if not requestResult:
                logger.warning("ERROR: Unable to Import Image from MediaBrowser.")
                self.core.popup("Unable to Import Image from MediaBrowser.")
                return False

            #   Set the Results
            self.setImportPath(requestResult[0])
            self.importData = requestResult[1]

            #   Import the Image
            result = self.importImage(requestResult[0], requestResult[1])

            if not result:
                return False
            
            self.nameChanged()
            self.updateUi()

        ##  If error
        else:
            logger.warning("ERROR: Unable to Import Image.")
            self.core.popup("Unable to Import Image.")
            return False

        getattr(self.core.appPlugin, "sm_import_startup", lambda x: None)(self)

        self.connectEvents()
        self.setToolTips()

        self.stateManager.saveImports()
        self.stateManager.saveStatesToScene()


    @err_catcher(name=__name__)
    def connectEvents(self):
        self.e_name.textChanged.connect(self.nameChanged)
        self.e_name.editingFinished.connect(self.stateManager.saveStatesToScene)
        self.b_browse.clicked.connect(self.browse)
        self.b_browse.customContextMenuRequested.connect(self.openFolder)
        self.b_importLatest.clicked.connect(self.importLatest)
        self.chb_autoUpdate.stateChanged.connect(self.autoUpdateChanged)
        self.e_layerName.editingFinished.connect(
            lambda: self.updateLayerName(self.e_layerName.text())
            )



    #########################
    #       Wrapped         #
    #   Prism Functions     #
    #########################


    #   Returns the version label name from version filepath
    @err_catcher(name=__name__)
    def getMasterVersionLabel(self, filepath:str) -> str:
        '''Returns the version label name from version filepath'''
        return self.core.mediaProducts.getMasterVersionLabel(filepath)
    

    #   Returns highest version context from a given context
    @err_catcher(name=__name__)
    def getLatestVersion(self, context:dict, includeMaster:bool) -> dict:
        '''Returns highest version context from a given context'''
        mediaProducts = self.core.mediaProducts
        return mediaProducts.getLatestVersionFromIdentifier(context, includeMaster=includeMaster)
    

    #   Returns a context from the currently selected version
    @err_catcher(name=__name__)
    def getCurrentVersion(self) -> dict:
        '''Returns a context from the currently selected version in the MediaBrowser'''
        try:
            self.mediaBrowser = self.mediaChooser.w_browser
            self.mediaPlayer = self.mediaBrowser.w_preview.mediaPlayer
            return self.mediaBrowser.getCurrentVersion()
        
        except Exception as e:
            logger.warning(f"ERROR:  Unable to get Current Version from Prism Functions:\n\n{e}")
    

    #   Returns a list of AOV dicts for a given context
    @err_catcher(name=__name__)
    def getAOVsFromVersion(self, version:dict) -> list:
        '''Returns a list of AOV dicts for a given context'''
        try:
            return self.core.mediaProducts.getAOVsFromVersion(version)
        except Exception as e:
            logger.warning(f"ERROR:  Unable to get AOVs from Prism Functions:\n\n{e}")


    #   Returns a list of all the image files for a given context
    @err_catcher(name=__name__)
    def getFilesFromContext(self, aovItem:dict) -> list:
        '''Returns a list of all the image files for a given context'''
        try:
            return self.core.mediaProducts.getFilesFromContext(aovItem)
        except Exception as e:
            logger.warning(f"ERROR:  Unable to get Files from Prism Context Functions:\n\n{e}")



    #########################
    #         STATE         #
    #########################

    #   Set State Name and Icon
    @err_catcher(name=__name__)
    def nameChanged(self, text=None):
        name = self.e_name.text()

        if text:
            name = text
        else:
            try:
                name = self.importData['identifier']
            except Exception as e:
                name = text

        #   Set the Name for the State list
        self.e_name.setText(name)
        self.state.setText(0, name)

        #   Add Icon to State name
        self.state.setIcon(0, QIcon(STATE_ICON))

        self.stateManager.saveImports()
        self.stateManager.saveStatesToScene()


    #   Opens Media Chooser to select version
    @err_catcher(name=__name__)
    def browse(self):
        title = "Change Layer Image"
        text = ("Please Note:\n\n"
                "Changing the Layer Image could affect any changes made\n"
                "in Gimp.  Please save the file before changing\n"
                "the images.\n\n\n"
                "Would you like to continue?")

        result = self.core.popupQuestion(text, title)

        if result != "Yes":
            return False

        currVersion = self.getCurrentVersion()

        if currVersion:
            #   Call the MediaWindow with the MediaId
            requestResult = self.callMediaWindow(currVersion)
        else:
            #   Just call without a MediaId
            requestResult = self.callMediaWindow()

        if requestResult == "Cancelled":
            logger.debug("Media Import cancelled")
            return False
        
        if requestResult == "Empty":
            return False
        
        if not requestResult:
            logger.warning("ERROR: Unable to Import Image from MediaBrowser.")
            self.core.popup("Unable to Import Image from MediaBrowser.")
            return False
    
        self.setImportPath(requestResult[0])
        basefile = requestResult[0]
        self.importData = requestResult[1]

        result = self.updateImportedImage(basefile, self.importData)

        self.updateUi()


    @err_catcher(name=__name__)
    def importLatest(self):
        title = "Change Layer Image"
        text = ("Please Note:\n\n"
                "Changing the Layer Image could affect any changes made\n"
                "in Gimp.  Please save the file before changing\n"
                "the images.\n\n\n"
                "Would you like to continue?")

        result = self.core.popupQuestion(text, title)

        if result != "Yes":
            return False

        versionData = self.getLatestVersion(self.importData, includeMaster=True)
        basefile = self.getFilepathFromVersion(versionData)
        self.importData = versionData
        self.setImportPath(basefile)

        result = self.updateImportedImage(basefile, self.importData)

        self.updateUi()


    @err_catcher(name=__name__)
    def openFolder(self, pos):
        path = self.getImportPath()

        if os.path.isfile(path):
            path = os.path.dirname(path)

        self.core.openFolder(path)


    @err_catcher(name=__name__)
    def getImportPath(self):
        path = getattr(self, "importPath", "")
        if path:
            path = os.path.normpath(path)

        return path


    @err_catcher(name=__name__)
    def setImportPath(self, path):
        self.importPath = path
        self.l_text_Current.setToolTip(path)
        self.stateManager.saveImports()
        self.stateManager.saveStatesToScene()


    #   Updates the Auto-update UI
    @err_catcher(name=__name__)
    def autoUpdateChanged(self, checked):
        self.w_importLatest.setVisible(not checked)

        try:
            if checked:
                curVersion, latestVersion = self.checkLatestVersion()
                if self.chb_autoUpdate.isChecked():
                    if (curVersion.get("version")
                        and latestVersion.get("version")
                        and curVersion["version"] != latestVersion["version"]
                        ):
                        self.importLatest(refreshUi=True, selectedStates=False)

            self.stateManager.saveImports()
            self.stateManager.saveStatesToScene()

        except Exception as e:
            logger.warning(f"ERROR:  AutoUpdate Change failed:\n\n{e}")


    @err_catcher(name=__name__)
    def runSanityChecks(self, cachePath):
        result = True

        if getattr(self.core.appPlugin, "hasFrameRange", True):
            result = self.checkFrameRange(cachePath)

        if not result:
            return False

        return True

   
    
    #########################
    #          UI           #
    #########################

    @err_catcher(name=__name__)
    def setToolTips(self):
        tip = "Media Identifier of Imported Shot"
        self.e_name.setToolTip(tip)

        tip = "Opens the Media Browser to select a specific version"
        self.b_browse.setToolTip(tip)

        tip = "Will import the latest version of the media."
        self.b_importLatest.setToolTip(tip)

        tip = ("Name of Layer in Gimp for this Image.\n\n"
               "You may change the name and it will be\n"
               "reflected in Gimp.  Also the version\n"
               "number (if any) will be updated with changes\n"
               "to the selected version.")
        self.l_layerName.setToolTip(tip)
        self.e_layerName.setToolTip(tip)


    #   Opens the Custom MediaBrowser window to choose import
    @err_catcher(name=__name__)
    def callMediaWindow(self, itemData=None):
        #   Sets Objects
        self.mediaBrowser = self.mediaChooser.w_browser
        self.mediaPlayer = self.mediaBrowser.w_preview.mediaPlayer

        #   If passed itemData, navigate to the Media Item
        if itemData:
            try:
                #   Navigate to the correct tab/table
                self.mediaBrowser.navigateToEntity(itemData)
                #   Get the item title
                mediaId = (itemData.get("displayName")
                        or itemData.get("mediaId")
                        or itemData.get("identifier")
                        )

                #   Find and select the Identifier
                items = self.mediaBrowser.tw_identifier.findItems(
                    mediaId,
                    Qt.MatchFlag(Qt.MatchExactly & Qt.MatchCaseSensitive ^ Qt.MatchRecursive)
                    )
                
                if items:
                    self.mediaBrowser.tw_identifier.setCurrentItem(items[0])
            except:
                logger.debug("ERROR:  Unable to navigate to State's entity in the MediaBrowser")

        #   Connects clicked signal
        self.mediaChooser.mediaSelected.connect(lambda selResult: self.setSelectedMedia(selResult))
        #   Calls the MediaBrowser and receives result
        result = self.mediaChooser.exec_()

        #   If cancelled
        if result == QDialog.Rejected:
            return "Cancelled"
        
        #   If error
        if not self.selResult:
            return False

        #   Gets the result
        clicked = self.selResult[0]
        self.importData = self.selResult[1]

        #   Makes funct call based on what was clicked (Identifier or Version)
        if clicked == "version":
            versionData = self.getCurrentVersion()

        if clicked == "identifier":
            versionData = self.getLatestVersion(self.importData, includeMaster=True)

        basefile = self.getFilepathFromVersion(versionData)

        if not result:
            return False
        
        if result == "Empty":
            return False
        
        else:
            return basefile, versionData
        

    def getFilepathFromVersion(self, versionContext):
        aovs = self.core.mediaProducts.getAOVsFromVersion(versionContext)

        if aovs:
            mediaFiles = self.core.mediaProducts.getFilesFromContext(aovs[0])

        else:
            basePath = versionContext["path"]
            mediaFiles = [
                os.path.join(basePath, f)
                for f in os.listdir(basePath)
                if os.path.isfile(os.path.join(basePath, f))
            ]
            mediaFiles = sorted(mediaFiles)

        validFiles = self.core.media.filterValidMediaFiles(mediaFiles)

        return validFiles[0]


    #   Sets the Selected Result from the MediaChooser
    @err_catcher(name=__name__)
    def setSelectedMedia(self, selResult):        
        self.selResult = selResult


    #   Updates the Layer Name in GIMP
    @err_catcher(name=__name__)
    def updateLayerName(self, newName=None):
        #   Gets Layer Tattoo from the State
        layerTattoo = getattr(self, "layerTattoo", None)
        if layerTattoo is None:
            return

        if newName is not None:
            newName = newName.strip()
            if not newName:
                return

            #   Call for Rename in GIMP
            confirmed = self.gimpFuncts.renameLayer(
                self,
                newName,
                layerTattoo=layerTattoo,
            )

            #   Update the State and UI
            if confirmed:
                self.importData["layerName"] = confirmed
                self.trackedLayerName = confirmed

                self.e_layerName.blockSignals(True)
                self.e_layerName.setText(confirmed)
                self.e_layerName.blockSignals(False)

                self.stateManager.saveStatesToScene()

        else:
            #   Name Not Passed — Get Current Name from GIMP
            current_name = self.gimpFuncts.getLayerName(
                self,
                layerTattoo=layerTattoo,
            )

            if current_name is not None:
                self.importData["layerName"] = current_name
                self.trackedLayerName = current_name
                self.e_layerName.blockSignals(True)
                self.e_layerName.setText(current_name)
                self.e_layerName.blockSignals(False)


    #   Finds and Changes the Version Suffix (_v001, _v002, _master)
    @err_catcher(name=__name__)
    def updateNameVersion(self, currentName:str, newVerStr:str) -> str | None:
        verPadding = self.core.versionPadding

        pattern = rf"(_v\d{{{verPadding}}}|_master)"
        matches = list(re.finditer(pattern, currentName or ""))

        if matches and newVerStr:
            last_match = matches[-1]
            start, end = last_match.span()

            newName = (
                (currentName or "")[:start]
                + f"_{newVerStr}"
                + (currentName or "")[end:]
            )

            return newName

        else:
            return None


    @err_catcher(name=__name__)
    def setStateColor(self, status):
        if status == "ok":
            statusColor = COLOR_GREEN
        elif status == "warning":
            statusColor = COLOR_ORANGE
        elif status == "error":
            statusColor = COLOR_RED
        else:
            statusColor = COLOR_BLACK

        self.statusColor = statusColor
        self.stateManager.tw_import.repaint()


    @err_catcher(name=__name__)
    def updateUi(self):
        self.updateLayerName()

        versions = self.checkLatestVersion()
        if not versions:
            logger.debug("Skipped setting Latest Version Status")
            return

        if versions:
            curVersion, latestVersion = versions
        else:
            curVersion = latestVersion = ""

        if curVersion.get("version") == "master":
            filepath = self.getImportPath()
            curVersionName = self.getMasterVersionLabel(filepath)
        else:
            curVersionName = curVersion.get("version")

        if latestVersion.get("version") == "master":
            filepath = latestVersion["path"]
            latestVersionName = self.getMasterVersionLabel(filepath)
        else:
            latestVersionName = latestVersion.get("version")

        self.l_curVersion.setText(curVersionName or "-")
        self.l_latestVersion.setText(latestVersionName or "-")

        self.stateStatus = "error"

        if self.chb_autoUpdate.isChecked():
            if curVersionName and latestVersionName and curVersionName != latestVersionName:
                self.importLatest(refreshUi=False, selectedStates=False)

            if latestVersionName:
                self.stateStatus = "ok"
        else:
            useSS = getattr(self.core.appPlugin, "colorButtonWithStyleSheet", False)

            if (
                curVersionName
                and latestVersionName
                and curVersionName != latestVersionName
                and not curVersionName.startswith("master")
            ):
                self.stateStatus = "warning"
                if useSS:
                    self.b_importLatest.setStyleSheet(
                        "QPushButton { background-color: rgb(200,100,0); }"
                    )
                else:
                    self.b_importLatest.setPalette(self.updatePalette)
            else:
                if curVersionName and latestVersionName:
                    self.stateStatus = "ok"

                if useSS:
                    self.b_importLatest.setStyleSheet(
                        "QPushButton { background-color: rgb(0, 130, 0); }"
                    )
                else:
                    self.b_importLatest.setPalette(self.oldPalette)

        self.nameChanged()
        self.setStateColor(self.stateStatus)

        getattr(self.core.appPlugin, "sm_import_updateUi", lambda x: None)(self)

        self.stateManager.saveImports()
        self.stateManager.saveStatesToScene()



    #########################
    #         DATA          #
    #########################

    @err_catcher(name=__name__)
    def loadData(self, data):
        self.importData = data

        if "statename" in data:
            self.e_name.setText(data["statename"])

        if "taskname" in data:
            self.taskName = data["taskname"]

        if "setname" in data:
            self.setName = data["setname"]

        if "autoUpdate" in data:
            checked = eval(data["autoUpdate"])
            self.chb_autoUpdate.setChecked(checked)
            self.autoUpdateChanged(checked)

        if "filepath" in data:
            data["filepath"] = getattr(
                self.core.appPlugin, "sm_import_fixImportPath", lambda x: x
            )(data["filepath"])
            self.setImportPath(data["filepath"])

        layer_name = data.get("layerName", "")
        self.e_layerName.blockSignals(True)
        self.e_layerName.setText(layer_name or "")
        self.e_layerName.blockSignals(False)

        self.trackedLayerName = (
            data.get("trackedLayerName")
            or data.get("layerName")
            or data.get("shotUID")
            or None
        )

        layer_tattoo = data.get("layerTattoo")
        self.layerTattoo = int(layer_tattoo) if layer_tattoo is not None else None

        self.core.callback("onStateSettingsLoaded", self, data)


    @err_catcher(name=__name__)
    def getStateProps(self):
        self.importData["statename"] = self.e_name.text()
        self.importData["statemode"] = self.stateMode
        self.importData["trackedLayerName"] = self.trackedLayerName
        self.importData["filepath"] = self.getImportPath()
        self.importData["autoUpdate"] = str(self.chb_autoUpdate.isChecked())
        self.importData["taskname"] = self.taskName
        self.importData["layerName"] = self.e_layerName.text()
        self.importData["layerTattoo"] = getattr(self, "layerTattoo", None)

        return self.importData


    @err_catcher(name=__name__)
    def checkLatestVersion(self):
        try:
            path = self.getImportPath()

            curVerData = {"version": self.importData["version"], "path": path}

            latestVerDict = self.getLatestVersion(self.importData, includeMaster=True)

            lastestVerName = latestVerDict["version"]
            lastestVerPath = latestVerDict["path"]

            if latestVerDict:
                latestVersionData = {"version": lastestVerName, "path": lastestVerPath}
            else:
                latestVersionData = {}
            
            #   Sets Tooltips
            curVerPath = curVerData["path"]
            self.l_text_Current.setToolTip(curVerPath)
            self.l_curVersion.setToolTip(curVerPath)

            latestVerPath = latestVersionData["path"]
            self.l_text_Latest.setToolTip(latestVerPath)
            self.l_latestVersion.setToolTip(latestVerPath)

            return curVerData, latestVersionData
        
        except:
            logger.debug("ERROR:  Unable to get Latest Version.")
            return None


    #########################
    #        IMPORT         #
    #########################


    @err_catcher(name=__name__)
    def importImage(self, basefile, versionData):
        try:
            result = self.gimpFuncts.importImage(self, basefile, versionData)

            if not result:
                return False

            #   Extract Layer Name and Layer Tattoo from the response
            if isinstance(result, dict):
                layer_name = result.get("layerName") or ""
                layer_tattoo = result.get("layerTattoo")

            else:
                layer_name = str(result) if result is not True else ""
                layer_tattoo = None

            #   Store State Data
            self.layerTattoo = layer_tattoo
            self.trackedLayerName = layer_name
            self.importData["layerName"] = layer_name
            self.importData["layerTattoo"] = layer_tattoo

            #   Populate the Layer Name Text Box
            self.e_layerName.blockSignals(True)
            self.e_layerName.setText(layer_name)
            self.e_layerName.blockSignals(False)

            return layer_name or True

        except Exception as e:
            logger.warning(f"ERROR:  Unable to Import Image:\n\n{e}")
            self.core.popup("Unable to Import Image.")
            return False


    @err_catcher(name=__name__)
    def updateImportedImage(self, basefile, versionData):
        try:
            #   Get Image Layer Tattoo from the State
            layerTattoo = getattr(self, "layerTattoo", None)
            
            if layerTattoo is not None:
                current_layerName = (
                    getattr(self, "trackedLayerName", None)
                    or self.e_layerName.text().strip()
                )
                current_layerName = re.sub(r"\s#\d+$", "", str(current_layerName or ""))
                desired_layerName = self.updateNameVersion(
                    current_layerName,
                    (versionData or {}).get("version"),
                )

                #   Layer Already Exists - Replace with the New Version
                result = self.gimpFuncts.replaceLayerImage(
                    self,
                    newFilePath=basefile,
                    versionData=versionData,
                    layerTattoo=layerTattoo,
                    desiredLayerName=desired_layerName,
                )
                
                if result:
                    #   Update the State Data with the New Layer Name and Tattoo
                    if isinstance(result, dict):
                        updated_layer_name = result.get("layerName")
                        updated_layer_tattoo = result.get("layerTattoo")

                        if updated_layer_name:
                            self.trackedLayerName = updated_layer_name
                            self.importData["layerName"] = updated_layer_name
                            self.e_layerName.blockSignals(True)
                            self.e_layerName.setText(str(updated_layer_name))
                            self.e_layerName.blockSignals(False)

                        if updated_layer_tattoo is not None:
                            self.layerTattoo = updated_layer_tattoo
                            self.importData["layerTattoo"] = updated_layer_tattoo

                    #   Update State Data with New Version Info
                    merged_data = dict(versionData or {})
                    merged_data["layerName"] = getattr(self, "trackedLayerName", None)
                    merged_data["layerTattoo"] = getattr(self, "layerTattoo", None)
                    self.importData = merged_data
                    self.setImportPath(basefile)
                    logger.debug(f"Updated layer to new version: {(versionData or {}).get('version')}")
                    return True
                else:
                    logger.warning("Failed to replace layer image with new version")
                    self.core.popup("Failed to update layer image.")
                    return False
            
            else:
                #   No layer exists yet - do a fresh import
                result = self.importImage(basefile, versionData)
                
                if result:
                    #   Update State Data with New Version Info
                    self.importData = versionData
                    self.setImportPath(basefile)
                    logger.debug(f"Imported new layer for version: {(versionData or {}).get('version')}")
                    return True
                else:
                    logger.warning("Failed to import new image")
                    return False
        
        except Exception as e:
            logger.warning(f"ERROR:  Unable to update imported image:\n\n{e}")
            self.core.popup("Unable to update imported image.")
            return False


    @err_catcher(name=__name__)
    def preDelete(self, item):
        title = "Delete Layer"
        text = ("Would you like to delete the Layer in the Gimp File?")

        result = self.core.popupQuestion(text, title)

        if result == "Yes":
            try:
                self.gimpFuncts.deleteLayer(
                    self,
                    self.trackedLayerName,
                    versionData=getattr(self, "importData", {}),
                    layerTattoo=getattr(self, "layerTattoo", None),
                )

            except Exception as e:
                logger.warning(f"ERROR:  Unable to delete Layer:\n\n{e}")
                self.core.popup("Unable to delete Layer.")
                return False



#########################################################
##   Custom MediaBrowser to Choose Images to Import    ##
class ReadMediaDialog(QDialog):
    '''Custom MediaBrowser to Choose Images to Import.'''

    mediaSelected = Signal(object)

    def __init__(self, state, core):
        super(ReadMediaDialog, self).__init__()
        self.state:QTreeWidgetItem = state
        self.stateManager:StateManager = self.state.stateManager
        self.gimpFuncts:Prism_Gimp_Functions = self.state.gimpFuncts
        self.core:PrismCore = core

        self.isValid = False
        self.setupUi()


    @err_catcher(name=__name__)
    def setupUi(self):
        title = "Select Media"
        self.setWindowTitle(title)
        self.core.parentWindow(self)

        import MediaBrowser
        self.w_browser = MediaBrowser.MediaBrowser(core=self.core)
        self.w_browser.headerHeightSet = True

        ##   Disconnect native function of showing versionInfo, and connect to import the version
        ##   This is disabled unless the main code gets something connected to the ID table list widget
        # self.w_browser.tw_identifier.itemDoubleClicked.disconnect()
        self.w_browser.tw_identifier.itemDoubleClicked.connect(self.ident_dblClk)
        self.w_browser.lw_version.itemDoubleClicked.disconnect()
        self.w_browser.lw_version.itemDoubleClicked.connect(self.ver_dblClk)

        #   Disconnect native right-click-list and connect custom
        self.w_browser.tw_identifier.customContextMenuRequested.disconnect()
        # self.w_browser.tw_identifier.customContextMenuRequested.connect(self.customRclList)

        #   Create main window
        self.lo_main = QVBoxLayout()
        self.setLayout(self.lo_main)

        #   Create bottom layout
        self.lo_bottom = QHBoxLayout()

        #   Add instructions label text to bottom
        instructionsText = ("      Double-click Identifier to Import Latest Version      --      "
                            "Double-click Version to Load Version into State")
        l_instructions = QLabel(instructionsText)

        #   Add button box
        self.bb_main = QDialogButtonBox()
        self.bb_main.addButton("Import Selected", QDialogButtonBox.AcceptRole)
        ##  vvvvv    Disabled until functions added  vvvvvvvv    ##
        # self.bb_main.addButton("Import Custom", QDialogButtonBox.AcceptRole)
        # self.bb_main.addButton("Open Project Browser", QDialogButtonBox.AcceptRole)
        ##  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^   ##
        self.bb_main.addButton("Cancel", QDialogButtonBox.RejectRole)
        self.bb_main.clicked.connect(self.buttonClicked)

        # Add widgets to the bottom layout
        self.lo_bottom.addWidget(l_instructions)
        self.lo_bottom.addStretch()  # Expanding spacer
        self.lo_bottom.addWidget(self.bb_main)

        #   Add main Browser to window
        self.lo_main.addWidget(self.w_browser)
        # Add bottom layout to window
        self.lo_main.addLayout(self.lo_bottom)

        tip = ("Double-click Identifier to Load\n"
               "and Import the Latest Version.")
        self.w_browser.tw_identifier.setToolTip(tip)

        tip = ("Double-click Version to Load\n"
               "the Version into the State.")
        self.w_browser.lw_version.setToolTip(tip)

        tip = ("Single-selection:  load the selected version into the State.")
        self.bb_main.setToolTip(tip)


    #   Handles clicked buttons
    @err_catcher(name=__name__)
    def buttonClicked(self, button:QPushButton):
        if button == "select" or button.text() == "Import Selected":
            self.handelImportButton()

        elif button.text() == "Import Custom":
            self.core.popup("Not Yet Implemented")                                      #    TESTING

        elif button.text() == "Open Project Browser":                                   #   TODO
            self.reject()
            self.openProjectBrowser()

        elif button.text() == "Cancel":
            self.reject()

        else:
            self.reject()


    #   Handles if the Import Selected button clicked
    def handelImportButton(self):
        selectedItems = self.w_browser.tw_identifier.selectedItems()

        if len(selectedItems) == 0:
            self.core.popup("No Items Selected")

        if len(selectedItems) == 1:
            data = self.w_browser.getCurrentSource()
            if not data:
                data = self.w_browser.getCurrentAOV()
                if not data:
                    data = self.w_browser.getCurrentVersion()
                    if not data:
                        data = self.w_browser.getCurrentIdentifier()

            if not data:
                msg = "Invalid version selected."
                self.core.popup(msg, parent=self)
                return
            
            selResult = ["version", data]

            self.mediaSelected.emit(selResult)
            self.accept()

        # elif len(selectedItems) > 1:
        #     self.handleRclImport(selectedItems)


    #   Handle import from custom RCL
    # @err_catcher(name=__name__)
    # def handleRclImport(self, selectedItems):
    #     #   Close Dialogue
    #     self.reject()

    #     #   If single item, import directly in this state
    #     if len(selectedItems) == 1:
    #         self.ident_dblClk(selectedItems[0])
    #     #   If multiple items, call the import through the main plugin
    #     elif len(selectedItems) > 1:
    #         for item in selectedItems:
    #             iData = item.data(0, Qt.UserRole)
    #             self.fuseFuncts.addImportState(self.stateManager, "Image_Import", useUi=False, settings=iData)
    #     else:
    #         logger.debug("No Media Items Selected")


    #   Sends data back to the main code to import the latest version
    @err_catcher(name=__name__)
    def ident_dblClk(self, item:QListWidgetItem, column:int=None):
        #   Get Item Data
        data = item.data(0, Qt.UserRole)

        #   Return if No Data or is a Group (folder)
        if not data or data.get("isGroup") is True:
            return

        selResult = ["identifier", item.data(0, Qt.UserRole)]

        self.mediaSelected.emit(selResult)
        self.accept() 


    #   Sends data back to main code to populate the version
    @err_catcher(name=__name__)
    def ver_dblClk(self, item:QListWidgetItem, column:int=None) -> None:
        data = self.w_browser.getCurrentSource()

        if not data:
            data = self.w_browser.getCurrentAOV()
            if not data:
                data = self.w_browser.getCurrentVersion()
                if not data:
                    data = self.w_browser.getCurrentIdentifier()

        if not data:
            msg = "Invalid version selected."
            self.core.popup(msg, parent=self)
            return
        
        selResult = ["version", data]

        self.mediaSelected.emit(selResult)
        self.accept()  


    @err_catcher(name=__name__)
    def openProjectBrowser(self):
        self.core.projectBrowser()
        if self.core.pb:
            self.core.pb.showTab("Libraries")



###############################################
##   Image Viewer for Survey Shots Editing   ##
class SurveyImageViewer(QDialog):
    '''Image Viewer for Survey Shots Editing'''

    def __init__(self, state, gimpFuncts, imageFiles:list=None, parent=None):
        super(SurveyImageViewer, self).__init__(parent or state)

        self.state:QTreeWidgetItem = state
        self.gimpFuncts:Prism_Gimp_Functions = gimpFuncts
        self.core:PrismCore = gimpFuncts.core
        self.iconDir:str = os.path.join(self.core.prismRoot, "Scripts", "UserInterfacesPrism")

        #   Set Default Playback Speed
        self.fps = 2
        
        #   Timer for Window Resize
        self.resizeTimer = QTimer(self)
        self.resizeTimer.setSingleShot(True)
        self.resizeTimer.timeout.connect(self.doResizeUpdate)

        #   Set Initial Image List
        self.imageFiles = imageFiles[:] if imageFiles else []
        #   Cached Pixmap List
        self.pixmapCache = []
        self.currentIndex = 0

        self.setupUi()
        self.connectEvents()
        self.loadImageRows()


    ##########################
    ##          UI          ##
    ##########################

    @err_catcher(name=__name__)
    def setupUi(self):
        self.setWindowTitle("Survey Image Viewer")
        self.core.parentWindow(self)

        #   Set Initial Window Size
        self.resize(650, 900)

        #   Create Splitter for Viewer and Image List Panels
        splitter = QSplitter(Qt.Vertical)

        ###   Main Layout    ###
        mainLayout = QVBoxLayout(self)
        mainLayout.addWidget(splitter)

        ###    Top Panel - Image Viewer    ###
        topWidget = QWidget()
        topLayout = QVBoxLayout(topWidget)
        topLayout.setContentsMargins(0, 0, 0, 10)

        #   Container for Image Viewer
        imageContainer = QWidget()
        imageContainer.setStyleSheet("background-color: #1a1a1a;")
        imageLayout = QVBoxLayout(imageContainer)
        imageLayout.setContentsMargins(0, 0, 0, 0)
        
        #   Image Viewer Label Object
        self.imageLabel = QLabel()
        self.imageLabel.setAlignment(Qt.AlignCenter)
        self.imageLabel.setMinimumSize(400, 300)
        self.imageLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.imageLabel.setStyleSheet("border: 1px solid #ccc;")
        imageLayout.addWidget(self.imageLabel)
        topLayout.addWidget(imageContainer)

        #   Playback Controls
        self.w_timeslider = QWidget()
        self.lo_timeslider = QHBoxLayout(self.w_timeslider)
        self.lo_timeslider.setContentsMargins(0, 0, 0, 0)
        self.l_start = QLabel("1")
        self.l_end = QLabel(str(max(1, len(self.imageFiles))))
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, max(0, len(self.imageFiles) - 1))
        self.slider.setSingleStep(1)
        self.slider.setPageStep(1)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.slider.setSizePolicy(sizePolicy)
        self.slider.setObjectName("slider")
        self.sp_current = QSpinBox()
        self.sp_current.setStyleSheet("min-width: 30px;")
        self.sp_current.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.sp_current.setRange(1, max(1, len(self.imageFiles)))
        self.sp_current.setValue(1 if self.imageFiles else 1)
        self.lo_timeslider.addWidget(self.l_start)
        self.lo_timeslider.addWidget(self.slider)
        self.lo_timeslider.addWidget(self.l_end)
        self.lo_timeslider.addWidget(self.sp_current)
        topLayout.addWidget(self.w_timeslider)

        self.w_playerCtrls = QWidget()
        self.lo_playerCtrls = QHBoxLayout(self.w_playerCtrls)
        self.lo_playerCtrls.setContentsMargins(0, 0, 0, 0)
        self.b_first = QToolButton()
        self.b_prev = QToolButton()
        self.b_play = QToolButton()
        self.b_next = QToolButton()
        self.b_last = QToolButton()
        self.lo_playerCtrls.addWidget(self.b_first)
        self.lo_playerCtrls.addStretch()
        self.lo_playerCtrls.addWidget(self.b_prev)
        self.lo_playerCtrls.addWidget(self.b_play)
        self.lo_playerCtrls.addWidget(self.b_next)
        self.lo_playerCtrls.addStretch()
        self.lo_playerCtrls.addWidget(self.b_last)
        topLayout.addWidget(self.w_playerCtrls)

        #   Set Button Icons
        firstPath = os.path.join(self.iconDir, "first.png")
        if os.path.exists(firstPath):
            icon = self.core.media.getColoredIcon(firstPath)
            self.b_first.setIcon(icon)
        self.b_first.setToolTip("Go to First Frame")

        prevPath = os.path.join(self.iconDir, "prev.png")
        if os.path.exists(prevPath):
            icon = self.core.media.getColoredIcon(prevPath)
            self.b_prev.setIcon(icon)
        self.b_prev.setToolTip("Go to Previous Frame")

        playPath = os.path.join(self.iconDir, "play.png")
        if os.path.exists(playPath):
            icon = self.core.media.getColoredIcon(playPath)
            self.b_play.setIcon(icon)
        self.b_play.setToolTip("Start Playback")
        self.b_play.setContextMenuPolicy(Qt.CustomContextMenu)

        nextPath = os.path.join(self.iconDir, "next.png")
        if os.path.exists(nextPath):
            icon = self.core.media.getColoredIcon(nextPath)
            self.b_next.setIcon(icon)
        self.b_next.setToolTip("Go to Next Frame")

        lastPath = os.path.join(self.iconDir, "last.png")
        if os.path.exists(lastPath):
            icon = self.core.media.getColoredIcon(lastPath)
            self.b_last.setIcon(icon)
        self.b_last.setToolTip("Go to Last Frame")

        splitter.addWidget(topWidget)

        ###    Bottom Panel - Image List    ###
        listContainer = QWidget()
        listLayout = QVBoxLayout(listContainer)
        listLayout.setContentsMargins(0, 10, 0, 0)
        self.listWidget = QListWidget()
        self.listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.listWidget.setDragDropMode(QAbstractItemView.InternalMove)
        self.listWidget.setDefaultDropAction(Qt.MoveAction)
        self.listWidget.setMovement(QListView.Snap)
        self.listWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listWidget.setStyleSheet("QListWidget::item { border: 1px solid #465e75; padding: 4px; }")
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        listLayout.addWidget(self.listWidget)

        splitter.addWidget(listContainer)

        #   Setup Initial Splitter Settings
        splitter.setSizes([460, 440])
        splitter.setHandleWidth(8)
        splitter.setStyleSheet(
            "QSplitter::handle { background-color: #465e75; "
            "border: 1px solid #1a1a1a; "
            "background-image: url('" + os.path.join(self.iconDir, "reorder.png").replace("\\", "/") + "'); "
            "background-repeat: no-repeat; "
            "background-position: center; } "
            "QSplitter::handle:hover { background-color: #3a3a3a; }"
        )

        #   Connect Splitter for Resize
        splitter.splitterMoved.connect(lambda: self.displayImage(self.currentIndex))

        #   Bottom Buttons
        buttonLayout = QHBoxLayout()
        self.addButton = QPushButton("Add Images")
        self.clearButton = QPushButton("Clear Images")
        self.okButton = QPushButton("OK")
        self.cancelButton = QPushButton("Cancel")
        buttonLayout.addWidget(self.addButton)
        buttonLayout.addWidget(self.clearButton)
        buttonLayout.addStretch()
        buttonLayout.addWidget(self.cancelButton)
        buttonLayout.addWidget(self.okButton)

        mainLayout.addLayout(buttonLayout)


    @err_catcher(name=__name__)
    def connectEvents(self):
        self.slider.valueChanged.connect(self.sliderChanged)
        self.sp_current.valueChanged.connect(self.onCurrentChanged)
        self.b_first.clicked.connect(self.onFirstClicked)
        self.b_prev.clicked.connect(self.onPrevClicked)
        self.b_play.clicked.connect(self.onPlayClicked)
        self.b_play.customContextMenuRequested.connect(self.showPlayContextMenu)
        self.b_next.clicked.connect(self.onNextClicked)
        self.b_last.clicked.connect(self.onLastClicked)
        self.listWidget.model().rowsMoved.connect(self.onRowsMoved)
        self.listWidget.customContextMenuRequested.connect(self.showContextMenu)
        self.addButton.clicked.connect(self.addFiles)
        self.clearButton.clicked.connect(self.clearFiles)
        self.okButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)


    #   Delay Resize Update until Resizing Stops
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.resizeTimer.start(200)  # 200ms delay


    #   Update All List Items When Resize is Complete
    @err_catcher(name=__name__)
    def doResizeUpdate(self):
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            filepath = item.data(Qt.UserRole)
            widget = self.createListItemWidget(filepath, i)
            item.setSizeHint(widget.sizeHint())
            self.listWidget.setItemWidget(item, widget)

        self.displayImage(self.currentIndex)


    #   List Items RCL Menu
    @err_catcher(name=__name__)
    def showContextMenu(self, pos):
        menu = QMenu(self)
        removeAction = menu.addAction("Remove Image")
        removeAction.triggered.connect(self.removeSelectedImages)
        menu.addSeparator()
        
        # New actions
        invertAction = menu.addAction("Invert Order")
        invertAction.triggered.connect(self.invertSelection)
        
        sortAscAction = menu.addAction("Sort Ascending")
        sortAscAction.triggered.connect(self.sortSelectionAscending)
        
        sortDescAction = menu.addAction("Sort Descending")
        sortDescAction.triggered.connect(self.sortSelectionDescending)
        
        menu.addSeparator()
        openAction = menu.addAction("Open in Explorer")
        openAction.triggered.connect(self.openInExplorer)
        
        #   Enable/disable based on Selection
        selectedItems = self.listWidget.selectedItems()

        if selectedItems:
            removeAction.setEnabled(True)
            openAction.setEnabled(True)
        else:
            removeAction.setEnabled(False)
            openAction.setEnabled(False)

        if len(selectedItems) > 1:
            invertAction.setEnabled(True)
            filepaths = [item.data(Qt.UserRole) for item in selectedItems]
            seqFiles = self.core.media.detectSequence(filepaths)
            isSequence = len(seqFiles) > 1
            sortAscAction.setEnabled(isSequence)
            sortDescAction.setEnabled(isSequence)

        else:
            invertAction.setEnabled(False)
            sortAscAction.setEnabled(False)
            sortDescAction.setEnabled(False)
        
        menu.exec_(self.listWidget.mapToGlobal(pos))


    #   Play/Pause Button RCL Menu
    @err_catcher(name=__name__)
    def showPlayContextMenu(self, pos):
        #   Create Small Dialog Popup
        fpsPopup = QDialog(self)
        fpsPopup.setWindowTitle("Playback Speed")
        fpsPopup.setModal(True)
        lo_fps = QVBoxLayout(fpsPopup)
        
        #   Label and Spinbox for FPS
        l_fps = QLabel("Frames per second:")
        lo_fps.addWidget(l_fps)

        sp_fps = QSpinBox()
        sp_fps.setRange(1, 60)
        sp_fps.setValue(self.fps)
        lo_fps.addWidget(sp_fps)
        
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(fpsPopup.accept)
        buttonBox.rejected.connect(fpsPopup.reject)
        lo_fps.addWidget(buttonBox)
        
        if fpsPopup.exec_() == QDialog.Accepted:
            self.setPlaybackFps(sp_fps.value())


    #   Updates FPS Timer
    @err_catcher(name=__name__)
    def setPlaybackFps(self, fps:int):
        self.fps = fps
        if hasattr(self, 'timer') and self.timer.isActive():
            interval = max(10, int(1000 / fps))
            self.timer.setInterval(interval)


    ####################################
    ##            CONTROLS            ##
    ####################################

    #   Plays Images Based on FPS Timer
    @err_catcher(name=__name__)
    def play(self):
        if not hasattr(self, 'timer'):
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.nextFramePlay)

        #   Minimum 10ms to Prevent Overload
        interval = max(10, int(1000 / self.fps))
        self.timer.start(interval)

        pausePath = os.path.join(self.iconDir, "pause.png")
        if os.path.exists(pausePath):
            icon = self.core.media.getColoredIcon(pausePath)
            self.b_play.setIcon(icon)

        self.b_play.setToolTip("Pause")


    @err_catcher(name=__name__)
    def pause(self):
        if hasattr(self, 'timer'):
            self.timer.stop()

        playPath = os.path.join(self.iconDir, "play.png")
        if os.path.exists(playPath):
            icon = self.core.media.getColoredIcon(playPath)
            self.b_play.setIcon(icon)

        self.b_play.setToolTip("Play")


    @err_catcher(name=__name__)
    def nextFramePlay(self):
        if not self.imageFiles:
            self.pause()
            return
        
        self.currentIndex = (self.currentIndex + 1) % len(self.imageFiles)
        self.slider.setValue(self.currentIndex)

        self.displayImage(self.currentIndex)


    @err_catcher(name=__name__)
    def onFirstClicked(self):
        if self.imageFiles:
            self.currentIndex = 0
            self.slider.setValue(self.currentIndex)

            self.displayImage(self.currentIndex)


    @err_catcher(name=__name__)
    def onLastClicked(self):
        if self.imageFiles:
            self.currentIndex = len(self.imageFiles) - 1
            self.slider.setValue(self.currentIndex)

            self.displayImage(self.currentIndex)


    @err_catcher(name=__name__)
    def onPrevClicked(self):
        if self.imageFiles:
            self.currentIndex = max(0, self.currentIndex - 1)
            self.slider.setValue(self.currentIndex)

            self.displayImage(self.currentIndex)


    @err_catcher(name=__name__)
    def onNextClicked(self):
        if self.imageFiles:
            self.currentIndex = min(len(self.imageFiles) - 1, self.currentIndex + 1)
            self.slider.setValue(self.currentIndex)

            self.displayImage(self.currentIndex)


    @err_catcher(name=__name__)
    def onPlayClicked(self):
        if hasattr(self, 'timer') and self.timer.isActive():
            self.pause()
        else:
            if self.imageFiles:
                self.play()


    @err_catcher(name=__name__)
    def onCurrentChanged(self, value):
        self.currentIndex = value - 1
        self.slider.setValue(self.currentIndex)

        self.displayImage(self.currentIndex)


    @err_catcher(name=__name__)
    def sliderChanged(self, value):
        self.currentIndex = value

        self.displayImage(value)


    ####################################
    ##         FILE HANDLING          ##
    ####################################

    #   Opens File Explorer to Choose Image Files
    @err_catcher(name=__name__)
    def addFiles(self) -> None:
        #   Resolve Initial Dir to Open To
        existingDir = None

        #   If first Image if it Exists
        if self.imageFiles:
            firstFile = self.imageFiles[0]
            if firstFile and os.path.isfile(firstFile):
                existingDir = os.path.dirname(firstFile)

        #   Or Use Project Dir
        if not existingDir:
            existingDir = self.core.projectPath

        #   Or Fallback
        if not existingDir:
            existingDir = os.getcwd()

        fileDialog = QFileDialog(self)
        fileDialog.setDirectory(existingDir)
        fileDialog.setFileMode(QFileDialog.ExistingFiles)
        fileDialog.setNameFilter("Image Files (*.png *.jpg *.jpeg *.tif *.tiff *.exr *.dpx);;All Files (*)")

        if fileDialog.exec_():
            #   Get Selected Files
            files = fileDialog.selectedFiles()

            for file in files:
                #   If File not Already in List, Get Pixmap and Add to Cache
                if file not in self.imageFiles:
                    self.imageFiles.append(file)
                    self.pixmapCache.append(self.loadPixmap(file))

            self.listWidget.clear()

            #   Rebuild List to Update Row Numbers
            for i, file in enumerate(self.imageFiles):
                item = QListWidgetItem()
                item.setData(Qt.UserRole, file)
                item.setToolTip(file)
                widget = self.createListItemWidget(file, i)
                item.setSizeHint(widget.sizeHint())
                self.listWidget.addItem(item)
                self.listWidget.setItemWidget(item, widget)

            self.slider.setRange(0, max(0, len(self.imageFiles) - 1))
            self.sp_current.setRange(1, max(1, len(self.imageFiles)))

            if self.imageFiles:
                self.displayImage(0)
            else:
                self.l_end.setText("1")
                self.sp_current.setValue(1)


    #   Clears the Image List and Resets Player UI
    @err_catcher(name=__name__)
    def clearFiles(self):
        #   Stop Playback before Clearing
        if hasattr(self, 'timer') and self.timer.isActive():
            self.pause()

        self.imageFiles.clear()
        self.pixmapCache.clear()
        self.listWidget.clear()
        self.slider.setRange(0, 0)
        self.currentIndex = 0
        self.slider.setValue(0)
        self.sp_current.setValue(1)
        self.imageLabel.clear()
        self.l_end.setText("1")


    #   Loads the Viewer and Displays
    @err_catcher(name=__name__)
    def load(self, iflPath:str, imageFiles:list) -> None:
        '''Loads the Viewer and Displays'''

        self.iflPath = iflPath
        self.imageFiles = imageFiles[:] if imageFiles else []
        self.pixmapCache.clear()
        self.currentIndex = 0

        if hasattr(self, 'loadTimer') and self.loadTimer.isActive():
            self.loadTimer.stop()

        self.listWidget.clear()
        self.slider.setRange(0, max(0, len(self.imageFiles) - 1))
        self.slider.setValue(0)
        self.sp_current.setRange(1, max(1, len(self.imageFiles)))
        self.sp_current.setValue(1)
        self.l_end.setText(str(max(1, len(self.imageFiles))))
        self.l_start.setText("1")
        self.imageLabel.clear()

        self.loadImageRows()
        self.show()


    #   Returns a List of the User-sorted Survey Image Paths
    @err_catcher(name=__name__)
    def getOrderedFiles(self) -> list:
        '''Returns a List of the User-sorted Survey Image Paths'''
        return self.imageFiles


    ####################################
    ##       RCL MENU ACTIONS         ##
    ####################################

    #   Opens Item in File Explorer in Separate Process
    def openInExplorer(self):
        selectedItems = self.listWidget.selectedItems()

        if not selectedItems:
            return
        
        #   Get the Path of the First Selected Item
        item = selectedItems[0]
        filePath = item.data(Qt.UserRole)

        if os.path.isfile(filePath):
            import subprocess

            try:
                filePath = os.path.normpath(filePath)
                subprocess.Popen(['explorer', '/select,', filePath])

            except Exception as e:
                logger.warning(f"Failed to open Explorer: {e}")


    #   Remove the Selected Image Rows from List
    @err_catcher(name=__name__)
    def removeSelectedImages(self):
        selectedItems = self.listWidget.selectedItems()
        if not selectedItems:
            return
        
        #   Get Indices, Sort Descending to Remove
        indices = sorted([self.listWidget.row(item) for item in selectedItems], reverse=True)

        #   Remove from List and Cache
        for idx in indices:
            del self.imageFiles[idx]
            del self.pixmapCache[idx]

        self.listWidget.clear()

        #   Rebuild List to Update Row Numbers
        for i, file in enumerate(self.imageFiles):
            item = QListWidgetItem()
            item.setData(Qt.UserRole, file)
            item.setToolTip(file)
            widget = self.createListItemWidget(file, i)
            item.setSizeHint(widget.sizeHint())
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, widget)

        #   Update Player UI
        self.slider.setRange(0, max(0, len(self.imageFiles) - 1))
        self.sp_current.setRange(1, max(1, len(self.imageFiles)))

        if self.currentIndex >= len(self.imageFiles):
            self.currentIndex = len(self.imageFiles) - 1 if self.imageFiles else 0

        self.slider.setValue(self.currentIndex)

        self.displayImage(self.currentIndex)


    #   Inverts the Selected Rows
    @err_catcher(name=__name__)
    def invertSelection(self):
        selectedItems = self.listWidget.selectedItems()
        if len(selectedItems) <= 1:
            return
        
        #   Get Selected Indices
        indices = sorted([self.listWidget.row(item) for item in selectedItems])

        #   Get the Files and Pixmaps from Cache in Order
        selectedFiles = [self.imageFiles[i] for i in indices]
        selectedPixmaps = [self.pixmapCache[i] for i in indices]

        #   Reverse the Selected Objects
        selectedFiles.reverse()
        selectedPixmaps.reverse()

        # Replace the List Items and Cache
        for i, idx in enumerate(indices):
            self.imageFiles[idx] = selectedFiles[i]
            self.pixmapCache[idx] = selectedPixmaps[i]

        #   Rebuild List
        self.rebuildList()


    #   Calls to Sort the Image List Ascending
    @err_catcher(name=__name__)
    def sortSelectionAscending(self):
        self._sortSelection(reverse=False)


    #   Calls to Sort the Image List Descending
    @err_catcher(name=__name__)
    def sortSelectionDescending(self):
        self._sortSelection(reverse=True)


    #   Sorts the Selected Items 
    def _sortSelection(self, reverse:bool=False):

        #   Small Helper from Prism
        def getFrameNum(file:str) -> int:
            return self.core.media.getFrameNumberFromFilename(file) or 0
        
        #   Get Selected Items
        selectedItems = self.listWidget.selectedItems()
        if len(selectedItems) <= 1:
            return
        
        #   Get Indices
        indices = sorted([self.listWidget.row(item) for item in selectedItems])

        #   Get the Files and Pixmaps in Order
        selectedFiles = [self.imageFiles[i] for i in indices]
        selectedPixmaps = [self.pixmapCache[i] for i in indices]

        #   Sort the Items Data Pairs
        sorted_pairs = sorted(zip(selectedFiles, selectedPixmaps), key=lambda x: getFrameNum(x[0]), reverse=reverse)
        selectedFiles, selectedPixmaps = zip(*sorted_pairs)

        # Replace the List Items
        for i, idx in enumerate(indices):
            self.imageFiles[idx] = selectedFiles[i]
            self.pixmapCache[idx] = selectedPixmaps[i]

        #   Rebuild Image List
        self.rebuildList()


    ####################################
    ##           IMAGE ROWS           ##
    ####################################

    #   Loads the Image File Rows into the Image List
    @err_catcher(name=__name__)
    def loadImageRows(self):
        #   Timer for Deferred Image Loading
        self.loadTimer = QTimer(self)
        self.loadTimer.setSingleShot(True)

        #   Called Each Time the Timer Expires
        self.loadTimer.timeout.connect(self.createImagesRow)

        self.loadIndex = 0

        #   Defer Image Loading to After UI is Displayed
        self.loadTimer.start(100)


    #   Loads Each Image File into Image File List
    @err_catcher(name=__name__)
    def createImagesRow(self):
        #   Will Execute if there are Still Images not yet Loaded
        if self.loadIndex < len(self.imageFiles):
            #   Get Pixmap of the File and Add to Cache
            file = self.imageFiles[self.loadIndex]
            pixmap = self.loadPixmap(file)
            self.pixmapCache.append(pixmap)
            
            #   Create Image File Item
            item = QListWidgetItem()
            item.setData(Qt.UserRole, file)
            item.setToolTip(file)
            widget = self.createListItemWidget(file, self.loadIndex)
            item.setSizeHint(widget.sizeHint())

            #   Add to Image List
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, widget)
            
            #   Update Player UI
            self.slider.setRange(0, max(0, len(self.pixmapCache) - 1))
            self.sp_current.setRange(1, max(1, len(self.pixmapCache)))
            self.l_end.setText(str(max(1, len(self.pixmapCache))))
            
            #   Display First Image
            if self.loadIndex == 0:
                self.displayImage(0)
            
            #   Schedule Next Image Load (non-blocking)
            self.loadIndex += 1
            self.loadTimer.start(50)


    #   Update Rows Order Based on List Order
    @err_catcher(name=__name__)
    def onRowsMoved(self, *args):
        old_files = self.imageFiles[:]
        self.imageFiles = []

        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            self.imageFiles.append(item.data(Qt.UserRole))

        #   Reorder Pixmap Cache to Match New Order
        self.pixmapCache = [self.pixmapCache[old_files.index(f)] for f in self.imageFiles]
        self.slider.setRange(0, max(0, len(self.imageFiles) - 1))

        if self.currentIndex >= len(self.imageFiles):
            self.currentIndex = len(self.imageFiles) - 1 if self.imageFiles else 0

        self.slider.setValue(self.currentIndex)

        self.displayImage(self.currentIndex)


    #   Rebuilt Image List with Current Items
    def rebuildList(self):
        self.listWidget.clear()

        for i, file in enumerate(self.imageFiles):
            item = QListWidgetItem()
            item.setData(Qt.UserRole, file)
            item.setToolTip(file)
            widget = self.createListItemWidget(file, i)
            item.setSizeHint(widget.sizeHint())
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, widget)

        #   Update Current Index if Needed
        if self.currentIndex >= len(self.imageFiles):
            self.currentIndex = len(self.imageFiles) - 1 if self.imageFiles else 0
        self.slider.setValue(self.currentIndex)

        self.displayImage(self.currentIndex)


    @err_catcher(name=__name__)
    def _getElidedPath(self, filepath:str, maxWidth:int) -> str:
        """Returns an elided version of the filepath for display."""

        fontMetrics = self.listWidget.fontMetrics()
        return fontMetrics.elidedText(filepath, Qt.ElideMiddle, maxWidth)


    def _calculateItemHeight(self) -> int:
        """Calculate the proper height for list items."""

        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        fontMetrics = QFontMetrics(font)

        #   Font eight + padding + stylesheet padding
        return fontMetrics.height() + 10 + 8  


    @err_catcher(name=__name__)
    def createListItemWidget(self, filepath:str, index:int) -> QWidget:
        """Creates a custom widget for list items with thumbnail and text."""

        itemHeight = self._calculateItemHeight()
        widget = ListItemWidget(itemHeight)
        
        layout = widget.layout()
        layout.setContentsMargins(2, 0, 2, 0)
        layout.setSpacing(2)

        #   Frame Number
        frameLabel = QLabel(str(index + 1))
        frameLabel.setStyleSheet("font-weight: bold; color: #888;")
        layout.addWidget(frameLabel)

        layout.addSpacing(6)

        #   Reorder Icon
        reorderLabel = QLabel()
        reorderIcon = QIcon(os.path.join(self.iconDir, "reorder.png"))
        reorderLabel.setPixmap(reorderIcon.pixmap(12, 12))
        layout.addWidget(reorderLabel)

        layout.addSpacing(6)

        #   File Name in Bold
        filename = os.path.basename(filepath)
        filenameLabel = QLabel(filename)
        filenameLabel.setStyleSheet("font-weight: bold; font-size: 12px;")
        layout.addWidget(filenameLabel)

        layout.addSpacing(16)

        # Full Filepath
        fontMetrics = self.listWidget.fontMetrics()
        filenameWidth = fontMetrics.horizontalAdvance(filename)
        usedWidth = 50 + 6 + 16 + 6 + filenameWidth + 16 + 10
        availablePathWidth = max(self.listWidget.width() - usedWidth, 100)
        
        elidedPath = self._getElidedPath(filepath, availablePathWidth)
        pathLabel = QLabel(f"({elidedPath})")
        pathLabel.setStyleSheet("color: #a3a2a2; font-size: 11px;")
        pathLabel.setMaximumWidth(availablePathWidth)
        layout.addWidget(pathLabel)

        layout.addStretch()

        return widget


    ####################################
    ##         VIEWER DISPLAY         ##
    ####################################

    #   Gets Pixmap from Prism Media
    def loadPixmap(self, filepath:str) -> QPixmap:
        try:
            pixmap = self.core.media.getPixmapFromPath(filepath)

        except Exception as e:
            logger.warning(f"Failed to load {filepath} with OpenImageIO: {e}")
            #   Create Null Oixmap
            pixmap = QPixmap()
        
        return pixmap


    #   Displays the Current Image in the Viewer and Updates UI
    @err_catcher(name=__name__)
    def displayImage(self, index:int):
        if self.pixmapCache and 0 <= index < len(self.pixmapCache):
            pixmap = self.pixmapCache[index]

            if not pixmap.isNull():
                #   Scale Pixmap and Set to Viewer Label
                scaledPixmap = pixmap.scaled(self.imageLabel.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.imageLabel.setPixmap(scaledPixmap)

            else:
                #   Display Error Message if Pixmap Failed to Load
                self.imageLabel.clear()
                self.imageLabel.setStyleSheet("font-weight: bold; color: #e0e0e0;")
                self.imageLabel.setText("Unable to load image")

            self.sp_current.setValue(index + 1)

        else:
            self.imageLabel.clear()
            self.sp_current.setValue(1)

        #   Update Player UI
        self.l_end.setText(str(max(1, len(self.imageFiles))))
        self.sp_current.setRange(1, max(1, len(self.imageFiles)))

        #   Highlight Current Item in List
        self.listWidget.blockSignals(True)

        for i in range(self.listWidget.count()):
            self.listWidget.item(i).setSelected(i == index)

        self.listWidget.blockSignals(False)


        if 0 <= index < self.listWidget.count():
            self.listWidget.scrollToItem(self.listWidget.item(index))



###################################
##    Custom List Widget Item    ##
class ListItemWidget(QWidget):
    '''Custom List Widget Item '''

    def __init__(self, height, parent=None):
        super(ListItemWidget, self).__init__(parent)
        self.itemHeight:int = height
        self.mainLayout = QHBoxLayout(self)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(0)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    
    def sizeHint(self):
        # Return Min Width with Fixed Height
        return QSize(0, self.itemHeight)
    
    def layout(self):
        """Return the main layout for adding widgets."""
        return self.mainLayout
    


###################################
##      Custom Resize Filter     ##
class _StateResizeFilter(QObject):
    """Event filter installed on sa_stateSettings to trigger re-eliding on resize."""

    def __init__(self, callback):
        super().__init__()
        self._callback = callback

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Resize:
            self._callback()
        return False