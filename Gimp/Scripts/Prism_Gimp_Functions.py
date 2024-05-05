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
#                        Gimp2 Plugin for Prism2
#
#                           Joshua Breckeen
#                              Alta Arts
#                          josh@alta-arts.com
#
###########################################################################


import os
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
    prismRoot = r"C:/Prism2"                #   TODO Integration


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
                                    priority=40)

        self.getGimpPluginConfig()

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

        logger.debug("Getting Current Filename")

        # sendCommand = "getCurrentFilename"                                                        #   OLD VERSION - DELETE WHEN FINISHED TESTING
        # sendPayload = None

        # rcvCommand, rcvPayload = self.sendCmdToGimp(sendCommand, sendPayload)

        # if rcvCommand is not None and rcvCommand == "currentFilename":
        #     filePath = rcvPayload.get("filePath")
        # else:
        #     filePath = ""

        # self.core.popup(f"filePath in PRISM GIMP FUCNT: {filePath}")                                      #    TESTING


        filePath = os.environ["Gimp_CurrentImagePath"]

        return filePath


    @err_catcher(name=__name__)
    def getSceneExtension(self, origin):
        return self.sceneFormats[0]


    @err_catcher(name=__name__)
    def saveScene(self, origin, filePath, details={}):
        logger.debug("Saving Scenefile")

        sendCommand = "saveVersion"
        sendPayload = {"imagePath": os.environ["Gimp_CurrentImagePath"],
                       "savePath": filePath}
        
        try:
            rcvCommand, rcvPayload = self.sendCmdToGimp(sendCommand, sendPayload)

            if os.path.exists(filePath):
                os.environ["Gimp_CurrentImagePath"] = filePath
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
        sendPayload = {"imagePath": os.environ["Gimp_CurrentImagePath"],
                       "ssPath": ssPath}

        rcvCommand, rcvData = self.sendCmdToGimp(sendCommand, sendPayload)
        pm = self.core.media.getPixmapFromPath(ssPath)

        try:
            os.remove(ssPath)
        except:
            pass

        if rcvCommand == "Success":
            return pm
        else:
            return False
        

    @err_catcher(name=__name__)                                             #   ???
    def getAppVersion(self, origin):

        self.core.popup("GETTING APP VERSION")                                      #    TESTING
        return "1.0"

    @err_catcher(name=__name__)
    def openScene(self, origin, filepath, force=False):
        # load scenefile - I believe it checks if there is an open scenefile
        # But proably not needed for Gimp
        return True

    
    @err_catcher(name=__name__)
    def sm_render_startup(self, origin):
        pass


    @err_catcher(name=__name__)
    def sm_render_preSubmit(self, origin, rSettings):
        pass


    @err_catcher(name=__name__)
    def sm_render_startLocalRender(self, origin, outputName, rSettings):

        sendCommand = "exportFile"

        sendPayload = {"imagePath": os.environ["Gimp_CurrentImagePath"],
                       "rSettings": rSettings}
        
        rcvCommand, rcvPayload = self.sendCmdToGimp(sendCommand, sendPayload)
        
        return rcvPayload


    @err_catcher(name=__name__)
    def sm_render_undoRenderSettings(self, origin, rSettings):
        pass


    @err_catcher(name=__name__)                                             #   ????
    def getCurrentRenderer(self, origin):
        self.core.popup("GETTING CURRENT RENDERER")                                      #    TESTING
        return "Renderer"


    @err_catcher(name=__name__)
    def getCurrentSceneFiles(self, origin):
        curFileName = self.core.getCurrentFileName()
        scenefiles = [curFileName]
        return scenefiles


    @err_catcher(name=__name__)
    def sm_render_preExecute(self, origin):
        warnings = []

        return warnings


    @err_catcher(name=__name__)                                         #   ????
    def getProgramVersion(self, origin):
        self.core.popup("GETTING PROGRAM VERSION")                                      #    TESTING
        return "1.0"


    @err_catcher(name=__name__)
    def sm_saveStates(self, origin, buf):
        stateData = json.dumps(buf)

        sendCommand = "saveStates"
        sendPayload = {"imagePath": os.environ["Gimp_CurrentImagePath"],
                       "stateData": stateData}
        
        self.sendCmdToGimp(sendCommand, sendPayload)


    @err_catcher(name=__name__)
    def sm_readStates(self, origin):
        emptyState = '''{
    "states": [
        {
            "statename": "publish",
            "comment": "",
            "description": ""
        }
    ]
}'''
    
        # try:                                                                              #   TODO REINSTATE TRY/EXCEPT
        sendCommand = "getStates"
        sendPayload = {"imagePath": os.environ["Gimp_CurrentImagePath"]}
        rcvCommand, rcvPayload = self.sendCmdToGimp(sendCommand, sendPayload)

        stateData = rcvPayload.get("stateData")

        if stateData is not None and stateData != "":
            return stateData
        else:
            return emptyState
            
        # except Exception as e:
        #     logger.warning(f"Failed to read states: {e}")
        #     return emptyState


    @err_catcher(name=__name__)
    def sm_deleteStates(self, origin):
        emptyState = '''{
    "states": [
        {
            "statename": "publish",
            "comment": "",
            "description": ""
        }
    ]
}'''

        self.sm_saveStates(origin, emptyState)


    @err_catcher(name=__name__)
    def onStateManagerOpen(self, origin):

        origin.setProperty("sizePolicy", "Expanding")
        origin.setMaximumSize(800, 800)  # Adjust the width and height

        origin.b_showImportStates.setStyleSheet("padding-left: 1px;padding-right: 1px;")
        origin.b_showExportStates.setStyleSheet("padding-left: 1px;padding-right: 1px;")
        origin.gb_import.setEnabled(False)
        origin.gb_import.hide()
        origin.b_createExport.hide()
        origin.b_createRender.setProperty("sizePolicy", "Expanding")
        origin.b_createRender.setStyleSheet("QPushButton { min-width: 200px; }")
        origin.b_createPlayblast.hide()
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
                        "Standalone USD Render",]

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
