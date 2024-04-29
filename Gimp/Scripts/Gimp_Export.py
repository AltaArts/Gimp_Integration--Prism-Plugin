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
import sys
import time
import traceback
import platform
import logging

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *


from PrismUtils.Decorators import err_catcher
from StateUserInterfaces import Gimp_Export_ui



logger = logging.getLogger(__name__)


# class GimpExportClass(object):
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

        self.curCam = None
        self.renderingStarted = False
        self.cleanOutputdir = True

        self.setupUi(self)

        self.e_name.setText(state.text(0) + " - {identifier}")

        # self.rangeTypes = [
        #     "Scene",
        #     "Shot",
        #     "Single Frame",
        #     "Custom",
        #     "Expression",
        # ]
        # self.cb_rangeType.addItems(self.rangeTypes)
        # for idx, rtype in enumerate(self.rangeTypes):
        #     self.cb_rangeType.setItemData(
        #         idx, self.stateManager.getFrameRangeTypeToolTip(rtype), Qt.ToolTipRole
        #     )
        # self.w_frameExpression.setToolTip(
        #     self.stateManager.getFrameRangeTypeToolTip("ExpressionField")
        # )

        # self.renderPresets = (
        #     self.stateManager.stateTypes["RenderSettings"].getPresets(self.core)
        #     if "RenderSettings" in self.stateManager.stateTypes
        #     else {}
        # )
        # if self.renderPresets:
        #     self.cb_renderPreset.addItems(self.renderPresets.keys())
        # else:
        #     self.w_renderPreset.setVisible(False)

        self.l_name.setVisible(False)
        self.e_name.setVisible(False)
        # self.gb_submit.setChecked(False)
        # self.f_renderLayer.setVisible(False)

        getattr(self.core.appPlugin, "sm_render_startup", lambda x: None)(self)

        masterItems = ["Set as master", "Add to master", "Don't update master"]
        self.cb_master.addItems(masterItems)

        self.product_paths = self.core.paths.getRenderProductBasePaths()
        self.cb_outPath.addItems(list(self.product_paths.keys()))
        if len(self.product_paths) < 2:
            self.w_outPath.setVisible(False)

        # self.mediaType = "3drenders"
        self.mediaType = "2drenders"
        self.tasknameRequired = True

        self.outputFormats = [".png", ".exr", ".jpg"]                   #   TODO
        self.cb_format.addItems(self.outputFormats)                     #   TODO


        alphaFill = ["checker", "black", "white", "pink"]
        self.cb_alphaFill.addItems(alphaFill)
        self.cb_alphaFill.setCurrentIndex(0)

        pngCompressItems = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        self.cb_png_compress.addItems(pngCompressItems)
        self.cb_png_compress.setCurrentIndex(4)

        self.chb_png_interlaced.setChecked(False)
        self.chb_png_gamma.setChecked(False)
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

        # self.resolutionPresets = self.core.projects.getResolutionPresets()
        # if "Get from rendersettings" not in self.resolutionPresets:
        #     self.resolutionPresets.append("Get from rendersettings")

        # self.e_osSlaves.setText("All")

        self.connectEvents()

        self.oldPalette = self.b_changeTask.palette()
        self.warnPalette = QPalette()
        self.warnPalette.setColor(QPalette.Button, QColor(200, 0, 0))
        self.warnPalette.setColor(QPalette.ButtonText, QColor(255, 255, 255))

        self.setTaskWarn(True)
        self.nameChanged(state.text(0))

        # self.cb_manager.addItems([p.pluginName for p in self.core.plugins.getRenderfarmPlugins()])

        self.core.callback("onStateStartup", self)

        # if self.cb_manager.count() == 0:
        #     self.gb_submit.setVisible(False)

        # self.managerChanged(True)

        if stateData is not None:
            self.loadData(stateData)
        else:
            self.initializeContextBasedSettings()


    @err_catcher(name=__name__)
    def loadData(self, data):
        if "contextType" in data:
            self.setContextType(data["contextType"])
        if "customContext" in data:
            self.customContext = data["customContext"]
        if "taskname" in data:
            self.setTaskname(data["taskname"])

        self.updateUi()

        if "stateName" in data:
            self.e_name.setText(data["stateName"])
        elif "statename" in data:
            self.e_name.setText(data["statename"] + " - {identifier}")
        if "renderpresetoverride" in data:
            res = eval(data["renderpresetoverride"])
            self.chb_renderPreset.setChecked(res)
        if "currentrenderpreset" in data:
            idx = self.cb_renderPreset.findText(data["currentrenderpreset"])
            if idx != -1:
                self.cb_renderPreset.setCurrentIndex(idx)
                self.stateManager.saveStatesToScene()
        # if "rangeType" in data:
        #     idx = self.cb_rangeType.findText(data["rangeType"])
        #     if idx != -1:
        #         self.cb_rangeType.setCurrentIndex(idx)
        #         self.updateRange()
        # if "startframe" in data:
        #     self.sp_rangeStart.setValue(int(data["startframe"]))
        # if "endframe" in data:
        #     self.sp_rangeEnd.setValue(int(data["endframe"]))
        # if "frameExpression" in data:
        #     self.le_frameExpression.setText(data["frameExpression"])
        # if "currentcam" in data:
        #     camName = getattr(self.core.appPlugin, "getCamName", lambda x, y: "")(
        #         self, data["currentcam"]
        #     )
        #     idx = self.cb_cam.findText(camName)
        #     if idx != -1:
        #         self.curCam = self.camlist[idx]
        #         self.cb_cam.setCurrentIndex(idx)
        #         self.stateManager.saveStatesToScene()
        if "resoverride" in data:
            res = eval(data["resoverride"])
            self.chb_resOverride.setChecked(res[0])
            self.sp_resWidth.setValue(res[1])
            self.sp_resHeight.setValue(res[2])
        if "masterVersion" in data:
            idx = self.cb_master.findText(data["masterVersion"])
            if idx != -1:
                self.cb_master.setCurrentIndex(idx)
        if "curoutputpath" in data:
            idx = self.cb_outPath.findText(data["curoutputpath"])
            if idx != -1:
                self.cb_outPath.setCurrentIndex(idx)

        if "outputFormat" in data:
            idx = self.cb_format.findText(data["outputFormat"])
            if idx != -1:
                self.cb_format.setCurrentIndex(idx)

        if "colorMode" in data:
            idx = self.cb_colorMode.findText(data["colorMode"])
            if idx != -1:
                self.cb_colorMode.setCurrentIndex(idx)

        if "alphaFill" in data:
            idx = self.cb_alphaFill.findText(data["alphaFill"])
            if idx != -1:
                self.cb_alphaFill.setCurrentIndex(idx)

        if "bitDepth" in data:
            idx = self.cb_bitDepth.findText(data["bitDepth"])
            if idx != -1:
                self.cb_bitDepth.setCurrentIndex(idx)

        if "png_Compress" in data:
            idx = self.cb_png_compress.findText(data["png_Compress"])
            if idx != -1:
                self.cb_png_compress.setCurrentIndex(idx)

        if "png_Interlaced" in data:
            self.chb_png_interlaced.setChecked(data["png_Interlaced"])

        if "png_Gamma" in data:
            self.chb_png_gamma.setChecked(data["png_Gamma"])

        if "png_Rez" in data:
            self.chb_png_rez.setChecked(data["png_Rez"])
            
        if "png_BgColor" in data:
            self.chb_png_bgColor.setChecked(data["png_BgColor"])

        if "png_LayerOffset" in data:
            self.chb_png_layerOffset.setChecked(data["png_LayerOffset"])

        if "png_AlphaColor" in data:
            self.chb_png_alphaColor.setChecked(data["png_AlphaColor"])                                    

        if "jpg_Qual" in data:
            idx = self.cb_jpg_qual.findText(data["jpg_Qual"])
            if idx != -1:
                self.cb_jpg_qual.setCurrentIndex(idx)

        if "jpg_Smooth" in data:
            idx = self.cb_jpg_smooth.findText(data["jpg_Smooth"])
            if idx != -1:
                self.cb_jpg_smooth.setCurrentIndex(idx)

        if "jpg_SubSample" in data:
            idx = self.cb_jpg_subSample.findText(data["jpg_SubSample"])
            if idx != -1:
                self.cb_jpg_subSample.setCurrentIndex(idx)

        if "jpg_Optimize" in data:
            self.chb_jpg_optimize.setChecked(data["jpg_Optimize"])

        if "jpg_Progressive" in data:
            self.chb_jpg_progressive.setChecked(data["jpg_Progressive"])

        if "jpg_ArithCode" in data:
            self.chb_jpg_arithCode.setChecked(data["jpg_ArithCode"])

        if "exportComment" in data:
            self.e_comment.setText(data["exportComment"])


        if "lastexportpath" in data:
            lePath = self.core.fixPath(data["lastexportpath"])
            self.l_pathLast.setText(lePath)
            self.l_pathLast.setToolTip(lePath)
        if "stateenabled" in data:
            if type(data["stateenabled"]) == int:
                self.state.setCheckState(
                    0, Qt.CheckState(data["stateenabled"]),
                )

        self.updateUiOptions()

        self.core.callback("onStateSettingsLoaded", self, data)


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

        self.e_comment.editingFinished.connect(self.stateManager.saveStatesToScene)






        self.b_pathLast.clicked.connect(self.showLastPathMenu)
        # self.lw_passes.itemDoubleClicked.connect(
        #     lambda x: self.core.appPlugin.sm_render_openPasses(self)
        # )



    @err_catcher(name=__name__)
    def updateUiOptions(self, *args):

        format = self.cb_format.currentText()
        colorMode = self.cb_colorMode.currentText()
        currentMode = self.cb_colorMode.currentText()

        if colorMode in ["RGB", "GRAY"]:
            self.gb_alphaFill.show()
        else:
            self.gb_alphaFill.hide()

        self.gb_jpgOptions.hide()
        self.gb_pngOptions.hide()

        if format == ".jpg":
            self.gb_jpgOptions.show()
            imageColorMode = ["RGB", "GRAY"]
            colorModeIdx = 0
            imageBitDepth = ["8"]
            bitIdx = 0

        elif format == ".png":
            self.gb_pngOptions.show()
            imageColorMode = ["RGB", "RGBA", "GRAY", "GRAYA"]
            colorModeIdx = 0
            imageBitDepth = ["8", "16"]
            bitIdx = 1

        elif format == ".exr":
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




        self.cb_bitDepth.clear()
        self.cb_bitDepth.addItems(imageBitDepth)
        self.cb_bitDepth.setCurrentIndex(bitIdx)





    @err_catcher(name=__name__)
    def initializeContextBasedSettings(self):
        context = self.getCurrentContext()
        # if context.get("type") == "asset":
        #     self.setRangeType("Single Frame")
        # elif context.get("type") == "shot":
        #     self.setRangeType("Shot")
        # elif self.stateManager.standalone:
        #     self.setRangeType("Custom")
        # else:
        #     self.setRangeType("Scene")

        # start, end = self.getFrameRange("Scene")
        # if start is not None:
        #     self.sp_rangeStart.setValue(start)

        # if end is not None:
        #     self.sp_rangeEnd.setValue(end)

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
    def rangeTypeChanged(self, state):
        self.updateUi()
        self.stateManager.saveStatesToScene()

    @err_catcher(name=__name__)
    def startChanged(self):
        if self.sp_rangeStart.value() > self.sp_rangeEnd.value():
            self.sp_rangeEnd.setValue(self.sp_rangeStart.value())

        self.stateManager.saveStatesToScene()

    @err_catcher(name=__name__)
    def endChanged(self):
        if self.sp_rangeEnd.value() < self.sp_rangeStart.value():
            self.sp_rangeStart.setValue(self.sp_rangeEnd.value())

        self.stateManager.saveStatesToScene()

    @err_catcher(name=__name__)
    def frameExpressionChanged(self, text=None):
        if not hasattr(self, "expressionWinLabel"):
            return

        frames = self.core.resolveFrameExpression(self.le_frameExpression.text())
        if len(frames) > 1000:
            frames = frames[:1000]
            frames.append("...")

        for idx in range(int(len(frames) / 30.0)):
            frames.insert((idx+1)*30, "\n")

        frameStr = ",".join([str(x) for x in frames]) or "invalid expression"
        self.expressionWinLabel.setText(frameStr)
        self.expressionWin.resize(1, 1)

    @err_catcher(name=__name__)
    def exprMoveEvent(self, event):
        self.showExpressionWin(event)
        if hasattr(self, "expressionWin") and self.expressionWin.isVisible():
            self.expressionWin.move(
                QCursor.pos().x() + 20, QCursor.pos().y() - self.expressionWin.height()
            )
        self.le_frameExpression.origMoveEvent(event)

    @err_catcher(name=__name__)
    def showExpressionWin(self, event):
        if not hasattr(self, "expressionWin") or not self.expressionWin.isVisible():
            if hasattr(self, "expressionWin"):
                self.expressionWin.close()

            self.expressionWin = QFrame()
            ss = getattr(self.core.appPlugin, "getFrameStyleSheet", lambda x: "")(self)
            self.expressionWin.setStyleSheet(
                ss + """ .QFrame{ border: 2px solid rgb(100,100,100);} """
            )

            self.core.parentWindow(self.expressionWin)
            winwidth = 10
            winheight = 10
            VBox = QVBoxLayout()
            frames = self.core.resolveFrameExpression(self.le_frameExpression.text())
            if len(frames) > 1000:
                frames = frames[:1000]
                frames.append("...")

            for idx in range(int(len(frames) / 30.0)):
                frames.insert((idx+1)*30, "\n")

            frameStr = ",".join([str(x) for x in frames]) or "invalid expression"
            self.expressionWinLabel = QLabel(frameStr)
            VBox.addWidget(self.expressionWinLabel)
            self.expressionWin.setLayout(VBox)
            self.expressionWin.setWindowFlags(
                Qt.FramelessWindowHint  # hides the window controls
                | Qt.WindowStaysOnTopHint  # forces window to top... maybe
                | Qt.SplashScreen  # this one hides it from the task bar!
            )

            self.expressionWin.setGeometry(0, 0, winwidth, winheight)
            self.expressionWin.move(QCursor.pos().x() + 20, QCursor.pos().y())
            self.expressionWin.setAttribute(Qt.WA_ShowWithoutActivating)
            self.expressionWin.show()

    @err_catcher(name=__name__)
    def exprLeaveEvent(self, event):
        if hasattr(self, "expressionWin") and self.expressionWin.isVisible():
            self.expressionWin.close()

    @err_catcher(name=__name__)
    def exprFocusOutEvent(self, event):
        if hasattr(self, "expressionWin") and self.expressionWin.isVisible():
            self.expressionWin.close()

    @err_catcher(name=__name__)
    def setCam(self, index):
        self.curCam = self.camlist[index]
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
            taskType="3d",
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
    def presetOverrideChanged(self, checked):
        self.cb_renderPreset.setEnabled(checked)
        self.stateManager.saveStatesToScene()

    @err_catcher(name=__name__)
    def resOverrideChanged(self, checked):
        self.sp_resWidth.setEnabled(checked)
        self.sp_resHeight.setEnabled(checked)
        self.b_resPresets.setEnabled(checked)

        self.stateManager.saveStatesToScene()

    @err_catcher(name=__name__)
    def showResPresets(self):
        pmenu = QMenu(self)

        for preset in self.resolutionPresets:
            pAct = QAction(preset, self)
            res = self.getResolution(preset)
            if not res:
                continue

            pwidth, pheight = res

            pAct.triggered.connect(
                lambda x=None, v=pwidth: self.sp_resWidth.setValue(v)
            )
            pAct.triggered.connect(
                lambda x=None, v=pheight: self.sp_resHeight.setValue(v)
            )
            pAct.triggered.connect(lambda: self.stateManager.saveStatesToScene())
            pmenu.addAction(pAct)

        pmenu.exec_(QCursor.pos())

    @err_catcher(name=__name__)
    def getRangeType(self):
        return self.cb_rangeType.currentText()

    @err_catcher(name=__name__)
    def setRangeType(self, rangeType):
        idx = self.cb_rangeType.findText(rangeType)
        if idx != -1:
            self.cb_rangeType.setCurrentIndex(idx)
            self.updateRange()
            return True

        return False

    @err_catcher(name=__name__)
    def getResolution(self, resolution):
        res = None
        if resolution == "Get from rendersettings":
            if hasattr(self.core.appPlugin, "getResolution"):
                res = self.core.appPlugin.getResolution()
            else:
                res = [1920, 1080]
        elif resolution.startswith("Project ("):
            res = resolution[9:-1].split("x")
            res = [int(r) for r in res]
        else:
            try:
                pwidth = int(resolution.split("x")[0])
                pheight = int(resolution.split("x")[1])
                res = [pwidth, pheight]
            except:
                res = getattr(
                    self.core.appPlugin, "evaluateResolution", lambda x: None
                )(resolution)

        return res

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

        # # update Cams
        # self.cb_cam.clear()
        # self.camlist = camNames = []

        # if not self.stateManager.standalone:
        #     self.camlist = self.core.appPlugin.getCamNodes(self, cur=True)
        #     camNames = [self.core.appPlugin.getCamName(self, i) for i in self.camlist]

        # self.cb_cam.addItems(camNames)

        # if self.curCam in self.camlist:
        #     self.cb_cam.setCurrentIndex(self.camlist.index(self.curCam))
        # else:
        #     self.cb_cam.setCurrentIndex(0)
        #     if len(self.camlist) > 0:
        #         self.curCam = self.camlist[0]
        #     else:
        #         self.curCam = None

        #     self.stateManager.saveStatesToScene()

        # self.updateRange()

        if not self.core.mediaProducts.getUseMaster():
            self.w_master.setVisible(False)

        # update Render Layer
        # curLayer = self.cb_renderLayer.currentText()
        # self.cb_renderLayer.clear()

        # layerList = getattr(
        #     self.core.appPlugin, "sm_render_getRenderLayer", lambda x: []
        # )(self)

        # self.cb_renderLayer.addItems(layerList)

        # if curLayer in layerList:
        #     self.cb_renderLayer.setCurrentIndex(layerList.index(curLayer))
        # else:
        #     self.cb_renderLayer.setCurrentIndex(0)
        #     self.stateManager.saveStatesToScene()

        # self.refreshSubmitUi()
        # getattr(self.core.appPlugin, "sm_render_refreshPasses", lambda x: None)(self)

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

    @err_catcher(name=__name__)
    def refreshSubmitUi(self):
        if not self.gb_submit.isHidden():
            if not self.gb_submit.isCheckable():
                return

            submitChecked = self.gb_submit.isChecked()
            for idx in reversed(range(self.gb_submit.layout().count())):
                self.gb_submit.layout().itemAt(idx).widget().setHidden(not submitChecked)

            if submitChecked:
                self.core.plugins.getRenderfarmPlugin(self.cb_manager.currentText()).sm_render_updateUI(self)

    @err_catcher(name=__name__)
    def updateRange(self):
        rangeType = self.cb_rangeType.currentText()
        isCustom = rangeType == "Custom"
        isExp = rangeType == "Expression"
        self.l_rangeStart.setVisible(not isCustom and not isExp)
        self.l_rangeEnd.setVisible(not isCustom and not isExp)
        self.sp_rangeStart.setVisible(isCustom)
        self.sp_rangeEnd.setVisible(isCustom)
        self.w_frameRangeValues.setVisible(not isExp)
        self.w_frameExpression.setVisible(isExp)

        if not isCustom and not isExp:
            frange = self.getFrameRange(rangeType=rangeType)
            start = str(int(frange[0])) if frange[0] is not None else "-"
            end = str(int(frange[1])) if frange[1] is not None else "-"
            self.l_rangeStart.setText(start)
            self.l_rangeEnd.setText(end)

    @err_catcher(name=__name__)
    def getFrameRange(self, rangeType):
        startFrame = 1
        endFrame = 1

        return startFrame, endFrame

    @err_catcher(name=__name__)
    def openSlaves(self):
        if eval(os.getenv("PRISM_DEBUG", "False")):
            try:
                del sys.modules["SlaveAssignment"]
            except:
                pass

        import SlaveAssignment

        self.sa = SlaveAssignment.SlaveAssignment(
            core=self.core, curSlaves=self.e_osSlaves.text()
        )
        result = self.sa.exec_()

        if result == 1:
            selSlaves = ""
            if self.sa.rb_exclude.isChecked():
                selSlaves = "exclude "
            if self.sa.rb_all.isChecked():
                selSlaves += "All"
            elif self.sa.rb_group.isChecked():
                selSlaves += "groups: "
                for i in self.sa.activeGroups:
                    selSlaves += i + ", "

                if selSlaves.endswith(", "):
                    selSlaves = selSlaves[:-2]

            elif self.sa.rb_custom.isChecked():
                slavesList = [x.text() for x in self.sa.lw_slaves.selectedItems()]
                for i in slavesList:
                    selSlaves += i + ", "

                if selSlaves.endswith(", "):
                    selSlaves = selSlaves[:-2]

            self.e_osSlaves.setText(selSlaves)
            self.stateManager.saveStatesToScene()

    @err_catcher(name=__name__)
    def gpuPtChanged(self):
        self.w_dlGPUdevices.setEnabled(self.sp_dlGPUpt.value() == 0)
        self.stateManager.saveStatesToScene()

    @err_catcher(name=__name__)
    def gpuDevicesChanged(self):
        self.w_dlGPUpt.setEnabled(self.le_dlGPUdevices.text() == "")
        self.stateManager.saveStatesToScene()

    @err_catcher(name=__name__)
    def showPasses(self):
        steps = getattr(
            self.core.appPlugin, "sm_render_getRenderPasses", lambda x: None
        )(self)

        if steps is None or len(steps) == 0:
            return False

        if self.core.isStr(steps):
            steps = eval(steps)

        if eval(os.getenv("PRISM_DEBUG", "False")):
            try:
                del sys.modules["ItemList"]
            except:
                pass

        import ItemList

        self.il = ItemList.ItemList(core=self.core)
        self.il.setWindowTitle("Select Passes")
        self.core.parentWindow(self.il)
        self.il.tw_steps.doubleClicked.connect(self.il.accept)
        self.il.tw_steps.horizontalHeaderItem(0).setText("Name")
        self.il.tw_steps.setColumnHidden(1, True)
        for i in sorted(steps, key=lambda s: s.lower()):
            rc = self.il.tw_steps.rowCount()
            self.il.tw_steps.insertRow(rc)
            item1 = QTableWidgetItem(i)
            self.il.tw_steps.setItem(rc, 0, item1)

        result = self.il.exec_()

        if result != 1:
            return False

        for i in self.il.tw_steps.selectedItems():
            if i.column() == 0:
                self.core.appPlugin.sm_render_addRenderPass(
                    self, passName=i.text(), steps=steps
                )

        self.updateUi()
        self.stateManager.saveStatesToScene()

    @err_catcher(name=__name__)
    def rclickPasses(self, pos):
        if self.lw_passes.currentItem() is None or not getattr(
            self.core.appPlugin, "canDeleteRenderPasses", True
        ):
            return

        rcmenu = QMenu()

        delAct = QAction("Delete", self)
        delAct.triggered.connect(self.deleteAOVs)
        rcmenu.addAction(delAct)

        rcmenu.exec_(QCursor.pos())

    @err_catcher(name=__name__)
    def deleteAOVs(self):
        items = self.lw_passes.selectedItems()
        for i in items:
            self.core.appPlugin.removeAOV(i.text())
        self.updateUi()

    @err_catcher(name=__name__)
    def rjToggled(self, checked):
        self.refreshSubmitUi()
        self.stateManager.saveStatesToScene()

    @err_catcher(name=__name__)
    def managerChanged(self, text=None):
        plugin = self.core.plugins.getRenderfarmPlugin(self.cb_manager.currentText())
        if plugin:
            plugin.sm_render_managerChanged(self)

        self.stateManager.saveStatesToScene()

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
                "colorMode": self.cb_colorMode.currentText(),
                "bitDepth": self.cb_bitDepth.currentText(),
                "alphaFill": self.cb_alphaFill.currentText(),
                "imageComment": self.e_comment.text()
                }

            if outputType == ".jpg":


                rSettings.update({"jpg_Quality": self.cb_jpg_qual.currentText(),
                                  "jpg_Smoothing": self.cb_jpg_smooth.currentText(),
                                  "jpg_SubSample": self.cb_jpg_subSample.currentIndex(),
                                  "jpg_Optimize": self.chb_jpg_optimize.isChecked(),
                                  "jpg_Progressive": self.chb_jpg_progressive.isChecked(),
                                  "jpg_ArithCode": self.chb_jpg_arithCode.isChecked()
                                })
                
            elif outputType == ".png":
                rSettings.update({"png_Compress": self.cb_png_compress.currentText(),
                                  "png_Interlaced": self.chb_png_interlaced.isChecked(),
                                  "png_Gamma": self.chb_png_gamma.isChecked(),
                                  "png_Rez": self.chb_png_rez.isChecked(),
                                  "png_BgColor": self.chb_png_bgColor.isChecked(),
                                  "png_LayerOffset": self.chb_png_layerOffset.isChecked(),
                                  "png_AlphaColor": self.chb_png_alphaColor.isChecked()
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
            self.core.mediaProducts.updateMasterVersion(outputName)
        elif masterAction == "Add to master":
            self.core.mediaProducts.addToMasterVersion(outputName)

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
            # "renderpresetoverride": str(self.chb_renderPreset.isChecked()),
            # "currentrenderpreset": self.cb_renderPreset.currentText(),
            # "rangeType": str(self.cb_rangeType.currentText()),
            # "startframe": self.sp_rangeStart.value(),
            # "endframe": self.sp_rangeEnd.value(),
            # "frameExpression": self.le_frameExpression.text(),
            # "currentcam": str(self.curCam),
            # "resoverride": str(
            #     [
            #         self.chb_resOverride.isChecked(),
            #         self.sp_resWidth.value(),
            #         self.sp_resHeight.value(),
            #     ]
            # ),
            "masterVersion": self.cb_master.currentText(),
            "curoutputpath": self.cb_outPath.currentText(),
            # "renderlayer": str(self.cb_renderLayer.currentText()),
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

            "exportComment": self.e_comment.text(),

            # "submitrender": str(self.gb_submit.isChecked()),
            # "rjmanager": str(self.cb_manager.currentText()),
            # "rjprio": self.sp_rjPrio.value(),
            # "rjframespertask": self.sp_rjFramesPerTask.value(),
            # "rjtimeout": self.sp_rjTimeout.value(),
            # "rjsuspended": str(self.chb_rjSuspended.isChecked()),
            # "osdependencies": str(self.chb_osDependencies.isChecked()),
            # "osupload": str(self.chb_osUpload.isChecked()),
            # "ospassets": str(self.chb_osPAssets.isChecked()),
            # "osslaves": self.e_osSlaves.text(),
            # "dlconcurrent": self.sp_dlConcurrentTasks.value(),
            # "dlgpupt": self.sp_dlGPUpt.value(),
            # "dlgpudevices": self.le_dlGPUdevices.text(),
            "lastexportpath": self.l_pathLast.text().replace("\\", "/"),
            # "enablepasses": str(self.gb_passes.isChecked()),
            "stateenabled": self.core.getCheckStateValue(self.state.checkState(0)),
        }
        self.core.callback("onStateGetSettings", self, stateProps)
        return stateProps
