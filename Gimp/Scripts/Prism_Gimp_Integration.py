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
import sys
import platform
import shutil
import re

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

if platform.system() == "Windows":
    if sys.version[0] == "3":
        import winreg as _winreg
    else:
        import _winreg

from PrismUtils.Decorators import err_catcher_plugin as err_catcher


class Prism_Gimp_Integration(object):
    def __init__(self, core, plugin):
        self.core = core
        self.plugin = plugin

        if platform.system() == "Windows":
            self.examplePath = (
                os.path.dirname(self.getGimpPath())
                or r"C:\Program Files\GIMP 2.99\lib\gimp\2.99\plug-ins"
                )
        elif platform.system() == "Linux":
            userName = (
                os.environ["SUDO_USER"]
                if "SUDO_USER" in os.environ
                else os.environ["USER"]
            )
            self.examplePath = os.path.join("/home", userName, "Gimp", "2019")
        elif platform.system() == "Darwin":
            userName = (
                os.environ["SUDO_USER"]
                if "SUDO_USER" in os.environ
                else os.environ["USER"]
            )
            self.examplePath = (
                "/Users/%s/Library/Preferences/Autodesk/Gimp/2019" % userName
            )

    @err_catcher(name=__name__)                                         #   WORKING
    def getExecutable(self):
        execPath = ""
        if platform.system() == "Windows":
            defaultpath = os.path.join(self.getGimpPath(), "Gimp-2.99.exe")         #   TODO    HARDCODED
            if os.path.exists(defaultpath):
                execPath = defaultpath

        return execPath

    @err_catcher(name=__name__)
    def getGimpPath(self):                                              #   WORKING
        try:
            key = _winreg.OpenKey(
                _winreg.HKEY_LOCAL_MACHINE,
                "SOFTWARE\\Classes\\GIMP2.xcf\\shell\\open\\command",
                0,
                _winreg.KEY_READ | _winreg.KEY_WOW64_64KEY,
            )
            gimpPath = (
                (_winreg.QueryValueEx(key, ""))[0].split(' "%1"')[0].replace('"', "")
            )

            if os.path.exists(gimpPath):
                return gimpPath
            else:
                return ""

        except:
            return ""

    def addIntegration(self, installPath):                                 #   WORKING WITH HARDCODED USER APPDATA PATH
        try:
            integrationBase = os.path.join(
                os.path.dirname(os.path.dirname(__file__)), "Integration"
            )
            addedFiles = []

            match = re.search(r'GIMP (\d+\.\d+)', installPath)
            gimpVersion = match.group(1)

            if platform.system() == "Windows":
                appdataFolder = os.environ['APPDATA']
                initpath = os.path.join(appdataFolder, "GIMP", gimpVersion, "plug-ins", "PrismInit.py")
            else:
                msgStr = ("Gimp may only be Installed on Windows at this time")
                QMessageBox.warning(self.core.messageParent, "Prism Integration", msgStr)
                return False

            origInitFile = os.path.join(integrationBase, "PrismInit.py")

            shutil.copy2(origInitFile, initpath)
            addedFiles.append(initpath)

            with open(initpath, "r") as init:
                initStr = init.read()

            with open(initpath, "w") as init:
                initStr = initStr.replace(
                    "PRISMROOT", '"%s"' % self.core.prismRoot.replace("\\", "/")
                )
                init.write(initStr)

            if platform.system() in ["Linux", "Darwin"]:
                for i in addedFiles:
                    os.chmod(i, 0o777)

            return True

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()

            msgStr = (
                "Errors occurred during the installation of the Gimp integration.\nThe installation is possibly incomplete.\n\n%s\n%s\n%s"
                % (str(e), exc_type, exc_tb.tb_lineno)
            )
            msgStr += "\n\nRunning this application as administrator could solve this problem eventually."

            QMessageBox.warning(self.core.messageParent, "Prism Integration", msgStr)
            return False

    def removeIntegration(self, installPath):                       #   WORKING WITH HARDCODED USER APPDATA PATH
        try:
            if platform.system() == "Windows":
                appdataFolder = os.environ['APPDATA']
                installPath = os.path.join(appdataFolder, "GIMP", "2.10", "plug-ins")
            else:
                msgStr = ("Gimp may only be Installed on Windows at this time")

                QMessageBox.warning(self.core.messageParent, "Prism Integration", msgStr)
                return False



            initPy = os.path.join(installPath, "PrismInit.py")
            initPyc = os.path.join(installPath, "PrismInit.pyc")

            for i in [initPy, initPyc]:
                if os.path.exists(i):
                    os.remove(i)

            userSetup = os.path.join(installPath, "scripts", "userSetup.py")
            self.core.integration.removeIntegrationData(filepath=userSetup)

            return True
        

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()

            msgStr = (
                "Errors occurred during the removal of the Gimp integration.\n\n%s\n%s\n%s"
                % (str(e), exc_type, exc_tb.tb_lineno)
            )
            msgStr += "\n\nRunning this application as administrator could solve this problem eventually."

            QMessageBox.warning(self.core.messageParent, "Prism Integration", msgStr)
            return False

    def updateInstallerUI(self, userFolders, pItem):                                        #   TODO
        try:
            pluginItem = QTreeWidgetItem([self.plugin.pluginName])
            pItem.addChild(pluginItem)

            pluginPath = self.examplePath

            if pluginPath != None and os.path.exists(pluginPath):
                pluginItem.setCheckState(0, Qt.Checked)
                pluginItem.setText(1, pluginPath)
                pluginItem.setToolTip(0, pluginPath)
            else:
                pluginItem.setCheckState(0, Qt.Unchecked)
                pluginItem.setText(1, "< doubleclick to browse path >")
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            msg = QMessageBox.warning(
                self.core.messageParent,
                "Prism Installation",
                "Errors occurred during the installation.\n The installation is possibly incomplete.\n\n%s\n%s\n%s\n%s"
                % (__file__, str(e), exc_type, exc_tb.tb_lineno),
            )
            return False

    def installerExecute(self, pluginItem, result):                                     #   TODO
        try:
            pluginPaths = []
            installLocs = []

            if pluginItem.checkState(0) != Qt.Checked:
                return installLocs

            for i in range(pluginItem.childCount()):
                item = pluginItem.child(i)
                if item.checkState(0) == Qt.Checked and os.path.exists(item.text(1)):
                    pluginPaths.append(item.text(1))

            for i in pluginPaths:
                result[
                    "Gimp integration"
                ] = self.core.integration.addIntegration(
                    self.plugin.pluginName, path=i, quiet=True
                )
                if result["Gimp integration"]:
                    installLocs.append(i)

            return installLocs
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            msg = QMessageBox.warning(
                self.core.messageParent,
                "Prism Installation",
                "Errors occurred during the installation.\n The installation is possibly incomplete.\n\n%s\n%s\n%s\n%s"
                % (__file__, str(e), exc_type, exc_tb.tb_lineno),
            )
            return False
