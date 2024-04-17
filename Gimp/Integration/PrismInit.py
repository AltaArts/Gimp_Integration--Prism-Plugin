#!/usr/bin/env python

import os
import sys
import platform
import subprocess

from gimpfu import *


pluginPath = os.path.dirname(__file__)


def saveVersionAction():

    gimp.message("INSIDE saveVersionAction")                                    #   TESTING
    command = "SaveVer"
    filepath = r"n:\Data\Projects\Prism Tests\03_Production\Assets\Gimp_Test\Scenefiles\gimp\Gimp\Gimp_Test_Gimp_v0001.xcf"         #   TESTING
    executeCmd(command, filepath)


def saveVerCommentAction():

    gimp.message("INSIDE saveVerCommentAction")                                 #   TESTING
    command = "SaveVerComment"
    executeCmd(command)


def openBrowser():

    gimp.message("INSIDE openBrowser")                                          #   TESTING
    command = "ProjectBrowser"
    executeCmd(command)


def openStateMgr():

    gimp.message("INSIDE openStateMgr")                                         #   TESTING
    command = "StateManager"
    executeCmd(command)


def executeCmd(command):

    python37_path = "C:\\Prism2\\Python39\\python.exe"
    # python37_path = "C:\\Prism2\\Python39\\pythonw.exe"     #    TO MAKE IT SILENT

    bridgeScriptPath = os.path.join(pluginPath, "gimp-prism_bridge.py")
    subprocess.call([python37_path, bridgeScriptPath, command])                      #   <<-- need to pass command arg





# SAVE VERSION
register(
    "python-fu_prism_saveVersion_action",               #   UNIQUE NAME
    "Save Version <0>",                                 #   NAME IN MENU  ???  DOES NOT SEEM TO MATTER
    "Description of Save Action",                       #   DESCRIPTION
    "Joshua Breckeen",                                  #   AUTHORS NAME
    "Copyright (C) Your Year",                          #   COPYRIGHT INFO
    "2023",                                             #   VERSION OF SCRIPT
    "Save Version",                                     #   NAME DISPLAYED IN MENU
    "",                                                 #   No need for * when it's not a submenu
    [],                                                 #   ADDITIONAL ARGS
    [],                                                 #   RETURN TYPES
    saveVersionAction,                                  #   FUNCTION CALLED WHEN ACTIVATED
    "<Image>/Prism",                                    #   WHERE IN MENU
)

# SAVE VER WITH COMMENT
register(
    "python-fu_prism_saveVerWithComment_action",
    "Save Ver with Comment <1>",
    "Description of Save Action",
    "Joshua Breckeen",
    "Copyright (C) Your Year",
    "2023",
    "Save Ver with Comment",
    "",  # No need for * when it's not a submenu
    [],
    [],
    saveVerCommentAction,
    "<Image>/Prism",
)

# OPEN PROJECT BROWSER
register(
    "python-fu_prism_openProjectBrowser_action",
    "Project Browser <2>",
    "Description of Save Action",
    "Joshua Breckeen",
    "Copyright (C) Your Year",
    "2023",
    "Project Browser",
    "",  # No need for * when it's not a submenu
    [],
    [],
    openBrowser,
    "<Image>/Prism",
)

# OPEN STATE MANAGER
register(
    "python-fu_prism_openStateManager_action",
    "State Manager <3>",
    "Description of Save Action",
    "Joshua Breckeen",
    "Copyright (C) Your Year",
    "2023",
    "State Manager",
    "",  # No need for * when it's not a submenu
    [],
    [],
    openStateMgr,
    "<Image>/Prism",
)

main()
