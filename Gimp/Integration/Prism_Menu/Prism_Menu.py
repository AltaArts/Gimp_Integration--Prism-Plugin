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
###########################################################################
#
#                    Gimp3 (2.99) Plugin for Prism2
#
#                           Joshua Breckeen
#                              Alta Arts
#                          josh@alta-arts.com
#
###########################################################################

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

def N_(message): return message
def _(message): return GLib.dgettext(None, message)

help_doc = r"""
Menu items and functions for intergration
with Prism Pipeline
"""

from pypdb import pdb

if "PRISM_ROOT" in os.environ:
    prismRoot = os.environ["PRISM_ROOT"]
    if not prismRoot:
        raise Exception("PRISM_ROOT is not set")
else:
    prismRoot = PRISMROOT


pluginPath = os.path.dirname(__file__)

if os.path.exists(os.path.join(prismRoot, "Python311")):
    prismEXE = r"C:\Prism2\Python311\Prism.exe"
elif os.path.exists(os.path.join(prismRoot, "Python39")):
    prismEXE = r"C:\Prism2\Python39\Prism.exe"

bridgeScript = os.path.join(pluginPath, "Prism_Bridge.py")

host = "127.0.0.1"
port_gimpToPrism = 40404


def startScriptServer():

    global server_thread

    if not isServerRunning():
        print(f"*** Starting Server on {host} {port_gimpToPrism}***")

        def startServer():
            pdb.plug_in_script_fu_server(host, port_gimpToPrism)

        # Start the server in a separate thread
        server_thread = threading.Thread(target=startServer)
        server_thread.start()

    else:
        print("Server is already running")

        
def isServerRunning():
    try:
        # Attempt to connect to the server
        with socket.create_connection((host, port_gimpToPrism), timeout=1) as sock:
            return True
    except (ConnectionRefusedError, socket.timeout):
        return False


def save_version(procedure, run_mode, image, n_drawables, drawables, args, data):

    startScriptServer()
    subprocess.Popen([prismEXE, bridgeScript, prismRoot, "SaveVersion"])

    return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, GLib.Error())


def save_ver_with_comment(procedure, run_mode, image, n_drawables, drawables, args, data):

    startScriptServer()
    subprocess.Popen([prismEXE, bridgeScript, prismRoot, "SaveComment"])

    return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, GLib.Error())


def project_browser(procedure, run_mode, image, n_drawables, drawables, args, data):

    startScriptServer()
    subprocess.Popen([prismEXE, bridgeScript, prismRoot, "ProjectBrowser"])

    return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, GLib.Error())


def state_manager(procedure, run_mode, image, n_drawables, drawables, args, data):

    startScriptServer()
    subprocess.Popen([prismEXE, bridgeScript, prismRoot, "StateManager"])

    return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, GLib.Error())




def testProc(procedure, run_mode, image, n_drawables, drawables, args, data):

    print("*** TEST PROCEDURE ***\n\n")

    return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, GLib.Error())



class PrismMenuPlugin (Gimp.PlugIn):
    ## Parameters ##

    ## GimpPlugIn virtual methods ##
    def do_set_i18n(self, procname):
        return True, 'gimp30-python', None

    def do_query_procedures(self):
        return [
            'python-fu-prism-saveVersion',
            'python-fu-prism-saveVerWithComment',
            'python-fu-prism-projectBrowser',
            'python-fu-prism-stateManager',
            'python-fu-prism-testProc'
            ]

    def do_create_procedure(self, name):

        procedure = Gimp.ImageProcedure.new(self, name,
                                    Gimp.PDBProcType.PLUGIN,
                                    save_version if name == 'python-fu-prism-saveVersion' else
                                    save_ver_with_comment if name == 'python-fu-prism-saveVerWithComment' else
                                    project_browser if name == 'python-fu-prism-projectBrowser' else
                                    state_manager if name == 'python-fu-prism-stateManager' else
                                    testProc,
                                    None)
        
        procedure.set_sensitivity_mask (Gimp.ProcedureSensitivityMask.NO_IMAGE)

        procedure.set_documentation ("Prism Pipeline",
                                     help_doc,
                                     name)
        
       # Set individual names for each menu entry
        if name == 'python-fu-prism-saveVersion':
            procedure.set_menu_label("Save Version")
        elif name == 'python-fu-prism-saveVerWithComment':
            procedure.set_menu_label("Save Ver with Comment")
        elif name == 'python-fu-prism-projectBrowser':
            procedure.set_menu_label("Project Browser")
        elif name == 'python-fu-prism-stateManager':
            procedure.set_menu_label("State Manager")
        elif name == 'python-fu-prism-testProc':
            procedure.set_menu_label("Test Procedure")
            

        procedure.set_attribution("Joshua Breckeen",
                                  "Prism2",
                                  "2024")
        
        # Top level menu "Prism"
        procedure.add_menu_path ("<Image>/Prism")


        return procedure

    print("********* STARTING PRISM MENU ***********")
    time.sleep(.1)


Gimp.main(PrismMenuPlugin.__gtype__, sys.argv)
