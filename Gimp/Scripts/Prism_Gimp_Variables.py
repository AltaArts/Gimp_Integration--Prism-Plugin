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


class Prism_Gimp_Variables(object):
    def __init__(self, core, plugin):
        self.version = "v3.0.0"
        self.pluginName = "Gimp"
        self.pluginType = "App"
        self.appShortName = "Gimp"
        self.appType = "2d"
        self.hasQtParent = False
        self.hasFrameRange = False
        self.sceneFormats = [".xcf", "psd"]
        self.appSpecificFormats = self.sceneFormats
        self.importFormats = [".png", ".exr", ".jpg", "bmp"]                                        #   TODO - ADD FORMATS
        self.outputFormats = [".png", ".exr", ".jpg", "bmp"]                                        #   TODO - ADD FORMATS
        self.appColor = [200, 180, 0]
        self.canDeleteRenderPasses = False
        self.colorButtonWithStyleSheet = True
        self.platforms = ["Windows", "Linux", "Darwin"]
        self.pluginDirectory = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        self.appIcon = os.path.join(self.pluginDirectory, "UserInterfaces", "Gimp.ico")
        self.prismAppIcon = os.path.join(self.pluginDirectory, "UserInterfaces", "Gimp.ico")

        self.gimpDefaults = {
            "bridgePort_out": 50600,
            "bridgePort_in": 50601
            }

        self.gimpStates = [
            "Folder",
            "Gimp_Render"
            ]
 