# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Gimp_ExportdicIPc.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

class Ui_wg_Gimp_Export(object):
    def setupUi(self, wg_Gimp_Export):
        if not wg_Gimp_Export.objectName():
            wg_Gimp_Export.setObjectName(u"wg_Gimp_Export")
        wg_Gimp_Export.resize(482, 1123)
        self.verticalLayout = QVBoxLayout(wg_Gimp_Export)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.w_name = QWidget(wg_Gimp_Export)
        self.w_name.setObjectName(u"w_name")
        self.horizontalLayout_5 = QHBoxLayout(self.w_name)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(9, 0, 18, 0)
        self.l_name = QLabel(self.w_name)
        self.l_name.setObjectName(u"l_name")

        self.horizontalLayout_5.addWidget(self.l_name)

        self.e_name = QLineEdit(self.w_name)
        self.e_name.setObjectName(u"e_name")
        self.e_name.setMinimumSize(QSize(0, 0))
        self.e_name.setMaximumSize(QSize(9999, 16777215))

        self.horizontalLayout_5.addWidget(self.e_name)

        self.l_class = QLabel(self.w_name)
        self.l_class.setObjectName(u"l_class")
        font = QFont()
        font.setBold(True)
        self.l_class.setFont(font)

        self.horizontalLayout_5.addWidget(self.l_class)


        self.verticalLayout.addWidget(self.w_name)

        self.gb_export = QGroupBox(wg_Gimp_Export)
        self.gb_export.setObjectName(u"gb_export")
        self.gb_export.setEnabled(True)
        self.verticalLayout_2 = QVBoxLayout(self.gb_export)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.w_context = QWidget(self.gb_export)
        self.w_context.setObjectName(u"w_context")
        self.horizontalLayout_10 = QHBoxLayout(self.w_context)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(9, 0, 9, 0)
        self.label_4 = QLabel(self.w_context)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_10.addWidget(self.label_4)

        self.horizontalSpacer_5 = QSpacerItem(37, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)

        self.l_context = QLabel(self.w_context)
        self.l_context.setObjectName(u"l_context")

        self.horizontalLayout_10.addWidget(self.l_context)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)

        self.b_context = QPushButton(self.w_context)
        self.b_context.setObjectName(u"b_context")

        self.horizontalLayout_10.addWidget(self.b_context)

        self.cb_context = QComboBox(self.w_context)
        self.cb_context.setObjectName(u"cb_context")

        self.horizontalLayout_10.addWidget(self.cb_context)


        self.verticalLayout_2.addWidget(self.w_context)

        self.w_taskname = QWidget(self.gb_export)
        self.w_taskname.setObjectName(u"w_taskname")
        self.horizontalLayout_4 = QHBoxLayout(self.w_taskname)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(9, 0, 9, 0)
        self.l_tasklabel = QLabel(self.w_taskname)
        self.l_tasklabel.setObjectName(u"l_tasklabel")

        self.horizontalLayout_4.addWidget(self.l_tasklabel)

        self.l_taskName = QLabel(self.w_taskname)
        self.l_taskName.setObjectName(u"l_taskName")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l_taskName.sizePolicy().hasHeightForWidth())
        self.l_taskName.setSizePolicy(sizePolicy)
        self.l_taskName.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.l_taskName)

        self.b_changeTask = QPushButton(self.w_taskname)
        self.b_changeTask.setObjectName(u"b_changeTask")
        self.b_changeTask.setEnabled(True)
        self.b_changeTask.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_4.addWidget(self.b_changeTask)


        self.verticalLayout_2.addWidget(self.w_taskname)

        self.w_master = QWidget(self.gb_export)
        self.w_master.setObjectName(u"w_master")
        self.horizontalLayout_20 = QHBoxLayout(self.w_master)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(9, 0, 9, 0)
        self.l_master = QLabel(self.w_master)
        self.l_master.setObjectName(u"l_master")

        self.horizontalLayout_20.addWidget(self.l_master)

        self.horizontalSpacer_29 = QSpacerItem(113, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_29)

        self.cb_master = QComboBox(self.w_master)
        self.cb_master.setObjectName(u"cb_master")
        self.cb_master.setMinimumSize(QSize(124, 0))

        self.horizontalLayout_20.addWidget(self.cb_master)


        self.verticalLayout_2.addWidget(self.w_master)

        self.w_outPath = QWidget(self.gb_export)
        self.w_outPath.setObjectName(u"w_outPath")
        self.horizontalLayout_11 = QHBoxLayout(self.w_outPath)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(9, 0, 9, 0)
        self.l_outPath = QLabel(self.w_outPath)
        self.l_outPath.setObjectName(u"l_outPath")

        self.horizontalLayout_11.addWidget(self.l_outPath)

        self.horizontalSpacer_6 = QSpacerItem(113, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_6)

        self.cb_outPath = QComboBox(self.w_outPath)
        self.cb_outPath.setObjectName(u"cb_outPath")
        self.cb_outPath.setMinimumSize(QSize(124, 0))

        self.horizontalLayout_11.addWidget(self.cb_outPath)


        self.verticalLayout_2.addWidget(self.w_outPath)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.bg_imageSpecs = QGroupBox(self.gb_export)
        self.bg_imageSpecs.setObjectName(u"bg_imageSpecs")
        self.w_imageSpecs = QVBoxLayout(self.bg_imageSpecs)
        self.w_imageSpecs.setObjectName(u"w_imageSpecs")
        self.w_imageSpecs.setContentsMargins(40, -1, 80, -1)
        self.w_imageSpecsLabel = QHBoxLayout()
        self.w_imageSpecsLabel.setObjectName(u"w_imageSpecsLabel")
        self.l_imageSpecs = QLabel(self.bg_imageSpecs)
        self.l_imageSpecs.setObjectName(u"l_imageSpecs")

        self.w_imageSpecsLabel.addWidget(self.l_imageSpecs)


        self.w_imageSpecs.addLayout(self.w_imageSpecsLabel)

        self.w_specs_resolution = QHBoxLayout()
        self.w_specs_resolution.setObjectName(u"w_specs_resolution")
        self.w_specs_resolution.setContentsMargins(30, -1, 30, -1)
        self.l_spec_rezLabel = QLabel(self.bg_imageSpecs)
        self.l_spec_rezLabel.setObjectName(u"l_spec_rezLabel")

        self.w_specs_resolution.addWidget(self.l_spec_rezLabel)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.w_specs_resolution.addItem(self.horizontalSpacer_13)

        self.l_specs_Xrez = QLabel(self.bg_imageSpecs)
        self.l_specs_Xrez.setObjectName(u"l_specs_Xrez")

        self.w_specs_resolution.addWidget(self.l_specs_Xrez)

        self.l_specs_rezXtext = QLabel(self.bg_imageSpecs)
        self.l_specs_rezXtext.setObjectName(u"l_specs_rezXtext")

        self.w_specs_resolution.addWidget(self.l_specs_rezXtext)

        self.l_specs_Yrez = QLabel(self.bg_imageSpecs)
        self.l_specs_Yrez.setObjectName(u"l_specs_Yrez")

        self.w_specs_resolution.addWidget(self.l_specs_Yrez)


        self.w_imageSpecs.addLayout(self.w_specs_resolution)

        self.w_specs_ColorMode = QHBoxLayout()
        self.w_specs_ColorMode.setObjectName(u"w_specs_ColorMode")
        self.w_specs_ColorMode.setContentsMargins(30, -1, 30, -1)
        self.l_specs_ColorMode_text = QLabel(self.bg_imageSpecs)
        self.l_specs_ColorMode_text.setObjectName(u"l_specs_ColorMode_text")

        self.w_specs_ColorMode.addWidget(self.l_specs_ColorMode_text)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.w_specs_ColorMode.addItem(self.horizontalSpacer_14)

        self.l_specs_ColorMode = QLabel(self.bg_imageSpecs)
        self.l_specs_ColorMode.setObjectName(u"l_specs_ColorMode")

        self.w_specs_ColorMode.addWidget(self.l_specs_ColorMode)


        self.w_imageSpecs.addLayout(self.w_specs_ColorMode)

        self.w_specs_BitDepth = QHBoxLayout()
        self.w_specs_BitDepth.setObjectName(u"w_specs_BitDepth")
        self.w_specs_BitDepth.setContentsMargins(30, -1, 30, -1)
        self.l_specs_BitDepth_text = QLabel(self.bg_imageSpecs)
        self.l_specs_BitDepth_text.setObjectName(u"l_specs_BitDepth_text")

        self.w_specs_BitDepth.addWidget(self.l_specs_BitDepth_text)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.w_specs_BitDepth.addItem(self.horizontalSpacer_17)

        self.l_specs_BitDepth = QLabel(self.bg_imageSpecs)
        self.l_specs_BitDepth.setObjectName(u"l_specs_BitDepth")

        self.w_specs_BitDepth.addWidget(self.l_specs_BitDepth)


        self.w_imageSpecs.addLayout(self.w_specs_BitDepth)

        self.w_specs_Gamma = QHBoxLayout()
        self.w_specs_Gamma.setObjectName(u"w_specs_Gamma")
        self.w_specs_Gamma.setContentsMargins(30, -1, 30, -1)
        self.l_specs_Gamma_text = QLabel(self.bg_imageSpecs)
        self.l_specs_Gamma_text.setObjectName(u"l_specs_Gamma_text")

        self.w_specs_Gamma.addWidget(self.l_specs_Gamma_text)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.w_specs_Gamma.addItem(self.horizontalSpacer_20)

        self.l_specs_Gamma = QLabel(self.bg_imageSpecs)
        self.l_specs_Gamma.setObjectName(u"l_specs_Gamma")

        self.w_specs_Gamma.addWidget(self.l_specs_Gamma)


        self.w_imageSpecs.addLayout(self.w_specs_Gamma)

        self.w_specs_Alpha = QHBoxLayout()
        self.w_specs_Alpha.setObjectName(u"w_specs_Alpha")
        self.w_specs_Alpha.setContentsMargins(30, -1, 30, -1)
        self.l_specs_Alpha_text = QLabel(self.bg_imageSpecs)
        self.l_specs_Alpha_text.setObjectName(u"l_specs_Alpha_text")

        self.w_specs_Alpha.addWidget(self.l_specs_Alpha_text)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.w_specs_Alpha.addItem(self.horizontalSpacer_19)

        self.l_specs_Alpha = QLabel(self.bg_imageSpecs)
        self.l_specs_Alpha.setObjectName(u"l_specs_Alpha")

        self.w_specs_Alpha.addWidget(self.l_specs_Alpha)


        self.w_imageSpecs.addLayout(self.w_specs_Alpha)


        self.verticalLayout_2.addWidget(self.bg_imageSpecs)

        self.verticalSpacer_4 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.w_scale = QWidget(self.gb_export)
        self.w_scale.setObjectName(u"w_scale")
        self.horizontalLayout_14 = QHBoxLayout(self.w_scale)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(9, 0, 9, 0)
        self.l_scale = QLabel(self.w_scale)
        self.l_scale.setObjectName(u"l_scale")

        self.horizontalLayout_14.addWidget(self.l_scale)

        self.horizontalSpacer_12 = QSpacerItem(113, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_12)

        self.cb_scale = QComboBox(self.w_scale)
        self.cb_scale.setObjectName(u"cb_scale")
        self.cb_scale.setMinimumSize(QSize(124, 0))

        self.horizontalLayout_14.addWidget(self.cb_scale)


        self.verticalLayout_2.addWidget(self.w_scale)

        self.w_outGamma = QWidget(self.gb_export)
        self.w_outGamma.setObjectName(u"w_outGamma")
        self.horizontalLayout_24 = QHBoxLayout(self.w_outGamma)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(9, 0, 9, 0)
        self.l_outGamma = QLabel(self.w_outGamma)
        self.l_outGamma.setObjectName(u"l_outGamma")

        self.horizontalLayout_24.addWidget(self.l_outGamma)

        self.horizontalSpacer_41 = QSpacerItem(113, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_41)

        self.cb_outGamma = QComboBox(self.w_outGamma)
        self.cb_outGamma.setObjectName(u"cb_outGamma")
        self.cb_outGamma.setMinimumSize(QSize(124, 0))

        self.horizontalLayout_24.addWidget(self.cb_outGamma)


        self.verticalLayout_2.addWidget(self.w_outGamma)

        self.w_outType = QWidget(self.gb_export)
        self.w_outType.setObjectName(u"w_outType")
        self.horizontalLayout_9 = QHBoxLayout(self.w_outType)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(9, 0, 9, 0)
        self.l_outType = QLabel(self.w_outType)
        self.l_outType.setObjectName(u"l_outType")

        self.horizontalLayout_9.addWidget(self.l_outType)

        self.horizontalSpacer_3 = QSpacerItem(113, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)

        self.cb_format = QComboBox(self.w_outType)
        self.cb_format.setObjectName(u"cb_format")
        self.cb_format.setMinimumSize(QSize(124, 0))

        self.horizontalLayout_9.addWidget(self.cb_format)


        self.verticalLayout_2.addWidget(self.w_outType)

        self.gb_imageOptions = QGroupBox(self.gb_export)
        self.gb_imageOptions.setObjectName(u"gb_imageOptions")
        self.w_imageOptions = QHBoxLayout(self.gb_imageOptions)
        self.w_imageOptions.setObjectName(u"w_imageOptions")
        self.w_imageOptions.setContentsMargins(30, 5, 30, 0)
        self.l_colorMode = QLabel(self.gb_imageOptions)
        self.l_colorMode.setObjectName(u"l_colorMode")

        self.w_imageOptions.addWidget(self.l_colorMode)

        self.cb_colorMode = QComboBox(self.gb_imageOptions)
        self.cb_colorMode.setObjectName(u"cb_colorMode")
        self.cb_colorMode.setMinimumSize(QSize(80, 0))

        self.w_imageOptions.addWidget(self.cb_colorMode)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.w_imageOptions.addItem(self.horizontalSpacer_9)

        self.l_bitDepth = QLabel(self.gb_imageOptions)
        self.l_bitDepth.setObjectName(u"l_bitDepth")

        self.w_imageOptions.addWidget(self.l_bitDepth)

        self.cb_bitDepth = QComboBox(self.gb_imageOptions)
        self.cb_bitDepth.setObjectName(u"cb_bitDepth")
        self.cb_bitDepth.setMinimumSize(QSize(80, 0))

        self.w_imageOptions.addWidget(self.cb_bitDepth)


        self.verticalLayout_2.addWidget(self.gb_imageOptions)

        self.gb_alphaFill = QGroupBox(self.gb_export)
        self.gb_alphaFill.setObjectName(u"gb_alphaFill")
        self.gb_alphaFill.setEnabled(True)
        self.gb_jpg_options_2 = QVBoxLayout(self.gb_alphaFill)
        self.gb_jpg_options_2.setObjectName(u"gb_jpg_options_2")
        self.gb_jpg_options_2.setContentsMargins(-1, 5, -1, 0)
        self.w_alphaFill = QHBoxLayout()
        self.w_alphaFill.setObjectName(u"w_alphaFill")
        self.w_alphaFill.setContentsMargins(30, -1, 30, -1)
        self.l_alphaFill = QLabel(self.gb_alphaFill)
        self.l_alphaFill.setObjectName(u"l_alphaFill")

        self.w_alphaFill.addWidget(self.l_alphaFill)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.w_alphaFill.addItem(self.horizontalSpacer_11)

        self.cb_alphaFill = QComboBox(self.gb_alphaFill)
        self.cb_alphaFill.setObjectName(u"cb_alphaFill")
        self.cb_alphaFill.setMinimumSize(QSize(124, 0))

        self.w_alphaFill.addWidget(self.cb_alphaFill)


        self.gb_jpg_options_2.addLayout(self.w_alphaFill)


        self.verticalLayout_2.addWidget(self.gb_alphaFill)

        self.gb_jpgOptions = QGroupBox(self.gb_export)
        self.gb_jpgOptions.setObjectName(u"gb_jpgOptions")
        self.gb_jpgOptions.setEnabled(True)
        self.gb_jpg_options = QVBoxLayout(self.gb_jpgOptions)
        self.gb_jpg_options.setObjectName(u"gb_jpg_options")
        self.w_jpg_qual = QHBoxLayout()
        self.w_jpg_qual.setObjectName(u"w_jpg_qual")
        self.w_jpg_qual.setContentsMargins(30, -1, 30, -1)
        self.l_jpg_qual = QLabel(self.gb_jpgOptions)
        self.l_jpg_qual.setObjectName(u"l_jpg_qual")

        self.w_jpg_qual.addWidget(self.l_jpg_qual)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.w_jpg_qual.addItem(self.horizontalSpacer_8)

        self.cb_jpg_qual = QComboBox(self.gb_jpgOptions)
        self.cb_jpg_qual.setObjectName(u"cb_jpg_qual")
        self.cb_jpg_qual.setMinimumSize(QSize(124, 0))

        self.w_jpg_qual.addWidget(self.cb_jpg_qual)


        self.gb_jpg_options.addLayout(self.w_jpg_qual)

        self.w_jpg_smooth = QHBoxLayout()
        self.w_jpg_smooth.setObjectName(u"w_jpg_smooth")
        self.w_jpg_smooth.setContentsMargins(30, -1, 30, -1)
        self.l_jpg_smooth = QLabel(self.gb_jpgOptions)
        self.l_jpg_smooth.setObjectName(u"l_jpg_smooth")

        self.w_jpg_smooth.addWidget(self.l_jpg_smooth)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.w_jpg_smooth.addItem(self.horizontalSpacer_2)

        self.cb_jpg_smooth = QComboBox(self.gb_jpgOptions)
        self.cb_jpg_smooth.setObjectName(u"cb_jpg_smooth")
        self.cb_jpg_smooth.setMinimumSize(QSize(124, 0))

        self.w_jpg_smooth.addWidget(self.cb_jpg_smooth)


        self.gb_jpg_options.addLayout(self.w_jpg_smooth)

        self.w_jpg_subSample = QHBoxLayout()
        self.w_jpg_subSample.setObjectName(u"w_jpg_subSample")
        self.w_jpg_subSample.setContentsMargins(30, -1, 30, -1)
        self.l_jpg_subSample = QLabel(self.gb_jpgOptions)
        self.l_jpg_subSample.setObjectName(u"l_jpg_subSample")

        self.w_jpg_subSample.addWidget(self.l_jpg_subSample)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.w_jpg_subSample.addItem(self.horizontalSpacer_10)

        self.cb_jpg_subSample = QComboBox(self.gb_jpgOptions)
        self.cb_jpg_subSample.setObjectName(u"cb_jpg_subSample")
        self.cb_jpg_subSample.setMinimumSize(QSize(124, 0))

        self.w_jpg_subSample.addWidget(self.cb_jpg_subSample)


        self.gb_jpg_options.addLayout(self.w_jpg_subSample)

        self.w_jpg_options = QHBoxLayout()
        self.w_jpg_options.setObjectName(u"w_jpg_options")
        self.w_jpg_options.setContentsMargins(20, -1, 30, -1)
        self.chb_jpg_optimize = QCheckBox(self.gb_jpgOptions)
        self.chb_jpg_optimize.setObjectName(u"chb_jpg_optimize")
        self.chb_jpg_optimize.setLayoutDirection(Qt.RightToLeft)

        self.w_jpg_options.addWidget(self.chb_jpg_optimize)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.w_jpg_options.addItem(self.horizontalSpacer_7)

        self.chb_jpg_progressive = QCheckBox(self.gb_jpgOptions)
        self.chb_jpg_progressive.setObjectName(u"chb_jpg_progressive")
        self.chb_jpg_progressive.setLayoutDirection(Qt.RightToLeft)

        self.w_jpg_options.addWidget(self.chb_jpg_progressive)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.w_jpg_options.addItem(self.horizontalSpacer_4)

        self.chb_jpg_baseline = QCheckBox(self.gb_jpgOptions)
        self.chb_jpg_baseline.setObjectName(u"chb_jpg_baseline")
        self.chb_jpg_baseline.setLayoutDirection(Qt.RightToLeft)

        self.w_jpg_options.addWidget(self.chb_jpg_baseline)


        self.gb_jpg_options.addLayout(self.w_jpg_options)


        self.verticalLayout_2.addWidget(self.gb_jpgOptions)

        self.gb_pngOptions = QGroupBox(self.gb_export)
        self.gb_pngOptions.setObjectName(u"gb_pngOptions")
        self.gb_pngOptions.setEnabled(True)
        self.gb_jpg_options_5 = QVBoxLayout(self.gb_pngOptions)
        self.gb_jpg_options_5.setObjectName(u"gb_jpg_options_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, 40, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_24)

        self.l_png_compress = QLabel(self.gb_pngOptions)
        self.l_png_compress.setObjectName(u"l_png_compress")
        self.l_png_compress.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_2.addWidget(self.l_png_compress)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.chb_png_alphaColor = QCheckBox(self.gb_pngOptions)
        self.chb_png_alphaColor.setObjectName(u"chb_png_alphaColor")
        self.chb_png_alphaColor.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_6.addWidget(self.chb_png_alphaColor)

        self.chb_png_bgColor = QCheckBox(self.gb_pngOptions)
        self.chb_png_bgColor.setObjectName(u"chb_png_bgColor")
        self.chb_png_bgColor.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_6.addWidget(self.chb_png_bgColor)

        self.chb_png_gamma = QCheckBox(self.gb_pngOptions)
        self.chb_png_gamma.setObjectName(u"chb_png_gamma")
        self.chb_png_gamma.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_6.addWidget(self.chb_png_gamma)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, 40, -1)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_16)

        self.cb_png_compress = QComboBox(self.gb_pngOptions)
        self.cb_png_compress.setObjectName(u"cb_png_compress")
        self.cb_png_compress.setMinimumSize(QSize(124, 0))

        self.horizontalLayout_3.addWidget(self.cb_png_compress)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.chb_png_interlaced = QCheckBox(self.gb_pngOptions)
        self.chb_png_interlaced.setObjectName(u"chb_png_interlaced")
        self.chb_png_interlaced.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_5.addWidget(self.chb_png_interlaced)

        self.chb_png_rez = QCheckBox(self.gb_pngOptions)
        self.chb_png_rez.setObjectName(u"chb_png_rez")
        self.chb_png_rez.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_5.addWidget(self.chb_png_rez)

        self.chb_png_layerOffset = QCheckBox(self.gb_pngOptions)
        self.chb_png_layerOffset.setObjectName(u"chb_png_layerOffset")
        self.chb_png_layerOffset.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_5.addWidget(self.chb_png_layerOffset)


        self.horizontalLayout.addLayout(self.verticalLayout_5)


        self.gb_jpg_options_5.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.gb_pngOptions)

        self.gb_tiffOptions = QGroupBox(self.gb_export)
        self.gb_tiffOptions.setObjectName(u"gb_tiffOptions")
        self.gb_tiffOptions.setEnabled(True)
        self.gb_jpg_options_6 = QVBoxLayout(self.gb_tiffOptions)
        self.gb_jpg_options_6.setObjectName(u"gb_jpg_options_6")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, 40, -1)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_25)

        self.l_tiff_compress = QLabel(self.gb_tiffOptions)
        self.l_tiff_compress.setObjectName(u"l_tiff_compress")
        self.l_tiff_compress.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_7.addWidget(self.l_tiff_compress)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.l_tiff_useBig = QLabel(self.gb_tiffOptions)
        self.l_tiff_useBig.setObjectName(u"l_tiff_useBig")
        self.l_tiff_useBig.setLayoutDirection(Qt.RightToLeft)
        self.l_tiff_useBig.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_7.addWidget(self.l_tiff_useBig)

        self.l_tiff_alphaColor = QLabel(self.gb_tiffOptions)
        self.l_tiff_alphaColor.setObjectName(u"l_tiff_alphaColor")
        self.l_tiff_alphaColor.setLayoutDirection(Qt.RightToLeft)
        self.l_tiff_alphaColor.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_7.addWidget(self.l_tiff_alphaColor)


        self.horizontalLayout_6.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, -1, 40, -1)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_18)

        self.cb_tiff_compress = QComboBox(self.gb_tiffOptions)
        self.cb_tiff_compress.setObjectName(u"cb_tiff_compress")
        self.cb_tiff_compress.setMinimumSize(QSize(124, 0))

        self.horizontalLayout_8.addWidget(self.cb_tiff_compress)


        self.verticalLayout_8.addLayout(self.horizontalLayout_8)

        self.chb_tiff_useBig = QCheckBox(self.gb_tiffOptions)
        self.chb_tiff_useBig.setObjectName(u"chb_tiff_useBig")
        self.chb_tiff_useBig.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_8.addWidget(self.chb_tiff_useBig)

        self.chb_tiff_alphaColor = QCheckBox(self.gb_tiffOptions)
        self.chb_tiff_alphaColor.setObjectName(u"chb_tiff_alphaColor")
        self.chb_tiff_alphaColor.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_8.addWidget(self.chb_tiff_alphaColor)


        self.horizontalLayout_6.addLayout(self.verticalLayout_8)


        self.gb_jpg_options_6.addLayout(self.horizontalLayout_6)


        self.verticalLayout_2.addWidget(self.gb_tiffOptions)

        self.gb_pdfOptions = QGroupBox(self.gb_export)
        self.gb_pdfOptions.setObjectName(u"gb_pdfOptions")
        self.gb_pdfOptions.setEnabled(True)
        self.gb_jpg_options_7 = QVBoxLayout(self.gb_pdfOptions)
        self.gb_jpg_options_7.setObjectName(u"gb_jpg_options_7")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, -1, 40, -1)
        self.chb_pdf_omitHidden = QCheckBox(self.gb_pdfOptions)
        self.chb_pdf_omitHidden.setObjectName(u"chb_pdf_omitHidden")
        self.chb_pdf_omitHidden.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_9.addWidget(self.chb_pdf_omitHidden)

        self.chb_pdf_applyLayers = QCheckBox(self.gb_pdfOptions)
        self.chb_pdf_applyLayers.setObjectName(u"chb_pdf_applyLayers")
        self.chb_pdf_applyLayers.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_9.addWidget(self.chb_pdf_applyLayers)


        self.horizontalLayout_15.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, -1, 40, -1)
        self.chb_pdf_convertToVector = QCheckBox(self.gb_pdfOptions)
        self.chb_pdf_convertToVector.setObjectName(u"chb_pdf_convertToVector")
        self.chb_pdf_convertToVector.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_10.addWidget(self.chb_pdf_convertToVector)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer)


        self.horizontalLayout_15.addLayout(self.verticalLayout_10)


        self.gb_jpg_options_7.addLayout(self.horizontalLayout_15)


        self.verticalLayout_2.addWidget(self.gb_pdfOptions)

        self.gb_psdOptions = QGroupBox(self.gb_export)
        self.gb_psdOptions.setObjectName(u"gb_psdOptions")
        self.gb_psdOptions.setEnabled(True)
        self.gb_psdOptions.setLayoutDirection(Qt.LeftToRight)
        self.gb_jpg_options_8 = QVBoxLayout(self.gb_psdOptions)
        self.gb_jpg_options_8.setObjectName(u"gb_jpg_options_8")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_15)

        self.chb_psd_saveAsScene = QCheckBox(self.gb_psdOptions)
        self.chb_psd_saveAsScene.setObjectName(u"chb_psd_saveAsScene")
        self.chb_psd_saveAsScene.setLayoutDirection(Qt.RightToLeft)

        self.horizontalLayout_16.addWidget(self.chb_psd_saveAsScene)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_21)


        self.gb_jpg_options_8.addLayout(self.horizontalLayout_16)


        self.verticalLayout_2.addWidget(self.gb_psdOptions)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.gb_previous = QGroupBox(self.gb_export)
        self.gb_previous.setObjectName(u"gb_previous")
        self.horizontalLayout_13 = QHBoxLayout(self.gb_previous)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(9, 9, 9, 9)
        self.scrollArea = QScrollArea(self.gb_previous)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 411, 69))
        self.horizontalLayout_12 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.l_pathLast = QLabel(self.scrollAreaWidgetContents)
        self.l_pathLast.setObjectName(u"l_pathLast")

        self.horizontalLayout_12.addWidget(self.l_pathLast)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_13.addWidget(self.scrollArea)

        self.b_pathLast = QToolButton(self.gb_previous)
        self.b_pathLast.setObjectName(u"b_pathLast")
        self.b_pathLast.setEnabled(True)
        self.b_pathLast.setArrowType(Qt.DownArrow)

        self.horizontalLayout_13.addWidget(self.b_pathLast)


        self.verticalLayout_2.addWidget(self.gb_previous)


        self.verticalLayout.addWidget(self.gb_export)

        QWidget.setTabOrder(self.e_name, self.b_context)
        QWidget.setTabOrder(self.b_context, self.cb_context)
        QWidget.setTabOrder(self.cb_context, self.cb_outPath)
        QWidget.setTabOrder(self.cb_outPath, self.cb_format)
        QWidget.setTabOrder(self.cb_format, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.b_pathLast)

        self.retranslateUi(wg_Gimp_Export)

        self.cb_colorMode.setCurrentIndex(-1)
        self.cb_bitDepth.setCurrentIndex(-1)
        self.cb_alphaFill.setCurrentIndex(-1)
        self.cb_jpg_qual.setCurrentIndex(-1)
        self.cb_jpg_smooth.setCurrentIndex(-1)
        self.cb_jpg_subSample.setCurrentIndex(-1)
        self.cb_png_compress.setCurrentIndex(-1)
        self.cb_tiff_compress.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(wg_Gimp_Export)
    # setupUi

    def retranslateUi(self, wg_Gimp_Export):
        wg_Gimp_Export.setWindowTitle(QCoreApplication.translate("wg_Gimp_Export", u"Export", None))
        self.l_name.setText(QCoreApplication.translate("wg_Gimp_Export", u"Name:", None))
        self.l_class.setText(QCoreApplication.translate("wg_Gimp_Export", u"Export", None))
        self.gb_export.setTitle(QCoreApplication.translate("wg_Gimp_Export", u"General", None))
        self.label_4.setText(QCoreApplication.translate("wg_Gimp_Export", u"Context:", None))
        self.l_context.setText("")
        self.b_context.setText(QCoreApplication.translate("wg_Gimp_Export", u"Select", None))
        self.l_tasklabel.setText(QCoreApplication.translate("wg_Gimp_Export", u"Identifier:", None))
        self.l_taskName.setText("")
        self.b_changeTask.setText(QCoreApplication.translate("wg_Gimp_Export", u"change", None))
        self.l_master.setText(QCoreApplication.translate("wg_Gimp_Export", u"Master Version:", None))
        self.l_outPath.setText(QCoreApplication.translate("wg_Gimp_Export", u"Location:", None))
        self.l_imageSpecs.setText(QCoreApplication.translate("wg_Gimp_Export", u"Image Info:", None))
        self.l_spec_rezLabel.setText(QCoreApplication.translate("wg_Gimp_Export", u"Resolution:", None))
        self.l_specs_Xrez.setText(QCoreApplication.translate("wg_Gimp_Export", u"XXXX", None))
        self.l_specs_rezXtext.setText(QCoreApplication.translate("wg_Gimp_Export", u"  x  ", None))
        self.l_specs_Yrez.setText(QCoreApplication.translate("wg_Gimp_Export", u"XXXX", None))
        self.l_specs_ColorMode_text.setText(QCoreApplication.translate("wg_Gimp_Export", u"Color Mode:", None))
        self.l_specs_ColorMode.setText(QCoreApplication.translate("wg_Gimp_Export", u"XXXX", None))
        self.l_specs_BitDepth_text.setText(QCoreApplication.translate("wg_Gimp_Export", u"Bit Depth", None))
        self.l_specs_BitDepth.setText(QCoreApplication.translate("wg_Gimp_Export", u"XXXX", None))
        self.l_specs_Gamma_text.setText(QCoreApplication.translate("wg_Gimp_Export", u"Gamma:", None))
        self.l_specs_Gamma.setText(QCoreApplication.translate("wg_Gimp_Export", u"XXXX", None))
        self.l_specs_Alpha_text.setText(QCoreApplication.translate("wg_Gimp_Export", u"Has Alpha:", None))
        self.l_specs_Alpha.setText(QCoreApplication.translate("wg_Gimp_Export", u"XXXX", None))
        self.l_scale.setText(QCoreApplication.translate("wg_Gimp_Export", u"Output Scale:", None))
        self.l_outGamma.setText(QCoreApplication.translate("wg_Gimp_Export", u"Output Gamma:", None))
        self.l_outType.setText(QCoreApplication.translate("wg_Gimp_Export", u"Output Format:", None))
        self.l_colorMode.setText(QCoreApplication.translate("wg_Gimp_Export", u"Color Mode", None))
        self.l_bitDepth.setText(QCoreApplication.translate("wg_Gimp_Export", u"Bit Depth", None))
        self.l_alphaFill.setText(QCoreApplication.translate("wg_Gimp_Export", u"Fill Transparent Pixels with:", None))
        self.l_jpg_qual.setText(QCoreApplication.translate("wg_Gimp_Export", u"Quality", None))
        self.l_jpg_smooth.setText(QCoreApplication.translate("wg_Gimp_Export", u"Smoothing", None))
        self.l_jpg_subSample.setText(QCoreApplication.translate("wg_Gimp_Export", u"Sub Sample", None))
        self.chb_jpg_optimize.setText(QCoreApplication.translate("wg_Gimp_Export", u"Optimize", None))
        self.chb_jpg_progressive.setText(QCoreApplication.translate("wg_Gimp_Export", u"Progressive", None))
        self.chb_jpg_baseline.setText(QCoreApplication.translate("wg_Gimp_Export", u"Baseline", None))
        self.l_png_compress.setText(QCoreApplication.translate("wg_Gimp_Export", u"Compression", None))
        self.chb_png_alphaColor.setText(QCoreApplication.translate("wg_Gimp_Export", u"PreMult Alpha", None))
        self.chb_png_bgColor.setText(QCoreApplication.translate("wg_Gimp_Export", u"Save BG Color", None))
        self.chb_png_gamma.setText(QCoreApplication.translate("wg_Gimp_Export", u"Save Gamma     ", None))
        self.chb_png_interlaced.setText(QCoreApplication.translate("wg_Gimp_Export", u"Interlaced          ", None))
        self.chb_png_rez.setText(QCoreApplication.translate("wg_Gimp_Export", u"Save Resolution", None))
        self.chb_png_layerOffset.setText(QCoreApplication.translate("wg_Gimp_Export", u"Save Layer Offset", None))
        self.l_tiff_compress.setText(QCoreApplication.translate("wg_Gimp_Export", u"Compression Method", None))
        self.l_tiff_useBig.setText(QCoreApplication.translate("wg_Gimp_Export", u"Save as BIGTIFF", None))
        self.l_tiff_alphaColor.setText(QCoreApplication.translate("wg_Gimp_Export", u"Save Tranparent Color", None))
        self.chb_tiff_useBig.setText("")
        self.chb_tiff_alphaColor.setText("")
        self.chb_pdf_omitHidden.setText(QCoreApplication.translate("wg_Gimp_Export", u"Omit hidden layers", None))
        self.chb_pdf_applyLayers.setText(QCoreApplication.translate("wg_Gimp_Export", u"Apply layers masks", None))
        self.chb_pdf_convertToVector.setText(QCoreApplication.translate("wg_Gimp_Export", u"Bitmaps to Vector", None))
        self.chb_psd_saveAsScene.setText(QCoreApplication.translate("wg_Gimp_Export", u"Save .psd as Scenefile        ", None))
        self.gb_previous.setTitle(QCoreApplication.translate("wg_Gimp_Export", u"Last export", None))
        self.l_pathLast.setText(QCoreApplication.translate("wg_Gimp_Export", u"None", None))
        self.b_pathLast.setText(QCoreApplication.translate("wg_Gimp_Export", u"...", None))
    # retranslateUi

