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

import os
import time
import socket
import logging
import sys
import shutil
import errno
import json

from gimpfu import *
import gimpcolor


if "PRISM_ROOT" in os.environ:
    PRISMROOT = os.environ["PRISM_ROOT"]
    if not PRISMROOT:
        raise Exception("PRISM_ROOT is not set")
else:
    PRISMROOT = r"C:/Prism2"
    # PRISMROOT = r_RISMROOTREPLACE                         #   TODO CHANGE FOR INTERGRATION - change "p"

PLUGINROOT = r"C:/ProgramData/Prism2/plugins/Gimp"
# pluginRoot = r_LUGINROOT                                  #   TODO CHANGE FOR INTERGRATION - change "p"

##    CONSTANTS    ##                                                       
PLUGIN_PATH = os.path.dirname(__file__)
CONFIGFILE = os.path.join(PLUGINROOT, "GimpConfig.json")
ALPHA_BG_FILE = os.path.join(PLUGIN_PATH, "Prism_Util", "alpha_BG.png")
HOST = "127.0.0.1"



class PrismGimpLogger:
    def __init__(self, debugEnabled, logPath):
        self.debugEnabled = debugEnabled
        sys.stderr = open(logPath, 'a')
        sys.stdout = sys.stderr
        
    def debug(self, message):
        if self.debugEnabled:
            pdb.gimp_message("PRISM FUNCTIONS:   %s" % message)
            
        logging.warning("PRISM FUNCTIONS:  %s" % message)

    def warning(self, message):
        logging.warning("PRISM FUNCTIONS:  %s" % message)
        pdb.gimp_message("PRISM FUNCTIONS:   %s" % message)



class PrismServer:
    def __init__(self):
        self.host = HOST
        self.port_prismToGimp = port
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


#   To perform actions when Gimp loads
def initActions():
    global log
    global server
    global logMaxSize

    debugEnabled, logPath, logMaxSize  = getGimpPluginConfig()

    log = PrismGimpLogger(debugEnabled, logPath)
    server = PrismServer()


def getGimpPluginConfig():
    global port
    global logPath
    global logMaxSize

    try:
        with open(CONFIGFILE, 'r') as file:
            gimpSettings = json.load(file)

        # Update global variables with values from gimpSettings dictionary
        port = int(gimpSettings.get("commPort"))
        debugEnabled = gimpSettings.get("debugEnabled")
        logPath = gimpSettings.get("logLocation")
        logMaxSize = gimpSettings.get("logMax")

        return debugEnabled, logPath, logMaxSize

    except FileNotFoundError:
        log.warning("Config file %s not found." % CONFIGFILE)

    except Exception as e:
        log.warning("Error reading config file: %s" % e)
        pass


def startServer():

    handleServerLog()
    time.sleep(1)                        #   NEEDED?

    if not isServerRunning():
        log.warning("Launching Server")
        server.start()

    else:
        log.warning("Server is already running")
        pass


def handleServerLog():
    global logPath
    global logMaxSize
    logDir = os.path.dirname(logPath)
    
    if os.path.exists(logPath):
        try:
            logSize = os.path.getsize(logPath)
            thresholdSize = logMaxSize * 1024  # logSizeMax in kb's
            
            if logSize > thresholdSize:

                # Generate the new filename with "_old" suffix
                oldLogfile = logPath.replace(".log", "_OLD.log")
                log.debug("*** Backing up log to %s ***" % oldLogfile)
                
                # Rename the logfile
                shutil.copy(logPath, oldLogfile)

                #   Clear the logfile, since Gimp is restricting from deleting
                with open(logPath, 'w'):  # Open the file in write mode to truncate it
                    pass
                
                log.debug("The logfile has been renamed to: %s" % oldLogfile)

        except Exception as e:
            log.warning("ERROR:  %s" % e)

    else:
        if not os.path.exists(logDir):
            os.mkdir(logDir)


def cmdDataToJson(command, payload):
    log.debug("Creating json for:  %s" % command)

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
    log.debug("decoding json:")
    log.debug(jData)

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
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Try to bind the socket
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
            log.warning("Socket error: %s" % e)
            return False

    finally:
        sock.close()


def handleCmd(jData):

    command, payload = jsonToCmdData(jData)

    log.debug("Command received:   %s" % command)

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
    numImages, image_ids = pdb.gimp_image_list()
    if numImages < 1:
        return False
    
    rSettings = data.get("rSettings")

    log.debug(rSettings)

    currentImage = gimp.image_list()[0]
    currentDrawable = pdb.gimp_image_get_active_layer(currentImage)
    filePath = rSettings["outputName"]

    outputType = rSettings["outputType"]
    if outputType == ".png":
        result = exportPNG(rSettings, currentImage, currentDrawable, filePath)
    elif outputType == ".exr":
        result = exportEXR(rSettings, currentImage, currentDrawable, filePath)
    elif outputType == ".jpg":
        result = exportJPG(rSettings, currentImage, currentDrawable, filePath)

    if result:
        sendPayload = "Result=Success"
    else:
        sendPayload = "Result=Failed"

    sendCommand = "Result"
    jData = cmdDataToJson(sendCommand, sendPayload)
    return jData


def exportPNG(rSettings, currentImage, currentDrawable, filePath):

    png_Compress = int(rSettings["png_Compress"]) - 1    #   so that GUI is 1-10
    png_Interlaced = rSettings["png_Interlaced"]
    png_Gamma = rSettings["png_Compress"]
    png_Rez = rSettings["png_Rez"]
    png_BgColor = rSettings["png_BgColor"]
    png_LayerOffset = rSettings["png_LayerOffset"]
    png_AlphaColor = rSettings["png_AlphaColor"]
    colorMode = rSettings["colorMode"]
    bitDepth = rSettings["bitDepth"]
    exportScale = int(rSettings["exportScale"])
    alphaFill = rSettings["alphaFill"]
    
    mergedLayer = createExportLayer(currentImage, currentDrawable, exportScale, colorMode, bitDepth, alphaFill)

    result = savePNG(currentImage,
                        mergedLayer,
                        filePath,
                        png_Interlaced,
                        png_Compress,
                        png_BgColor,
                        png_Gamma,
                        png_LayerOffset,
                        png_Rez,
                        1,
                        0,
                        png_AlphaColor
                        )
        
    pdb.gimp_image_remove_layer(currentImage, mergedLayer)

    pdb.gimp_image_clean_all(currentImage)
    pdb.gimp_displays_flush()

    return result


def savePNG(image=None,
            drawable=None,
            filePath=None,
            interlace=0,
            compression=5,
            bkgd=1,
            gama=1,
            offs=0,
            phys=1,
            time=1,
            comment=0,
            svtrans=1
            ):

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

        return True

    except Exception as e:
        log.warning("ERROR:  ", e)
        return False


def exportEXR(rSettings, currentImage, currentDrawable, filePath):

    colorMode = rSettings["colorMode"]
    bitDepth = rSettings["bitDepth"]
    exportScale = int(rSettings["exportScale"])
    alphaFill = rSettings["alphaFill"]

    mergedLayer = createExportLayer(currentImage, currentDrawable, exportScale, colorMode, bitDepth, alphaFill)

    result = saveEXR(currentImage,
                        mergedLayer,
                        filePath,
                        )

    pdb.gimp_image_remove_layer(currentImage, mergedLayer)

    pdb.gimp_image_clean_all(currentImage)
    pdb.gimp_displays_flush()

    return result


def saveEXR(image=None,                     #   Unfortunatly that is all the options Gimps API has
            drawable=None,
            filePath=None,
            ):

    try: 
        pdb.file_exr_save(image,
                           drawable,
                           filePath,
                           filePath)
        
        return True

    except Exception as e:
        log.warning("ERROR:  ", e)
        return False


def exportJPG(rSettings, currentImage, currentDrawable, filePath):
    bgLayer = False

    quality = rSettings["jpg_Quality"]
    smoothing = rSettings["jpg_Smoothing"]
    subSample = rSettings["jpg_SubSample"]
    optimize = rSettings["jpg_Optimize"]
    progressive = rSettings["jpg_Progressive"]
    arithCode = rSettings["jpg_ArithCode"]
    colorMode = rSettings["colorMode"]
    bitDepth = rSettings["bitDepth"]
    exportScale = int(rSettings["exportScale"])
    alphaFill = rSettings["alphaFill"]

    mergedLayer = createExportLayer(currentImage, currentDrawable, exportScale, colorMode, bitDepth, alphaFill)

    result = saveJPG(currentImage,
                        mergedLayer,
                        filePath,
                        quality,
                        smoothing,
                        optimize,
                        progressive,
                        "",
                        subSample,
                        arithCode
                        )

    pdb.gimp_image_remove_layer(currentImage, mergedLayer)

    pdb.gimp_image_clean_all(currentImage)
    pdb.gimp_displays_flush()

    return result


def saveJPG(image=None,
            drawable=None,
            filePath=None,
            quality=.5,
            smoothing=.5,
            optimize=1,
            progressive=0,
            comment="",
            subsmp=0,
            baseline=0,
            restart=0,
            dct=0
            ):

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
        
        return True

    except Exception as e:
        log.warning("ERROR:  ", e)
        return False


def createExportLayer(currentImage, currentDrawable, exportScale, colorMode, bitDepth, alphaFill):
    tempBgLayer = False

    xRez = (pdb.gimp_image_width(currentImage) * exportScale) / 100
    yRez = (pdb.gimp_image_height(currentImage) * exportScale) / 100

    if colorMode not in ["RGBA", "GRAYA"]:
        if pdb.gimp_drawable_has_alpha(currentDrawable):
            tempBgLayer = fillAlphaBG(currentImage, alphaFill)

    mergedLayer = pdb.gimp_layer_new_from_visible(currentImage, currentImage, "tempVisable")
    pdb.gimp_image_insert_layer(currentImage, mergedLayer, None, 0)

    if tempBgLayer:
        pdb.gimp_image_remove_layer(currentImage, tempBgLayer)

    if exportScale != 100:
        pdb.gimp_layer_scale_full(mergedLayer, xRez, yRez, 1, 2)

    return mergedLayer


def fillAlphaBG(image, alphaFill):
    #   Gets rez of original image
    xRez = pdb.gimp_image_width(image)  
    yRez = pdb.gimp_image_height(image)
    #   gets number of layers in the image
    numLayers, _ = pdb.gimp_image_get_layers(image) 

    #   Uses the checker BG from plugin directory
    if alphaFill == "checker":
        bgLayer = pdb.gimp_file_load_layer(image, ALPHA_BG_FILE)

    #   Fills BG with selected color
    else:
        #   creates new layer with image dimensions
        bgLayer = pdb.gimp_layer_new(image, xRez, yRez, 0, "tempBgLayer", 100, 0)
        #   saves original foreground color
        origFgColor = pdb.gimp_context_get_foreground()

        if alphaFill == "white":
            fillColor = gimpcolor.RGB(255, 255, 255)  # White
        elif alphaFill == "gray":
            fillColor = gimpcolor.RGB(100, 100, 100)  # Gray
        elif alphaFill == "pink":
            fillColor = gimpcolor.RGB(255, 0, 255)    # Pink
        else:
            fillColor = gimpcolor.RGB(0, 0, 0)        #   Black

        #   sets foreground color
        pdb.gimp_context_set_foreground(fillColor)
        #   Fills layer with FG color
        pdb.gimp_drawable_fill(bgLayer, 0)  
        #   Reset Fg color to original
        pdb.gimp_context_set_foreground(origFgColor)  

    #   inserts this temp layer to bottom
    pdb.gimp_image_insert_layer(image, bgLayer, None, numLayers + 1)
    #   scales temp layer to image size
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



initActions()   #   Run init actions such getting config info and setting up logger


### vvvvv REGISTER PLUG-IN vvvvv ###

# START SERVER
register(
    "python-fu_prism_serverStart",                      #   UNIQUE NAME
    "Prism Server Start Action",                        #   BLURB
    "Enables socket comms between Prism and Gimp",      #   DESCRIPTION
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
#     "python-fu_prism_serverReset",
#     "Prism Server Reset Action",
#     "Resets socket comms between Prism and Gimp",
#     "Joshua Breckeen",
#     "Copyright (C) Your Year",
#     "2023",
#     "6 - Reset Prism Server",
#     "",
#     [],
#     [],
#     resetServer,
#     "<Image>/Prism",
# )

main()