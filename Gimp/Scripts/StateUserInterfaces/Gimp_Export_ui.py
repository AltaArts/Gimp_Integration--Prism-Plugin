# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Gimp_ExportlRtvdH.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
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
        wg_Gimp_Export.resize(400, 547)
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
        # font.setWeight(75)
        self.l_class.setFont(font)

        self.horizontalLayout_5.addWidget(self.l_class)


        self.verticalLayout.addWidget(self.w_name)

        self.gb_Gimp_Export = QGroupBox(wg_Gimp_Export)
        self.gb_Gimp_Export.setObjectName(u"gb_Gimp_Export")
        self.verticalLayout_2 = QVBoxLayout(self.gb_Gimp_Export)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.w_context = QWidget(self.gb_Gimp_Export)
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

        self.w_taskname = QWidget(self.gb_Gimp_Export)
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

        self.w_range = QWidget(self.gb_Gimp_Export)
        self.w_range.setObjectName(u"w_range")
        self.horizontalLayout_6 = QHBoxLayout(self.w_range)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(9, 0, 9, 0)

        self.verticalLayout_2.addWidget(self.w_range)

        self.w_master = QWidget(self.gb_Gimp_Export)
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

        self.chb_master = QCheckBox(self.w_master)
        self.chb_master.setObjectName(u"chb_master")
        self.chb_master.setChecked(True)

        self.horizontalLayout_20.addWidget(self.chb_master)


        self.verticalLayout_2.addWidget(self.w_master)

        self.w_outPath = QWidget(self.gb_Gimp_Export)
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

        self.w_outType = QWidget(self.gb_Gimp_Export)
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

        self.cb_outType = QComboBox(self.w_outType)
        self.cb_outType.setObjectName(u"cb_outType")
        self.cb_outType.setMinimumSize(QSize(124, 0))

        self.horizontalLayout_9.addWidget(self.cb_outType)


        self.verticalLayout_2.addWidget(self.w_outType)

        self.w_selectCam = QWidget(self.gb_Gimp_Export)
        self.w_selectCam.setObjectName(u"w_selectCam")
        self.horizontalLayout_2 = QHBoxLayout(self.w_selectCam)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 0, 9, 0)
        self.b_selectCam = QPushButton(self.w_selectCam)
        self.b_selectCam.setObjectName(u"b_selectCam")
        self.b_selectCam.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.b_selectCam)


        self.verticalLayout_2.addWidget(self.w_selectCam)

        self.w_additionalOptions = QWidget(self.gb_Gimp_Export)
        self.w_additionalOptions.setObjectName(u"w_additionalOptions")
        self.horizontalLayout_15 = QHBoxLayout(self.w_additionalOptions)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(9, 0, 9, 0)
        self.l_additionalOptions = QLabel(self.w_additionalOptions)
        self.l_additionalOptions.setObjectName(u"l_additionalOptions")

        self.horizontalLayout_15.addWidget(self.l_additionalOptions)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_11)

        self.chb_additionalOptions = QCheckBox(self.w_additionalOptions)
        self.chb_additionalOptions.setObjectName(u"chb_additionalOptions")
        self.chb_additionalOptions.setChecked(False)

        self.horizontalLayout_15.addWidget(self.chb_additionalOptions)


        self.verticalLayout_2.addWidget(self.w_additionalOptions)

        self.gb_previous = QGroupBox(self.gb_Gimp_Export)
        self.gb_previous.setObjectName(u"gb_previous")
        self.horizontalLayout_13 = QHBoxLayout(self.gb_previous)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(9, 9, 9, 9)
        self.scrollArea = QScrollArea(self.gb_previous)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 329, 256))
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


        self.verticalLayout.addWidget(self.gb_Gimp_Export)

        QWidget.setTabOrder(self.e_name, self.b_context)
        QWidget.setTabOrder(self.b_context, self.cb_context)
        QWidget.setTabOrder(self.cb_context, self.chb_master)
        QWidget.setTabOrder(self.chb_master, self.cb_outPath)
        QWidget.setTabOrder(self.cb_outPath, self.cb_outType)
        QWidget.setTabOrder(self.cb_outType, self.chb_additionalOptions)
        QWidget.setTabOrder(self.chb_additionalOptions, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.b_pathLast)

        self.retranslateUi(wg_Gimp_Export)

        QMetaObject.connectSlotsByName(wg_Gimp_Export)
    # setupUi

    def retranslateUi(self, wg_Gimp_Export):
        wg_Gimp_Export.setWindowTitle(QCoreApplication.translate("wg_Gimp_Export", u"Gimp_Export", None))
        self.l_name.setText(QCoreApplication.translate("wg_Gimp_Export", u"Name:", None))
        self.l_class.setText(QCoreApplication.translate("wg_Gimp_Export", u"Gimp_Export", None))
        self.gb_Gimp_Export.setTitle(QCoreApplication.translate("wg_Gimp_Export", u"General", None))
        self.label_4.setText(QCoreApplication.translate("wg_Gimp_Export", u"Context:", None))
        self.l_context.setText("")
        self.b_context.setText(QCoreApplication.translate("wg_Gimp_Export", u"Select", None))
        self.l_tasklabel.setText(QCoreApplication.translate("wg_Gimp_Export", u"Productname:", None))
        self.l_taskName.setText("")
        self.b_changeTask.setText(QCoreApplication.translate("wg_Gimp_Export", u"change", None))
        self.l_master.setText(QCoreApplication.translate("wg_Gimp_Export", u"Update Master Version:", None))
        self.chb_master.setText("")
        self.l_outPath.setText(QCoreApplication.translate("wg_Gimp_Export", u"Location:", None))
        self.l_outType.setText(QCoreApplication.translate("wg_Gimp_Export", u"Outputtype:", None))
        self.b_selectCam.setText(QCoreApplication.translate("wg_Gimp_Export", u"Select", None))
        self.l_additionalOptions.setText(QCoreApplication.translate("wg_Gimp_Export", u"Show additional options on publish:", None))
        self.chb_additionalOptions.setText("")
        self.gb_previous.setTitle(QCoreApplication.translate("wg_Gimp_Export", u"Last export", None))
        self.l_pathLast.setText(QCoreApplication.translate("wg_Gimp_Export", u"None", None))
        self.b_pathLast.setText(QCoreApplication.translate("wg_Gimp_Export", u"...", None))
    # retranslateUi

