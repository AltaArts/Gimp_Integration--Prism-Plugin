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


import os
import platform
import re
import subprocess
import json


from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from PrismUtils.Decorators import err_catcher_plugin as err_catcher

PLUGIN_PATH = os.path.dirname(os.path.dirname(__file__))
CONFIG_FILE = os.path.join(PLUGIN_PATH, "GimpConfig.json")


class Prism_Gimp_externalAccess_Functions(object):
    def __init__(self, core, plugin):
        self.core = core
        self.plugin = plugin

        self.core.registerCallback("getPresetScenes",
                                   self.getPresetScenes,
                                   plugin=self.plugin)

        self.core.registerCallback("userSettings_saveSettings",
                                   self.userSettings_saveSettings,
                                   plugin=self.plugin,)
        
        self.core.registerCallback("userSettings_loadSettings",
                                   self.userSettings_loadSettings,
                                   plugin=self.plugin,)

        ssheetPath = os.path.join(self.pluginDirectory, "UserInterfaces", "GimpStyleSheet")
        self.core.registerStyleSheet(ssheetPath)


    @err_catcher(name=__name__)
    def userSettings_loadUI(self, origin, tab):
        origin.gb_settings = QGroupBox("Settings")
        lo_settings = QVBoxLayout()

        ##   defaults    ##
        df_port = "40404"
        df_logSize = 500
        logPath = os.path.join(PLUGIN_PATH, "Logs", "Gimp-Prism_Log.log")

        # Debug Log Level
        l_logLevel = QLabel("Gimp Msg Display")
        logLevelItems = "Log Only", "Minimal", "All" 
        origin.cb_gimp_logLevel = QComboBox()
        origin.cb_gimp_logLevel.addItems(logLevelItems)
        origin.cb_gimp_logLevel.setCurrentIndex(1)

        spacer_1 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Max Log Size
        l_maxSize = QLabel("Max Log Size: ")
        origin.spb_gimp_maxSize = QSpinBox()
        origin.spb_gimp_maxSize.setMinimum(100)  # Set minimum value to 100
        origin.spb_gimp_maxSize.setMaximum(1000)  # Set maximum value to 1000
        origin.spb_gimp_maxSize.setValue(df_logSize)  # Default value
        l_kb = QLabel("kb's")

        spacer_2 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Prism->Gimp Comm Port
        l_port = QLabel("Comm Port")
        origin.e_gimp_port = QLineEdit()
        origin.e_gimp_port.setText(df_port)  # Default value
        origin.e_gimp_port.setFixedWidth(100)  # Set the width to 100 pixels

        #   Add to H layout
        lo_settings_1 = QHBoxLayout()
        lo_settings_1.addWidget(l_logLevel)
        lo_settings_1.addWidget(origin.cb_gimp_logLevel)
        lo_settings_1.addItem(spacer_1)
        lo_settings_1.addWidget(l_maxSize)
        lo_settings_1.addWidget(origin.spb_gimp_maxSize)
        lo_settings_1.addWidget(l_kb)
        lo_settings_1.addItem(spacer_2)
        lo_settings_1.addWidget(l_port)
        lo_settings_1.addWidget(origin.e_gimp_port)
        container_settings_1 = QWidget()
        container_settings_1.setLayout(lo_settings_1)

        # Open Log Button
        but_openLog = QPushButton("Open Log")
        but_openLog.setFixedWidth(100)  # Set the button width to 40 pixels

        # Line Edit for Log Path
        origin.e_logPath = QLineEdit()
        origin.e_logPath.setText(logPath)
        origin.e_logPath.setReadOnly(True)

        # Button for browsing
        but_changeLogLoc = QPushButton("...")
        but_changeLogLoc.setFixedWidth(60)

        lo_settings_2 = QHBoxLayout()
        lo_settings_2.addWidget(but_openLog)
        lo_settings_2.addWidget(origin.e_logPath)
        lo_settings_2.addWidget(but_changeLogLoc)
        container_settings_2 = QWidget()
        container_settings_2.setLayout(lo_settings_2)

        origin.gb_settings.setStyleSheet("QGroupBox { margin-left: 10px; margin-right: 10px; }")
        # lo_settings.setVerticalSpacing(1)  # Set the spacing between rows to 5 pixels

        #   Connections
        origin.e_gimp_port.editingFinished.connect(lambda: self.checkPortInput(origin))
        but_openLog.clicked.connect(lambda: self.openLog(origin))
        but_changeLogLoc.clicked.connect(lambda: self.changeLogDir(origin))

        #   Tool Tips
        tip = ("Select how logging is displayed in Gimp.\n"       #   TODO
               "Messages will be displayed in the Error Console\n\n"
               "Notes:\n"
               "    Messages can slow down Gimp's interface\n"
               "    Messages will always be logged to logfile")
        l_logLevel.setToolTip(tip)
        origin.cb_gimp_logLevel.setToolTip(tip)

        tip = ("Max Size of the Prism-Gimp log in kilobytes.  After reaching this,\n"
               "the log will be backed up and a new one wil be started.  Max two files.")
        l_maxSize.setToolTip(tip)
        origin.spb_gimp_maxSize.setToolTip(tip)
        l_kb.setToolTip(tip)

        tip = ("Port to use for socket communications between Prism and Gimp.\n"
               "All data is contained in the single machine's local 127.0.0.1.\n"
               "An open and availble port must be used for Gimp-Prism functions")
        l_port.setToolTip(tip)
        origin.e_gimp_port.setToolTip(tip)

        tip = "Open the Prism-Gimp log file"
        but_openLog.setToolTip(tip)

        tip = ("Location of Prism-Gimp Logfile.\n"
               "Set automatically during intergration.")
        origin.e_logPath.setToolTip(tip)

        tip = ("Change Log File location")
        but_changeLogLoc.setToolTip(tip)

        lo_settings.addWidget(container_settings_1)
        lo_settings.addWidget(container_settings_2)
        lo_settings.setSpacing(0)

        origin.gb_settings.setLayout(lo_settings)
        tab.layout().addWidget(origin.gb_settings)


    @err_catcher(name=__name__)
    def userSettings_saveSettings(self, origin, settings):
        #   Saves to both Prism settings and Gimp Plugin config
        if "gimp" not in settings:
            settings["gimp"] = {}
        
        gimpSettings = {}

        commPort = origin.e_gimp_port.text()
        settings["gimp"]["commPort"] = commPort
        gimpSettings["commPort"] = commPort

        logMax = origin.spb_gimp_maxSize.value()
        settings["gimp"]["logMax"] = logMax
        gimpSettings["logMax"] = logMax

        logLevel = origin.cb_gimp_logLevel.currentText()
        settings["gimp"]["logLevel"] = logLevel
        gimpSettings["logLevel"] = logLevel

        logLocation = origin.e_logPath.text()
        settings["gimp"]["logLocation"] = logLocation
        gimpSettings["logLocation"] = logLocation

        #    save to specific Gimp config file so Gimp intergrtion can find it
        with open(CONFIG_FILE, 'w') as file:
            json.dump(gimpSettings, file, indent=4)
        

    @err_catcher(name=__name__)
    def userSettings_loadSettings(self, origin, settings):
        if "gimp" in settings:
            if "commPort" in settings["gimp"]:
                origin.e_gimp_port.setText(settings["gimp"]["commPort"])

            if "logMax" in settings["gimp"]:
                origin.spb_gimp_maxSize.setValue(settings["gimp"]["logMax"])

            if "logLevel" in settings["gimp"]:
                idx = origin.cb_gimp_logLevel.findText(settings["gimp"]["logLevel"])
                if idx != -1:
                    origin.cb_gimp_logLevel.setCurrentIndex(idx)

            if "logLocation" in settings["gimp"]:
                origin.e_logPath.setText(settings["gimp"]["logLocation"])


    @err_catcher(name=__name__)
    def openLog(self, origin):

        logFile = origin.e_logPath.text()

        if os.path.exists(logFile):
            try:
                subprocess.Popen([logFile], shell=True)
            except Exception as e:
                self.core.popup(f"Error opening log file:\n{e}")
        else:
            self.core.popup(f"Log file does not exist: {logFile}")


    @err_catcher(name=__name__)
    def changeLogDir(self, origin):            
        newDir = QFileDialog.getExistingDirectory(origin, "Select Log Directory")

        if newDir:
                logPath = os.path.join(newDir, "Gimp-Prism_Log.log")

                if platform.system() == "Windows":
                    logPath = logPath.replace("/", "\\")

                origin.e_logPath.setText(logPath)


    @err_catcher(name=__name__)
    def checkPortInput(self, origin):
        port_text = origin.e_gimp_port.text()

        # Regular expression to match only digits
        if re.match(r'^\d+$', port_text):
            # Check if the port number is within the valid range
            port = int(port_text)
            if 0 <= port <= 65535:
                return True
            else:
                self.core.popup("Port is not within the valid range (0-65535)")
        else:
            self.core.popup("Input contains non-numeric characters")
    

    @err_catcher(name=__name__)
    def getAutobackPath(self, origin):
        autobackpath = ""
        if platform.system() == "Windows":
            autobackpath = os.path.join(
                self.core.getWindowsDocumentsPath(), "Gimp"
            )

        fileStr = "Gimp Scene File ("
        for i in self.sceneFormats:
            fileStr += "*%s " % i

        fileStr += ")"

        return autobackpath, fileStr


    @err_catcher(name=__name__)
    def copySceneFile(self, origin, origFile, targetPath, mode="copy"):
        pass


    @err_catcher(name=__name__)
    def getPresetScenes(self, presetScenes):
        presetDir = os.path.join(self.pluginDirectory, "Presets")
        scenes = self.core.entities.getPresetScenesFromFolder(presetDir)
        presetScenes += scenes