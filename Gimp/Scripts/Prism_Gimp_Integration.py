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
#                       Gimp2 Plugin for Prism2
#
#                           Joshua Breckeen
#                              Alta Arts
#                          josh@alta-arts.com
#
###########################################################################


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

        self.pluginRoot = os.path.dirname(os.path.dirname(__file__))

        if platform.system() == "Windows":
            self.examplePath = (
                os.path.dirname(self.getGimpPath())
                or r"C:\Program Files\GIMP 2.10\lib\gimp\2.10\plug-ins"
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

    @err_catcher(name=__name__)
    def getExecutable(self):
        execPath = ""
        if platform.system() == "Windows":
            defaultpath = os.path.join(self.getGimpPath(), "Gimp-2.10.exe")
            if os.path.exists(defaultpath):
                execPath = defaultpath

        return execPath


    @err_catcher(name=__name__)
    def getGimpPath(self):
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


    @err_catcher(name=__name__)
    def findGimpVersion(self, installPath):

        # List all files in the GIMP bin directory
        files = os.listdir(installPath)
        
        # match GIMP version number in filenames like "gimp-x.xx.exe"
        pattern = r"gimp-(\d+\.\d+)\.exe"

        # Iterate over the files and look for the version number
        for file in files:
            match = re.match(pattern, file)
            if match:
                verNumber = match.group(1)

                return verNumber
        
        # If no version number is found, return None
        return None
    

    @err_catcher(name=__name__)
    def addIntegration(self, installPath):
        try:
            if platform.system() != "Windows":
                msgStr = ("Gimp may only be Installed on Windows at this time")
                QMessageBox.warning(self.core.messageParent, "Prism Integration", msgStr)
                return False

            integrationBase = os.path.join(
                os.path.dirname(os.path.dirname(__file__)), "Integration"
                )
            
            #   Gets Gimp ver number based on .exe 
            gimpVer = self.findGimpVersion(installPath)
            gimpVerNum = float("{:.2f}".format(float(gimpVer)))

            if gimpVerNum >= 2.99:
                # intergrationPath = os.path.join(integrationBase, "Gimp3")                         #   TODO add Gimp3 support
                self.core.popup(f"Gimp{gimpVer} is not supported.  Please use Gimp 2.10.")
                return False
            elif 2 < gimpVerNum < 2.99:
                intergrationPath = os.path.join(integrationBase, "Gimp2")
            else:
                self.core.popup(f"Gimp{gimpVer} is not supported.  Please use Gimp 2.99 and above")
                return False

            gimpPluginPath = os.path.expanduser(f"~\\AppData\\Roaming\\GIMP\\{gimpVer}\\plug-ins")
            gimpPluginPath = gimpPluginPath.replace("\\", "/")

            for item in os.listdir(intergrationPath):
                srcItem = os.path.join(intergrationPath, item)
                if os.path.isfile(srcItem):
                    shutil.copy(srcItem, gimpPluginPath)
                elif os.path.isdir(srcItem):
                    destItem = os.path.join(gimpPluginPath, item)
                    shutil.copytree(srcItem, destItem)
               
            #   Edits the plugin files to replace hardcoded root paths
            result = self.replacePluginPaths(gimpPluginPath)

            if not result:
                self.core.popup("Failed to write paths to intergrtion.")
                raise Exception
            
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
        

    @err_catcher(name=__name__)
    def replacePluginPaths(self, gimpPluginPath):
        try:
            # Modify files in moved directories
            for root, _, files in os.walk(gimpPluginPath):
                for filename in files:
                    if filename.startswith("Prism"):
                        file_path = os.path.join(root, filename)
                        with open(file_path, "r") as interFile:
                            interFileStr = interFile.read()
                        with open(file_path, "w") as interFile:
                            #   Replaces paths as needed
                            interFileStr = interFileStr.replace(
                                "PRISMROOTREPLACE", 
                                '"%s"' % self.core.prismRoot.replace("\\", "/")
                                )
                            interFileStr = interFileStr.replace(
                                "PLUGINROOTREPLACE", 
                                '"%s"' % self.pluginRoot.replace("\\", "/")
                                )
                            interFile.write(interFileStr)

            if platform.system() in ["Linux", "Darwin"]:
                for root, dirs, _ in os.walk(gimpPluginPath):
                    for item in dirs:
                        os.chmod(os.path.join(root, item), 0o777)

            return True

        except OSError as e:
            # Handle specific OSError, e.g., permission errors, etc.
            # Log the error or display a warning message if needed.
            print("Error:", e)
            return False
        
        except Exception as e:
            # Handle other specific exceptions if needed
            print("Unexpected error:", e)
            return False


    @err_catcher(name=__name__)
    def removeIntegration(self, installPath):
        try:
            if platform.system() != "Windows":
                msgStr = ("Gimp may only be Installed on Windows at this time")

                QMessageBox.warning(self.core.messageParent, "Prism Integration", msgStr)
                return False

            gimpVer = self.findGimpVersion(installPath)

            gimpPluginPath = os.path.expanduser(f"~\\AppData\\Roaming\\GIMP\\{gimpVer}\\plug-ins")
            gimpPluginPath = gimpPluginPath.replace("\\", "/")


            for root, dirs, files in os.walk(gimpPluginPath):
                for filename in files:
                    removeItem = os.path.join(root, filename)
                    os.remove(removeItem)
                    
            for dirpath, dirnames, _ in os.walk(gimpPluginPath, topdown=False):
                for dirname in dirnames:
                    removeDir = os.path.join(dirpath, dirname)
                    shutil.rmtree(removeDir)

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


    @err_catcher(name=__name__)
    def updateInstallerUI(self, userFolders, pItem):
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


    @err_catcher(name=__name__)
    def installerExecute(self, pluginItem, result):
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
