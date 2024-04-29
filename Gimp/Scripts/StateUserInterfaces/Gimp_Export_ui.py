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
        wg_Gimp_Export.resize(482, 718)
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

        self.w_range = QWidget(self.gb_export)
        self.w_range.setObjectName(u"w_range")
        self.horizontalLayout_6 = QHBoxLayout(self.w_range)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(9, 0, 9, 0)

        self.verticalLayout_2.addWidget(self.w_range)

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

        self.w_imageOptions = QHBoxLayout()
        self.w_imageOptions.setObjectName(u"w_imageOptions")
        self.w_imageOptions.setContentsMargins(30, -1, 30, -1)
        self.l_colorMode = QLabel(self.gb_export)
        self.l_colorMode.setObjectName(u"l_colorMode")

        self.w_imageOptions.addWidget(self.l_colorMode)

        self.cb_colorMode = QComboBox(self.gb_export)
        self.cb_colorMode.setObjectName(u"cb_colorMode")
        self.cb_colorMode.setMinimumSize(QSize(80, 0))

        self.w_imageOptions.addWidget(self.cb_colorMode)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.w_imageOptions.addItem(self.horizontalSpacer_9)

        self.l_bitDepth = QLabel(self.gb_export)
        self.l_bitDepth.setObjectName(u"l_bitDepth")

        self.w_imageOptions.addWidget(self.l_bitDepth)

        self.cb_bitDepth = QComboBox(self.gb_export)
        self.cb_bitDepth.setObjectName(u"cb_bitDepth")
        self.cb_bitDepth.setMinimumSize(QSize(80, 0))

        self.w_imageOptions.addWidget(self.cb_bitDepth)


        self.verticalLayout_2.addLayout(self.w_imageOptions)

        self.gb_alphaFill = QGroupBox(self.gb_export)
        self.gb_alphaFill.setObjectName(u"gb_alphaFill")
        self.gb_alphaFill.setEnabled(True)
        self.gb_jpg_options_2 = QVBoxLayout(self.gb_alphaFill)
        self.gb_jpg_options_2.setObjectName(u"gb_jpg_options_2")
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
        self.w_jpg_options.setContentsMargins(20, -1, 20, -1)
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

        self.chb_jpg_arithCode = QCheckBox(self.gb_jpgOptions)
        self.chb_jpg_arithCode.setObjectName(u"chb_jpg_arithCode")
        self.chb_jpg_arithCode.setLayoutDirection(Qt.RightToLeft)

        self.w_jpg_options.addWidget(self.chb_jpg_arithCode)


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

        self.chb_png_interlaced = QCheckBox(self.gb_pngOptions)
        self.chb_png_interlaced.setObjectName(u"chb_png_interlaced")
        self.chb_png_interlaced.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_6.addWidget(self.chb_png_interlaced)

        self.chb_png_gamma = QCheckBox(self.gb_pngOptions)
        self.chb_png_gamma.setObjectName(u"chb_png_gamma")
        self.chb_png_gamma.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_6.addWidget(self.chb_png_gamma)

        self.chb_png_rez = QCheckBox(self.gb_pngOptions)
        self.chb_png_rez.setObjectName(u"chb_png_rez")
        self.chb_png_rez.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_6.addWidget(self.chb_png_rez)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, 60, -1)
        self.cb_png_compress = QComboBox(self.gb_pngOptions)
        self.cb_png_compress.setObjectName(u"cb_png_compress")
        self.cb_png_compress.setMinimumSize(QSize(124, 0))

        self.verticalLayout_5.addWidget(self.cb_png_compress)

        self.chb_png_bgColor = QCheckBox(self.gb_pngOptions)
        self.chb_png_bgColor.setObjectName(u"chb_png_bgColor")
        self.chb_png_bgColor.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_5.addWidget(self.chb_png_bgColor)

        self.chb_png_layerOffset = QCheckBox(self.gb_pngOptions)
        self.chb_png_layerOffset.setObjectName(u"chb_png_layerOffset")
        self.chb_png_layerOffset.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_5.addWidget(self.chb_png_layerOffset)

        self.chb_png_alphaColor = QCheckBox(self.gb_pngOptions)
        self.chb_png_alphaColor.setObjectName(u"chb_png_alphaColor")
        self.chb_png_alphaColor.setLayoutDirection(Qt.RightToLeft)

        self.verticalLayout_5.addWidget(self.chb_png_alphaColor)


        self.horizontalLayout.addLayout(self.verticalLayout_5)


        self.gb_jpg_options_5.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.gb_pngOptions)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.w_comment = QHBoxLayout()
        self.w_comment.setObjectName(u"w_comment")
        self.l_comment = QLabel(self.gb_export)
        self.l_comment.setObjectName(u"l_comment")

        self.w_comment.addWidget(self.l_comment)

        self.e_comment = QLineEdit(self.gb_export)
        self.e_comment.setObjectName(u"e_comment")

        self.w_comment.addWidget(self.e_comment)


        self.verticalLayout_2.addLayout(self.w_comment)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

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
        self.l_tasklabel.setText(QCoreApplication.translate("wg_Gimp_Export", u"Productname:", None))
        self.l_taskName.setText("")
        self.b_changeTask.setText(QCoreApplication.translate("wg_Gimp_Export", u"change", None))
        self.l_master.setText(QCoreApplication.translate("wg_Gimp_Export", u"Master Version:", None))
        self.l_outPath.setText(QCoreApplication.translate("wg_Gimp_Export", u"Location:", None))
        self.l_outType.setText(QCoreApplication.translate("wg_Gimp_Export", u"Outputtype:", None))
        self.l_colorMode.setText(QCoreApplication.translate("wg_Gimp_Export", u"Color Mode", None))
        self.l_bitDepth.setText(QCoreApplication.translate("wg_Gimp_Export", u"Bit Depth", None))
        self.l_alphaFill.setText(QCoreApplication.translate("wg_Gimp_Export", u"Fill Transparent Pixels with:", None))
        self.l_jpg_qual.setText(QCoreApplication.translate("wg_Gimp_Export", u"Quality", None))
        self.l_jpg_smooth.setText(QCoreApplication.translate("wg_Gimp_Export", u"Smoothing", None))
        self.l_jpg_subSample.setText(QCoreApplication.translate("wg_Gimp_Export", u"Sub Sample", None))
        self.chb_jpg_optimize.setText(QCoreApplication.translate("wg_Gimp_Export", u"Optimize", None))
        self.chb_jpg_progressive.setText(QCoreApplication.translate("wg_Gimp_Export", u"Progressive", None))
        self.chb_jpg_arithCode.setText(QCoreApplication.translate("wg_Gimp_Export", u"Arithmetic Coding", None))
        self.l_png_compress.setText(QCoreApplication.translate("wg_Gimp_Export", u"Compression", None))
        self.chb_png_interlaced.setText(QCoreApplication.translate("wg_Gimp_Export", u"Interlaced          ", None))
        self.chb_png_gamma.setText(QCoreApplication.translate("wg_Gimp_Export", u"Save Gamma     ", None))
        self.chb_png_rez.setText(QCoreApplication.translate("wg_Gimp_Export", u"Save Resolution", None))
        self.chb_png_bgColor.setText(QCoreApplication.translate("wg_Gimp_Export", u"Save Background Color", None))
        self.chb_png_layerOffset.setText(QCoreApplication.translate("wg_Gimp_Export", u"Save Layer Offset", None))
        self.chb_png_alphaColor.setText(QCoreApplication.translate("wg_Gimp_Export", u"Preserve Color in Alpha", None))
        self.l_comment.setText(QCoreApplication.translate("wg_Gimp_Export", u"Comment", None))
        self.gb_previous.setTitle(QCoreApplication.translate("wg_Gimp_Export", u"Last export", None))
        self.l_pathLast.setText(QCoreApplication.translate("wg_Gimp_Export", u"None", None))
        self.b_pathLast.setText(QCoreApplication.translate("wg_Gimp_Export", u"...", None))
    # retranslateUi

