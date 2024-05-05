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

#
#
#
#
#
#
#                   #######         TODO            ##########
#
#
#
#
#


import os
import time
import platform
import logging

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from PrismUtils.Decorators import err_catcher
from StateUserInterfaces import Gimp_Export_ui

logger = logging.getLogger(__name__)


def boolToBit(bool):
    if bool == True:
        return 1
    else:
        return 0
    


class GimpExportClass(QWidget, Gimp_Export_ui.Ui_wg_Gimp_Export):

    className = "Gimp_Render"
    listType = "Export"
    stateCategories = {"Render": [{"label": className, "stateType": className}]}


    @err_catcher(name=__name__)
    def setup(self, state, core, stateManager, node=None, stateData=None):
        self.state = state
        self.core = core
        self.stateManager = stateManager
        self.canSetVersion = True
        self.customContext = None
        self.allowCustomContext = False

        self.renderingStarted = False
        self.cleanOutputdir = True

        self.setupUi(self)

        self.e_name.setText(state.text(0) + " - {identifier}")

        self.l_name.setVisible(False)
        self.e_name.setVisible(False)

        getattr(self.core.appPlugin, "sm_render_startup", lambda x: None)(self)

        masterItems = ["Set as master", "Don't update master"]
        self.cb_master.addItems(masterItems)

        self.product_paths = self.core.paths.getRenderProductBasePaths()
        self.cb_outPath.addItems(list(self.product_paths.keys()))
        if len(self.product_paths) < 2:
            self.w_outPath.setVisible(False)

        self.mediaType = "2drenders"
        self.tasknameRequired = True

        self.outputFormats = [".png", ".exr", ".jpg"]                   #   TODO
        self.cb_format.addItems(self.outputFormats)                     #   TODO

        scaleOptions = ["10", "25", "50", "100", "150", "200", "300"]
        self.cb_scale.addItems(scaleOptions)
        self.cb_scale.setCurrentIndex(3)


        alphaFill = ["checker", "black", "gray", "white", "pink"]
        self.cb_alphaFill.addItems(alphaFill)
        self.cb_alphaFill.setCurrentIndex(0)

        pngCompressItems = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.cb_png_compress.addItems(pngCompressItems)
        self.cb_png_compress.setCurrentIndex(4)

        self.chb_png_interlaced.setChecked(False)
        self.chb_png_gamma.setChecked(True)
        self.chb_png_rez.setChecked(True)
        self.chb_png_bgColor.setChecked(True)
        self.chb_png_layerOffset.setChecked(False)
        self.chb_png_alphaColor.setChecked(True)


        jpgQualItems = ["0", ".1", ".2", ".3", ".4", ".5", ".6", ".7", ".8", ".9", "1"]
        self.cb_jpg_qual.addItems(jpgQualItems)
        self.cb_jpg_qual.setCurrentIndex(5)

        jpgSmoothItems = ["0", ".1", ".2", ".3", ".4", ".5", ".6", ".7", ".8", ".9", "1"]
        self.cb_jpg_smooth.addItems(jpgSmoothItems)
        self.cb_jpg_smooth.setCurrentIndex(5)

        jpgSubSample = ["4:2:0", "4:2:2", "4:4:4"] # -> 0, 1, 2 in python function
        self.cb_jpg_subSample.addItems(jpgSubSample)
        self.cb_jpg_subSample.setCurrentIndex(1)

        self.chb_jpg_optimize.setChecked(True)
        self.chb_jpg_progressive.setChecked(False)
        self.chb_jpg_arithCode.setChecked(False)

        self.updateUiOptions()
        self.connectEvents()

        self.oldPalette = self.b_changeTask.palette()
        self.warnPalette = QPalette()
        self.warnPalette.setColor(QPalette.Button, QColor(200, 0, 0))
        self.warnPalette.setColor(QPalette.ButtonText, QColor(255, 255, 255))

        self.setTaskWarn(True)
        self.nameChanged(state.text(0))

        self.core.callback("onStateStartup", self)

        if stateData is not None:
            self.loadData(stateData)
        else:
            self.initializeContextBasedSettings()


    @err_catcher(name=__name__)
    def loadData(self, stateData):

        if "contextType" in stateData:
            self.setContextType(stateData["contextType"])
        if "customContext" in stateData:
            self.customContext = stateData["customContext"]
        if "taskname" in stateData:
            self.setTaskname(stateData["taskname"])

        self.updateUi()

        if "stateName" in stateData:
            self.e_name.setText(stateData["stateName"])
        elif "statename" in stateData:
            self.e_name.setText(stateData["statename"] + " - {identifier}")

        if "masterVersion" in stateData:
            idx = self.cb_master.findText(stateData["masterVersion"])
            if idx != -1:
                self.cb_master.setCurrentIndex(idx)
        if "curoutputpath" in stateData:
            idx = self.cb_outPath.findText(stateData["curoutputpath"])
            if idx != -1:
                self.cb_outPath.setCurrentIndex(idx)

        if "specs_xRez" in stateData:
            self.l_specs_Xrez.setText(str(stateData["specs_xRez"]))

        if "specs_yRez" in stateData:
            self.l_specs_Yrez.setText(str(stateData["specs_yRez"]))

        if "colorMode" in stateData:
            self.l_specs_ColorMode.setText(stateData["colorMode"])

        if "bitDepth" in stateData:
            self.l_specs_BitDepth.setText(stateData["bitDepth"])

        if "gamma" in stateData:
            self.l_specs_Gamma.setText(stateData["gamma"])

        if "hasAlpha" in stateData:
            self.l_specs_Alpha.setText(str(stateData["hasAlpha"]))

        if "exportScale" in stateData:
            idx = self.cb_scale.findText(stateData["exportScale"])
            if idx != -1:
                self.cb_format.setCurrentIndex(idx)
        
        if "outputFormat" in stateData:
            idx = self.cb_format.findText(stateData["outputFormat"])
            if idx != -1:
                self.cb_format.setCurrentIndex(idx)

        if "colorMode" in stateData:
            idx = self.cb_colorMode.findText(stateData["colorMode"])
            if idx != -1:
                self.cb_colorMode.setCurrentIndex(idx)

        if "bitDepth" in stateData:
            idx = self.cb_bitDepth.findText(stateData["bitDepth"])
            if idx != -1:
                self.cb_bitDepth.setCurrentIndex(idx)

        if "alphaFill" in stateData:
            idx = self.cb_alphaFill.findText(stateData["alphaFill"])
            if idx != -1:
                self.cb_alphaFill.setCurrentIndex(idx)

        if "png_Compress" in stateData:
            idx = self.cb_png_compress.findText(stateData["png_Compress"])
            if idx != -1:
                self.cb_png_compress.setCurrentIndex(idx)

        if "png_Interlaced" in stateData:
            self.chb_png_interlaced.setChecked(stateData["png_Interlaced"])

        if "png_Gamma" in stateData:
            self.chb_png_gamma.setChecked(stateData["png_Gamma"])

        if "png_Rez" in stateData:
            self.chb_png_rez.setChecked(stateData["png_Rez"])
            
        if "png_BgColor" in stateData:
            self.chb_png_bgColor.setChecked(stateData["png_BgColor"])

        if "png_LayerOffset" in stateData:
            self.chb_png_layerOffset.setChecked(stateData["png_LayerOffset"])

        if "png_AlphaColor" in stateData:
            self.chb_png_alphaColor.setChecked(stateData["png_AlphaColor"])                                    

        if "jpg_Qual" in stateData:
            idx = self.cb_jpg_qual.findText(stateData["jpg_Qual"])
            if idx != -1:
                self.cb_jpg_qual.setCurrentIndex(idx)

        if "jpg_Smooth" in stateData:
            idx = self.cb_jpg_smooth.findText(stateData["jpg_Smooth"])
            if idx != -1:
                self.cb_jpg_smooth.setCurrentIndex(idx)

        if "jpg_SubSample" in stateData:
            idx = self.cb_jpg_subSample.findText(stateData["jpg_SubSample"])
            if idx != -1:
                self.cb_jpg_subSample.setCurrentIndex(idx)

        if "jpg_Optimize" in stateData:
            self.chb_jpg_optimize.setChecked(stateData["jpg_Optimize"])

        if "jpg_Progressive" in stateData:
            self.chb_jpg_progressive.setChecked(stateData["jpg_Progressive"])

        if "jpg_ArithCode" in stateData:
            self.chb_jpg_arithCode.setChecked(stateData["jpg_ArithCode"])

        if "lastexportpath" in stateData:
            lePath = self.core.fixPath(stateData["lastexportpath"])
            self.l_pathLast.setText(lePath)
            self.l_pathLast.setToolTip(lePath)
        if "stateenabled" in stateData:
            if type(stateData["stateenabled"]) == int:
                self.state.setCheckState(
                    0, Qt.CheckState(stateData["stateenabled"]),
                )

        self.updateUiOptions()

        self.core.callback("onStateSettingsLoaded", self, stateData)


    @err_catcher(name=__name__)                                                         #   TODO
    def connectEvents(self):
        self.e_name.textChanged.connect(self.nameChanged)
        self.e_name.editingFinished.connect(self.stateManager.saveStatesToScene)
        self.cb_context.activated.connect(self.onContextTypeChanged)
        self.b_context.clicked.connect(self.selectContextClicked)
        self.b_changeTask.clicked.connect(self.changeTask)
        self.cb_master.activated.connect(self.stateManager.saveStatesToScene)
        self.cb_outPath.activated.connect(self.stateManager.saveStatesToScene)
        self.cb_format.activated.connect(self.updateUiOptions)
        self.cb_colorMode.activated.connect(self.updateUiOptions)
        self.cb_format.activated.connect(self.stateManager.saveStatesToScene)
        self.cb_colorMode.activated.connect(self.stateManager.saveStatesToScene)
        self.cb_bitDepth.activated.connect(self.stateManager.saveStatesToScene)
        self.cb_alphaFill.activated.connect(self.stateManager.saveStatesToScene)
        self.cb_jpg_qual.activated.connect(self.stateManager.saveStatesToScene)
        self.cb_jpg_smooth.activated.connect(self.stateManager.saveStatesToScene)
        self.cb_jpg_subSample.activated.connect(self.stateManager.saveStatesToScene)
        self.chb_jpg_optimize.toggled.connect(self.stateManager.saveStatesToScene)
        self.chb_jpg_progressive.toggled.connect(self.stateManager.saveStatesToScene)
        self.chb_jpg_arithCode.toggled.connect(self.stateManager.saveStatesToScene)
        self.b_pathLast.clicked.connect(self.showLastPathMenu)


    @err_catcher(name=__name__)
    def updateUiOptions(self, *args):

        format = self.cb_format.currentText()
        colorMode = self.cb_colorMode.currentText()
        currentMode = self.cb_colorMode.currentText()
        currentBitIdx = self.cb_bitDepth.currentText()

        self.gb_jpgOptions.hide()
        self.gb_pngOptions.hide()

        match format:
            case ".jpg":
                self.gb_jpgOptions.show()
                imageColorMode = ["RGB", "GRAY"]
                colorModeIdx = 0
                imageBitDepth = ["8"]
                bitIdx = 0

            case ".png":
                self.gb_pngOptions.show()
                imageColorMode = ["RGB", "RGBA", "GRAY", "GRAYA"]
                colorModeIdx = 0
                imageBitDepth = ["8", "16"]
                bitIdx = 1

            case ".exr":
                imageColorMode = ["RGB", "RGBA", "GRAY", "GRAYA"]
                colorModeIdx = 0
                imageBitDepth = ["16", "32"]
                bitIdx = 1

        self.cb_colorMode.clear()
        self.cb_colorMode.addItems(imageColorMode)
        
        idx = self.cb_colorMode.findText(currentMode)
        if idx != -1:
            self.cb_colorMode.setCurrentIndex(idx)
        else:
            self.cb_colorMode.setCurrentIndex(colorModeIdx)

        if colorMode in ["RGB", "GRAY"]:
            self.gb_alphaFill.show()
        else:
            self.gb_alphaFill.hide()

        self.cb_bitDepth.clear()
        self.cb_bitDepth.addItems(imageBitDepth)

        idx = self.cb_bitDepth.findText(currentBitIdx)
        if idx != -1:
            self.cb_bitDepth.setCurrentIndex(idx)
        else:
            self.cb_bitDepth.setCurrentIndex(bitIdx)


    @err_catcher(name=__name__)
    def initializeContextBasedSettings(self):
        context = self.getCurrentContext()

        if context.get("task"):
            self.setTaskname(context.get("task"))

        self.updateUi()


    @err_catcher(name=__name__)
    def showLastPathMenu(self, state=None):
        path = self.l_pathLast.text()
        if path == "None":
            return

        menu = QMenu(self)

        act_open = QAction("Play", self)
        act_open.triggered.connect(lambda: self.core.media.playMediaInExternalPlayer(path))
        menu.addAction(act_open)

        act_open = QAction("Open in Media Browser", self)
        act_open.triggered.connect(lambda: self.openInMediaBrowser(path))
        menu.addAction(act_open)

        act_open = QAction("Open in explorer", self)
        act_open.triggered.connect(lambda: self.core.openFolder(path))
        menu.addAction(act_open)

        act_copy = QAction("Copy", self)
        act_copy.triggered.connect(lambda: self.core.copyToClipboard(path, file=True))
        menu.addAction(act_copy)

        menu.exec_(QCursor.pos())


    @err_catcher(name=__name__)
    def openInMediaBrowser(self, path):
        self.core.projectBrowser()
        self.core.pb.showTab("Media")
        data = self.core.paths.getRenderProductData(path)
        self.core.pb.mediaBrowser.showRender(entity=data, identifier=data.get("identifier"), version=data.get("version"))


    @err_catcher(name=__name__)
    def selectContextClicked(self, state=None):
        self.dlg_entity = self.stateManager.entityDlg(self)
        data = self.getCurrentContext()
        self.dlg_entity.w_entities.navigate(data)
        self.dlg_entity.entitySelected.connect(lambda x: self.setCustomContext(x))
        self.dlg_entity.show()


    @err_catcher(name=__name__)
    def setCustomContext(self, context):
        self.customContext = context
        self.refreshContext()
        self.stateManager.saveStatesToScene()


    @err_catcher(name=__name__)
    def onContextTypeChanged(self, state):
        self.refreshContext()
        self.stateManager.saveStatesToScene()


    @err_catcher(name=__name__)
    def nameChanged(self, text):
        text = self.e_name.text()
        context = {}
        context["identifier"] = self.getTaskname() or "None"
        num = 0
        try:
            if "{#}" in text:
                while True:
                    context["#"] = num or ""
                    name = text.format(**context)
                    for state in self.stateManager.states:
                        if state.ui.listType != "Export":
                            continue

                        if state is self.state:
                            continue

                        if state.text(0) == name:
                            num += 1
                            break
                    else:
                        break
            else:
                name = text.format(**context)
        except Exception:
            name = text

        if self.state.text(0).endswith(" - disabled"):
            name += " - disabled"

        self.state.setText(0, name)


    @err_catcher(name=__name__)
    def getFormat(self):
        self.cb_format.currentText()


    @err_catcher(name=__name__)
    def setFormat(self, fmt):
        idx = self.cb_format.findText(fmt)
        if idx != -1:
            self.cb_format.setCurrentIndex(idx)
            self.stateManager.saveStatesToScene()
            return True

        return False
    

    @err_catcher(name=__name__)
    def getContextType(self):
        contextType = self.cb_context.currentText()
        return contextType


    @err_catcher(name=__name__)
    def setContextType(self, contextType):
        idx = self.cb_context.findText(contextType)
        if idx != -1:
            self.cb_context.setCurrentIndex(idx)
            self.refreshContext()
            return True

        return False


    @err_catcher(name=__name__)
    def getTaskname(self):
        taskName = self.l_taskName.text()
        return taskName
    

    @err_catcher(name=__name__)
    def setTaskname(self, taskname):
        self.l_taskName.setText(taskname)
        self.setTaskWarn(not bool(taskname))
        self.updateUi()


    @err_catcher(name=__name__)
    def getSortKey(self):
        return self.getTaskname()
    

    @err_catcher(name=__name__)
    def changeTask(self):
        from PrismUtils import PrismWidgets
        self.nameWin = PrismWidgets.CreateItem(
            startText=self.getTaskname(),
            showTasks=True,
            taskType="2d",
            core=self.core,
        )
        self.core.parentWindow(self.nameWin)
        self.nameWin.setWindowTitle("Change Identifier")
        self.nameWin.l_item.setText("Identifier:")
        self.nameWin.buttonBox.buttons()[0].setText("Ok")
        self.nameWin.e_item.selectAll()
        result = self.nameWin.exec_()

        if result == 1:
            self.setTaskname(self.nameWin.e_item.text())
            self.nameChanged(self.e_name.text())
            self.stateManager.saveStatesToScene()


    @err_catcher(name=__name__)
    def getMasterVersion(self):
        return self.cb_master.currentText()
    

    @err_catcher(name=__name__)
    def setMasterVersion(self, master):
        idx = self.cb_master.findText(master)
        if idx != -1:
            self.cb_master.setCurrentIndex(idx)
            self.stateManager.saveStatesToScene()
            return True

        return False
    

    @err_catcher(name=__name__)
    def getLocation(self):
        return self.cb_outPath.currentText()
    

    @err_catcher(name=__name__)
    def setLocation(self, location):
        idx = self.cb_outPath.findText(location)
        if idx != -1:
            self.cb_outPath.setCurrentIndex(idx)
            self.stateManager.saveStatesToScene()
            return True

        return False
    

    @err_catcher(name=__name__)
    def updateUi(self):
        self.w_context.setHidden(not self.allowCustomContext)
        self.refreshContext()

        if not self.core.mediaProducts.getUseMaster():
            self.w_master.setVisible(False)

        self.nameChanged(self.e_name.text())
        return True
    

    @err_catcher(name=__name__)
    def refreshContext(self):
        context = self.getCurrentContext()
        contextStr = self.getContextStrFromEntity(context)
        self.l_context.setText(contextStr)


    @err_catcher(name=__name__)
    def getCurrentContext(self):
        context = None
        if self.allowCustomContext:
            ctype = self.getContextType()
            if ctype == "Custom":
                context = self.customContext

        if not context:
            fileName = self.core.getCurrentFileName()
            context = self.core.getScenefileData(fileName)
        
        if "username" in context:
            del context["username"]

        if "user" in context:
            del context["user"]

        return context
    

    # @err_catcher(name=__name__)
    # def refreshSubmitUi(self):
    #     if not self.gb_submit.isHidden():
    #         if not self.gb_submit.isCheckable():
    #             return

    #         submitChecked = self.gb_submit.isChecked()
    #         for idx in reversed(range(self.gb_submit.layout().count())):
    #             self.gb_submit.layout().itemAt(idx).widget().setHidden(not submitChecked)

    #         if submitChecked:
    #             self.core.plugins.getRenderfarmPlugin(self.cb_manager.currentText()).sm_render_updateUI(self)


    @err_catcher(name=__name__)
    def getContextStrFromEntity(self, entity):
        if not entity:
            return ""

        entityType = entity.get("type", "")
        if entityType == "asset":
            entityName = entity.get("asset_path").replace("\\", "/")
        elif entityType == "shot":
            entityName = self.core.entities.getShotName(entity)
        else:
            return ""

        context = "%s - %s" % (entityType.capitalize(), entityName)
        return context
    

    @err_catcher(name=__name__)
    def preExecuteState(self):
        warnings = []

        self.updateUi()

        if self.tasknameRequired and not self.getTaskname():
            warnings.append(["No identifier is given.", "", 3])

        warnings += self.core.appPlugin.sm_render_preExecute(self)

        return [self.state.text(0), warnings]
    

    @err_catcher(name=__name__)
    def getOutputName(self, useVersion="next"):
        if self.tasknameRequired and not self.getTaskname():
            return

        task = self.getTaskname()
        extension = self.cb_format.currentText()
        context = self.getCurrentContext()
        framePadding = ""

        if "type" not in context:
            return

        singleFrame = True
        location = self.cb_outPath.currentText()
        outputPathData = self.core.mediaProducts.generateMediaProductPath(
            entity=context,
            task=task,
            extension=extension,
            framePadding=framePadding,
            comment=self.stateManager.publishComment,
            version=useVersion if useVersion != "next" else None,
            location=location,
            singleFrame=singleFrame,
            returnDetails=True,
            mediaType=self.mediaType,
            state=self,
        )

        outputFolder = os.path.dirname(outputPathData["path"])
        hVersion = outputPathData["version"]

        return outputPathData["path"], outputFolder, hVersion
    

    @err_catcher(name=__name__)
    def executeState(self, parent, useVersion="next"):
        endFrame = startFrame = 1
        updateMaster = True
        fileName = self.core.getCurrentFileName()
        context = self.getCurrentContext()

        if not self.renderingStarted:
            if self.tasknameRequired and not self.getTaskname():
                return [
                    self.state.text(0)
                    + ": error - no identifier is given. Skipped the activation of this state."
                ]

            outputName, outputPath, hVersion = self.getOutputName(useVersion=useVersion)
            expandedOutputPath = os.path.expandvars(outputPath)

            outLength = len(outputName)
            if platform.system() == "Windows" and os.getenv("PRISM_IGNORE_PATH_LENGTH") != "1" and outLength > 255:
                return [
                    self.state.text(0)
                    + " - error - The outputpath is longer than 255 characters (%s), which is not supported on Windows. Please shorten the outputpath by changing the comment, taskname or projectpath."
                    % outLength
                ]

            if not os.path.exists(os.path.dirname(expandedOutputPath)):
                os.makedirs(os.path.dirname(expandedOutputPath))

            details = context.copy()
            if "filename" in details:
                del details["filename"]

            if "extension" in details:
                del details["extension"]

            details["version"] = hVersion                   #   TODO DETAILS SAVED TO VERSIONINFO
            details["sourceScene"] = fileName
            details["identifier"] = self.getTaskname()
            details["comment"] = self.stateManager.publishComment

            if self.mediaType == "3drenders":
                infopath = os.path.dirname(expandedOutputPath)
            else:
                infopath = expandedOutputPath

            self.core.saveVersionInfo(
                filepath=infopath, details=details
            )

            self.l_pathLast.setText(outputName)
            self.l_pathLast.setToolTip(outputName)
            self.stateManager.saveStatesToScene()

            outputType = self.cb_format.currentText()

            rSettings = {
                "outputName": outputName,
                "outputType": outputType,
                "startFrame": startFrame,
                "endFrame": endFrame,
                "frames": 1,
                "rangeType": "Single Frame",
                "exportScale": self.cb_scale.currentText(),
                "colorMode": self.cb_colorMode.currentText(),
                "bitDepth": self.cb_bitDepth.currentText(),
                "alphaFill": self.cb_alphaFill.currentText()
                }

            match outputType:    
                case ".png":
                    rSettings.update({"png_Compress": self.cb_png_compress.currentText(),
                                    "png_Interlaced": boolToBit(self.chb_png_interlaced.isChecked()),
                                    "png_Gamma": boolToBit(self.chb_png_gamma.isChecked()),
                                    "png_Rez": boolToBit(self.chb_png_rez.isChecked()),
                                    "png_BgColor": boolToBit(self.chb_png_bgColor.isChecked()),
                                    "png_LayerOffset": boolToBit(self.chb_png_layerOffset.isChecked()),
                                    "png_AlphaColor": boolToBit(not self.chb_png_alphaColor.isChecked())
                                    })
                    
                case ".exr":
                    pass

                case ".jpg":
                    rSettings.update({"jpg_Quality": self.cb_jpg_qual.currentText(),
                                    "jpg_Smoothing": self.cb_jpg_smooth.currentText(),
                                    "jpg_SubSample": self.cb_jpg_subSample.currentIndex(),
                                    "jpg_Optimize": boolToBit(self.chb_jpg_optimize.isChecked()),
                                    "jpg_Progressive": boolToBit(self.chb_jpg_progressive.isChecked()),
                                    "jpg_ArithCode": boolToBit(self.chb_jpg_arithCode.isChecked())
                                    })


            self.core.appPlugin.sm_render_preSubmit(self, rSettings)

            kwargs = {
                "state": self,
                "scenefile": fileName,
                "settings": rSettings,
            }

            result = self.core.callback("preRender", **kwargs)
            for res in result:
                if isinstance(res, dict) and res.get("cancel", False):
                    return [
                        self.state.text(0)
                        + " - error - %s" % res.get("details", "preRender hook returned False")
                    ]

            if not os.path.exists(os.path.expandvars(os.path.dirname(rSettings["outputName"]))):
                os.makedirs(os.path.expandvars(os.path.dirname(rSettings["outputName"])))

            if self.stateManager.actionSaveDuringPub.isChecked():
                self.core.saveScene(versionUp=False, prismReq=False)

            if self.core.getConfig("globals", "backupScenesOnPublish", config="project"):
                self.core.entities.backupScenefile(os.path.expandvars(os.path.dirname(rSettings["outputName"])), bufferMinutes=0)

  
            result = self.core.appPlugin.sm_render_startLocalRender(
                self, rSettings["outputName"], rSettings
                )
        else:
            rSettings = self.LastRSettings
            result = self.core.appPlugin.sm_render_startLocalRender(
                self, rSettings["outputName"], rSettings
            )
            outputName = rSettings["outputName"]

        if not self.renderingStarted:
            self.core.appPlugin.sm_render_undoRenderSettings(self, rSettings)

        if result == "publish paused":
            return [self.state.text(0) + " - publish paused"]
        else:
            if updateMaster:
                self.handleMasterVersion(os.path.expandvars(outputName))

            kwargs = {
                "state": self,
                "scenefile": fileName,
                "settings": rSettings,
                "result": result,
            }

            self.core.callback("postRender", **kwargs)

            if "Result=Success" in result:
                return [self.state.text(0) + " - success"]
            else:
                erStr = "%s ERROR - sm_default_imageRenderPublish %s:\n%s" % (
                    time.strftime("%d/%m/%y %X"),
                    self.core.version,
                    result,
                )
                if not result.startswith("Execute Canceled: "):
                    if result == "unknown error (files do not exist)":
                        QMessageBox.warning(
                            self.core.messageParent,
                            "Warning",
                            "No files were created during the rendering. If you think this is a Prism bug please report it in the forum:\nwww.prism-pipeline.com/forum/\nor write a mail to contact@prism-pipeline.com",
                        )
                    else:
                        self.core.writeErrorLog(erStr)
                return [self.state.text(0) + " - error - " + result]
            

    @err_catcher(name=__name__)
    def isUsingMasterVersion(self):
        useMaster = self.core.mediaProducts.getUseMaster()
        if not useMaster:
            return False

        masterAction = self.cb_master.currentText()
        if masterAction == "Don't update master":
            return False

        return True
    

    @err_catcher(name=__name__)
    def handleMasterVersion(self, outputName):
        if not self.isUsingMasterVersion():
            return

        masterAction = self.cb_master.currentText()
        if masterAction == "Set as master":
            self.core.mediaProducts.updateMasterVersion(outputName, mediaType="2drenders")


    @err_catcher(name=__name__)
    def setTaskWarn(self, warn):
        useSS = getattr(self.core.appPlugin, "colorButtonWithStyleSheet", False)
        if warn:
            if useSS:
                self.b_changeTask.setStyleSheet(
                    "QPushButton { background-color: rgb(200,0,0); }"
                )
            else:
                self.b_changeTask.setPalette(self.warnPalette)
        else:
            if useSS:
                self.b_changeTask.setStyleSheet("")
            else:
                self.b_changeTask.setPalette(self.oldPalette)


    @err_catcher(name=__name__)
    def getStateProps(self):
        stateProps = {
            "stateName": self.e_name.text(),
            "contextType": self.getContextType(),
            "customContext": self.customContext,
            "taskname": self.getTaskname(),
            "masterVersion": self.cb_master.currentText(),
            "curoutputpath": self.cb_outPath.currentText(),
            "exportScale": self.cb_scale.currentText(),
            "outputFormat": self.cb_format.currentText(),
            "colorMode": self.cb_colorMode.currentText(),
            "bitDepth": self.cb_bitDepth.currentText(),
            "alphaFill": self.cb_alphaFill.currentText(),
            "png_Compress": self.cb_png_compress.currentText(),
            "png_Interlaced": self.chb_png_interlaced.isChecked(),
            "png_Gamma": self.chb_png_gamma.isChecked(),
            "png_Rez": self.chb_png_rez.isChecked(),
            "png_BgColor": self.chb_png_bgColor.isChecked(),
            "png_LayerOffset": self.chb_png_layerOffset.isChecked(),
            "png_AlphaColor": self.chb_png_alphaColor.isChecked(),  
            "jpg_Qual": self.cb_jpg_qual.currentText(),
            "jpg_Smooth": self.cb_jpg_smooth.currentText(),
            "jpg_SubSample": self.cb_jpg_subSample.currentText(),
            "jpg_Optimize": self.chb_jpg_optimize.isChecked(),
            "jpg_Progressive": self.chb_jpg_progressive.isChecked(),
            "jpg_ArithCode": self.chb_jpg_arithCode.isChecked(),
            "lastexportpath": self.l_pathLast.text().replace("\\", "/"),
            "stateenabled": self.core.getCheckStateValue(self.state.checkState(0)),
        }
        self.core.callback("onStateGetSettings", self, stateProps)
        return stateProps
