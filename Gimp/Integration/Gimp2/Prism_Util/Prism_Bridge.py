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
#                        Gimp2 Plugin for Prism2
#
#                           Joshua Breckeen
#                              Alta Arts
#                          josh@alta-arts.com
#
###########################################################################


import os
import sys
import platform

prismRoot = sys.argv[1]

sys.path.insert(0, os.path.join(prismRoot, "Scripts"))
import PrismCore

from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *


os.environ["Gimp_CurrentImagePath"] = sys.argv[3]
# os.environ["Gimp_CurrentDrawable"] = sys.argv[4]          #   NOT USED RIGHT NOW


qapp = QApplication.instance()
if qapp is None:
    qapp = QApplication(sys.argv)

pcore = PrismCore.create(app="Gimp", prismArgs=["noProjectBrowser"])

if not platform.system() == "Darwin":
    curPrj = pcore.getConfig("globals", "current project")

    result = False
    command = sys.argv[2]
    match command:
        case "SaveVersion":
            result = pcore.saveScene()
        case "SaveComment":
            result = pcore.saveWithComment()
        case "Export":
            result = pcore.appPlugin.exportImage()
        case "ProjectBrowser":
            result = pcore.projectBrowser()
        case "StateManager":
            result = pcore.stateManager()

    if result:
        qapp.exec_()
