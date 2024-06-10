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

import os
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
    
#   Gets set during Intergration installation
else:
    PRISMROOT = rPRISMROOTREPLACE

PLUGINROOT = rPLUGINROOTREPLACE

##    CONSTANTS    ##                                                       
PLUGIN_PATH = os.path.dirname(__file__)
CONFIGFILE = os.path.join(PLUGINROOT, "GimpConfig.json")
ALPHA_BG_FILE = os.path.join(PLUGIN_PATH, "Prism_Util", "alpha_BG.png")
HOST = "127.0.0.1"

#   Conversion Dict for Gimp Codes
COLORMODEDATA = {
    "8_Linear": {"precision": 100, "display": "8 bit", "bitDepth": 8, "gamma": "Linear"},
    "8_sRGB": {"precision": 150, "display": "8 bit", "bitDepth": 8, "gamma": "sRGB"},
    "16_Linear": {"precision": 200, "display": "16 bit", "bitDepth": 16, "gamma": "Linear"},
    "16_sRGB": {"precision": 250, "display": "16 bit", "bitDepth": 16, "gamma": "sRGB"},
    "32_Linear": {"precision": 300, "display": "32 bit", "bitDepth": 32, "gamma": "Linear"},
    "32_sRGB": {"precision": 350, "display": "32 bit", "bitDepth": 32, "gamma": "sRGB"},
    "Half-float-16_Linear": {"precision": 500, "display": "Half-float 16", "bitDepth": 16, "gamma": "Linear"},
    "Half-float-16_sRGB": {"precision": 550, "display": "Half-float 16", "bitDepth": 16, "gamma": "sRGB"},
    "Float-32_Linear": {"precision": 600, "display": "Float 32", "bitDepth": 32, "gamma": "Linear"},
    "Float-32_sRGB": {"precision": 650, "display": "Float 32", "bitDepth": 32, "gamma": "sRGB"}
    }



#   Custom logger since Gimps logging is not great
#   This will print to the logfile, and display in Gimps Error Console
class PrismGimpLogger:
    def __init__(self, logLevel, logPath):
        self.logLevel = logLevel
        sys.stderr = open(logPath, 'a')
        sys.stdout = sys.stderr

    #   Debug: will only be printed to logfile unless All
    #   is selected in Prism settings
    def debug(self, message):
        if self.logLevel == "All":
            pdb.gimp_message("PRISM FUNCTIONS:   %s" % message)
            
        logging.warning("PRISM FUNCTIONS:  %s" % message)

    #   Warning: will be printed in both the logfile
    #   and Gimps Error Console
    def warning(self, message):
        if self.logLevel in ["Minimal", "All"]:
            pdb.gimp_message("PRISM FUNCTIONS:   %s" % message)

        logging.warning("PRISM FUNCTIONS:  %s" % message)



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

            log.debug("Connected by:  %s" % str(addr))

            #   Gets large blocks since the StateData can be large-ish
            jData = conn.recv(40960)
            if not jData:
                break
            
            log.debug("Received Data")
            responseData = handleCmd(jData)

            log.debug("Responding")
            if responseData is None:
                responseData = ""
            conn.sendall(responseData.encode())

    #   Not Used right now
    # def stop(self):
    #     if self.socket:
    #         self.socket.close()
    #         self.socket = None
    #         log.warning("Server stopped.")

    #   Not used right now
    # def reset(self):
    #     self.stop()
    #     self.start()
    #     log.warning("Reset Comms")


#   To perform actions when Gimp loads
def initActions():
    global log
    global server
    global logMaxSize

    #   Gets Gimp config items set in Prism settings
    logLevel, logPath, logMaxSize  = getGimpPluginConfig()
    #   Sets custom logger instance
    log = PrismGimpLogger(logLevel, logPath)
    #   Sets socket server instance
    server = PrismServer()


#   Gets config items set in Prism Settings
#   under DCC->Gimp
def getGimpPluginConfig():
    global port
    global logPath
    global logMaxSize

    try:
        with open(CONFIGFILE, 'r') as file:
            gimpSettings = json.load(file)

        # Update global variables with values from gimpSettings dictionary
        port = int(gimpSettings.get("commPort"))
        logLevel = gimpSettings.get("logLevel")
        logPath = gimpSettings.get("logLocation")
        logMaxSize = gimpSettings.get("logMax")

        return logLevel, logPath, logMaxSize

    except FileNotFoundError:
        log.warning("ERROR: Config file %s not found." % CONFIGFILE)

    except Exception as e:
        log.warning("ERROR: Cannot read config file: %s" % e)
        pass


#   Is called with Gimp menu item
def startServer():
    #   Starts log
    handleServerLog()
    #   Checks if server is already running
    if not isServerRunning():
        log.warning("Launching Server")
        server.start()
    else:
        log.warning("Server is already running")
        pass


#   Deals with custom log
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
            log.warning("ERROR: Log Error:  %s" % e)

    else:
        if not os.path.exists(logDir):
            os.mkdir(logDir)


#   To convert cmds to json payload to send over socket
def cmdDataToJson(command, payload):
    log.debug("Creating json for:  %s" % command)

    try:
        pData = {
            "command": command,
            "data": payload
            }
        
        jData = json.dumps(pData)
        return jData
    
    except Exception as e:
        log.warning("ERROR: Cannot code json:  %s" % e)
        return None


#   To convert json payload to cmds
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
        log.warning("ERROR:  Cannot decode json:   %s" % e)
        return None
    
    
#   Checks if server is already running
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
        #   If the bind fails with the error code 10048
        #   (EADDRINUSE equivalent on Windows), the port is already in use
        if e.errno == 10048:
            return True
        
        #   If the bind fails with the error code EADDRINUSE
        #   (for non-Windows systems), the port is already in use
        elif e.errno == errno.EADDRINUSE:
            return True
        
        else:
            log.warning("ERROR: Socket error: %s" % e)
            return False
    finally:
        sock.close()

#   Receives data from socket and handles command
def handleCmd(jData):
    try:
        #   Converts from dict to command/payload
        command, payload = jsonToCmdData(jData)

        log.debug("Command received:   %s" % command)

        if command ==  "saveVersion":
            return saveVersion(payload)
        elif command == "captureScreenShot":
            return captureScreenShot(payload)
        elif command == "saveStates":
            return saveStates(payload)
        elif command == "getStates":
            return getStates(payload)
        elif command == "exportFile":
            return exportFile(payload)
        elif command == "getImageSpecs":
            return getImageSpecs(payload)
        
        else:
            log.warning("ERROR: Invalid Command Received")
            command = "FAILED"
            payload = "FAILED"

    except Exception as e:
        log.warning("ERROR: Error in Command Comms: %s" % e)
        command = "FAILED"
        payload = "FAILED"

    return cmdDataToJson(command, payload)

### ^^^^^ Socket Comms from Prism ^^^^^ ###
##############################################################



#########################################
### vvvvv Functions inside Gimp vvvvv ###

def saveVersion(data):
    log.debug("Saving new version")
    try:
        imagePath = data.get("imagePath")
        savePath = data.get("savePath")

        #   saves the .xcf and receives the original image
        currentFile = saveXCF(imagePath, savePath)
        #   Loads the newly saved image
        newFile = openXCF(currentFile, savePath)
        #   Handles the display of the new image
        switchUIimages(currentFile, newFile)

        sendCommand = "Success"
        sendPayload = {"filePath": savePath}
        log.debug("New Version Saved")

    except Exception as e:
        log.warning("ERROR: Failed to save version: \n%s" % e)
        sendCommand = "Failed"
        sendPayload = None

    #   Refreshes UI
    pdb.gimp_progress_end()
    pdb.gimp_displays_flush()

    jData = cmdDataToJson(sendCommand, sendPayload)
    return jData


#   Saves currently open image to the supplied filepath
def saveXCF(imagePath, savePath):

    log.debug("Saving .XCF")
    try:
        #   Checks if the image is alreadt an .xcf
        if os.path.splitext(imagePath)[1] == ".xcf":
            currentImage = getImageFromPath(imagePath)
        else:
            #   Loads the non-.xcf into a new temp image
            currentImage = pdb.file_png_load(imagePath, imagePath)

        currentDrawable = pdb.gimp_image_get_active_layer(currentImage)
        #   Saves the image to .xcf using supplied Prism Path
        pdb.gimp_xcf_save(1, currentImage, currentDrawable, savePath, savePath)

    except Exception as e:
        log.warning("ERROR: Failed to Save XCF")
        return None

    return currentImage


#   Self explanitory
def openXCF(currentFile, filePath):
    try:
        newImage = pdb.gimp_xcf_load(1, filePath, filePath)
        return newImage
    except:
        log.debug("Could not load new image")
        return currentFile


def exportFile(data):
    log.debug("Exporting Image")
    try:
        #   Checks there is an open image
        numImages, image_ids = pdb.gimp_image_list()
        if numImages < 1:
            return False
        
        rSettings = data.get("rSettings")
        #   Gets Gimp Image from supplied filepath
        currentImage = getImageFromPath(data.get("imagePath"))
        currentDrawable = pdb.gimp_image_get_active_layer(currentImage)
        filePath = rSettings["outputName"]
        outputType = rSettings["outputType"]

        exportFuncts = {".png": exportPNG,
                        ".exr": exportEXR,
                        ".jpg": exportJPG,
                        ".psd": exportPSD,
                        ".tif": exportTIFF
                        }
        
        # Call the appropriate export function
        if outputType in exportFuncts:
            log.debug("Exporting %s" % outputType)
            result = exportFuncts[outputType](rSettings, currentImage, currentDrawable, filePath)
        else:
            log.warning("Export file type not supported")

        if result:
            sendPayload = "Result=Success"
        else:
            sendPayload = "Result=Failed"

    except:
        log.warning("ERROR: Failed to Export Image")
        sendPayload = "Result=Failed"

    #   Refreshes UI
    pdb.gimp_progress_end()
    pdb.gimp_displays_flush()

    sendCommand = "Result"
    jData = cmdDataToJson(sendCommand, sendPayload)
    return jData


def exportPNG(rSettings, currentImage, currentDrawable, filePath):
    png_Compress = int(rSettings["png_Compress"]) - 1    #   so that GUI is 1-10
    png_Interlaced = rSettings["png_Interlaced"]
    png_Gamma = rSettings["png_Gamma"]
    png_Rez = rSettings["png_Rez"]
    png_BgColor = rSettings["png_BgColor"]
    png_LayerOffset = rSettings["png_LayerOffset"]
    png_AlphaColor = rSettings["png_AlphaColor"]
    exportGamma = rSettings["outputGamma"]
    colorMode = rSettings["colorMode"]
    bitDepth = rSettings["bitDepth"]
    exportScale = int(rSettings["exportScale"])
    alphaFill = rSettings["alphaFill"]
    exportFormat = rSettings["outputType"]
    
    #   Creates temp export image
    tempImage, tempLayer = createTempImage(currentImage,
                                           exportFormat,
                                           exportGamma,
                                           exportScale,
                                           colorMode,
                                           bitDepth,
                                           alphaFill)

    log.debug("Exporting PNG")

    #   Sends to save method
    result = savePNG(tempImage,
                        tempLayer,
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
    
    #   Removes temp image
    pdb.gimp_image_delete(tempImage)
    #   Removes unsaved changes flag
    pdb.gimp_image_clean_all(currentImage)


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

        log.debug("Saved PNG")
        return True

    except Exception as e:
        log.warning("ERROR:  %s" % e)
        return False


def exportEXR(rSettings, currentImage, currentDrawable, filePath):
    colorMode = rSettings["colorMode"]
    bitDepth = rSettings["bitDepth"]
    exportScale = int(rSettings["exportScale"])
    alphaFill = rSettings["alphaFill"]
    exportGamma = rSettings["outputGamma"]
    exportFormat = rSettings["outputType"]

    #   Creates temp export image
    tempImage, tempLayer = createTempImage(currentImage,
                                           exportFormat,
                                           exportGamma,
                                           exportScale,
                                           colorMode,
                                           bitDepth,
                                           alphaFill)

    log.debug("Exporting EXR")

    #   Sends to save method
    result = saveEXR(tempImage,
                        tempLayer,
                        filePath,
                        )
    
    #   Removes temp image
    pdb.gimp_image_delete(tempImage)
    #   Removes unsaved changes flag
    pdb.gimp_image_clean_all(currentImage)

    return result


def saveEXR(image=None,        #   Unfortunatly all the options Gimps API has
            drawable=None,
            filePath=None,
            ):

    try: 
        pdb.file_exr_save(image,
                           drawable,
                           filePath,
                           filePath)
        
        log.debug("Saved EXR")
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
    baseline = rSettings["jpg_Baseline"]
    colorMode = rSettings["colorMode"]
    bitDepth = rSettings["bitDepth"]
    exportScale = int(rSettings["exportScale"])
    alphaFill = rSettings["alphaFill"]
    exportGamma = rSettings["outputGamma"]
    exportFormat = rSettings["outputType"]

    #   Creates temp export image
    tempImage, tempLayer = createTempImage(currentImage,
                                           exportFormat,
                                           exportGamma,
                                           exportScale,
                                           colorMode,
                                           bitDepth,
                                           alphaFill)

    log.debug("Saving JPG")

    #   Sends to save method
    result = saveJPG(tempImage,
                        tempLayer,
                        filePath,
                        quality,
                        smoothing,
                        optimize,
                        progressive,
                        "",
                        subSample,
                        baseline
                        )

    #   Removes temp image
    pdb.gimp_image_delete(tempImage)
    #   Removes unsaved changes flag
    pdb.gimp_image_clean_all(currentImage)

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
        
        log.debug("Saved JPG")

        return True

    except Exception as e:
        log.warning("ERROR:  ", e)
        return False
    

#   Saves as a .psd to the Media Tab
def exportPSD(rSettings, currentImage, currentDrawable, filePath):

    log.debug("Saving PSD")

    #   Sends to save method
    result = savePSD(currentImage,
                     currentDrawable,
                     filePath)

    #   Removes unsaved changes flag
    pdb.gimp_image_clean_all(currentImage)

    return result


def savePSD(image=None,
            drawable=None,
            filePath=None,
            compression=0,
            fillOrder=0
            ):

    try: 
        pdb.file_psd_save(image,
                           drawable,
                           filePath,
                           filePath,
                           compression,
                           fillOrder)
                
        log.debug("Saved PSD")

        return True

    except Exception as e:
        log.warning("ERROR:  ", e)
        return False


def exportTIFF(rSettings, currentImage, currentDrawable, filePath):
    bgLayer = False

    compression = rSettings["tiff_Compression"]
    useBigTIFF = rSettings["tiff_useBigTiff"]
    saveTransPx = rSettings["tiff_SaveTransPx"]
    colorMode = rSettings["colorMode"]
    bitDepth = rSettings["bitDepth"]
    exportScale = int(rSettings["exportScale"])
    alphaFill = rSettings["alphaFill"]
    exportGamma = rSettings["outputGamma"]
    exportFormat = rSettings["outputType"]

    tiffCompressMap = {"None": 0,
                       "LZW (lossless)": 1,
                       "Pack Bits (lossless)": 2,
                       "Deflate (lossless)": 3,
                       "JPEG (lossy)": 4
                        }
    
    compressCode = tiffCompressMap.get(compression)

    #   Creates temp export image
    tempImage, tempLayer = createTempImage(currentImage,
                                           exportFormat,
                                           exportGamma,
                                           exportScale,
                                           colorMode,
                                           bitDepth,
                                           alphaFill)

    log.debug("Saving TIFF")

    #   Sends to save method
    result = saveTIFF(tempImage,
                      tempLayer,
                      filePath,
                      compressCode,
                      boolToBit(useBigTIFF),
                      boolToBit(saveTransPx)
                      )

    #   Removes temp image
    pdb.gimp_image_delete(tempImage)
    #   Removes unsaved changes flag
    pdb.gimp_image_clean_all(currentImage)

    return result


def saveTIFF(image=None,
            drawable=None,
            filePath=None,
            compression=3,
            useBigTiff=0,
            saveTransPx=0
            ):

    try:
        #   For Gimp bug with filenaming using tiff bigTiff & save2
        fileHack = "file:///%s" % filePath

        if useBigTiff == 1:
            pdb.file_bigtiff_save(image,
                                drawable,
                                fileHack,
                                fileHack,
                                compression,
                                saveTransPx,
                                useBigTiff)
            
            log.debug("Saved BigTIFF")
            return True
        
        else:
            pdb.file_tiff_save2(image,
                                drawable,
                                fileHack,
                                fileHack,
                                compression,
                                saveTransPx)
            
            log.debug("Saved Tiff using save2")
            return True

    #   Fallback in case using the file hack fails or they fix it
    except RuntimeError: 
        pdb.file_tiff_save(image,
                            drawable,
                            filePath,
                            filePath,
                            compression
                            )
        
        log.debug("Saved Fallback TIFF")

        return True

    except Exception as e:
        log.warning("ERROR:  ", e)
        return False


#   Gets Gimp Image from supplied filepath
def getImageFromPath(imagePath):
    #   Iterates through open images and finds the image matching the name

    log.debug("Getting Gimp Image")

    try:
        fileName = os.path.basename(imagePath)
        for image in gimp.image_list():
            if image.name == fileName:
                log.debug("Resolved Image from Path")
                return image
    except:    
        log.debug("ERROR: Failed to get Gimp Image from Path")
        return None


#   Converts Gimp 0/1 to True/False
def bitToBool(binary):
    if binary == 1:
        bool = True
    else:
        bool = False
    return bool


#   Converts True/False to Gimp 0/1
def boolToBit(bool):
    if bool == True:
        return 1
    else:
        return 0


def switchUIimages(oldImage, newImage):
    #   Try to reconnect, works if it is already a .xcf
    try:
        log.debug("Swapping UI Images")
        pdb.gimp_displays_reconnect(oldImage, newImage)

    #   If it was an imported image, will open in new tab
    except:
        log.debug("Opening new image")

        gimp.Display(newImage)
        gimp.displays_flush()
    #   Makes the open file not show needs saving
    pdb.gimp_image_clean_all(newImage)


def captureScreenShot(data):
    log.debug("Taking Screenshot")
    #   Gets image from supplied filepath
    currentImage = getImageFromPath(data.get("imagePath"))
    currentDrawable = pdb.gimp_image_get_active_layer(currentImage)
    ssPath = data.get("ssPath")

    try:
        #   If there is alpha
        if imageHasAlpha(currentImage):
            #   Loads the checker image from plugin folder
            alphaBGLayer = pdb.gimp_file_load_layer(currentImage, ALPHA_BG_FILE)
            numLayers, _ = pdb.gimp_image_get_layers(currentImage)
            #   Gets current image size
            xRez, yRez = getImageRez(currentImage)
            #   Inserts the checker at the bottom
            pdb.gimp_image_insert_layer(currentImage, alphaBGLayer, None, numLayers + 1)
            pdb.gimp_layer_scale(alphaBGLayer, xRez, yRez, False)

            #   Flattens the image to a temp layer
            mergedLayer = pdb.gimp_layer_new_from_visible(currentImage,
                                                          currentImage,
                                                          "tempVisable")
            
            #   Saves the temp layer to the supplied temp path
            result = saveJPG(currentImage, mergedLayer, ssPath)
            #   Delete temp layer
            pdb.gimp_image_remove_layer(currentImage, alphaBGLayer)
            #   Cleans and refreshes UI
            pdb.gimp_image_clean_all(currentImage)
            pdb.gimp_displays_flush()

        else:
            result = saveJPG(currentImage, currentDrawable, ssPath)

        if result:
            sendCommand = "Success"
        else:
            log.warning("ERROR: Screenshot Failed")
            sendCommand = "Failed"

    except Exception as e:
        log.warning("ERROR: Screenshot Failed:  %s" % e)
        sendCommand = "Failed"

    #   Refreshes UI
    pdb.gimp_progress_end()
    pdb.gimp_displays_flush()
    
    sendPayload = {"filePath": ssPath}

    jData = cmdDataToJson(sendCommand, sendPayload)
    return jData


def createTempImage(currentImage,
                    exportFormat,
                    exportGamma,
                    exportScale,
                    exportColorMode,
                    exportBitDepth,
                    alphaFill
                    ):

    log.debug("Creating Temp Image")

    #   Gets image resolution
    xRez, yRez = getImageRez(currentImage)
    #   Creates copy to temp image
    tempImage = pdb.gimp_image_duplicate(currentImage)

    log.debug("Converting Bit Depth of Temp Image")
    try:
        #   Converts bitDepth to Gimp code
        bitDepthCode = getBitDepthCode(exportFormat, exportGamma, exportBitDepth)
        log.debug("bitDepthCode: %s" % bitDepthCode)                                    #   TESTING

        #   Converts temp image to new bit depth
        pdb.gimp_image_convert_precision(tempImage, bitDepthCode)
    except:
        log.warning("ERROR: Failed to convert image's bit depth")

    log.debug("Applying Alpha Background to Temp Image")
    #   Checks if bottom layer has alpha
    if exportColorMode not in ["RGBA", "GRAYA"]:
        try:
            if imageHasAlpha(tempImage):
                #   Fills BG with selected type
                fillAlphaBG(tempImage, alphaFill)
            #   Flattens to remove alpha channel
            mergedLayer = pdb.gimp_image_flatten(tempImage)
        except:
            log.warning("ERROR: Failed to apply alpha background")

    else:
        #   Merge visable to keep alpha channel if output is RGBA or GRAYA
        mergedLayer = pdb.gimp_image_merge_visible_layers(tempImage, 1)

    log.debug("Converting Temp Image Color Mode")
    try:
        #   Converts to GRAY if needed
        if getColorMode(mergedLayer) == "RGB":
            if exportColorMode in ["GRAY", "GRAYA"]:
                pdb.gimp_image_convert_grayscale(tempImage)

        #   Converts to RGB if needed
        elif getColorMode(mergedLayer) == "GRAY":
            if exportColorMode in ["RGB", "RGBA"]:
                pdb.gimp_image_convert_rgb(tempImage)
    except Exception as e:
        log.warning("ERROR: Cannot convert color mode")

    log.debug("Scaling Temp Image")
    try:
        #   Scales image from options
        if exportScale != 100:
            xRez = (xRez * exportScale) / 100
            yRez = (yRez * exportScale) / 100
            pdb.gimp_layer_scale_full(mergedLayer, xRez, yRez, 1, 2)
    except Exception as e:
        log.warning("ERROR: Cannot scale image")

    return tempImage, mergedLayer


#   Used to fill the background of alpha images if needed
def fillAlphaBG(image, alphaFill):
    try:
        #   Gets rez of original image
        xRez, yRez = getImageRez(image)
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

            #   Sets foreground color
            pdb.gimp_context_set_foreground(fillColor)
            #   Fills layer with FG color
            pdb.gimp_drawable_fill(bgLayer, 0)  
            #   Reset Fg color to original
            pdb.gimp_context_set_foreground(origFgColor)  

        #   inserts this temp layer at the bottom
        pdb.gimp_image_insert_layer(image, bgLayer, None, numLayers + 1)
        #   scales temp layer to image size
        pdb.gimp_layer_scale(bgLayer, xRez, yRez, False)

        return bgLayer
    
    except Exception as e:
        log.warning("ERROR: Failed to generate background:\n%s" % e)
        return None


#   Saves StateManager states
def saveStates(data):
    #   Gets number of open images
    numImages, image_ids = pdb.gimp_image_list()
    #   Checks that an image is open
    if numImages > 0:
        try:
            #   Gets Gimp Image from supplied filepath
            currentImage = getImageFromPath(data.get("imagePath"))
            #   Get State data
            stateData = data.get("stateData")
            #   Attaches State data to the image
            currentImage.attach_new_parasite("stateData", 5, stateData)

            log.debug("Saved States")
            sendCommand = "Success"
        
        except:
            log.warning("ERROR: Save State Failed")
            sendCommand = "Failed"
    else:
        log.warning("ERROR: No image open")
        sendCommand = "Failed"

    sendPayload = ""

    jData = cmdDataToJson(sendCommand, sendPayload)
    return jData


def getImageSpecs(data):
    numImages, image_ids = pdb.gimp_image_list()
    #   Checks that an image is open
    if numImages > 0:
        #   Gets Gimp Image from supplied filepath
        currentImage = getImageFromPath(data.get("imagePath"))
        currentDrawable = pdb.gimp_image_get_active_layer(currentImage)

        try:
            xRez, yRez = getImageRez(currentImage)
            bitDepth, gamma = getBitDepthGamma(currentImage)
            colorMode = getColorMode(currentDrawable)
            hasAlpha = imageHasAlpha(currentImage)

            specData = {"xRez": xRez,
                        "yRez": yRez,
                        "bitDepth": bitDepth,
                        "gamma": gamma,
                        "colorMode": colorMode,
                        "hasAlpha": hasAlpha}
            
            sendCommand = "imageSpecs"
            sendPayload = {"imageSpecs": specData}
       
            jData = cmdDataToJson(sendCommand, sendPayload)
            return jData

        except Exception as e:
            log.warning("ERROR in getting Image Details:  %s" % e)
            return "", ""


#   Gets StateManager states from image
def getStates(data):
    #   Gets number of open images
    numImages, image_ids = pdb.gimp_image_list()
    #   Checks that an image is open
    if numImages > 0:
        #   Gets Gimp Image from supplied filepath
        currentImage = getImageFromPath(data.get("imagePath"))

        try:
            #   Gets parasite from image
            parasite  = currentImage.parasite_find("stateData")
            if parasite:
                stateData = json.loads(parasite.data)
                log.debug("State data retrieved")

            else:
                log.debug("No State data in Image")
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


def getImageRez(image):
    try:
        xRez = pdb.gimp_image_width(image)
        yRez = pdb.gimp_image_height(image)
        return xRez, yRez
    except:
        return " - ", " - "


#   Returns image Color Mode
def getColorMode(drawable):
    try:
        isGrayBinary = pdb.gimp_drawable_is_gray(drawable)
        if bitToBool(isGrayBinary):
            colorMode = "GRAY"
        else:
            colorMode = "RGB"
        return colorMode
    except:
        return " - "


#   Returns BitDepth and Display gamma from Gimp's precision code
def getBitDepthGamma(image):
    try:
        #   Gets image precision code
        precision = pdb.gimp_image_get_precision(image)

        #   Looks in dict to find code
        for key, value in COLORMODEDATA.items():
            if value["precision"] == precision:
                bitDepth = value["display"]
                gamma = value["gamma"]

                return bitDepth, gamma

        return " - ", " - "
    
    except:
        log.warning("ERROR: Cannot get images bitDepth")
        return " - ", " - "
    

def getBitDepthCode(format, gamma, bitDepth):
    #   Seperates dict to float for .exr
    if format == ".exr":
        filtered_data = {key: value for key, value in COLORMODEDATA.items() if value["precision"] >= 500}
    #   and integer for other formats
    else:
        filtered_data = {key: value for key, value in COLORMODEDATA.items() if value["precision"] < 500}
    #   Matches gamma and bitDepth in dict
    for key, value in filtered_data.items():
        if value["gamma"] == gamma and value["bitDepth"] == int(bitDepth):
            #   Returns matching Gimp code
            return value["precision"]
        
    return None


#   Returns if the bottom layer has an alpha channel
def imageHasAlpha(image):
    try:
        btmLayer = image.layers[-1]
        hasAlpha = pdb.gimp_drawable_has_alpha(btmLayer)
        return bitToBool(hasAlpha)
    except:
        log.warning("ERROR: Alpha check failed")
        return True



initActions()   #   Run init actions such getting config info and setting up logger



# ### vvvvv REGISTER PLUG-IN vvvvv ###

helpDoc = r"""
Menu items and functions for intergration
with Prism Pipeline
"""

attribution = "Prism: Richard Frangenberg\nPlugin: Joshua Breckeen"
copyright = "GNU LGPL-3.0-or-later"

# # START SERVER
register(
    "python-fu_prism_serverStart",                              #   UNIQUE NAME
    "Enables socket communications\nbetween Prism and Gimp",    #   TOOLTIP
    helpDoc,                                                    #   DESCRIPTION
    attribution,                                                #   AUTHORS NAME
    copyright,                                                  #   COPYRIGHT INFO
    "2023",                                                     #   VERSION or DATA
    "1 - Start Prism Server",                                   #   NAME DISPLAYED IN GUI MENU
    "",                                                         #   TYPE OF DRAWABLE: '' = can be none, * = any drawable, RGB, RGB, RGB* etc
    [],                                                         #   ADDITIONAL ARGS
    [],                                                         #   RETURN TYPES
    startServer,                                                #   FUNCTION CALLED WHEN ACTIVATED
    "<Image>/Prism",                                            #   WHERE IN GIMP UI
)

main()