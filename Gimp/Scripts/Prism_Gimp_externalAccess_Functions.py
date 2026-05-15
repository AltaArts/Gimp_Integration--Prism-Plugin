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
import logging
from typing import TYPE_CHECKING

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *

from PrismUtils.Decorators import err_catcher_plugin as err_catcher


if TYPE_CHECKING:
    from PrismCore import PrismCore
    from PrismSettings import UserSettings

logger = logging.getLogger(__name__)


class Prism_Gimp_externalAccess_Functions(object):
    def __init__(self, core:"PrismCore", plugin):
        self.core = core
        self.plugin = plugin

        self.core.registerCallback("userSettings_saveSettings", self.userSettings_saveSettings, plugin=self.plugin)
        self.core.registerCallback("userSettings_loadSettings", self.userSettings_loadSettings, plugin=self.plugin)
        self.core.registerCallback("getPresetScenes", self.getPresetScenes, plugin=self.plugin)

        ssheetPath = os.path.join(self.pluginDirectory, "UserInterfaces", "GimpStyleSheet")
        self.core.registerStyleSheet(ssheetPath)


    @err_catcher(name=__name__)
    def userSettings_loadUI(self, origin:"UserSettings", tab:QWidget):
        #   Options Groupbox
        origin.gb_gimpOptions = QGroupBox("Options")
        origin.gb_gimpOptions.setCheckable(False)
        origin.gb_gimpOptions.setChecked(True)

        #   Grid Layout
        lo_gimpOptions = QGridLayout()
        lo_gimpOptions.setContentsMargins(30, 10, 30, 10)
        lo_gimpOptions.setHorizontalSpacing(20)
        origin.gb_gimpOptions.setLayout(lo_gimpOptions)

        #   Bridge Out Port (Gimp -> Prism)
        l_port_out = QLabel("Bridge Port Out (Gimp -> Prism):")
        l_port_out.setFixedWidth(280)
        origin.sp_port_out = QSpinBox()
        origin.sp_port_out.setFixedWidth(150)
        origin.sp_port_out.setRange(49152, 65535)
        origin.sp_port_out.setValue(50600)
        lo_gimpOptions.addWidget(l_port_out, 0, 0, alignment=Qt.AlignLeft)
        lo_gimpOptions.addWidget(origin.sp_port_out, 0, 1, alignment=Qt.AlignLeft)

        #   Add Options to DCC Tab
        tab.layout().addWidget(origin.gb_gimpOptions)

        #   Bridge Out In (Prism -> Gimp)
        l_port_in = QLabel("Bridge Port In (Prism -> Gimp):")
        l_port_in.setFixedWidth(280)
        origin.sp_port_in = QSpinBox()
        origin.sp_port_in.setFixedWidth(150)
        origin.sp_port_in.setRange(49152, 65535)
        origin.sp_port_in.setValue(50601)
        lo_gimpOptions.addWidget(l_port_in, 1, 0, alignment=Qt.AlignLeft)
        lo_gimpOptions.addWidget(origin.sp_port_in, 1, 1, alignment=Qt.AlignLeft)

        #   Add Options to DCC Tab
        tab.layout().addWidget(origin.gb_gimpOptions)

        tip = ("The outbound port used when Gimp sends commands\n"
             "to Prism Core.")
        l_port_out.setToolTip(tip)
        origin.sp_port_out.setToolTip(tip)

        tip = ("The inbound port used when Prism sends commands\n"
             "to Gimp.")
        l_port_in.setToolTip(tip)
        origin.sp_port_in.setToolTip(tip)


    @err_catcher(name=__name__)
    def userSettings_saveSettings(self, origin:"UserSettings", settings:dict):
        if "Gimp" not in settings:
            settings["Gimp"] = {}

        if hasattr(origin, "sp_port_out"):
            settings["Gimp"]["bridgePort_out"] = origin.sp_port_out.value()

        if hasattr(origin, "sp_port_in"):
            settings["Gimp"]["bridgePort_in"] = origin.sp_port_in.value()


    @err_catcher(name=__name__)
    def userSettings_loadSettings(self, origin:"UserSettings", settings:dict):
        #   Get Gimp Settings from User Settings
        if "Gimp" in settings:
            sData = settings["Gimp"]

        #   Get Defaults from Variables
        else:
            sData = self.gimpDefaults

        if "bridgePort_out" in sData:
            origin.sp_port_out.setValue(sData["bridgePort_out"])

        if "bridgePort_in" in sData:
            origin.sp_port_in.setValue(sData["bridgePort_in"])


    @err_catcher(name=__name__)
    def getPresetScenes(self, presetScenes:list):
        if os.getenv("PRISM_SHOW_DEFAULT_SCENEFILE_PRESETS", "1") != "1":
            return

        presetDir = os.path.join(self.pluginDirectory, "Presets")
        scenes = self.core.entities.getPresetScenesFromFolder(presetDir)
        presetScenes += scenes
