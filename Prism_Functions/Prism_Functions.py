#!/usr/bin/env python3
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
####################################################
#
#           Gimp3 (2.99) Plugin for Prism2
#
#                 Joshua Breckeen
#                    Alta Arts
#                josh@alta-arts.com
#
####################################################

import sys
import os
import subprocess
import threading
import time
import socket

import gi
gi.require_version('Gimp', '3.0')
from gi.repository import Gimp
gi.require_version('GimpUi', '3.0')
from gi.repository import GimpUi
from gi.repository import GObject
from gi.repository import GLib
from gi.repository import Gio

from pypdb import pdb

if "PRISM_ROOT" in os.environ:
    prismRoot = os.environ["PRISM_ROOT"]
    if not prismRoot:
        raise Exception("PRISM_ROOT is not set")
else:
    prismRoot = r"C:/Prism2"

pluginPath = os.path.dirname(__file__)

if os.path.exists(os.path.join(prismRoot, "Python311")):
    prismEXE = r"C:\Prism2\Python311\Prism.exe"
elif os.path.exists(os.path.join(prismRoot, "Python39")):
    prismEXE = r"C:\Prism2\Python39\Prism.exe"

def N_(message): return message
def _(message): return GLib.dgettext(None, message)

help_doc = r"""
Menu items and functions for intergration
with Prism Pipeline
"""


class PrismFunctions(Gimp.PlugIn):
    ## Parameter: run-mode ##
    @GObject.Property(type=Gimp.RunMode,
                      default=Gimp.RunMode.NONINTERACTIVE,
                      nick="Run mode", blurb="The run mode")
    
    def run_mode(self):
        """Read-write integer property."""
        return self._run_mode

    @run_mode.setter
    def run_mode(self, run_mode):
        self._run_mode = run_mode

    ## Parameter: filePath ##
    @GObject.Property(type=str,
                      nick= _("File Path"),
                      blurb= _("File Path"))
    def filePath(self):
        return self._filePath

    @filePath.setter
    def filePath(self, filePath):
        self._filePath = filePath

    
    ## GimpPlugIn virtual methods ##
    def do_set_i18n(self, procname):
        return True, 'gimp30-python', None

    def do_query_procedures(self):
        return [ "python-fu-prism-saveAction" ]

    def do_create_procedure(self, name):
        procedure = Gimp.Procedure.new(self, name,
                                       Gimp.PDBProcType.PLUGIN,
                                       self.run, None)
        
        if name == 'python-fu-prism-saveAction':
            procedure.set_documentation(_("Prism save action"),
                                        help_doc,
                                        "")
            
            procedure.set_attribution("Joshua Breckeen",
                                      "Prism Pipeline",
                                      "2024")
            
            procedure.add_argument_from_property(self, "run-mode")
            procedure.add_argument_from_property(self, "filePath")
        else:
            procedure = None

        print("***** Loading Prism Functions ******")

        return procedure

    def run(procedure, config, filePath):
        runmode = config.get_property("run-mode")
        # filePath = config.get_property("filePath")


        print ("*** RUNNING ***")


        return True

Gimp.main(PrismFunctions.__gtype__, sys.argv)