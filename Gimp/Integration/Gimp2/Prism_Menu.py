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
import socket
import json
import logging
import errno

from gimpfu import *


# help_doc = r"""
# Menu items and functions for intergration
# with Prism Pipeline
# """


if "PRISM_ROOT" in os.environ:
    PRISMROOT = os.environ["PRISM_ROOT"]
    if not PRISMROOT:
        raise Exception("PRISM_ROOT is not set")
else:
    PRISMROOT = r"C:/Prism2"
    # PRISMROOT = r_RISMROOTREPLACE                         #   TODO CHANGE FOR INTERGRATION - change "p"

PLUGINROOT = r"C:/ProgramData/Prism2/plugins/Gimp"
# pluginRoot = r_LUGINROOT                                  #   TODO CHANGE FOR INTERGRATION - change "p"

if os.path.exists(os.path.join(PRISMROOT, "Python311")):
    PRISMEXE = os.path.join(PRISMROOT, "Python311", "Prism.exe")
elif os.path.exists(os.path.join(PRISMROOT, "Python39")):
    PRISMEXE = os.path.join(PRISMROOT, "Python39", "Prism.exe")


##    CONSTANTS    ##                                                       
PLUGINPATH = os.path.dirname(__file__)
CONFIGFILE = os.path.join(PLUGINROOT, "GimpConfig.json")
BRIDGESCRIPT = os.path.join(PLUGINPATH, "Prism_Util", "Prism_Bridge.py")
HOST = "127.0.0.1"



class PrismGimpLogger:
    def __init__(self, debugEnabled, logPath):
        self.debugEnabled = debugEnabled
        sys.stderr = open(logPath, 'a')
        sys.stdout = sys.stderr
        
    def debug(self, message):
        if self.debugEnabled:
            pdb.gimp_message("PRISM MENU:   %s" % message)
            
        logging.warning("PRISM MENU:  %s" % message)

    def warning(self, message):
        logging.warning("PRISM MENU:  %s" % message)
        pdb.gimp_message("PRISM MENU:   %s" % message)


def cmdDataToJson(command, payload):
    log.debug("Creating json for:  %s" % command)

    pData = {
        "command": command,
        "data": payload
        }
    
    jData = json.dumps(pData)
    return jData


def jsonToCmdData(jData):
    log.debug("decoding json")

    try:
        pData = json.loads(jData)

        command = pData.get("command")
        payload = pData.get("data")

        log.debug("decoded:   %s" % command)

        return command, payload
    
    except Exception as e:
        log.warning("Error decoding json:   %s" % e)
        return None
    

def isServerRunning():
    log.debug("Checking Server")

    getGimpPluginConfig()
    try:
        # Create a new socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Try to bind the socket to the host and port
        sock.bind((HOST, port))

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


def getGimpPluginConfig():
    global port

    try:
        with open(CONFIGFILE, 'r') as file:
            gimpSettings = json.load(file)

        # Update global variables with values from gimpSettings dictionary
        port = int(gimpSettings.get("commPort"))
        debugEnabled = gimpSettings.get("debugEnabled")
        logPath = gimpSettings.get("logLocation")

        return debugEnabled, logPath

    except FileNotFoundError:
        log.warning("Config file %s not found." % CONFIGFILE)

    except Exception as e:
        log.warning("Error reading config file: %s" % e)
        pass

#   To perform actions when Gimp loads
def initActions():
    global log

    debugEnabled, logPath = getGimpPluginConfig()

    log = PrismGimpLogger(debugEnabled, logPath)



def save_version():

    if isServerRunning():
        log.warning("Saving New Version")
        subprocess.Popen([PRISMEXE, BRIDGESCRIPT, PRISMROOT, "SaveVersion"])
    else:
        log.warning("Start Server First")


def save_ver_with_comment():

    if isServerRunning():
        log.warning("Opening Save Dialogue")
        subprocess.Popen([PRISMEXE, BRIDGESCRIPT, PRISMROOT, "SaveComment"])
    else:
        log.warning("Start Server First")


def project_browser():

    if isServerRunning():
        log.warning("Opening Project Browser")
        subprocess.Popen([PRISMEXE, BRIDGESCRIPT, PRISMROOT, "ProjectBrowser"])
    else:
        log.warning("Start Server First")


def state_manager():

    if isServerRunning():
        log.warning("Opening State Manager")
        subprocess.Popen([PRISMEXE, BRIDGESCRIPT, PRISMROOT, "StateManager"])
    else:
        log.warning("Start Server First")



initActions()   #   Run init actions such getting config info and setting up logger


### vvvvv REGISTER PLUG-IN vvvvv ###

# SAVE VERSION
register(
    "python-fu_prism_saveVersion",                              #   TODO Complete descriptions etc
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
    "State Manager",
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


main()