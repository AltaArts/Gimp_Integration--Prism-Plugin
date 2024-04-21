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
import time
import socket
import json
from datetime import datetime

import gi
gi.require_version('Gimp', '3.0')
from gi.repository import Gimp
gi.require_version('GimpUi', '3.0')
from gi.repository import GimpUi
from gi.repository import GObject
from gi.repository import GLib
from gi.repository import Gio

#   Library to simplify Gimp pdb calls - is included in plugin dir
from pypdb import pdb

if "PRISM_ROOT" in os.environ:                                                          #   TODO 's
    prismRoot = os.environ["PRISM_ROOT"]                                                #   Handled SUCCES return
    if not prismRoot:                                                                   #   Comms dir config
        raise Exception("PRISM_ROOT is not set")                                        #   Make bi-directional
else:                                                                                   #   Error handling
    prismRoot = r"C:/Prism2"                                                            #   add logger

if os.path.exists(os.path.join(prismRoot, "Python311")):
    prismEXE = r"C:\Prism2\Python311\Prism.exe"
elif os.path.exists(os.path.join(prismRoot, "Python39")):
    prismEXE = r"C:\Prism2\Python39\Prism.exe"

pluginPath = os.path.dirname(__file__)                              #   NEEDED ????

commsDir = os.path.join(prismRoot, "PrismGimpComms")

host = "127.0.0.1"
port_prismToGimp = 40404
port_gimpToPrism = 40405                                #   NEEDED?


def N_(message): return message
def _(message): return GLib.dgettext(None, message)

help_doc = r"""
Menu items and functions for intergration
with Prism Pipeline
"""


### vvvvv For Sending Commands to Prism vvvvv ###
def createCmdFile(pData):


#   pData command Template
#        pData = {
#            "command": "saveXCF",
#            "data":filepath
#            }

    commOutFile = createCommFileName()

    print("*** commOutFile:  ", commOutFile)
    
    # Write the dictionary to the JSON file
    with open(commOutFile, 'w') as json_file:
        json.dump(pData, json_file)


def createCommFileName():

    if not os.path.exists(commsDir):
        os.makedirs(commsDir)

    outName = "Gimp--Prism_Comm-" + str(getTimeStamp()) + ".json"
    commOutFile = os.path.join(commsDir, outName)

    return commOutFile


def getTimeStamp():            

    current_time = datetime.now().time()
    timeStamp = current_time.strftime("%H%M%S%f")

    return timeStamp



def sendCmdToPrism(pData):

    createCmdFile(pData)


### ^^^^^ For Sending Commands to Prism ^^^^^ ###


### vvvvv For receiving commands and data from Prism vvvvv ###
def pingFromPrism(procedure, config, data):

    print("*** IN PING ***")

    getCmdFile()

    return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, GLib.Error())


def getCmdFile():

    commands = ["getCurrentFilename", "saveVersion", "exportPNG"]

    files = os.listdir(commsDir)

    for fileName in files:
        if fileName.startswith("Prism--Gimp_Comm-"):
            filePath = os.path.join(commsDir, fileName)                     #   Handle old Cmd files
    
            # Open the   JSON file for reading
            with open(filePath, 'r') as json_file:
                # Load the JSON data from the file
                pData = json.load(json_file)

            if pData.get('command') in commands:
                os.remove(filePath)
                handleCmd(pData)
            else:
                print("ERROR:  COMMAND FILE IS NOT VALID")              #   TODO ERRORS

        else:
            print("ERROR: Invalid file:  ", fileName)


def handleCmd(pData):

    command = pData.get('command')

    if command == "getCurrentFilename":
        getCurrentFilename()

    elif command == "saveVersion":
        saveVersion(pData)

### ^^^^^ For receiving commands and data from Prism ^^^^^ ###


### vvvvv Functions inside Gimp vvvvv ###


#   Gets the currently open image's filepath
def getCurrentFilename():

    print("\n****  IN GET FILENAME ***\n\n")

    images = pdb.gimp_get_images()
    imageList = images[1]
    currentImage = imageList.data[0]

    gfile = currentImage.get_file()
    filePath = gfile.get_path()

    print("filePath from Gimp:  ", filePath)

    pData = {
        "command": "currentFilename",
        "data":filePath
        }

    sendCmdToPrism(pData)


def saveVersion(pData):

    filePath = pData.get("data")

    saveAction(filePath)


    openXCF(filePath)

        

#   Saves curretly open image to the supplied filepath
def saveAction(filePath):

    print("\n*** IN saveAction ***\n")                          #   DEBUG


    images = pdb.gimp_get_images()
    imageList = images[1]
    currentImage = imageList.data[0]

    file = Gio.File.new_for_path(filePath)

    # Save the image in the .xcf file format
    pdb.gimp_xcf_save(image=currentImage , file=file)


def openXCF(filePath):
    
    print("\n*** IN OPEN XCF ***\n")                          #   DEBUG

    print("*** filePath:  ", filePath, "\n")

    file = Gio.File.new_for_path(filePath)

    print("*** file:  ", file, "\n")


    newVerImage = pdb.gimp_xcf_load(file=file)

    # pdb.gimp_displays_flush()                               #   NEEDED ???

    print("*** newVerImage:  ", newVerImage)




### ^^^^^ Functions inside Gimp ^^^^^ ###


### vvvvv Reistration of plugin inside Gimp vvvvv ###
class PrismFunctions(Gimp.PlugIn):

    def __init__(self):
        super().__init__()
    
    ## GimpPlugIn virtual methods ##
    def do_set_i18n(self, procname):
        return True, 'gimp30-python', None

    def do_query_procedures(self):
        return [ "python-fu-prism-pingFromPrism" ]

    def do_create_procedure(self, name):

        procedure = None
        
        if name == 'python-fu-prism-pingFromPrism':

            procedure = Gimp.Procedure.new(self,
                                        name,
                                        Gimp.PDBProcType.PLUGIN,
                                        # Gimp.PDBProcType.EXTENSION,  # Change to EXTENSION ???
                                        pingFromPrism,
                                        None
                                        )
            
            procedure.set_documentation(_("Prism communication"),
                                        help_doc,
                                        "")
            
            procedure.set_attribution("Joshua Breckeen",
                                      "Prism Pipeline",
                                      "2024")

        else:
            procedure = None

        return procedure

    
    print("***** Loading Prism Functions ******")                   #   DEBUG
    time.sleep(.1)

Gimp.main(PrismFunctions.__gtype__, sys.argv)