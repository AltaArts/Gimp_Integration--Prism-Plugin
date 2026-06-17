# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Gimp_ImportImage.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

class Ui_wg_Gimp_ImportImage(object):
    def setupUi(self, wg_Gimp_ImportImage):
        if not wg_Gimp_ImportImage.objectName():
            wg_Gimp_ImportImage.setObjectName(u"wg_Gimp_ImportImage")
        wg_Gimp_ImportImage.resize(441, 789)
        self.verticalLayout = QVBoxLayout(wg_Gimp_ImportImage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.l_class = QLabel(wg_Gimp_ImportImage)
        self.l_class.setObjectName(u"l_class")
        font = QFont()
        font.setBold(True)
        self.l_class.setFont(font)

        self.horizontalLayout.addWidget(self.l_class)

        self.e_name = QLineEdit(wg_Gimp_ImportImage)
        self.e_name.setObjectName(u"e_name")
        self.e_name.setMinimumSize(QSize(0, 0))
        self.e_name.setMaximumSize(QSize(9999, 16777215))
        self.e_name.setReadOnly(True)

        self.horizontalLayout.addWidget(self.e_name)

        self.l_name = QLabel(wg_Gimp_ImportImage)
        self.l_name.setObjectName(u"l_name")

        self.horizontalLayout.addWidget(self.l_name)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gb_import = QGroupBox(wg_Gimp_ImportImage)
        self.gb_import.setObjectName(u"gb_import")
        self.verticalLayout_2 = QVBoxLayout(self.gb_import)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.gb_version = QGroupBox(self.gb_import)
        self.gb_version.setObjectName(u"gb_version")
        self.verticalLayout_3 = QVBoxLayout(self.gb_version)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lo_versions = QWidget(self.gb_version)
        self.lo_versions.setObjectName(u"lo_versions")
        self.horizontalLayout_5 = QHBoxLayout(self.lo_versions)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(9, 0, 9, 0)
        self.lo_currVersion = QHBoxLayout()
        self.lo_currVersion.setObjectName(u"lo_currVersion")
        self.l_text_Current = QLabel(self.lo_versions)
        self.l_text_Current.setObjectName(u"l_text_Current")

        self.lo_currVersion.addWidget(self.l_text_Current)

        self.l_curVersion = QLabel(self.lo_versions)
        self.l_curVersion.setObjectName(u"l_curVersion")

        self.lo_currVersion.addWidget(self.l_curVersion)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lo_currVersion.addItem(self.horizontalSpacer)


        self.horizontalLayout_5.addLayout(self.lo_currVersion)

        self.lo_latestVersion = QHBoxLayout()
        self.lo_latestVersion.setObjectName(u"lo_latestVersion")
        self.l_text_Latest = QLabel(self.lo_versions)
        self.l_text_Latest.setObjectName(u"l_text_Latest")

        self.lo_latestVersion.addWidget(self.l_text_Latest)

        self.l_latestVersion = QLabel(self.lo_versions)
        self.l_latestVersion.setObjectName(u"l_latestVersion")

        self.lo_latestVersion.addWidget(self.l_latestVersion)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lo_latestVersion.addItem(self.horizontalSpacer_4)


        self.horizontalLayout_5.addLayout(self.lo_latestVersion)


        self.verticalLayout_3.addWidget(self.lo_versions)

        self.w_importLatest = QWidget(self.gb_version)
        self.w_importLatest.setObjectName(u"w_importLatest")
        self.horizontalLayout_7 = QHBoxLayout(self.w_importLatest)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(9, 0, 9, 0)
        self.b_browse = QPushButton(self.w_importLatest)
        self.b_browse.setObjectName(u"b_browse")
        self.b_browse.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.b_browse.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)

        self.horizontalLayout_7.addWidget(self.b_browse)

        self.b_importLatest = QPushButton(self.w_importLatest)
        self.b_importLatest.setObjectName(u"b_importLatest")
        self.b_importLatest.setMinimumSize(QSize(0, 0))
        self.b_importLatest.setMaximumSize(QSize(99999, 16777215))
        self.b_importLatest.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.horizontalLayout_7.addWidget(self.b_importLatest)


        self.verticalLayout_3.addWidget(self.w_importLatest)

        self.w_autoUpdate = QWidget(self.gb_version)
        self.w_autoUpdate.setObjectName(u"w_autoUpdate")
        self.horizontalLayout_14 = QHBoxLayout(self.w_autoUpdate)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(9, 0, 9, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_2)

        self.l_autoUpdate = QLabel(self.w_autoUpdate)
        self.l_autoUpdate.setObjectName(u"l_autoUpdate")

        self.horizontalLayout_14.addWidget(self.l_autoUpdate)

        self.chb_autoUpdate = QCheckBox(self.w_autoUpdate)
        self.chb_autoUpdate.setObjectName(u"chb_autoUpdate")
        self.chb_autoUpdate.setChecked(False)

        self.horizontalLayout_14.addWidget(self.chb_autoUpdate)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addWidget(self.w_autoUpdate)


        self.verticalLayout_2.addWidget(self.gb_version)

        self.gb_options = QGroupBox(self.gb_import)
        self.gb_options.setObjectName(u"gb_options")
        self.verticalLayout_6 = QVBoxLayout(self.gb_options)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.f_layerName = QWidget(self.gb_options)
        self.f_layerName.setObjectName(u"f_layerName")
        self.horizontalLayout_2 = QHBoxLayout(self.f_layerName)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, -1, 9, -1)
        self.l_layerName = QLabel(self.f_layerName)
        self.l_layerName.setObjectName(u"l_layerName")

        self.horizontalLayout_2.addWidget(self.l_layerName)

        self.e_layerName = QLineEdit(self.f_layerName)
        self.e_layerName.setObjectName(u"e_layerName")

        self.horizontalLayout_2.addWidget(self.e_layerName)


        self.verticalLayout_6.addWidget(self.f_layerName)


        self.verticalLayout_2.addWidget(self.gb_options)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.gb_import)


        self.retranslateUi(wg_Gimp_ImportImage)

        QMetaObject.connectSlotsByName(wg_Gimp_ImportImage)
    # setupUi

    def retranslateUi(self, wg_Gimp_ImportImage):
        wg_Gimp_ImportImage.setWindowTitle(QCoreApplication.translate("wg_Gimp_ImportImage", u"ImportFile", None))
        self.l_class.setText(QCoreApplication.translate("wg_Gimp_ImportImage", u"Import Image", None))
        self.l_name.setText(QCoreApplication.translate("wg_Gimp_ImportImage", u"State name:", None))
        self.gb_import.setTitle("")
        self.gb_version.setTitle(QCoreApplication.translate("wg_Gimp_ImportImage", u"Version", None))
        self.l_text_Current.setText(QCoreApplication.translate("wg_Gimp_ImportImage", u"CURRENT:", None))
        self.l_curVersion.setText(QCoreApplication.translate("wg_Gimp_ImportImage", u"-", None))
        self.l_text_Latest.setText(QCoreApplication.translate("wg_Gimp_ImportImage", u"LATEST:", None))
        self.l_latestVersion.setText(QCoreApplication.translate("wg_Gimp_ImportImage", u"-", None))
        self.b_browse.setText(QCoreApplication.translate("wg_Gimp_ImportImage", u"Select Version", None))
        self.b_importLatest.setText(QCoreApplication.translate("wg_Gimp_ImportImage", u"Import latest Version", None))
        self.l_autoUpdate.setText(QCoreApplication.translate("wg_Gimp_ImportImage", u"Auto load latest version:           ", None))
        self.chb_autoUpdate.setText("")
        self.gb_options.setTitle(QCoreApplication.translate("wg_Gimp_ImportImage", u"Options", None))
        self.l_layerName.setText(QCoreApplication.translate("wg_Gimp_ImportImage", u"Layer Name:  ", None))
    # retranslateUi

