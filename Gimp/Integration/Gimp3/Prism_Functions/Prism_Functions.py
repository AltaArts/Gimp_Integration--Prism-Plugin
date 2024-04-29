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

from pypdb import pdb   #   Library to simplify Gimp pdb calls - is included in plugin dir

if "PRISM_ROOT" in os.environ:
    prismRoot = os.environ["PRISM_ROOT"]
    if not prismRoot:
        raise Exception("PRISM_ROOT is not set")
else:
    prismRoot = PRISMROOT

commsDir = os.path.join(prismRoot, "Plugins", "PrismGimpComms")

host = "127.0.0.1"
port_prismToGimp = 40404


def N_(message): return message
def _(message): return GLib.dgettext(None, message)

help_doc = r"""
Menu items and functions for intergration
with Prism Pipeline
"""


### vvvvv For Sending Commands to Prism vvvvv ###
def createCmdFile(command, data):

#   pData command Template
    pData = {
        "command": command,
        "data": data
        }

    commOutFile = createCommFileName()
    
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



def sendCmdToPrism(command, data):

    createCmdFile(command, data)


### ^^^^^ For Sending Commands to Prism ^^^^^ ###


### vvvvv For receiving commands and data from Prism vvvvv ###
def pingFromPrism(procedure, config, data):

    print("*** IN PING ***")

    getCmdFile()

    return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, GLib.Error())


def getCmdFile():

    commands = ["getCurrentFilename",
                "saveVersion",
                "captureScreenShot",
                "exportPNG"]

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

    command = pData.get("command")

    if command == "getCurrentFilename":
        getCurrentFilename()

    elif command == "saveVersion":
        saveVersion(pData.get("data"))
    elif command == "captureScreenShot":
        captureScreenShot(pData.get("data"))


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

    command = "currentFilename"
    data = {"filePath": filePath}

    sendCmdToPrism(command, data)


def saveVersion(data):

    filePath = data.get("filePath")

    currentFile = saveAction(filePath)

    newFile = openXCF(currentFile, filePath)

    switchUIimages(currentFile, newFile)

        

#   Saves curretly open image to the supplied filepath
def saveAction(filePath):

    print("\n*** IN saveAction ***\n")                          #   DEBUG

    images = pdb.gimp_get_images()
    imageList = images[1]
    currentImage = imageList.data[0]

    file = Gio.File.new_for_path(filePath)

    # Save the image in the .xcf file format
    pdb.gimp_xcf_save(image=currentImage , file=file)

    return currentImage


def openXCF(currentFile, filePath):
    
    print("\n*** IN OPEN XCF ***\n")                          #   DEBUG

    file = Gio.File.new_for_path(filePath)

    newImage = pdb.gimp_xcf_load(file=file)

    return newImage


def switchUIimages(oldImage, newImage):

    pdb.gimp_displays_reconnect(oldImage, newImage)

    pdb.gimp_image_clean_all(newImage)


def captureScreenShot(data):

    print("\n*** IN SCREENSHOT ***\n\n")

    images = pdb.gimp_get_images()
    imageList = images[1]
    currentImage = imageList.data[0]

    # print(dir(Gimp.Drawable))

    # drawable = Gimp.Drawable.get_by_id()


    # # drawableName = Gimp.gimp_drawable_get_by_id(0)

    # print("\n*** drawable:  ", drawable, "\n")

    # ssPath = data.get("filePath")

    # ssFile = Gio.File.new_for_path(ssPath)

    # print("*** ssFile:  ", ssFile, "\n\n")

    # print("\n*** SAVING JPG ***\n")

    # try:
    #     pdb.file_jpeg_save(image=currentImage, drawables=drawable, file=ssFile)

    # except Exception as e:
    #     print("ERROR:  ", e)


    # print("\n*** AFTER SAVING JPG ***\n")


    # return ssPath


### ^^^^^ Functions inside Gimp ^^^^^ ###


### vvvvv Registration of plugin inside Gimp vvvvv ###
class PrismFunctions(Gimp.PlugIn):

    # def __init__(self):
    #     super().__init__()
    
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
            
            procedure.set_sensitivity_mask (Gimp.ProcedureSensitivityMask.NO_IMAGE)


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