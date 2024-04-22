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


class Prism_Gimp_Functions(object):
    def __init__(self, core, plugin):
        self.core = core
        self.plugin = plugin

        self.host = "127.0.0.1"
        self.port_prismToGimp = 40404
        self.port_gimpToPrism = 40405

        self.commsDir = os.path.join(prismRoot, "PrismGimpComms")

        self.core.registerCallback(
            "onStateManagerOpen", self.onStateManagerOpen, plugin=self.plugin
            )
        # self.core.registerCallback(
        #     "onStateCreated", self.onStateCreated, plugin=self.plugin
        #     )

        logger.debug("Starting Prism_Gimp_Functions")


    @err_catcher(name=__name__)
    def startup(self, origin):
        # 	for obj in QApplication.topLevelWidgets():
        # 		if obj.objectName() == 'GimpWindow':
        # 			QtParent = obj
        # 			break
        # 	else:
        # 		return False

        origin.timer.stop()

        self.core.setActiveStyleSheet("Blender")
        appIcon = QIcon(
            os.path.join(self.core.prismRoot, "Scripts", "UserInterfacesPrism", "p_tray.png")
            )

        origin.messageParent = QWidget()
        # 	origin.messageParent.setParent(QtParent, Qt.Window)
        if self.core.useOnTop:
            origin.messageParent.setWindowFlags(
                origin.messageParent.windowFlags() ^ Qt.WindowStaysOnTopHint
                )

        origin.startAutosaveTimer()


    @err_catcher(name=__name__)
    def autosaveEnabled(self, origin):
        # get autosave enabled
        return False



### vvvvv For Sending Commands to Gimp vvvvv ###

    @err_catcher(name=__name__)
    def createCmdFile(self, command, data):

        logger.debug("Creating Command File")

        pData = {
            "command": command,
            "data": data
            }
   
        commOutFile = self.createCommFileName()
       
        # Write the dictionary to the JSON file
        with open(commOutFile, 'w') as json_file:
            json.dump(pData, json_file)
    

    @err_catcher(name=__name__)
    def createCommFileName(self):

        if not os.path.exists(self.commsDir):
            os.makedirs(self.commsDir)

        outName = "Prism--Gimp_Comm-" + str(self.getTimeStamp()) + ".json"
        commOutFile = os.path.join(self.commsDir, outName)

        return commOutFile


    @err_catcher(name=__name__)
    def getTimeStamp(self):            

        current_time = datetime.now().time()
        timeStamp = current_time.strftime("%H%M%S%f")

        return timeStamp


    @err_catcher(name=__name__)
    def pingGimp(self):

        logger.debug("Sending Ping to Gimp")

        command = f'(python-fu-prism-pingFromPrism)'

        result = self.sendToGimp(command)

        return result


    @err_catcher(name=__name__)
    def sendToGimp(self, command):

        # Connect to the GIMP script server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketOut:                #   TODO  Look at configuring Addr/Port
            socketOut.connect((self.host, self.port_prismToGimp))
            
            # Construct the header
            header = b'G' + len(command).to_bytes(2, byteorder='big')

            # Send the header and the script command
            socketOut.sendall(header)
            socketOut.sendall(command.encode())

            # Receive the response
            response_header = socketOut.recv(4)
            response_length = int.from_bytes(response_header[1:], byteorder='big')
            response_data = b''

            while len(response_data) < response_length:
                chunk = socketOut.recv(min(4096, response_length - len(response_data)))
                if not chunk:
                    break
                response_data += chunk

            ####   TODO handle response    ####



    @err_catcher(name=__name__)
    def sendCmdToGimp(self, command, data):

        logger.debug("Sending Command to Gimp")

        #   command: string var
        #   data: dict containing str key/values
        self.createCmdFile(command, data)

        result = self.pingGimp()

        return result
    
### ^^^^^ For Sending Commands to Gimp ^^^^^ ###


### vvvvv For Receiving Commands from Gimp vvvvv ###

    @err_catcher(name=__name__)
    def getCmdFile(self):

        commands = ["currentFilename"]

        files = os.listdir(self.commsDir)

        for fileName in files:
            if fileName.startswith("Gimp--Prism_Comm-"):
                filePath = os.path.join(self.commsDir, fileName)
        
                # Open the   JSON file for reading
                with open(filePath, 'r') as json_file:
                    # Load the JSON data from the file
                    pData = json.load(json_file)

                if pData.get('command') in commands:
                    os.remove(filePath)
                    return pData
                else:
                    print("ERROR:  COMMAND FILE IS NOT VALID")              #   TODO ERRORS

            else:
                print("ERROR: Invalid file:  ", fileName)


### ^^^^^ For Receiving Commands from Gimp ^^^^^ ###



### vvvvv Functions call from Prism vvvvv ###

    @err_catcher(name=__name__)
    def sceneOpen(self, origin):
        if self.core.shouldAutosaveTimerRun():
            origin.startAutosaveTimer()


    @err_catcher(name=__name__)
    def getCurrentFileName(self, origin, path=True):

        logger.debug("Getting Current Filename")

        # pData = {
        #     "command": "getCurrentFilename",
        #     "data": None
        # }

        command = "getCurrentFilename"
        data = None

        result = self.sendCmdToGimp(command, data)

        try:
            pData = self.getCmdFile()
            data = pData.get("data")
            filePath = f"{data.get('filePath')}"

        except:
            filePath = ""

        return filePath


    @err_catcher(name=__name__)
    def getSceneExtension(self, origin):
        return self.sceneFormats[0]


    @err_catcher(name=__name__)
    def saveScene(self, origin, filePath, details={}):

        logger.debug("Saving Scenefile")

        command = "saveVersion"
        data = {"filePath": filePath}
        
        result = self.sendCmdToGimp(command, data)              #   TODO HANDLE RESULT

        try:
            self.core.pb.sceneBrowser.refreshScenefiles()
        except:
            pass
    
        return result
    

    @err_catcher(name=__name__)
    def captureViewportThumbnail(self):
        # ssPath = tempfile.NamedTemporaryFile(suffix=".jpg").name

        ssPath = r"C:\Users\Alta Arts\Desktop\testSS.jpg"

        command = "captureScreenShot"
        data = {"filePath": ssPath}

        result = self.sendCmdToGimp(command, data)

        pm = self.core.media.getPixmapFromPath(ssPath)
        # try:
        #     os.remove(ssPath)
        # except:
        #     pass

        return pm
    
    

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
        pass

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
    def sm_saveStates(self, origin, buf):
        pass

    @err_catcher(name=__name__)
    def sm_saveImports(self, origin, importPaths):
        pass

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
        return testState


    @err_catcher(name=__name__)
    def sm_deleteStates(self, origin):
        pass


    @err_catcher(name=__name__)
    def onStateManagerOpen(self, origin):

        origin.setProperty("sizePolicy", "Expanding")
        origin.setMaximumSize(700, 600)  # Adjust the width and height according to your needs

        origin.b_showImportStates.setStyleSheet("padding-left: 1px;padding-right: 1px;")
        origin.b_showExportStates.setStyleSheet("padding-left: 1px;padding-right: 1px;")
        origin.gb_import.setEnabled(False)
        origin.gb_import.hide()
        origin.b_createExport.setProperty("sizePolicy", "Expanding")
        origin.b_createExport.setStyleSheet("QPushButton { min-width: 200px; }")
        origin.b_createRender.hide()
        origin.b_createPlayblast.hide()
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

        #   Will only load Gimp_Export state if in Gimp
        if self.core.appPlugin.pluginName == "Gimp":
            origin.loadState(GimpExportClass)


    # @err_catcher(name=__name__)
    # def sm_saveStates(self, origin, buf):
    #     bpy.context.scene["PrismStates"] = buf

    @err_catcher(name=__name__)
    def sm_getExternalFiles(self, origin):
        extFiles = []
        return [extFiles, []]

    @err_catcher(name=__name__)
    def sm_createRenderPressed(self, origin):
        origin.createPressed("Render")
