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


from encodings.punycode import T
import os
import sys
import time
import platform
import logging

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from PrismUtils.Decorators import err_catcher
from StateUserInterfaces import Gimp_Render_ui

SCRIPT_ROOT = os.path.dirname(os.path.dirname(__file__))
if SCRIPT_ROOT not in sys.path:
    sys.path.insert(0, SCRIPT_ROOT)

from GimpMapping import (
    FORMAT_BIT_DEPTHS,
    FORMAT_COLOR_MODES,
    JPEG_QUALITY_OPTIONS,
    JPEG_SMOOTHING_OPTIONS,
    JPEG_SUBSAMPLING_LABELS,
    OUTPUT_FORMATS,
    PNG_COMPRESS_OPTIONS,
    SCALE_OPTIONS,
    TIFF_COMPRESSION_LABELS,
)


if TYPE_CHECKING:
    from PrismCore import PrismCore
    from StateManager import StateManager
    from Prism_Gimp_Functions import Prism_Gimp_Functions


logger = logging.getLogger(__name__)


#   Helper to Convert Bool to Bit (0/1)
def boolToBit(bool):
    if bool:
        return 1
    else:
        return 0


#   Helper to Convert Bit (0/1) to Bool
def bitToBool(bit):
    try:
        return bool(int(bit))
    except Exception:
        return bool(bit)


class Gimp_RenderClass(object):
    className = "Gimp_Render"
    listType = "Export"
    stateCategories = {"Render": [{"label": className, "stateType": className}]}


    @err_catcher(name=__name__)
    def setup(self, state, core, stateManager, node=None, stateData=None):
        self.state = state
        self.core:PrismCore = core
        self.stateManager:StateManager = stateManager
        self.gimpFuncts:Prism_Gimp_Functions = self.core.appPlugin
        self._isInitializingState = True

        self.canSetVersion = True
        self.customContext = None
        self.allowCustomContext = False
        self.renderingStarted = False

        try:
            self.core.registerCallback("onStateManagerClose", self.stateManager.saveStatesToScene, plugin=self)
        except Exception:
            pass

        self.e_name.setText(state.text(0) + " - {identifier}")
        self.l_name.setVisible(False)
        self.e_name.setVisible(False)
        self.w_context.setHidden(True)

        try:
            getattr(self.core.appPlugin, "sm_render_startup", lambda x: None)(self)
        except Exception:
            pass

        masterItems = ["Set as master", "Don't update master"]
        self.cb_master.clear()
        self.cb_master.addItems(masterItems)

        self.product_paths = self.core.paths.getRenderProductBasePaths() or {}
        self.cb_outPath.clear()
        self.cb_outPath.addItems(list(self.product_paths.keys()))
        if len(self.product_paths) < 2:
            self.w_outPath.setVisible(False)

        self.mediaType = "2drenders"
        self.tasknameRequired = True

        ##  Setup Format Options
        self.outputFormats = OUTPUT_FORMATS
        self.cb_format.clear()
        self.cb_format.addItems(self.outputFormats)

        #   Scale
        self.cb_scale.clear()
        self.cb_scale.addItems(SCALE_OPTIONS)
        self.cb_scale.setCurrentIndex(3)

        #   PNG
        self.cb_png_bitDepth.clear()
        self.cb_png_bitDepth.addItems(FORMAT_BIT_DEPTHS[".png"])
        self.cb_png_bitDepth.setCurrentIndex(1)

        self.cb_png_compress.clear()
        self.cb_png_compress.addItems(PNG_COMPRESS_OPTIONS)
        self.cb_png_compress.setCurrentIndex(4)

        self.chb_png_interlaced.setChecked(False)
        self.chb_png_gamma.setChecked(True)
        self.chb_png_rez.setChecked(True)
        self.chb_png_bgColor.setChecked(False)

        #   Hidden Since Gimp3 Does Not Seem to Expose This Option Anymore
        self.chb_png_gamma.setVisible(False)
        
        self.chb_png_layerOffset.setChecked(False)
        self.chb_png_alphaColor.setChecked(True)

        #   JPEG
        self.cb_jpg_qual.clear()
        self.cb_jpg_qual.addItems(JPEG_QUALITY_OPTIONS)
        self.cb_jpg_qual.setCurrentIndex(5)

        self.cb_jpg_smooth.clear()
        self.cb_jpg_smooth.addItems(JPEG_SMOOTHING_OPTIONS)
        self.cb_jpg_smooth.setCurrentIndex(5)

        self.cb_jpg_subSample.clear()
        self.cb_jpg_subSample.addItems(JPEG_SUBSAMPLING_LABELS)
        self.cb_jpg_subSample.setCurrentIndex(1)

        self.chb_jpg_optimize.setChecked(True)
        self.chb_jpg_progressive.setChecked(False)
        self.chb_jpg_baseline.setChecked(True)

        #   TIFF
        self.cb_tiff_compress.clear()
        self.cb_tiff_compress.addItems(TIFF_COMPRESSION_LABELS)
        self.cb_tiff_compress.setCurrentIndex(3)
        self.chb_tiff_saveLayers.setChecked(False)

        #   PDF
        self.chb_pdf_omitHidden.setChecked(True)
        self.chb_pdf_convertToVector.setChecked(True)

        self.setToolTips()
        self.connectEvents()

        self.oldPalette = self.b_changeTask.palette()
        self.warnPalette = QPalette()
        self.warnPalette.setColor(QPalette.Button, QColor(200, 0, 0))
        self.warnPalette.setColor(QPalette.ButtonText, QColor(255, 255, 255))

        self.setTaskWarn(True)
        self.nameChanged(state.text(0))

        self.loadImageSpecs()
        self.updateUiOptions()

        self.core.callback("onStateStartup", self)

        try:
            if stateData is not None:
                self.loadData(stateData)
            else:
                self.gimpFuncts.markSceneDirty()
                self.initializeContextBasedSettings()
        finally:
            self._isInitializingState = False



    @err_catcher(name=__name__)
    def setToolTips(self):
        tip = "Image Details"
        self.bg_imageSpecs.setToolTip(tip)

        tip = "Image Resolution"
        self.l_spec_rezLabel.setToolTip(tip)
        self.l_specs_Xrez.setToolTip(tip)
        self.l_specs_Yrez.setToolTip(tip)

        tip = "Image Color Mode"
        self.l_specs_ColorMode_text.setToolTip(tip)
        self.l_specs_ColorMode.setToolTip(tip)

        tip = "Image Bit Depth"
        self.l_specs_BitDepth_text.setToolTip(tip)
        self.l_specs_BitDepth.setToolTip(tip)

        tip = "Image Display Gamma"
        self.l_specs_Gamma_text.setToolTip(tip)
        self.l_specs_Gamma.setToolTip(tip)

        tip = "If the Image's bottom layer has an alpha channel"
        self.l_specs_Alpha_text.setToolTip(tip)
        self.l_specs_Alpha.setToolTip(tip)

        tip = ("Export image scale based on image resolution.\n"
               "Does not affect scenefile.")
        self.cb_scale.setToolTip(tip)

        tip = "Export File Format"
        self.cb_format.setToolTip(tip)

        tip = ("Export Image Color Mode.\n"
               "Does not affect scenefile.")
        self.l_colorMode.setToolTip(tip)
        self.cb_colorMode.setToolTip(tip)

        tip = "PNG Bit Depth"
        self.l_png_bitDepth.setToolTip(tip)
        self.cb_png_bitDepth.setToolTip(tip)

        tip = ("PNG Lossless Compression:\n"
               "Higher = smaller file but slower to\n"
               "generate, load and save.")
        self.l_png_compress.setToolTip(tip)
        self.cb_png_compress.setToolTip(tip)
        
        tip = "Premultiple Alpha Channel"
        self.chb_png_alphaColor.setToolTip(tip)

        tip = ("Helps with web viewing of images\n"
               "with many transparent levels.")
        self.chb_png_bgColor.setToolTip(tip)
        
        tip = "Saves images display gamma function"
        self.chb_png_gamma.setToolTip(tip)

        tip = ("Saves image as interlaced.\n"
               "Helps progressive load for web.")
        self.chb_png_interlaced.setToolTip(tip)
        
        tip = "Saves resolution in metadata in ppi."
        self.chb_png_rez.setToolTip(tip)

        tip = ("Saves layer offsets.\n"
               "Do not use.")
        self.chb_png_layerOffset.setToolTip(tip)

        tip = ("JPG Qaulity:\n"
               "Higher = better quality but larger file")
        self.l_jpg_qual.setToolTip(tip)
        self.cb_jpg_qual.setToolTip(tip)

        tip = ("JPG Smoothing:\n"
               "Helps compression artifacts but can blur image")
        self.l_jpg_smooth.setToolTip(tip)
        self.cb_jpg_smooth.setToolTip(tip)

        tip = ("Color Sampling mode:\n"
               "Higher = better image but larger file")
        self.l_jpg_subSample.setToolTip(tip)
        self.cb_jpg_subSample.setToolTip(tip)
        
        tip = ("Optimize JPG:\n"
               "Produces smaller file, but slower to generate")
        self.chb_jpg_optimize.setToolTip(tip)
        
        tip = ("Encodes to allow progressive load.\n"
               "Useful for web, but slightly larger file.")
        self.chb_jpg_progressive.setToolTip(tip)
        
        tip = ("Choose to encode without baseline.\n"
               "Should usually keep enabled")
        self.chb_jpg_baseline.setToolTip(tip)

        tip = "Choose method of compression."
        self.l_tiff_compress.setToolTip(tip)
        self.cb_tiff_compress.setToolTip(tip)

        tip = ("Save each Gimp layer as a separate TIFF page.\n\n"
               "This may not be readable by all Applications.")
        self.l_tiff_saveLayers.setToolTip(tip)
        self.chb_tiff_saveLayers.setToolTip(tip)

        tip = ("Save as a BigTIFF file.\n"
               "This allows for file sizes greater than 4gb.\n"
               "Not all applications can read BigTIFFs.")
        self.l_tiff_useBig.setToolTip(tip)
        self.chb_tiff_useBig.setToolTip(tip)

        tip = "Save color values of transparent pixels"
        self.l_tiff_alphaColor.setToolTip(tip)
        self.chb_tiff_alphaColor.setToolTip(tip)

        tip = "Omits layers that are not enabled or with zero opacity."
        self.chb_pdf_omitHidden.setToolTip(tip)

        tip = "Convert bitmaps to vector graphics where possible."
        self.chb_pdf_convertToVector.setToolTip(tip)

        tip = "Apply layer masks before export."
        self.chb_pdf_applyLayers.setToolTip(tip)

        tip = ("Saves the .psd file to the SceneBrowser next to the original\n"
               "and will use the same version number as the original .xcf file.\n"
               "This will not save to the Media tab.")
        self.chb_psd_saveAsScene.setToolTip(tip)


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

        if "specs_colorMode" in stateData:
            self.l_specs_ColorMode.setText(stateData["specs_colorMode"])

        if "specs_bitDepth" in stateData:
            self.l_specs_BitDepth.setText(stateData["specs_bitDepth"])

        if "specs_gamma" in stateData:
            self.l_specs_Gamma.setText(stateData["specs_gamma"])

        if "exportScale" in stateData:
            idx = self.cb_scale.findText(stateData["exportScale"])
            if idx != -1:
                self.cb_scale.setCurrentIndex(idx)
        
        if "outputFormat" in stateData:
            idx = self.cb_format.findText(stateData["outputFormat"])
            if idx != -1:
                self.cb_format.setCurrentIndex(idx)

        if "colorMode" in stateData:
            idx = self.cb_colorMode.findText(stateData["colorMode"])
            if idx != -1:
                self.cb_colorMode.setCurrentIndex(idx)

        if "png_BitDepth" in stateData:
            idx = self.cb_png_bitDepth.findText(stateData["png_BitDepth"])
            if idx != -1:
                self.cb_png_bitDepth.setCurrentIndex(idx)

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

        if "jpg_Baseline" in stateData:
            self.chb_jpg_baseline.setChecked(stateData["jpg_Baseline"])

        if "tiff_Compression" in stateData:
            idx = self.cb_tiff_compress.findText(stateData["tiff_Compression"])
            if idx != -1:
                self.cb_tiff_compress.setCurrentIndex(idx)

        if "tiff_useBigTiff" in stateData:
            self.chb_tiff_useBig.setChecked(stateData["tiff_useBigTiff"])

        if "tiff_SaveLayers" in stateData:
            self.chb_tiff_saveLayers.setChecked(stateData["tiff_SaveLayers"])

        if "tiff_SaveTransPx" in stateData:
            self.chb_tiff_alphaColor.setChecked(stateData["tiff_SaveTransPx"])

        if "pdf_OmitHidden" in stateData:
            self.chb_pdf_omitHidden.setChecked(stateData["pdf_OmitHidden"])

        if "pdf_ConvertToVector" in stateData:
            self.chb_pdf_convertToVector.setChecked(stateData["pdf_ConvertToVector"])

        if "pdf_ApplyLayers" in stateData:
            self.chb_pdf_applyLayers.setChecked(stateData["pdf_ApplyLayers"])

        if "psd_SaveAsScenefile" in stateData:
            self.chb_psd_saveAsScene.setChecked(stateData["psd_SaveAsScenefile"])

        if "lastexportpath" in stateData:
            lePath = self.core.fixPath(stateData["lastexportpath"])
            self.l_pathLast.setText(lePath)
            self.l_pathLast.setToolTip(lePath)

        if "stateenabled" in stateData:
            if type(stateData["stateenabled"]) == int:
                self.state.setCheckState(
                    0, Qt.CheckState(stateData["stateenabled"]),
                )

        self.updateUi()
        self.updateUiOptions()
        self.stateManager.saveStatesToScene()
        
        self.core.callback("onStateSettingsLoaded", self, stateData)


    @err_catcher(name=__name__)
    def loadImageSpecs(self):
        imageSpecs = {}

        try:
            imageSpecs = getattr(self.core.appPlugin, "getImageSpecs", lambda: {})() or {}
        except Exception as e:
            logger.warning(f"Failed to read image specs: {e}")

        if "xRez" in imageSpecs:
            self.l_specs_Xrez.setText(str(imageSpecs["xRez"]))

        if "yRez" in imageSpecs:
            self.l_specs_Yrez.setText(str(imageSpecs["yRez"]))

        if "colorMode" in imageSpecs:
            self.l_specs_ColorMode.setText(imageSpecs["colorMode"])

        if "bitDepth" in imageSpecs:
            self.l_specs_BitDepth.setText(imageSpecs["bitDepth"])

        if "gamma" in imageSpecs:
            self.l_specs_Gamma.setText(imageSpecs["gamma"])

        if "hasAlpha" in imageSpecs:
            self.l_specs_Alpha.setText(str(imageSpecs["hasAlpha"]))


    @err_catcher(name=__name__)
    def connectEvents(self):
        self.e_name.textChanged.connect(self.nameChanged)
        self.e_name.editingFinished.connect(self.saveStatesToScene)
        self.cb_context.activated.connect(self.onContextTypeChanged)
        self.b_context.clicked.connect(self.selectContextClicked)
        self.b_changeTask.clicked.connect(self.changeTask)
        self.cb_master.activated.connect(self.saveStatesToScene)
        self.cb_outPath.activated.connect(self.saveStatesToScene)

        self.cb_format.activated.connect(self.updateUiOptions)
        self.cb_format.activated.connect(self.saveStatesToScene)
        self.cb_colorMode.activated.connect(self.updateUiOptions)
        self.cb_colorMode.activated.connect(self.saveStatesToScene)

        self.cb_png_bitDepth.activated.connect(self.saveStatesToScene)
        self.cb_png_compress.activated.connect(self.saveStatesToScene)
        self.chb_png_alphaColor.toggled.connect(self.saveStatesToScene)
        self.chb_png_bgColor.toggled.connect(self.saveStatesToScene)
        self.chb_png_gamma.toggled.connect(self.saveStatesToScene)
        self.chb_png_interlaced.toggled.connect(self.saveStatesToScene)
        self.chb_png_rez.toggled.connect(self.saveStatesToScene)
        self.chb_png_layerOffset.toggled.connect(self.saveStatesToScene)

        self.cb_jpg_qual.activated.connect(self.saveStatesToScene)
        self.cb_jpg_smooth.activated.connect(self.saveStatesToScene)
        self.cb_jpg_subSample.activated.connect(self.saveStatesToScene)
        self.chb_jpg_optimize.toggled.connect(self.saveStatesToScene)
        self.chb_jpg_progressive.toggled.connect(self.saveStatesToScene)
        self.chb_jpg_baseline.toggled.connect(self.saveStatesToScene)

        self.cb_tiff_compress.activated.connect(self.saveStatesToScene)
        self.chb_tiff_saveLayers.toggled.connect(self.saveStatesToScene)
        self.chb_tiff_useBig.toggled.connect(self.saveStatesToScene)
        self.chb_tiff_alphaColor.toggled.connect(self.saveStatesToScene)

        self.chb_pdf_omitHidden.toggled.connect(self.saveStatesToScene)
        self.chb_pdf_convertToVector.toggled.connect(self.saveStatesToScene)
        self.chb_pdf_applyLayers.toggled.connect(self.saveStatesToScene)

        self.chb_psd_saveAsScene.toggled.connect(self.saveStatesToScene)

        self.b_pathLast.clicked.connect(self.showLastPathMenu)


    @err_catcher(name=__name__)
    def saveStatesToScene(self, *args):
        self.stateManager.saveStatesToScene()

        if getattr(self, "_isInitializingState", False):
            return

        self.gimpFuncts.markSceneDirty()


    #   Updates Ui based on Selected Options
    @err_catcher(name=__name__)
    def updateUiOptions(self, *args):

        #   Captures current settings
        format = self.cb_format.currentText()
        currentMode = self.cb_colorMode.currentText()

        #   Initially Hides all boxes
        self.gb_jpgOptions.hide()
        self.gb_pngOptions.hide()
        self.gb_tiffOptions.hide()
        self.gb_pdfOptions.hide()
        self.gb_psdOptions.hide()

        #   Show only the group boxes relevant to this format
        format_group_boxes = {
            ".jpg": [self.gb_jpgOptions],
            ".png": [self.gb_pngOptions],
            ".exr": [self.gb_outputOptions],
            ".psd": [self.gb_psdOptions],
            ".tif": [self.gb_tiffOptions],
            ".pdf": [self.gb_pdfOptions],
        }
        for gb in format_group_boxes.get(format, []):
            gb.show()

        imageColorMode = FORMAT_COLOR_MODES.get(format, ["RGB", "RGBA", "GRAY", "GRAYA"])
        colorModeIdx   = 0

        #   Clear then load color mode options
        self.cb_colorMode.clear()
        self.cb_colorMode.addItems(imageColorMode)

        #   Restore previous selection if still valid
        idx = self.cb_colorMode.findText(currentMode)
        if idx != -1:
            self.cb_colorMode.setCurrentIndex(idx)
        else:
            self.cb_colorMode.setCurrentIndex(colorModeIdx)


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
        self.saveStatesToScene()


    @err_catcher(name=__name__)
    def onContextTypeChanged(self, state):
        self.refreshContext()
        self.saveStatesToScene()


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
        return self.cb_format.currentText()


    @err_catcher(name=__name__)
    def setFormat(self, fmt):
        idx = self.cb_format.findText(fmt)
        if idx != -1:
            self.cb_format.setCurrentIndex(idx)
            self.saveStatesToScene()
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
            self.saveStatesToScene()


    @err_catcher(name=__name__)
    def getMasterVersion(self):
        return self.cb_master.currentText()
    

    @err_catcher(name=__name__)
    def setMasterVersion(self, master):
        idx = self.cb_master.findText(master)
        if idx != -1:
            self.cb_master.setCurrentIndex(idx)
            self.saveStatesToScene()
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
            self.saveStatesToScene()
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


    #   Creates .PSD Scenefile Filepath
    @err_catcher(name=__name__)
    def getPsdScenefileOutputName(self):
        curFile = self.core.getCurrentFileName()
        if not curFile:
            self.core.showFileNotInProjectWarning()
            return None, None

        if not self.core.fileInPipeline(curFile, validateFilename=False):
            self.core.showFileNotInProjectWarning()
            return None, None

        fnameData = self.core.getScenefileData(curFile, getEntityFromPath=True)
        if "department" not in fnameData:
            title = "Could not save the file"
            msg = (
                "Couldn't get the required data from the current scenefile. "
                "Did you save it using Prism?\n"
                "Use the Project Browser to save your current scenefile with the correct name."
            )
            self.core.popup(msg, title=title)
            return None, None

        if "project_path" in fnameData:
            del fnameData["project_path"]

        hVersion = self.core.getHighestVersion(
            fnameData,
            fnameData.get("department"),
            fnameData.get("task"),
        )

        outputName = self.core.generateScenePath(
            entity=fnameData,
            department=fnameData["department"],
            task=fnameData["task"],
            comment=self.stateManager.publishComment,
            extension=".psd",
            location=self.cb_outPath.currentText(),
        )

        if not outputName:
            return None, None

        return outputName, hVersion


    #   Extracts Render Settings to Include in Version Info Files
    @err_catcher(name=__name__)
    def getVersionInfoRenderDetails(self, renderSettings):
        if not isinstance(renderSettings, dict):
            return {}

        bitFlagKeys = {
            "png_Interlaced",
            "png_Gamma",
            "png_Rez",
            "png_BgColor",
            "png_LayerOffset",
            "png_AlphaColor",
            "jpg_Optimize",
            "jpg_Progressive",
            "jpg_Baseline",
            "tiff_SaveLayers",
            "tiff_useBigTiff",
            "tiff_SaveTransPx",
            "pdf_OmitHidden",
            "pdf_ConvertToVector",
            "pdf_ApplyLayers",
        }

        detailData = {}
        for key, value in renderSettings.items():
            if key in ["outputType", "exportScale", "colorMode"]:
                detailData[key] = value
            elif key.startswith("png_"):
                detailData[key] = value
            elif key.startswith("jpg_"):
                detailData[key] = value
            elif key.startswith("tiff_"):
                detailData[key] = value
            elif key.startswith("pdf_"):
                detailData[key] = value

            if key in bitFlagKeys:
                detailData[key] = bitToBool(value)

        return detailData
    

    @err_catcher(name=__name__)
    def executeState(self, parent, useVersion="next"):
        endFrame = startFrame = 1
        updateMaster = True
        fileName = self.core.getCurrentFileName()
        context = self.getCurrentContext()

        #   Get Outout File Format
        outputType = self.cb_format.currentText()

        #   If Save as Scenefile is Checked for PSD
        savePSDasScenefile = outputType == ".psd" and self.chb_psd_saveAsScene.isChecked()

        if not self.renderingStarted:
            if self.tasknameRequired and not self.getTaskname():
                return [
                    self.state.text(0)
                    + ": error - no identifier is given. Skipped the activation of this state."
                ]

            #   Create .PSD Scenefile Name
            if savePSDasScenefile:
                outputName, hVersion = self.getPsdScenefileOutputName()
                if not outputName:
                    return [self.state.text(0) + " - error - unable to resolve PSD scenefile path."]

                outputPath = os.path.dirname(outputName)
                updateMaster = False

            #   Create Regular Media Output Name
            else:
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

            #   Build Render Settings
            rSettings = {
                "outputName": outputName,
                "outputType": outputType,
                "startFrame": startFrame,
                "endFrame": endFrame,
                "frames": 1,
                "rangeType": "Single Frame",
                "exportScale": self.cb_scale.currentText(),
                "colorMode": self.cb_colorMode.currentText(),
                }

            #   Add Additional Settings Based on Format
            match outputType:    
                case ".png":
                    rSettings.update({"png_Compress": self.cb_png_compress.currentText(),
                                    "png_Interlaced": boolToBit(self.chb_png_interlaced.isChecked()),
                                    "png_Gamma": boolToBit(self.chb_png_gamma.isChecked()),
                                    "png_Rez": boolToBit(self.chb_png_rez.isChecked()),
                                    "png_BgColor": boolToBit(self.chb_png_bgColor.isChecked()),
                                    "png_LayerOffset": boolToBit(self.chb_png_layerOffset.isChecked()),
                                    "png_AlphaColor": boolToBit(not self.chb_png_alphaColor.isChecked()),
                                    "png_BitDepth": self.cb_png_bitDepth.currentText(),
                                    })
                    
                case ".exr":
                    pass

                case ".jpg":
                    rSettings.update({"jpg_Quality": self.cb_jpg_qual.currentText(),
                                    "jpg_Smoothing": self.cb_jpg_smooth.currentText(),
                                    "jpg_SubSample": self.cb_jpg_subSample.currentText(),
                                    "jpg_Optimize": boolToBit(self.chb_jpg_optimize.isChecked()),
                                    "jpg_Progressive": boolToBit(self.chb_jpg_progressive.isChecked()),
                                    "jpg_Baseline": boolToBit(self.chb_jpg_baseline.isChecked())
                                    })

                case ".tif":
                    rSettings.update({"tiff_Compression": self.cb_tiff_compress.currentText(),
                                    "tiff_SaveLayers": boolToBit(self.chb_tiff_saveLayers.isChecked()),
                                    "tiff_useBigTiff": boolToBit(self.chb_tiff_useBig.isChecked()),
                                    "tiff_SaveTransPx": boolToBit(self.chb_tiff_alphaColor.isChecked())
                                    })
                    
                case ".pdf":
                    rSettings.update({"pdf_OmitHidden": boolToBit(self.chb_pdf_omitHidden.isChecked()),
                                    "pdf_ConvertToVector": boolToBit(self.chb_pdf_convertToVector.isChecked()),
                                    "pdf_ApplyLayers": boolToBit(self.chb_pdf_applyLayers.isChecked())
                                    })

                case ".psd": 
                    pass

            self.core.appPlugin.sm_render_preSubmit(self, rSettings)

            #   Create VersionInfo Details
            details = context.copy()
            if "filename" in details:
                del details["filename"]

            if "extension" in details:
                del details["extension"]

            details["version"] = hVersion
            details["sourceScene"] = fileName
            details["identifier"] = self.getTaskname()
            details["comment"] = self.stateManager.publishComment
            details.update(self.getVersionInfoRenderDetails(rSettings))

            #   Handle .PSD Scenefile Saving and Version Info Creation
            if savePSDasScenefile:
                if self.core.getConfig("globals", "capture_viewport", config="user", dft=True):
                    appPreview = getattr(self.core.appPlugin, "captureViewportThumbnail", lambda: None)()
                    if appPreview:
                        preview = self.core.media.scalePixmap(
                            appPreview,
                            self.core.scenePreviewWidth,
                            self.core.scenePreviewHeight,
                            fitIntoBounds=False,
                            crop=True,
                        )
                    else:
                        preview = None
                else:
                    preview = None

                self.core.saveSceneInfo(filepath=outputName, details=details, preview=preview)
                self.core.addToRecent(outputName)

            #   Handle Regular Media Output Saving and Version Info Creation
            else:
                if self.mediaType == "3drenders":
                    infopath = os.path.dirname(expandedOutputPath)
                else:
                    infopath = expandedOutputPath

                self.core.saveVersionInfo(
                    filepath=infopath, details=details
                )

            self.l_pathLast.setText(outputName)
            self.l_pathLast.setToolTip(outputName)
            self.saveStatesToScene()

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
    def preDelete(self, item=None):
        self.gimpFuncts.markSceneDirty()


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
            "png_BitDepth": self.cb_png_bitDepth.currentText(),
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
            "jpg_Baseline": self.chb_jpg_baseline.isChecked(),
            "tiff_Compression": self.cb_tiff_compress.currentText(),
            "tiff_SaveLayers": self.chb_tiff_saveLayers.isChecked(),
            "tiff_useBigTiff": self.chb_tiff_useBig.isChecked(),
            "tiff_SaveTransPx": self.chb_tiff_alphaColor.isChecked(),
            "pdf_OmitHidden": self.chb_pdf_omitHidden.isChecked(),
            "pdf_ConvertToVector": self.chb_pdf_convertToVector.isChecked(),
            "pdf_ApplyLayers": self.chb_pdf_applyLayers.isChecked(),
            "psd_SaveAsScenefile": self.chb_psd_saveAsScene.isChecked(),
            "lastexportpath": self.l_pathLast.text().replace("\\", "/"),
            "stateenabled": self.core.getCheckStateValue(self.state.checkState(0)),
        }
        self.core.callback("onStateGetSettings", self, stateProps)
        return stateProps
