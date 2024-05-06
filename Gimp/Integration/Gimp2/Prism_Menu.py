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
#                       Gimp2 Plugin for Prism2
#
#                           Joshua Breckeen
#                              Alta Arts
#                          josh@alta-arts.com
#
###########################################################################


import sys
import os
import subprocess
import socket
import json
import logging
import errno

from gimpfu import *

if "PRISM_ROOT" in os.environ:
    PRISMROOT = os.environ["PRISM_ROOT"]
    if not PRISMROOT:
        raise Exception("PRISM_ROOT is not set")
    
#   Gets set during Intergration installation
else:
    PRISMROOT = r"C:/Prism2"
    # PRISMROOT = r_RISMROOTREPLACE                         #   TODO CHANGE FOR INTERGRATION - change "p"

PLUGINROOT = r"C:/ProgramData/Prism2/plugins/Gimp"
# pluginRoot = r_LUGINROOT                                  #   TODO CHANGE FOR INTERGRATION - change "p"

#   Sets Prism executable
if os.path.exists(os.path.join(PRISMROOT, "Python311")):
    PRISMEXE = os.path.join(PRISMROOT, "Python311", "Prism.exe")
elif os.path.exists(os.path.join(PRISMROOT, "Python39")):
    PRISMEXE = os.path.join(PRISMROOT, "Python39", "Prism.exe")


##    CONSTANTS    ##                                                       
PLUGINPATH = os.path.dirname(__file__)
CONFIGFILE = os.path.join(PLUGINROOT, "GimpConfig.json")
BRIDGESCRIPT = os.path.join(PLUGINPATH, "Prism_Util", "Prism_Bridge.py")
HOST = "127.0.0.1"


#   Custom logger since Gimps logging is not great
#   This will print to the logfile, and display in Gimps Error Console
class PrismGimpLogger:
    def __init__(self, logLevel, logPath):
        self.logLevel = logLevel
        sys.stderr = open(logPath, 'a')
        sys.stdout = sys.stderr

    #   Debug will only be printed to logfile unless All
    #   is selected in Prism settings
    def debug(self, message):
        if self.logLevel == "All":
            pdb.gimp_message("PRISM MENU:   %s" % message)
            
        logging.warning("PRISM MENU:  %s" % message)

    #   Warning will be printed in both the logfile
    #   and Gimps Error Console
    def warning(self, message):
        if self.logLevel in ["Minimal", "All"]:
            pdb.gimp_message("PRISM MENU:   %s" % message)

        logging.warning("PRISM MENU:  %s" % message)


#   To perform actions when Gimp first loads
def initActions():
    global log

    #   Retrieves Gimp config items
    logLevel, logPath = getGimpPluginConfig()

    #   Gets logger instance
    log = PrismGimpLogger(logLevel, logPath)


#   Gets config items set in Prism Settings
#   under DCC->Gimp
def getGimpPluginConfig():
    global port

    try:
        with open(CONFIGFILE, 'r') as file:
            gimpSettings = json.load(file)

        # Update global variables
        port = int(gimpSettings.get("commPort"))
        logLevel = gimpSettings.get("logLevel")
        logPath = gimpSettings.get("logLocation")

        return logLevel, logPath

    except FileNotFoundError:
        log.warning("ERROR:  Config file %s not found." % CONFIGFILE)

    except Exception as e:
        log.warning("ERROR:  Error reading config file: %s" % e)
        pass


#   Checks if socket is in use
def isServerRunning():
    log.debug("Checking Server")

    getGimpPluginConfig()
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Try to bind the socket to the host and port
        sock.bind((HOST, port))

        # If the bind is successful, the port is not in use
        sock.close()
        return False

    except socket.error as e:
        # If error code 10048 (EADDRINUSE equivalent on Windows), the port is already in use
        if e.errno == 10048:
            return True
        # If error code EADDRINUSE (non-Windows), the port is already in use
        elif e.errno == errno.EADDRINUSE:
            return True
        else:
            log.warning("ERROR:  Socket error: %s" % e)
            return False

    finally:
        sock.close()


#        vvvvv PROCEDURES CALLED FROM GIMP MENU vvvvv                       #
#   each on opens a process that calls for a Prism instance                 #
#   passes an arg to launch desired Prism function, and the current Image   #

def save_version(currentImage, currentDrawable):

    filePath = pdb.gimp_image_get_filename(currentImage)
    imageArg = "%s" % filePath

    if isServerRunning():
        log.warning("Saving New Version")
        subprocess.Popen([PRISMEXE, BRIDGESCRIPT, PRISMROOT, "SaveVersion", imageArg])
    else:
        log.warning("Start Server First")


def save_verWithComment(currentImage, currentDrawable):

    filePath = pdb.gimp_image_get_filename(currentImage)
    imageArg = "%s" % filePath

    if isServerRunning():
        log.warning("Opening Save Dialogue")
        subprocess.Popen([PRISMEXE, BRIDGESCRIPT, PRISMROOT, "SaveComment", imageArg])
    else:
        log.warning("Start Server First")


def project_browser(currentImage, currentDrawable):

    filePath = pdb.gimp_image_get_filename(currentImage)
    imageArg = "%s" % filePath

    if isServerRunning():
        log.warning("Opening Project Browser")
        subprocess.Popen([PRISMEXE, BRIDGESCRIPT, PRISMROOT, "ProjectBrowser", imageArg])
    else:
        log.warning("Start Server First")


def state_manager(currentImage, currentDrawable):

    filePath = pdb.gimp_image_get_filename(currentImage)
    imageArg = "%s" % filePath

    if isServerRunning():
        log.warning("Opening State Manager")
        subprocess.Popen([PRISMEXE, BRIDGESCRIPT, PRISMROOT, "StateManager", imageArg])
    else:
        log.warning("Start Server First")



initActions()   #   Run init actions such getting config info and setting up logger



### vvvvv REGISTER PLUG-IN PROCEDURES vvvvv ###

helpDoc = r"""
Menu items and functions for intergration
with Prism Pipeline
"""

attribution = "Prism: Richard Frangenberg\nPlugin: Joshua Breckeen"
copyright = "GNU LGPL-3.0-or-later"

# SAVE VERSION
register(
    "python-fu_prism_saveVersion",
    "Saves new vesion of scenefile to Prism",
    helpDoc,
    attribution,
    copyright,
    "2023",
    "2 - Save Version",
    "",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "drawable", "Input drawable", None)
    ],
    [],
    save_version,
    "<Image>/Prism",
)

# SAVE VER WITH COMMENT
register(
    "python-fu_prism_saveVerWithComment",
    "Opens dialogue to save a new version\n of scenefile to Prism",
    helpDoc,
    attribution,
    copyright,
    "2023",
    "3 - Save Ver with Comment",
    "",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "drawable", "Input drawable", None)
    ],
    [],
    save_verWithComment,
    "<Image>/Prism",
)

# OPEN PROJECT BROWSER
register(
    "python-fu_prism_openProjectBrowser",
    "Opens the Project Browser",
    helpDoc,
    attribution,
    copyright,
    "2023",
    "4 - Project Browser",
    "",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "drawable", "Input drawable", None)
    ],
    [],
    project_browser,
    "<Image>/Prism",
)

# OPEN STATE MANAGER
register(
    "python-fu_prism_openStateManager",
    "Opens the State Manager",
    helpDoc,
    attribution,
    copyright,
    "2023",
    "5 - State Manager",
    "",
    # [(PF_IMAGE, "image", "Input image", None)],
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "drawable", "Input drawable", None)
    ],
    [],
    state_manager,
    "<Image>/Prism",
)


main()