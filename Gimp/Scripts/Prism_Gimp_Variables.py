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


import os

class Prism_Gimp_Variables(object):
    def __init__(self, core, plugin):
        self.version = "v2.0.5-0.6-alpha"
        self.pluginName = "Gimp"
        self.pluginType = "App"
        self.appShortName = "Gimp"
        self.appType = "2d"
        # self.hasQtParent = True
        self.hasQtParent = False
        self.sceneFormats = [".xcf"]
        self.appSpecificFormats = self.sceneFormats
        self.outputFormats = [".xcf", ".png", ".jpg", "exr", "avi", "bmp", "sgi", "tga", "tif"]
        # self.appColor = [255, 255, 255]
        self.appColor = [115, 172, 230]
        self.hasFrameRange = False
        self.renderPasses = []
        self.platforms = ["Windows"]                                    #   TODO
        # self.platforms = ["Windows", "Linux", "Darwin"]
        self.pluginDirectory = os.path.abspath(
            os.path.dirname(os.path.dirname(__file__))
            )
        self.appIcon = os.path.join(
            self.pluginDirectory, "UserInterfaces", "Gimp.ico"
            )

        
