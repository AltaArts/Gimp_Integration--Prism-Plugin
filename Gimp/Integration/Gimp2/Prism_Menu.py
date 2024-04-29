#!/usr/bin/env python
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
import subprocess                                                           #   TODO CLEANUP
import threading
import time
import socket
import shutil
import json
import logging
import errno

from gimpfu import *


# help_doc = r"""
# Menu items and functions for intergration
# with Prism Pipeline
# """


if "PRISM_ROOT" in os.environ:
    prismRoot = os.environ["PRISM_ROOT"]
    if not prismRoot:
        raise Exception("PRISM_ROOT is not set")
else:
    # prismRoot = PRISMROOT
    prismRoot = r"C:\Prism2"                                            #   TODO CHANGE FOR INTERGRATION

if os.path.exists(os.path.join(prismRoot, "Python311")):
    PRISMEXE = os.path.join(prismRoot, "Python311", "Prism.exe")
elif os.path.exists(os.path.join(prismRoot, "Python39")):
    PRISMEXE = os.path.join(prismRoot, "Python39", "Prism.exe")


##    CONSTANTS    ##                                                       
PLUGINPATH = os.path.dirname(__file__)
LOGPATH = os.path.join(PLUGINPATH, "logs")
LOGFILE = os.path.join(LOGPATH, "Gimp-Prism_Log.log")
BRIDGESCRIPT = os.path.join(PLUGINPATH, "Prism_Util", "Prism_Bridge.py")
HOST = "127.0.0.1"
PORT_PRISMTOGIMP = 40404                                                        #   TODO ALLOW USER CONFIG IN SETTINGS


#   LOGGING
sys.stderr = open(LOGFILE, 'a')               #####   FOR TESTING
sys.stdout = sys.stderr
DEBUG = True    #   Set True to display all messages




class PrismGimpLogger:
    def debug(self, message):
        if DEBUG:
            pdb.gimp_message("PRISM FUNCTIONS:   %s" % message)
            
        logging.warning("PRISM FUNCTIONS:  %s" % message)

    def warning(self, message):
        logging.warning("PRISM FUNCTIONS:  %s" % message)
        pdb.gimp_message("PRISM FUNCTIONS:   %s" % message)


log = PrismGimpLogger()


def cmdDataToJson(command, payload):

    log.debug("Creating json for:  %s" % command)                                          #    DEBUG

    pData = {
        "command": command,
        "data": payload
        }
    
    jData = json.dumps(pData)
    return jData


def jsonToCmdData(jData):

    log.debug("decoding json")                                          #    DEBUG

    try:
        pData = json.loads(jData)

        command = pData.get("command")
        payload = pData.get("data")

        log.debug("decoded:   %s" % command)                                          #    DEBUG

        return command, payload
    
    except Exception as e:
        log.warning("Error decoding json:   %s" % e)                                      #    TESTING
        return None
    

def isServerRunning():
    log.debug("Checking Server")
    try:
        # Create a new socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Try to bind the socket to the host and port
        sock.bind((HOST, PORT_PRISMTOGIMP))

        # If the bind is successful, the port is not in use
        sock.close()
        return False

    except socket.error as e:
        # If the bind fails with the error code 10048 (EADDRINUSE equivalent on Windows), the port is already in use
        if e.errno == 10048:
            return True
        # If the bind fails with the error code EADDRINUSE (for non-Windows systems), the port is already in use
        elif e.errno == errno.EADDRINUSE:
            return True
        else:
            # Handle other socket errors
            log.warning("Socket error: %s" % e)
            return False

    finally:
        # Close the socket if it was created
        sock.close()



def save_version():
    if isServerRunning():
        log.warning("Saving New Version")
        subprocess.Popen([PRISMEXE, BRIDGESCRIPT, prismRoot, "SaveVersion"])
    else:
        log.warning("Start Server First")


def save_ver_with_comment():
    if isServerRunning():
        log.warning("Opening Save Dialogue")
        subprocess.Popen([PRISMEXE, BRIDGESCRIPT, prismRoot, "SaveComment"])
    else:
        log.warning("Start Server First")


def project_browser():
    if isServerRunning():
        log.warning("Opening Project Browser")
        subprocess.Popen([PRISMEXE, BRIDGESCRIPT, prismRoot, "ProjectBrowser"])
    else:
        log.warning("Start Server First")


def state_manager():
    if isServerRunning():
        log.warning("Opening State Manager")
        subprocess.Popen([PRISMEXE, BRIDGESCRIPT, prismRoot, "StateManager"])
    else:
        log.warning("Start Server First")


# def resetComms():                                                                     #####   TODO EMPLEMENT RESET

#     showMsg("Resetting Comms")

#     scriptServer = Script_Server()

#     if scriptServer.isRunning():

#         try:
#             with open(PID_FILE, "r") as f:
#                 scriptFuProcessID = int(f.read().strip())

#         except Exception as e:
#             showMsg("Error reading PID from file: %s" % e)
#             return None

#         try:
#             # Terminate all script-fu.exe processes except the one with scriptFuProcessID
#             output = subprocess.check_output(['tasklist', '/FO', 'CSV', '/NH'])
#             for line in output.splitlines():
#                 fields = line.strip().split(',')
#                 if len(fields) >= 2 and fields[0].strip('"') == "script-fu.exe":
#                     pid = int(fields[1].strip('"'))

#                     if pid != scriptFuProcessID and scriptFuProcessID is not None:
#                         subprocess.check_call(['taskkill', '/F', '/PID', str(pid)])

        
#         except Exception as e:
#             showMsg("Error:  %s" % e)

#         if os.path.exists(COMMS_DIR):
#             shutil.rmtree(COMMS_DIR)

#         if os.path.exists(SERVERLOG):
#             serverFile = os.path.basename(SERVERLOG)
#             shutil.copy(SERVERLOG, os.path.join(GIMP_LOCAL_DIR, serverFile.replace(".txt", "_RESET.txt")))
#             shutil.rmtree(LOG_DIR)

        



### vvvvv REGISTER PLUG-IN vvvvv ###

# START SERVER
# register(
#     "python-fu_prism_startServer",                      #   UNIQUE NAME
#     "Start Script Server",                              #   BLURB
#     "Description of Save Action",                       #   DESCRIPTION
#     "Joshua Breckeen",                                  #   AUTHORS NAME
#     "Copyright (C) Your Year",                          #   COPYRIGHT INFO
#     "2023",                                             #   VERSION OF SCRIPT
#     "1 - Start Prism Server",                           #   NAME DISPLAYED IN MENU
#     "",                                                 #   TYPE OF DRAWABLE: '' = can be none, * = any drawable, RGB, RGB, RGB* etc
#     [],                                                 #   ADDITIONAL ARGS
#     [],                                                 #   RETURN TYPES
#     startServer,                                        #   FUNCTION CALLED WHEN ACTIVATED
#     "<Image>/Prism",                                    #   WHERE IN MENU
# )


# SAVE VERSION
register(
    "python-fu_prism_saveVersion",
    "Save Version",
    "Description of Save Action",
    "Joshua Breckeen",
    "Copyright (C) Your Year",
    "2023",
    "2 - Save Version",
    "",
    [],
    [],
    save_version,
    "<Image>/Prism",
)

# SAVE VER WITH COMMENT
register(
    "python-fu_prism_saveVerWithComment",
    "Save Ver with Comment",
    "Description of Save Action",
    "Joshua Breckeen",
    "Copyright (C) Your Year",
    "2023",
    "3 - Save Ver with Comment",
    "",  # No need for * when it's not a submenu
    [],
    [],
    save_ver_with_comment,
    "<Image>/Prism",
)

# OPEN PROJECT BROWSER
register(
    "python-fu_prism_project_browser",
    "Project Browser",
    "Description of Save Action",
    "Joshua Breckeen",
    "Copyright (C) Your Year",
    "2023",
    "4 - Project Browser",
    "",  # No need for * when it's not a submenu
    [],
    [],
    project_browser,
    "<Image>/Prism",
)

# OPEN STATE MANAGER
register(
    "python-fu_prism_openStateManager",
    "State Manager <3>",
    "Description of Save Action",
    "Joshua Breckeen",
    "Copyright (C) Your Year",
    "2023",
    "5 - State Manager",
    "",  # No need for * when it's not a submenu
    [],
    [],
    state_manager,
    "<Image>/Prism",
)

# RESET COMMS
# register(
#     "python-fu_prism_resetComms",
#     "Reset Comms",
#     "Description of Reset Comms",
#     "Joshua Breckeen",
#     "Copyright (C) Your Year",
#     "2023",
#     "6 - Reset Comms",
#     "",  # No need for * when it's not a submenu
#     [],
#     [],
#     resetComms,
#     "<Image>/Prism",
# )


main()