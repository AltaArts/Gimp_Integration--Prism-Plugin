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

# from dis import show_code
# from distutils import cmd
import os
import time
import socket
import logging
import sys
import shutil
import errno


import json

from gimpfu import *


if "PRISM_ROOT" in os.environ:
    prismRoot = os.environ["PRISM_ROOT"]
    if not prismRoot:
        raise Exception("PRISM_ROOT is not set")
else:
    # prismRoot = PRISMROOT
    prismRoot = r"C:\Prism2"                                                    #   TODO CHANGE FOR INTERGRATION


##    CONSTANTS    ##                                                       
PLUGIN_PATH = os.path.dirname(__file__)
LOGPATH = os.path.join(PLUGIN_PATH, "logs")
LOGFILE = os.path.join(LOGPATH, "Gimp-Prism_Log.log")
ALPHA_BG_FILE = os.path.join(PLUGIN_PATH, "Prism_Util", "alpha_BG.png")
HOST = "127.0.0.1"
PORT_PRISMTOGIMP = 40404                                                        #   TODO ALLOW USER CONFIG IN SETTINGS
LOG_SIZE_MAX = 500  # size in kb's                                               #   TODO ALLOW USER CONFIG IN SETTINGS


#   LOGGING
sys.stderr = open(LOGFILE, 'a')
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


class PrismServer:
    def __init__(self):
        self.host = HOST
        self.port_prismToGimp = PORT_PRISMTOGIMP
        self.socket = None


    def start(self):
        log.warning("Listening on {}:{}".format(self.host, self.port_prismToGimp))

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port_prismToGimp))
        self.socket.listen(1)  # Note: Specify the number of pending connections
        
        while True:
            conn, addr = self.socket.accept()
            # with conn:
            log.debug("Connected by:  %s" % str(addr))
            jData = conn.recv(40960)

            if not jData:
                break
            
            log.debug("Received Data")
            responseData = handleCmd(jData)

            log.debug("Responding")
            if responseData is None:
                responseData = ""
            conn.sendall(responseData.encode())


    def stop(self):
        if self.socket:
            self.socket.close()
            self.socket = None
            log.warning("Server stopped.")


    def reset(self):
        self.stop()
        self.start()
        log.warning("Reset Comms")


def startServer():

    handleServerLog()

    time.sleep(1)                                               #   NEEDED?

    if not isServerRunning():

        log.warning("Launching Server*\n\n")

        server = PrismServer()
        server.start()

    else:
        log.warning("Server is already running")
        pass



def handleServerLog():
    
    # Check if the logfile exists
    if os.path.exists(LOGFILE):
        try:
            # Get the size of the logfile
            logSize = os.path.getsize(LOGFILE)
            
            # Convert logSizeMax from MB to bytes
            thresholdSize = LOG_SIZE_MAX * 1024  # logSizeMax in kb's
            
            # Check if the size exceeds the threshold
            if logSize > thresholdSize:

                # Generate the new filename with "_old" suffix
                oldLogfile = LOGFILE.replace(".log", "_OLD.log")
                log.debug("*** Backing up log to %s ***" % oldLogfile)
                
                # Rename the logfile
                shutil.copy(LOGFILE, oldLogfile)

                #   Clear the logfile, since Gimp is restricting from deleting
                with open(LOGFILE, 'w'):  # Open the file in write mode to truncate it
                    pass
                
                log.debug("The logfile has been renamed to: %s" % oldLogfile)

        except Exception as e:
            log.warning("ERROR:  %s" % e)

    else:
        if not os.path.exists(LOGPATH):
            os.mkdir(LOGPATH)


def cmdDataToJson(command, payload):

    log.debug("Creating json for:  %s" % command)                                          #    DEBUG

    try:
        pData = {
            "command": command,
            "data": payload
            }
        
        jData = json.dumps(pData)
        return jData
    
    except:
        return None


def jsonToCmdData(jData):

    log.debug("decoding json:")                                          #    DEBUG
    log.debug(jData)

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









def handleCmd(jData):

    command, payload = jsonToCmdData(jData)

    log.debug("Command received:   %s" % command)

    # if command == "PING":
    #     return pingTest()
    if command == "getCurrentFilename":
        return getCurrentFilename()
    elif command == "saveVersion":
        return saveVersion(payload)
    elif command == "captureScreenShot":
        return captureScreenShot(payload)
    elif command == "saveStates":
        return saveStates(payload)
    elif command == "getStates":
        return getStates()
    elif command == "exportFile":
        return exportFile(payload)

    else:
        command = "FAILED"
        payload = "FAILED"
        return cmdDataToJson(command, payload)

    


### ^^^^^ Socket Comms from Prism ^^^^^ ###
##############################################################



#########################################
### vvvvv Functions inside Gimp vvvvv ###

#   Gets the currently open image's filepath
def getCurrentFilename():

    try:
        image = gimp.image_list()[0]
        filePath = pdb.gimp_image_get_filename(image)
    except:
        filePath = ""

    log.debug("Current Filename:   %s" % filePath)                                          #    DEBUG

    sendCommand = "currentFilename"
    sendPayload = {"filePath": filePath}

    jData = cmdDataToJson(sendCommand, sendPayload)

    return jData


def saveVersion(data):

    filePath = data.get("filePath")

    currentFile = saveXCF(filePath)

    newFile = openXCF(filePath)

    switchUIimages(currentFile, newFile)

    sendCommand = "Success"
    sendPayload = {"filePath": filePath}

    jData = cmdDataToJson(sendCommand, sendPayload)

    return jData


def switchUIimages(oldImage, newImage):

    pdb.gimp_displays_reconnect(oldImage, newImage)
    pdb.gimp_image_clean_all(newImage)


def captureScreenShot(data):

    log.debug("IN SCREENSHOT")                                                #   DEBUG

    currentImage = gimp.image_list()[0]
    currentDrawable = pdb.gimp_image_get_active_layer(currentImage)
    ssPath = data.get("filePath")

    if pdb.gimp_drawable_has_alpha(currentDrawable):

        alphaBGLayer = pdb.gimp_file_load_layer(currentImage, ALPHA_BG_FILE)
        numLayers, _ = pdb.gimp_image_get_layers(currentImage)

        xRez = pdb.gimp_image_width(currentImage)
        yRez = pdb.gimp_image_height(currentImage)

        pdb.gimp_image_insert_layer(currentImage, alphaBGLayer, None, numLayers + 1)
        pdb.gimp_layer_scale(alphaBGLayer, xRez, yRez, False)

        mergedLayer = pdb.gimp_layer_new_from_visible(currentImage, currentImage, "tempVisable")

        result = saveJPG(currentImage, mergedLayer, ssPath)

        pdb.gimp_image_remove_layer(currentImage, alphaBGLayer)
        pdb.gimp_image_clean_all(currentImage)
        pdb.gimp_displays_flush()

    else:
        result = saveJPG(currentImage, currentDrawable, ssPath)

    if result:
        sendCommand = "Success"
    else:
        sendCommand = "Failed"
    
    sendPayload = {"filePath": ssPath}

    jData = cmdDataToJson(sendCommand, sendPayload)

    return jData


#   Saves curretly open image to the supplied filepath
def saveXCF(filePath):

    log.debug("IN saveAction")                          #   DEBUG

    currentImage = gimp.image_list()[0]

    currentDrawable = pdb.gimp_image_get_active_layer(currentImage)

    pdb.gimp_xcf_save(1, currentImage, currentDrawable, filePath, filePath)

    return currentImage


def openXCF(filePath):
    
    newImage = pdb.gimp_xcf_load(1, filePath, filePath)

    return newImage



def exportFile(data):

    rSettings = data.get("rSettings")

    log.debug(rSettings)

    outputType = rSettings["outputType"]

    if outputType == ".jpg":
        result = exportJPG(rSettings)

    elif outputType == ".png":
        result = exportPNG(rSettings)

    if result:
        sendPayload = "Result=Success"
    else:
        sendPayload = "Result=Failed"


    sendCommand = "Result"
    jData = cmdDataToJson(sendCommand, sendPayload)
    return jData


def exportJPG(rSettings):

    bgLayer = False
    numImages, image_ids = pdb.gimp_image_list()

    if numImages < 1:
        return False
    
    else:
        currentImage = gimp.image_list()[0]
        currentDrawable = pdb.gimp_image_get_active_layer(currentImage)
        filePath = rSettings["outputName"]

        alphaFill = rSettings["alphaFill"]
        quality = rSettings["jpg_Quality"]
        smoothing = rSettings["jpg_Smoothing"]
        subSample = rSettings["jpg_SubSample"]
        optimize = rSettings["jpg_Optimize"]
        progressive = rSettings["jpg_Progressive"]
        arithCode = rSettings["jpg_ArithCode"]
        comment = rSettings["imageComment"]
        
        if pdb.gimp_drawable_has_alpha(currentDrawable):
            bgLayer = fillAlphaBG(currentImage, alphaFill)

        mergedLayer = pdb.gimp_layer_new_from_visible(currentImage, currentImage, "tempVisable")

        result = saveJPG(currentImage,
                         mergedLayer,
                         filePath,
                         quality,
                         smoothing,
                         optimize,
                         progressive,
                         comment,
                         subSample,
                         arithCode
                         )

        if bgLayer:
            pdb.gimp_image_remove_layer(currentImage, bgLayer)

            pdb.gimp_image_clean_all(currentImage)
            pdb.gimp_displays_flush()

        return result


def exportPNG(rSettings):

    bgLayer = False
    numImages, image_ids = pdb.gimp_image_list()

    if numImages < 1:
        return False
    
    else:
        currentImage = gimp.image_list()[0]
        currentDrawable = pdb.gimp_image_get_active_layer(currentImage)
        filePath = rSettings["outputName"]

        png_Compress = (int(rSettings["png_Compress"]) - 1)    #   so that GUI is 1-10
        png_Interlaced = rSettings["png_Compress"]
        png_Gamma = rSettings["png_Compress"]
        png_Rez = rSettings["png_Compress"]
        png_BgColor = rSettings["png_Compress"]
        png_LayerOffset = rSettings["png_Compress"]
        png_AlphaColor = rSettings["png_Compress"]

        alphaFill = rSettings["alphaFill"]

        comment = rSettings["imageComment"]
        
        if pdb.gimp_drawable_has_alpha(currentDrawable):
            bgLayer = fillAlphaBG(currentImage, alphaFill)

        mergedLayer = pdb.gimp_layer_new_from_visible(currentImage, currentImage, "tempVisable")

        result = savePNG(currentImage,
                         mergedLayer,
                         filePath,
                         png_Interlaced,
                         png_Compress,
                         png_BgColor,
                         png_Gamma,
                         png_LayerOffset,
                         png_Rez,
                         0,
                        #  comment,
                        0,
                         png_AlphaColor
                         )

        if bgLayer:
            pdb.gimp_image_remove_layer(currentImage, bgLayer)

            pdb.gimp_image_clean_all(currentImage)
            pdb.gimp_displays_flush()

        return result



def savePNG(image=None,
            drawable=None,
            filePath=None,
            interlace=0,
            compression=5,
            bkgd=1,
            gama=0,
            offs=0,
            phys=0,
            time=0,
            comment="",
            svtrans=1
            ):

    log.debug("SAVING PNG ***\n")                                                 #   DEBUG

    try:
        pdb.file_png_save2(image,
                        drawable,
                        filePath,
                        filePath,
                        interlace,
                        compression,
                        bkgd,
                        gama,
                        offs,
                        phys,
                        time,
                        comment,
                        svtrans)

        log.debug("AFTER SAVE PNG")                                                   #   DEBUG
        return True

    except Exception as e:
        log.warning("ERROR:  ", e)
        return False


def saveJPG(image=None,
            drawable=None,
            filePath=None,
            quality=.5,
            smoothing=.5,
            optimize=0,
            progressive=0,
            comment="",
            subsmp=0,
            baseline=0,
            restart=0,
            dct=0
            ):


    log.debug("SAVING JPG ***\n")                                                 #   DEBUG

    try: 
        pdb.file_jpeg_save(image,
                           drawable,
                           filePath,
                           filePath,
                           quality,
                           smoothing,
                           optimize,
                           progressive,
                           comment,
                           subsmp,
                           baseline,
                           restart,
                           dct)
        
        log.debug("AFTER SAVE JPG")                                                   #   DEBUG
        return True

    except Exception as e:
        log.warning("ERROR:  ", e)
        return False


def fillAlphaBG(image, fillType):

    if fillType == "checker":
        bgLayer = pdb.gimp_file_load_layer(image, ALPHA_BG_FILE)
    elif fillType == "white":
        pass
    elif fillType == "pink":
        pass
    else:           #   fill with Black
        pass

    numLayers, _ = pdb.gimp_image_get_layers(image)

    xRez = pdb.gimp_image_width(image)
    yRez = pdb.gimp_image_height(image)

    pdb.gimp_image_insert_layer(image, bgLayer, None, numLayers + 1)
    pdb.gimp_layer_scale(bgLayer, xRez, yRez, False)

    return bgLayer


def saveStates(data):

    numImages, image_ids = pdb.gimp_image_list()

    if numImages > 0:
        currentImage = gimp.image_list()[0]
        
        try:
            stateData = data.get("stateData")
            currentImage.attach_new_parasite("stateData", 5, stateData)

            log.debug("Saved States")
            sendCommand = "Success"
        
        except:
            log.warning("Save State Failed")
            sendCommand = "Failed"
    else:
        log.warning("No image open")
        sendCommand = "Failed"

    sendPayload = ""


    jData = cmdDataToJson(sendCommand, sendPayload)
    return jData


def getStates():

    numImages, image_ids = pdb.gimp_image_list()

    if numImages > 0:
        currentImage = gimp.image_list()[0]

        try:
            parasite  = currentImage.parasite_find("stateData")

            log.debug("strData:   %s" % parasite )                                          #    DEBUG

            if parasite:
                stateData = parasite.data
            else:
                stateData = ""
        
        except Exception as e:
            log.warning("ERROR in getting State Data:  %s" % e)
            stateData = ""
    else:
        log.debug("No Image Loaded")
        stateData = ""

    sendCommand = "StateData"
    sendPayload = {"stateData": stateData}

    jData = cmdDataToJson(sendCommand, sendPayload)

    return jData




### vvvvv REGISTER PLUG-IN vvvvv ###

# START SERVER
register(
    "python-fu_prism_server",                      #   UNIQUE NAME
    "Prism Server",                              #   BLURB
    "Description of Server",                       #   DESCRIPTION
    "Joshua Breckeen",                                  #   AUTHORS NAME
    "Copyright (C) Your Year",                          #   COPYRIGHT INFO
    "2023",                                             #   VERSION OF SCRIPT
    "1 - Start Prism Server",                           #   NAME DISPLAYED IN MENU
    "",                                                 #   TYPE OF DRAWABLE: '' = can be none, * = any drawable, RGB, RGB, RGB* etc
    [],                                                 #   ADDITIONAL ARGS
    [],                                                 #   RETURN TYPES
    startServer,                                        #   FUNCTION CALLED WHEN ACTIVATED
    "<Image>/Prism",                                    #   WHERE IN MENU
)

# START SERVER
# register(
#     "python-fu_prism_listener",                      #   UNIQUE NAME
#     "Prism Listener",                              #   BLURB
#     "Description of Listener",                       #   DESCRIPTION
#     "Joshua Breckeen",                                  #   AUTHORS NAME
#     "Copyright (C) Your Year",                          #   COPYRIGHT INFO
#     "2023",                                             #   VERSION OF SCRIPT
#     "1 - Start Prism Listener",                           #   NAME DISPLAYED IN MENU
#     "",                                                 #   TYPE OF DRAWABLE: '' = can be none, * = any drawable, RGB, RGB, RGB* etc
#     [],                                                 #   ADDITIONAL ARGS
#     [],                                                 #   RETURN TYPES
#     startListener,                                        #   FUNCTION CALLED WHEN ACTIVATED
#     "<Image>/Prism",                                    #   WHERE IN MENU
# )

main()