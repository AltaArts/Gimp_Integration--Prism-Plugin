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
#
#                    Gimp3 (2.99) Plugin for Prism2
#
#                           Joshua Breckeen
#                              Alta Arts
#                          josh@alta-arts.com
#
###########################################################################


import os
import sys
import socket
import json
from datetime import datetime
import logging
import tempfile
import time

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from PrismUtils.Decorators import err_catcher as err_catcher

logger = logging.getLogger(__name__)

from Gimp_Export import GimpExportClass


if "PRISM_ROOT" in os.environ:
    prismRoot = os.environ["PRISM_ROOT"]
    if not prismRoot:
        raise Exception("PRISM_ROOT is not set")
else:
    prismRoot = r"C:/Prism2"     

##    CONSTANTS    ##                                                       
GIMPLOCALDIR = os.path.dirname(os.path.dirname(__file__))
CONFIGFILE = os.path.join(GIMPLOCALDIR, "GimpConfig.json")
HOST = "127.0.0.1"



class Prism_Gimp_Functions(object):
    def __init__(self, core, plugin):
        self.core = core
        self.plugin = plugin

        self.core.registerCallback("onStateManagerOpen",
                                    self.onStateManagerOpen,
                                    plugin=self.plugin,
                                    priority=40
                                    )
        

        self.getGimpPluginConfig()

        # self.core.registerCallback(                                           #   NEEDED ????
        #     "onStateCreated", self.onStateCreated, plugin=self.plugin
        #     )

        logger.debug("Starting Prism_Gimp_Functions")


    @err_catcher(name=__name__)
    def startup(self, origin):
        origin.timer.stop()

        self.core.setActiveStyleSheet("Blender")
        appIcon = QIcon(
            os.path.join(self.core.prismRoot, "Scripts", "UserInterfacesPrism", "p_tray.png")
            )

        origin.messageParent = QWidget()

        if self.core.useOnTop:
            origin.messageParent.setWindowFlags(
                origin.messageParent.windowFlags() ^ Qt.WindowStaysOnTopHint
                )

        origin.startAutosaveTimer()


    def getGimpPluginConfig(self):

        logger.debug("Getting Gimp Config")
        try:
            with open(CONFIGFILE, 'r') as file:
                gimpSettings = json.load(file)

            self.port = int(gimpSettings.get("commPort"))

        except FileNotFoundError:
            logger.warning("Config file %s not found." % CONFIGFILE)

        except Exception as e:
            logger.warning("Error reading config file: %s" % e)
            pass


    @err_catcher(name=__name__)
    def autosaveEnabled(self, origin):
        # get autosave enabled
        return False


    @err_catcher(name=__name__)
    def cmdDataToJson(self, command, payload):

        pData = {
            "command": command,
            "data": payload
            }
        
        jData = json.dumps(pData)

        return jData


    @err_catcher(name=__name__)
    def jsonToCmdData(self, jData):

        try:
            pData = json.loads(jData)

            command = pData.get("command")
            payload = pData.get("data")

            return command, payload
        
        except Exception as e:
            self.core.popup(f"Error decoding json:\n{e}")
            return None
    


### vvvvv For Sending Commands to Gimp vvvvv ###

    @err_catcher(name=__name__)
    def sendCmdToGimp(self, sendCmmand, sendData):

        jData = self.cmdDataToJson(sendCmmand, sendData)

        response = self.sendGimpComm(jData)
        rcvCommand, rcvData = self.jsonToCmdData(response)

        return rcvCommand, rcvData
    

    @err_catcher(name=__name__)
    def sendGimpComm(self, jData):
        logger.debug("Sending data to GIMP")

        # time.sleep(1)

        try:
            # Create a socket object
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                # Connect to GIMP
                s.connect((HOST, self.port))
                # Send pDataJson
                s.sendall(jData.encode())
                response = s.recv(40960).decode()

                return response

        except Exception as e:
            logger.error("Error sending data to GIMP: %s", e)
            self.core.popup(f"Error sending data to GIMP:\n{e}")                                      #    TESTING
            # Handle the error as needed

            return False
    
### ^^^^^ For Sending Commands to Gimp ^^^^^ ###




### vvvvv Functions calls from Prism vvvvv ###

    @err_catcher(name=__name__)
    def sceneOpen(self, origin):
        if self.core.shouldAutosaveTimerRun():
            origin.startAutosaveTimer()


    @err_catcher(name=__name__)
    def getCurrentFileName(self, origin, path=True):

        # logger.debug("Getting Current Filename")

        sendCommand = "getCurrentFilename"
        sendPayload = None

        rcvCommand, rcvPayload = self.sendCmdToGimp(sendCommand, sendPayload)

        if rcvCommand is not None and rcvCommand == "currentFilename":
            filePath = rcvPayload.get("filePath")
        else:
            filePath = ""

        return filePath


    @err_catcher(name=__name__)
    def getSceneExtension(self, origin):
        return self.sceneFormats[0]


    @err_catcher(name=__name__)
    def saveScene(self, origin, filePath, details={}):

        logger.debug("Saving Scenefile")

        sendCommand = "saveVersion"
        sendPayload = {"filePath": filePath}
        
        try:
            rcvCommand, rcvPayload = self.sendCmdToGimp(sendCommand, sendPayload)

            if os.path.exists(filePath):
                return True

            else:
                self.core.popup("Save Version Failed", severity="warning")
                return False
     
        except:
            return False
        

    @err_catcher(name=__name__)
    def captureViewportThumbnail(self):
        ssPath = tempfile.NamedTemporaryFile(suffix=".jpg").name

        sendCommand = "captureScreenShot"
        sendData = {"filePath": ssPath}

        rcvCommand, rcvData = self.sendCmdToGimp(sendCommand, sendData)
        pm = self.core.media.getPixmapFromPath(ssPath)

        try:
            os.remove(ssPath)
        except:
            pass

        if rcvCommand == "Success":
            return pm
        else:
            return False
        

    @err_catcher(name=__name__)
    def getImportPaths(self, origin):
        return []

    @err_catcher(name=__name__)
    def getFrameRange(self, origin):
        startframe = 0
        endframe = 100

        return [startframe, endframe]

    @err_catcher(name=__name__)
    def setFrameRange(self, origin, startFrame, endFrame):
        pass

    @err_catcher(name=__name__)
    def getFPS(self, origin):
        return 24

    @err_catcher(name=__name__)
    def setFPS(self, origin, fps):
        pass

    @err_catcher(name=__name__)
    def getAppVersion(self, origin):
        return "1.0"

    @err_catcher(name=__name__)
    def openScene(self, origin, filepath, force=False):
        # load scenefile
        return True

    @err_catcher(name=__name__)
    def sm_export_addObjects(self, origin, objects=None):
        if not objects:
            objects = []  # get selected objects from scene

        for i in objects:
            if not i in origin.nodes:
                origin.nodes.append(i)

        origin.updateUi()
        origin.stateManager.saveStatesToScene()

    @err_catcher(name=__name__)
    def getNodeName(self, origin, node):
        if self.isNodeValid(origin, node):
            try:
                return node.name
            except:
                QMessageBox.warning(
                    self.core.messageParent, "Warning", "Cannot get name from %s" % node
                )
                return node
        else:
            return "invalid"

    @err_catcher(name=__name__)
    def selectNodes(self, origin):
        if origin.lw_objects.selectedItems() != []:
            nodes = []
            for i in origin.lw_objects.selectedItems():
                node = origin.nodes[origin.lw_objects.row(i)]
                if self.isNodeValid(origin, node):
                    nodes.append(node)
            # select(nodes)

    @err_catcher(name=__name__)
    def isNodeValid(self, origin, handle):
        return True

    @err_catcher(name=__name__)
    def getCamNodes(self, origin, cur=False):
        sceneCams = []  # get cams from scene
        if cur:
            sceneCams = ["Current View"] + sceneCams

        return sceneCams

    @err_catcher(name=__name__)
    def getCamName(self, origin, handle):
        if handle == "Current View":
            return handle

        return str(nodes[0])

    @err_catcher(name=__name__)
    def selectCam(self, origin):
        if self.isNodeValid(origin, origin.curCam):
            select(origin.curCam)

    @err_catcher(name=__name__)
    def sm_export_startup(self, origin):
        pass

    # 	@err_catcher(name=__name__)
    # 	def sm_export_setTaskText(self, origin, prevTaskName, newTaskName):
    # 		origin.l_taskName.setText(newTaskName)

    @err_catcher(name=__name__)
    def sm_export_removeSetItem(self, origin, node):
        pass

    @err_catcher(name=__name__)
    def sm_export_clearSet(self, origin):
        pass

    @err_catcher(name=__name__)
    def sm_export_updateObjects(self, origin):
        pass

    @err_catcher(name=__name__)
    def sm_export_exportShotcam(self, origin, startFrame, endFrame, outputName):
        result = self.sm_export_exportAppObjects(
            origin,
            startFrame,
            endFrame,
            (outputName + ".abc"),
            nodes=[origin.curCam],
            expType=".abc",
        )
        result = self.sm_export_exportAppObjects(
            origin,
            startFrame,
            endFrame,
            (outputName + ".fbx"),
            nodes=[origin.curCam],
            expType=".fbx",
        )
        return result

    @err_catcher(name=__name__)
    def sm_export_exportAppObjects(
        self,
        origin,
        startFrame,
        endFrame,
        outputName,
        scaledExport=False,
        nodes=None,
        expType=None,
    ):
        pass

    @err_catcher(name=__name__)
    def sm_export_preDelete(self, origin):
        pass

    @err_catcher(name=__name__)
    def sm_export_unColorObjList(self, origin):
        origin.lw_objects.setStyleSheet(
            "QListWidget { border: 3px solid rgb(50,50,50); }"
        )

    @err_catcher(name=__name__)
    def sm_export_typeChanged(self, origin, idx):
        pass

    @err_catcher(name=__name__)
    def sm_export_preExecute(self, origin, startFrame, endFrame):
        warnings = []

        return warnings

    @err_catcher(name=__name__)
    def sm_export_loadData(self, origin, data):
        pass

    @err_catcher(name=__name__)
    def sm_export_getStateProps(self, origin, stateProps):
        stateProps.update()

        return stateProps

    @err_catcher(name=__name__)
    def sm_render_startup(self, origin):
        pass

    @err_catcher(name=__name__)
    def sm_render_getRenderLayer(self, origin):
        rlayerNames = []

        return rlayerNames

    @err_catcher(name=__name__)
    def sm_render_refreshPasses(self, origin):
        pass

    @err_catcher(name=__name__)
    def sm_render_openPasses(self, origin, item=None):
        pass

    @err_catcher(name=__name__)
    def removeAOV(self, aovName):
        pass

    @err_catcher(name=__name__)
    def sm_render_preSubmit(self, origin, rSettings):
        pass





    @err_catcher(name=__name__)
    def sm_render_startLocalRender(self, origin, outputName, rSettings):


        sendCommand = "exportFile"
        sendPayload = {"rSettings": rSettings}
        
        rcvCommand, rcvPayload = self.sendCmdToGimp(sendCommand, sendPayload)
        
        return rcvPayload






    @err_catcher(name=__name__)
    def sm_render_undoRenderSettings(self, origin, rSettings):
        pass

    @err_catcher(name=__name__)
    def sm_render_getDeadlineParams(self, origin, dlParams, homeDir):
        pass

    @err_catcher(name=__name__)
    def getCurrentRenderer(self, origin):
        return "Renderer"

    @err_catcher(name=__name__)
    def getCurrentSceneFiles(self, origin):
        curFileName = self.core.getCurrentFileName()
        scenefiles = [curFileName]
        return scenefiles

    @err_catcher(name=__name__)
    def sm_render_getRenderPasses(self, origin):
        return []

    @err_catcher(name=__name__)
    def sm_render_addRenderPass(self, origin, passName, steps):
        pass

    @err_catcher(name=__name__)
    def sm_render_preExecute(self, origin):
        warnings = []

        return warnings

    @err_catcher(name=__name__)
    def getProgramVersion(self, origin):
        return "1.0"

    @err_catcher(name=__name__)
    def sm_render_getDeadlineSubmissionParams(self, origin, dlParams, jobOutputFile):
        dlParams["Build"] = dlParams["build"]
        dlParams["OutputFilePath"] = os.path.split(jobOutputFile)[0]
        dlParams["OutputFilePrefix"] = os.path.splitext(
            os.path.basename(jobOutputFile)
        )[0]
        dlParams["Renderer"] = self.getCurrentRenderer(origin)

        if origin.chb_resOverride.isChecked() and "resolution" in dlParams:
            resString = "Image"
            dlParams[resString + "Width"] = str(origin.sp_resWidth.value())
            dlParams[resString + "Height"] = str(origin.sp_resHeight.value())

        return dlParams

    @err_catcher(name=__name__)
    def deleteNodes(self, origin, handles, num=0):
        pass

    @err_catcher(name=__name__)
    def sm_import_disableObjectTracking(self, origin):
        self.deleteNodes(origin, [origin.setName])

    @err_catcher(name=__name__)
    def sm_import_importToApp(self, origin, doImport, update, impFileName):
        return {"result": result, "doImport": doImport}

    @err_catcher(name=__name__)
    def sm_import_updateObjects(self, origin):
        pass

    @err_catcher(name=__name__)
    def sm_import_removeNameSpaces(self, origin):
        pass

    @err_catcher(name=__name__)
    def sm_playblast_startup(self, origin):
        frange = self.getFrameRange(origin)
        origin.sp_rangeStart.setValue(frange[0])
        origin.sp_rangeEnd.setValue(frange[1])

    @err_catcher(name=__name__)
    def sm_playblast_createPlayblast(self, origin, jobFrames, outputName):
        pass

    @err_catcher(name=__name__)
    def sm_playblast_preExecute(self, origin):
        warnings = []

        return warnings

    @err_catcher(name=__name__)
    def sm_playblast_execute(self, origin):
        pass

    @err_catcher(name=__name__)
    def sm_playblast_postExecute(self, origin):
        pass

    @err_catcher(name=__name__)
    def sm_saveImports(self, origin, importPaths):
        pass


    @err_catcher(name=__name__)
    def sm_saveStates(self, origin, buf):
        stateData = json.dumps(buf)

        sendCommand = "saveStates"
        sendPayload = {"stateData": stateData}
        
        result = self.sendCmdToGimp(sendCommand, sendPayload)              #   TODO HANDLE RESULT


    @err_catcher(name=__name__)
    def sm_readStates(self, origin):
        testState = '''{
    "states": [
        {
            "statename": "publish",
            "comment": "",
            "description": ""
        }
    ]
}'''
    
        ####    ADD TRY/EXCEPT
        
        sendCommand = "getStates"
        sendPayload = None
        
        rcvCommand, rcvPayload = self.sendCmdToGimp(sendCommand, sendPayload)

        stateDataRaw = rcvPayload.get("stateData")

        if stateDataRaw is not None and stateDataRaw != "":

            stateData = json.loads(stateDataRaw)

            return stateData
        
        else:
            return testState




    @err_catcher(name=__name__)                                 #   TODO
    def sm_deleteStates(self, origin):
        pass


    @err_catcher(name=__name__)
    def onStateManagerOpen(self, origin):

        origin.setProperty("sizePolicy", "Expanding")
        origin.setMaximumSize(800, 800)  # Adjust the width and height according to your needs

        origin.b_showImportStates.setStyleSheet("padding-left: 1px;padding-right: 1px;")
        origin.b_showExportStates.setStyleSheet("padding-left: 1px;padding-right: 1px;")
        origin.gb_import.setEnabled(False)
        origin.gb_import.hide()
        origin.b_createExport.hide()
        origin.b_createRender.setProperty("sizePolicy", "Expanding")
        origin.b_createRender.setStyleSheet("QPushButton { min-width: 200px; }")
        origin.b_createPlayblast.hide()
        # origin.b_createImport.setMinimumWidth(70 * self.core.uiScaleFactor)
        # origin.b_createImport.setMaximumWidth(70 * self.core.uiScaleFactor)
        # origin.b_createImport.setMinimumHeight(0)
        # origin.b_createImport.setMaximumHeight(500 * self.core.uiScaleFactor)
        # origin.b_shotCam.setMinimumHeight(0)
        # origin.b_shotCam.setMaximumHeight(50 * self.core.uiScaleFactor)
        # origin.b_showImportStates.setMinimumWidth(30 * self.core.uiScaleFactor)
        # origin.b_showImportStates.setMaximumWidth(30 * self.core.uiScaleFactor)
        # origin.b_showExportStates.setMinimumWidth(30 * self.core.uiScaleFactor)
        # origin.b_showExportStates.setMaximumWidth(30 * self.core.uiScaleFactor)
        # origin.b_createExport.setMinimumWidth(70 * self.core.uiScaleFactor)
        # origin.b_createExport.setMaximumWidth(70 * self.core.uiScaleFactor)
        # origin.b_createRender.setMinimumWidth(70 * self.core.uiScaleFactor)
        # origin.b_createRender.setMaximumWidth(70 * self.core.uiScaleFactor)
        # origin.b_createPlayblast.setMinimumWidth(80 * self.core.uiScaleFactor)
        # origin.b_createPlayblast.setMaximumWidth(80 * self.core.uiScaleFactor)
        origin.b_description.setMinimumWidth(35 * self.core.uiScaleFactor)
        origin.b_description.setMaximumWidth(35 * self.core.uiScaleFactor)
        origin.b_preview.setMinimumWidth(35 * self.core.uiScaleFactor)
        origin.b_preview.setMaximumWidth(35 * self.core.uiScaleFactor)

        
        #   Will only load Gimp_Export state if in Gimp
        if self.core.appPlugin.pluginName == "Gimp":

            self.removeDefaultStates(origin)

            origin.loadState(GimpExportClass)


    @err_catcher(name=__name__)
    def removeDefaultStates(self, origin):
        removeStates = ["ImageRender",
                        "ImportFile",
                        "Export",
                        "Playblast",
                        "Standalone USD Playblast",
                        "Standalone USD Render",
                        ]

        for state in removeStates:
            if state in origin.stateTypes.keys():
                del origin.stateTypes[state]



    @err_catcher(name=__name__)
    def sm_getExternalFiles(self, origin):
        extFiles = []
        return [extFiles, []]

    @err_catcher(name=__name__)
    def sm_createRenderPressed(self, origin):
        origin.createPressed("Render")
