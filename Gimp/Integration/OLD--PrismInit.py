#!/usr/bin/env python

import os
import sys
import platform
import subprocess

from gimpfu import *

pluginPath = os.path.dirname(__file__)

def prismInit():
    prismRoot = os.getenv("PRISM_ROOT")
    if not prismRoot:
        prismRoot = PRISMROOT

    scriptDir = os.path.join(prismRoot, "Scripts")

    if scriptDir not in sys.path:
        sys.path.append(scriptDir)

    import PrismCore

    pcore = PrismCore.PrismCore(app="PluginEmtpy")
    return pcore




def saveVersionAction():

    gimp.message("INSIDE saveVersionAction")                               #   TESTING


def saveVerCommentAction():

    gimp.message("INSIDE saveVerCommentAction")                               #   TESTING


def openBrowser():

    gimp.message("INSIDE openBrowser")                               #   TESTING


    python37_path = "C:\\Prism2\\Python39\\python.exe"
    bridgeScriptPath = os.path.join(pluginPath, "gimp-prism_bridge.py")
    subprocess.call([python37_path, bridgeScriptPath])


def openStateMgr():

    gimp.message("INSIDE openStateMgr")                               #   TESTING



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
