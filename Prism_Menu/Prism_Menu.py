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
    prismRoot = r"C:/Prism2"

pluginPath = os.path.dirname(__file__)

if os.path.exists(os.path.join(prismRoot, "Python311")):
    prismEXE = r"C:\Prism2\Python311\Prism.exe"
elif os.path.exists(os.path.join(prismRoot, "Python39")):
    prismEXE = r"C:\Prism2\Python39\Prism.exe"

bridgeScript = os.path.join(pluginPath, "Prism_Bridge.py")

host = "127.0.0.1"
port = 40404


def startScriptServer(mode):

    global server_thread

    if mode == "start":

        if not isServerRunning():

            print(f"*** Starting Server on {host} {port}***")

            def startServer():
                pdb.plug_in_script_fu_server(host, port)

            # Start the server in a separate thread
            server_thread = threading.Thread(target=startServer)
            server_thread.start()

            # time.sleep(5)                                                       #   TODO
        else:
            print("Server is already running")

    elif mode == "stop":
        if server_thread and server_thread.is_alive():
            print("*** Stopping Server ***")
            server_thread.terminate()
            server_thread.join()  # Wait for the server thread to terminate

        
def isServerRunning():
    try:
        # Attempt to connect to the server
        with socket.create_connection((host, port), timeout=1) as sock:
            return True
    except (ConnectionRefusedError, socket.timeout):
        return False



def save_version(procedure, run_mode, image, n_drawables, drawables, args, data):


    startScriptServer("start")

    # filePath = r"c:\tmp\test.xcf"

    # file = Gio.File.new_for_path(filePath)

    # Save the image in the .xcf file format
    # pdb.gimp_xcf_save(image, file=file)

    print("**** SAVING VERSION *******")
    
    subprocess.Popen([prismEXE, bridgeScript, prismRoot, "SaveVersion"])

    # startScriptServer("stop")


    return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, GLib.Error())


def save_ver_with_comment(procedure, run_mode, image, n_drawables, drawables, args, data):

    print("\n** IN SAVE VER with COMMENT **\n")
    Gimp.message("** IN SAVE VER with COMMENT **")


    return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, GLib.Error())


def project_browser(procedure, run_mode, image, n_drawables, drawables, args, data):

    print("\n** PRINT -- IN PROJECT BROWSER **\n")

    Gimp.message("** MESSAGE -- IN PROJECT BROWSER **")


    subprocess.Popen([prismEXE, bridgeScript, prismRoot, "ProjectBrowser"])



    return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, GLib.Error())


def state_manager(procedure, run_mode, image, n_drawables, drawables, args, data):

    print("\n** IN STATE MANAGER **\n")

    subprocess.Popen([prismEXE, bridgeScript, prismRoot, "StateManager"])


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
            'python-fu-prism-stateManager'
            ]

    def do_create_procedure(self, name):

        procedure = Gimp.ImageProcedure.new(self, name,
                                    Gimp.PDBProcType.PLUGIN,
                                    save_version if name == 'python-fu-prism-saveVersion' else
                                    save_ver_with_comment if name == 'python-fu-prism-saveVerWithComment' else
                                    project_browser if name == 'python-fu-prism-projectBrowser' else
                                    state_manager,
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
            

        procedure.set_attribution("Joshua Breckeen",
                                  "Prism2",
                                  "2024")
        
        # Top level menu "Prism"
        procedure.add_menu_path ("<Image>/Prism")

        print("********* STARTING PRISM MENU ***********")

        return procedure



Gimp.main(PrismMenuPlugin.__gtype__, sys.argv)
