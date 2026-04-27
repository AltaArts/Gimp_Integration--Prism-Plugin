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
import glob

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

        #   Sets Example Path for display in the Installer UI
        if platform.system() == "Windows":
            self.examplePath = (self.getHighestGimpPluginsDir() or
                os.path.join(os.path.expanduser("~"), "AppData/Roaming/GIMP/3.x/plug-ins"))

        elif platform.system() == "Linux":
            self.examplePath = os.path.expanduser("~/.config/GIMP/3.0/plug-ins")
        elif platform.system() == "Darwin":
            self.examplePath = os.path.expanduser("~/Library/Application Support/GIMP/3.0/plug-ins")
        else:
            self.examplePath = ""


    #   Returns Gimp EXE path from Registry
    @err_catcher(name=__name__)
    def findGimpExeFromReg(self):
        if platform.system() != "Windows":
            return None

        def keyVersionTuple(keyName):
            name_lower = keyName.lower().strip()
            if not name_lower.startswith("gimp"):
                return (0,)

            versionPart = keyName[4:].strip()
            if not versionPart:
                return (0,)

            try:
                return tuple(int(x) for x in versionPart.split("."))
            
            except Exception:
                return (0,)
            

        gimpKeys = []
        try:
            regKey = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE")

            idx = 0
            while True:
                try:
                    subKeyName = _winreg.EnumKey(regKey, idx)
                    idx += 1
                except OSError:
                    break

                if subKeyName.lower().startswith("gimp"):
                    gimpKeys.append(subKeyName)

        except Exception:
            gimpKeys = []

        for gimpKey in sorted(gimpKeys, key=keyVersionTuple, reverse=True):
            appIconPath = r"SOFTWARE\%s\Capabilities" % gimpKey

            try:
                key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, appIconPath)
                value, _ = _winreg.QueryValueEx(key, "ApplicationIcon")

            except Exception:
                continue

            rawValue = str(value).strip().strip('"')
            exePath = rawValue.split(",", 1)[0].strip().strip('"')

            if os.path.isfile(exePath):
                return exePath

        #   Fallback: Scan Common Install Locations
        for base in [r"C:\Program Files", r"C:\Program Files (x86)"]:
            for entry in glob.glob(os.path.join(base, "GIMP*", "bin", "gimp*.exe")):
                if os.path.isfile(entry):
                    return entry

        return None


    #   Returns the discovered GIMP executable path
    @err_catcher(name=__name__)
    def getExecutable(self):
        exe = self.findGimpExeFromReg()
        return exe if exe else ""


    #   Returns the GIMP user plug-ins base dir (AppData/Roaming/GIMP)
    @err_catcher(name=__name__)
    def getGimpRoamingDir(self):
        if platform.system() == "Windows":
            return os.path.join(os.path.expanduser("~"), "AppData/Roaming/GIMP")
        
        elif platform.system() == "Linux":
            return os.path.expanduser("~/.config/GIMP")
        elif platform.system() == "Darwin":
            return os.path.expanduser("~/Library/Application Support/GIMP")
        return ""


    #   Returns List of Discovered GIMP plug-ins dirs, Highest Ver First
    @err_catcher(name=__name__)
    def getGimpPluginsDirs(self):
        pluginsDirs = []
        roamingDir = self.getGimpRoamingDir()

        if not os.path.isdir(roamingDir):
            return pluginsDirs

        def versionKey(entry):
            parts = entry.split(".")
            if not parts:
                return None

            try:
                return tuple(int(x) for x in parts)
            except ValueError:
                return None

        versionEntries = []
        for entry in os.listdir(roamingDir):
            versionTuple = versionKey(entry)
            if versionTuple is not None:
                versionEntries.append((versionTuple, entry))

        for _, entry in sorted(versionEntries, key=lambda item: item[0], reverse=True):
            pluginsDir = os.path.join(roamingDir, entry, "plug-ins")
            if os.path.isdir(pluginsDir):
                pluginsDirs.append(os.path.normpath(pluginsDir))

        return pluginsDirs


    #   Returns the Highest Ver GIMP plug-ins Dir
    @err_catcher(name=__name__)
    def getHighestGimpPluginsDir(self):
        pluginsDirs = self.getGimpPluginsDirs() or []
        return pluginsDirs[0] if pluginsDirs else ""


    def addIntegration(self, installPath):
        try:
            #   installPath must be the GIMP user plug-ins directory
            #   e.g. C:\Users\<User>\AppData\Roaming\GIMP\3.2\plug-ins
            if not os.path.isdir(installPath):
                msgStr = (
                    "Invalid GIMP plug-ins path: %s\n\n"
                    "The path must be the GIMP user plug-ins directory, which usually looks like this:\n\n%s"
                    % (installPath, self.examplePath)
                )
                self.core.popup(msgStr, title="Prism Integration")
                return False

            integrationBase = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Integration")
            integrationBase = os.path.realpath(integrationBase)
            prismGimpDir = os.path.join(installPath, "Prism_Gimp")

            cmds = []
            addedFiles = []

            #   Cmd to Remove Prism_Gimp Subdir if Already Exists
            if os.path.exists(prismGimpDir):
                cmd = {"type": "removeFolder", "args": [prismGimpDir]}
                cmds.append(cmd)

            #   Cmd to Create the Prism_Gimp Subdir
            cmd = {"type": "createFolder", "args": [prismGimpDir]}
            cmds.append(cmd)

            #   Cmd to Copy each Integration File into Prism_Gimp Subdir
            for filename in os.listdir(integrationBase):
                srcFile = os.path.abspath(os.path.join(integrationBase, filename))
                dstFile = os.path.abspath(os.path.join(prismGimpDir, filename))
                if os.path.isfile(srcFile):
                    cmd = {"type": "copyFile", "args": [srcFile, dstFile]}
                    cmds.append(cmd)
                    addedFiles.append(dstFile)

            #   Run the Commands
            result = self.core.runFileCommands(cmds)

            if not result:
                return False

            #   Ensure Files are Executable on Linux/macOS
            if platform.system() in ["Linux", "Darwin"]:
                for f in addedFiles:
                    os.chmod(f, 0o777)

            #   Replace Path Placeholders in Copied Files
            result = self.replacePaths(prismGimpDir, addedFiles)

            if result is True:
                return True
            elif result is False:
                return False
            else:
                raise Exception(result)

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            msgStr = (
                "Errors occurred during the installation of the Gimp integration.\n"
                "The installation is possibly incomplete.\n\n%s\n%s\n%s"
                % (str(e), exc_type, exc_tb.tb_lineno)
            )
            msgStr += "\n\nRunning this application as administrator could solve this problem eventually."

            QMessageBox.warning(self.core.messageParent, "Prism Integration", msgStr)
            return False


    #   Replaces Path Placeholders in the Copied Integration Files
    def replacePaths(self, prismGimpDir, addedFiles):
        prismRoot = os.path.abspath(self.core.prismRoot).replace("\\", "/")
        pluginRoot = os.path.abspath(os.path.dirname(os.path.dirname(__file__))).replace("\\", "/")

        cmds = []

        for filePath in addedFiles:
            with open(filePath, "r", encoding="utf-8") as fh:
                fileStr = fh.read()

            fileStr = fileStr.replace("@PRISMROOTREPLACE@", prismRoot)
            fileStr = fileStr.replace("@GIMPPLUINREPLACE@", pluginRoot)

            cmd = {"type": "writeToFile", "args": [filePath, fileStr]}
            cmds.append(cmd)

        return self.core.runFileCommands(cmds)


    def removeIntegration(self, installPath):
        try:
            prismGimpDir = os.path.join(installPath, "Prism_Gimp")
            cmds = []

            #   Cmd to Remove the Prism_Gimp Subdir
            if os.path.exists(prismGimpDir):
                cmd = {"type": "removeFolder", "args": [prismGimpDir]}
                cmds.append(cmd)

            if not cmds:
                return True

            result = self.core.runFileCommands(cmds)

            if result is True:
                return True
            elif result is False:
                return False
            else:
                raise Exception(result)

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            msgStr = (
                "Errors occurred during the removal of the Gimp integration.\n\n%s\n%s\n%s"
                % (str(e), exc_type, exc_tb.tb_lineno)
            )
            msgStr += "\n\nRunning this application as administrator could solve this problem eventually."

            QMessageBox.warning(self.core.messageParent, "Prism Integration", msgStr)
            return False


    def updateInstallerUI(self, userFolders, pItem):
        try:
            gimpItem = QTreeWidgetItem(["Gimp"])
            gimpItem.setCheckState(0, Qt.Checked)
            pItem.addChild(gimpItem)

            pluginsDirs = self.getGimpPluginsDirs() or []

            browseStartPath = self.getHighestGimpPluginsDir() or self.getGimpRoamingDir() or self.examplePath

            gimpCustomItem = QTreeWidgetItem(["Custom"])
            gimpCustomItem.setToolTip(0, 'e.g. "%s"' % self.examplePath)
            gimpCustomItem.setToolTip(1, browseStartPath)
            gimpCustomItem.setText(1, "< doubleclick to browse path >")
            gimpCustomItem.setCheckState(0, Qt.Unchecked)
            gimpCustomItem.setFlags(gimpCustomItem.flags() & ~Qt.ItemIsAutoTristate)
            gimpItem.addChild(gimpCustomItem)
            gimpItem.setExpanded(True)

            activeVersion = False
            for pluginsDir in pluginsDirs:
                #   Use the GIMP version dir name as the label (e.g. "3.2")
                versionLabel = os.path.basename(os.path.dirname(pluginsDir))
                gimpVItem = QTreeWidgetItem([versionLabel])
                gimpItem.addChild(gimpVItem)

                gimpVItem.setCheckState(0, Qt.Checked)
                gimpVItem.setFlags(gimpVItem.flags() & ~Qt.ItemIsAutoTristate)
                gimpVItem.setText(1, pluginsDir)
                gimpVItem.setToolTip(0, pluginsDir)
                activeVersion = True

            if not activeVersion:
                gimpItem.setCheckState(0, Qt.Unchecked)
                gimpCustomItem.setFlags(~Qt.ItemIsEnabled)

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            msg = QMessageBox.warning(
                self.core.messageParent,
                "Prism Installation",
                "Errors occurred during the installation.\n The installation is possibly incomplete.\n\n%s\n%s\n%s\n%s"
                % (__file__, str(e), exc_type, exc_tb.tb_lineno),
            )
            return False


    def installerExecute(self, gimpItem, result):
        try:
            pluginsDirs = []
            installLocs = []

            if gimpItem.checkState(0) != Qt.Checked:
                return installLocs

            for i in range(gimpItem.childCount()):
                item = gimpItem.child(i)
                if item.checkState(0) == Qt.Checked and os.path.exists(item.text(1)):
                    pluginsDirs.append(item.text(1))

            for pluginsDir in pluginsDirs:
                result["Gimp integration"] = self.core.integration.addIntegration(
                    self.plugin.pluginName, path=pluginsDir, quiet=True
                )
                if result["Gimp integration"]:
                    installLocs.append(pluginsDir)

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
