
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
###########################################################################
#
#                    Gimp Integration for Prism2
#
#       https://github.com/AltaArts/Gimp_Integration--Prism-Plugin
#
#
#                           Joshua Breckeen
#                              Alta Arts
#                          josh@alta-arts.com
#
###########################################################################

###########################################################################
#                                                                         #
#   This is a Collection of Helper Functions for the Prism Gimp Plugin.   #
#                                                                         #


import os
import sys
import json
import datetime
import ctypes
import socket
import tempfile
import threading


PRISM_ROOT = r"@PRISMROOTREPLACE@"
GIMP_PLUGIN_ROOT = r"@GIMPPLUINREPLACE@"
SETTINGS_FILENAME = "Prism_Gimp_Settings.json"
LOG_FILENAME = "Prism_Gimp_Log.log"
HOST_SCRIPT_NAME = "Prism_Host.py"


###################################
##            SETTINGS           ##

def getPrismPythonRoot() -> str | None:
    '''Searches for the Prism Python root directory and returns its path.'''

    pythonDirs = []

    try:
        for entry_name in os.listdir(PRISM_ROOT):
            entry_path = os.path.join(PRISM_ROOT, entry_name)

            if not os.path.isdir(entry_path):
                continue

            if not entry_name.startswith("Python3"):
                continue

            ver_suffix = entry_name.removeprefix("Python")
            ver_key = tuple(int(part) for part in ver_suffix.split(".") if part.isdigit())
            pythonDirs.append((ver_key, entry_path))

    except Exception:
        return None

    if not pythonDirs:
        return None

    pythonDirs.sort(reverse=True)
    return pythonDirs[0][1]


def getSettingsPath() -> str:
    '''Returns the file path to the settings file.'''

    if not GIMP_PLUGIN_ROOT or GIMP_PLUGIN_ROOT.startswith("@"):
        raise RuntimeError("GIMP_PLUGIN_ROOT is not configured.")

    return os.path.join(GIMP_PLUGIN_ROOT, SETTINGS_FILENAME)


def loadSettings() -> dict:
    '''Loads and validates the settings from the settings file.'''

    settingsPath = getSettingsPath()

    try:
        with open(settingsPath, "r", encoding="utf-8") as handle:
            settings = json.load(handle)

    except FileNotFoundError as exc:
        raise RuntimeError(f"Prism Gimp settings file not found: {settingsPath}") from exc
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Prism Gimp settings file is not valid JSON: {settingsPath}") from exc

    if not isinstance(settings, dict):
           raise RuntimeError(f"Prism Gimp settings file must contain a JSON object: {settingsPath}")

    #   Key to Check Exists in Settings
    required_keys = [
        "bridgePort_out",
        "bridgePort_in",
        "hostStartTimeout",
        "log_fileName",
        "log_maxBytes",
        "attribution",
    ]

    #   Check for Missing Keys
    missing_keys = [key for key in required_keys if key not in settings]
    if missing_keys:
           raise RuntimeError(f"Prism Gimp settings file is missing keys: {', '.join(missing_keys)}")

    #   Validate and Convert Types
    try:
        settings["bridgePort_out"] = int(settings["bridgePort_out"])
    except Exception as exc:
        raise RuntimeError("'bridgePort_out' must be an integer.") from exc

    try:
        settings["bridgePort_in"] = int(settings["bridgePort_in"])
    except Exception as exc:
        raise RuntimeError("'bridgePort_in' must be an integer.") from exc

    try:
        settings["hostStartTimeout"] = float(settings["hostStartTimeout"])
    except Exception as exc:
        raise RuntimeError("'hostStartTimeout' must be a number.") from exc

    try:
        settings["log_maxBytes"] = int(settings["log_maxBytes"])
    except Exception as exc:
        raise RuntimeError("'log_maxBytes' must be an integer.") from exc

    attribution = settings["attribution"]
    if not isinstance(attribution, (list, tuple)) or len(attribution) != 3:
        raise RuntimeError("'attribution' must contain exactly three values.")

    settings["attribution"] = tuple(str(value) for value in attribution)

    return settings


def readSettingsData() -> dict:
    '''Reads the settings data from the settings file.'''

    settingsPath = getSettingsPath()

    with open(settingsPath, "r", encoding="utf-8") as handle:
        sData = json.load(handle)

    if not isinstance(sData, dict):
           raise RuntimeError(f"Prism Gimp settings file must contain a JSON object: {settingsPath}")

    return sData


def writeSettingsData(sData:dict) -> None:
    '''Writes the settings data to the settings file.'''

    if sData is None:
        raise RuntimeError("sData is required.")

    settingsPath = getSettingsPath()
    temp_path = f"{settingsPath}.tmp"

    with open(temp_path, "w", encoding="utf-8") as handle:
        json.dump(sData, handle, indent=4)
        handle.write("\n")

    os.replace(temp_path, settingsPath)


def updateSettingState(**updates) -> None:
    '''Updates the settings data with new values.\n
       If a value is None, the key will be removed from the settings data.'''
    
    sData = readSettingsData()

    for key, value in updates.items():
        if value is None:
            sData.pop(key, None)
        else:
            sData[key] = value

    writeSettingsData(sData)


###################################
##            LOGGING            ##

def getLogPath() -> str:
    '''Returns the file path to the log file.'''

    return os.path.join(tempfile.gettempdir(), LOG_FILENAME)


def getBackupLogPath() -> str:
    '''Returns the file path to the backup log file.'''

    log_name, log_ext = os.path.splitext(LOG_FILENAME)
    backup_name = f"{log_name}_old{log_ext}"

    return os.path.join(tempfile.gettempdir(), backup_name)


def rotateLog(settings:dict, logLock:threading.Lock) -> None:
    '''Rotates the log file if it exceeds the maximum size specified in the settings.'''

    log_path = getLogPath()

    with logLock:
        try:
            curr_size = os.path.getsize(log_path)
        except OSError:
            curr_size = 0

        if curr_size < settings["log_maxBytes"]:
            return

        backup_path = getBackupLogPath()

        try:
            if os.path.exists(backup_path):
                os.remove(backup_path)
        except OSError:
            pass

        try:
            if os.path.exists(log_path):
                os.replace(log_path, backup_path)
        except OSError:
            pass


def formatLogLine(message:str, source_label:str, **fields) -> str:
    '''Formats a log line with the given message, source label, and additional fields.'''
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    details = " ".join(f"{key}={value!r}" for key, value in fields.items())
    line = f"[{timestamp}] [{source_label}] {message}"

    if details:
        line = f"{line} | {details}"

    return f"{line}\n"


###################################
##          PROCESSES            ##

def readHostPid() -> int | None:
    '''Reads the host process ID from the settings data. Returns None if not found or invalid.'''

    try:
        host_pid = readSettingsData().get("HOST_PID")
        if host_pid in [None, ""]:
            return None
        return int(host_pid)

    except Exception:
        return None


def isProcessRunning(process_id:int) -> bool:
    '''Checks if a process with the given process ID is currently running.'''

    if not process_id or process_id <= 0:
        return False

    if os.name == "nt":
        try:
            #    Windows Query Basic Process Info (exit code/state)
            processQuery = 0x1000
            #    Windows GetExitCodeProcess returns 259 while the process is still running
            still_active = 259

            kernel32 = ctypes.windll.kernel32
            kernel32.SetLastError(0)
            process_handle = kernel32.OpenProcess(processQuery, False, process_id)

            if not process_handle:
                return False

            exit_code = ctypes.c_ulong()

            try:
                if not kernel32.GetExitCodeProcess(process_handle, ctypes.byref(exit_code)):
                    return True

                return exit_code.value == still_active
            
            finally:
                kernel32.CloseHandle(process_handle)

        except Exception:
            pass

    try:
        #    Signal 0 is an Alive Probe (does not actually kill)
        os.kill(process_id, 0)

    #    Process Exists, but Not Allowed to Signal it
    except PermissionError:
        return True
    #   Does Not Exist
    except OSError:
        return False

    #   Exists
    return True


def terminateProcess(process_id:int) -> None:
    '''Attempts to terminate the process with the given process ID.'''

    if not process_id or process_id <= 0:
        return

    if os.name == "nt":
        try:
            process_terminate = 0x0001
            kernel32 = ctypes.windll.kernel32
            process_handle = kernel32.OpenProcess(process_terminate, False, process_id)

            if process_handle:
                try:
                    kernel32.TerminateProcess(process_handle, 1)
                    return
                finally:
                    kernel32.CloseHandle(process_handle)
        except Exception:
            pass

    try:
        import signal
        os.kill(process_id, signal.SIGTERM)

    except Exception:
        pass


###################################
##        COMMUNICATIONS         ##

def canConnectToPrism(port_out:int, timeout:float=0.25) -> bool:
    '''Checks if a connection can be established to the Prism host.'''

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.settimeout(timeout)
            client.connect(("127.0.0.1", port_out))
        return True

    except Exception:
        return False


def sendJsonRequest(port:int, message:dict, timeout:float=1.0, host:str="127.0.0.1") -> dict:
    '''Sends a JSON request to Localhost and Returns the Response.'''

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.settimeout(timeout)
        client.connect((host, port))
        client.sendall(json.dumps(message).encode("utf-8"))
        rawResponse = client.recv(65536)

    if not rawResponse:
        raise RuntimeError("Socket endpoint returned no response")

    return json.loads(rawResponse.decode("utf-8"))


def getHostScriptPath() -> str:
    '''Constructs the file path to the host script.'''

    return os.path.join(os.path.dirname(__file__), HOST_SCRIPT_NAME)


def removeHostPidState(process_id=None, addToLog=None) -> None:
    '''Removes the host process ID state from the settings data if it matches the given process ID.'''

    if process_id is not None and readHostPid() != process_id:
        return

    try:
        updateSettingState(HOST_PID=None)
        if addToLog:
            addToLog("Removed host pid state")

    except FileNotFoundError:
        return
    except Exception as exc:
        if addToLog:
            addToLog("Failed to remove host pid state", error=str(exc))


def getHostPythonCommands() -> list:
    '''Determines the list of Python commands to attempt when launching the Prism host.'''
    
    commands = []
    override = os.environ.get("PRISM_GIMP_PYTHON")

    if override:
        commands.append([override])

    prismPythonRoot = getPrismPythonRoot()
    if prismPythonRoot:
        prism_pythonw = os.path.join(prismPythonRoot, "pythonw.exe")
        prism_python = os.path.join(prismPythonRoot, "python.exe")

        if os.path.exists(prism_pythonw):
            commands.append([prism_pythonw])

        if os.path.exists(prism_python):
            commands.append([prism_python])

    #   Avoid Falling Back to the GIMP-embedded Python.
    #   Prism Host must Run with Prism's Python and Qt libs.
    prismPythonRoot_norm = os.path.normcase(os.path.normpath(prismPythonRoot or ""))
    sysExec_norm = os.path.normcase(os.path.normpath(sys.executable or ""))

    if prismPythonRoot_norm and sysExec_norm.startswith(prismPythonRoot_norm):
        commands.append([sys.executable])

    unique_commands = []
    seen = set()
    for command in commands:
        key = tuple(command)
        if key not in seen:
            seen.add(key)
            unique_commands.append(command)

    return unique_commands


###################################
##        IMAGE HANDLING         ##

def isImageDirty(image:object) -> bool | None:
    '''Returns the dirty state of a Gimp image object.'''
    
    if image is None:
        return None

    for getter_name in ["is_dirty", "get_dirty"]:
        getter = getattr(image, getter_name, None)
        if callable(getter):
            try:
                return bool(getter())
            except Exception:
                continue

    dirty_value = getattr(image, "dirty", None)
    if isinstance(dirty_value, bool):
        return dirty_value

    return None


def getImageId(image:object) -> int | None:
    '''Returns a per-process ID for a Gimp image object.'''

    if image is None:
        return None

    image_id_getter = getattr(image, "get_id", None)
    if callable(image_id_getter):
        try:
            image_id = int(image_id_getter())
            if image_id > 0:
                return image_id
        except Exception:
            pass

    return id(image)


def getImageSize(image) -> tuple[int, int]:
    '''Returns image width and height, trying multiple getter names.'''

    w, h = 0, 0
    for attr in ["get_width", "width"]:
        getter = getattr(image, attr, None)
        if callable(getter):
            try:
                w = int(getter())
                break
            except Exception:
                pass
    for attr in ["get_height", "height"]:
        getter = getattr(image, attr, None)
        if callable(getter):
            try:
                h = int(getter())
                break
            except Exception:
                pass
    return w, h


###################################
##         DATA HANDLING         ##

def normalizeGimpItems(rawItems:object) -> list:
    '''Normalizes the output of Gimp getters to a flat list of items.'''

    if rawItems is None:
        return []

    if isinstance(rawItems, tuple):
        if len(rawItems) == 2 and isinstance(rawItems[0], int):
            rawItems = rawItems[1]
        elif len(rawItems) == 1:
            rawItems = rawItems[0]

    if not isinstance(rawItems, (list, tuple)):
        rawItems = [rawItems]

    return [item for item in rawItems if item]


def toBytes(value:object) -> bytes:
    '''Converts byte-like values from Gimp/GLib APIs into Python bytes.'''

    if value is None:
        return b""

    if isinstance(value, bytes):
        return value

    if isinstance(value, bytearray):
        return bytes(value)

    if isinstance(value, memoryview):
        return value.tobytes()

    if isinstance(value, list) and value and all(isinstance(item, int) for item in value):
        try:
            return bytes(value)
        except Exception:
            return b""

    get_data = getattr(value, "get_data", None)
    if callable(get_data):
        try:
            data = get_data()
            if isinstance(data, tuple):
                data = data[0] if data else b""
            return toBytes(data)
        except Exception:
            pass

    return b""


def unpackValue(value:object) -> object:
    '''Unpacks nested GI/PDB return values into plain Python values.'''

    unpack = getattr(value, "unpack", None)
    if callable(unpack):
        try:
            return unpack()
        except Exception:
            return value

    return value


def flattenValues(value:object) -> list:
    '''Flattens nested tuples/lists for easier result parsing.'''
    
    unpacked = unpackValue(value)

    #   Handle Gimp.ValueArray returns explicitly (common PDB return type).
    class_name = type(unpacked).__name__
    if "ValueArray" in class_name:
        items = []

        count = None
        for count_name in ["length", "get_length", "n_values", "get_n_values"]:
            count_getter = getattr(unpacked, count_name, None)
            if callable(count_getter):
                try:
                    count = int(count_getter())
                    break
                except Exception:
                    continue

        if count is not None and count >= 0:
            for idx in range(count):
                item = None
                for item_getter_name in ["index", "get_value", "get", "nth", "get_item"]:
                    item_getter = getattr(unpacked, item_getter_name, None)
                    if not callable(item_getter):
                        continue

                    try:
                        item = item_getter(idx)
                        break
                    except Exception:
                        continue

                if item is not None:
                    items.append(item)

        if not items:
            try:
                items = list(unpacked)
            except Exception:
                items = []

        if items:
            result = []
            for item in items:
                result.extend(flattenValues(item))
            return result

    if isinstance(unpacked, (list, tuple)):
        result = []
        for item in unpacked:
            result.extend(flattenValues(item))
        return result

    return [unpacked]


def setConfigValue(config:object, key:object, value:object) -> None:
    '''Sets a config property while ignoring unsupported keys/values.'''

    if value is None:
        return

    try:
        config.set_property(key, value)
        return
    except Exception:
        if not isinstance(key, str):
            return

    #   Some GI Bindings Use Underscores While C uses Hyphens - Try Alt First
    alt_key = None
    if "-" in key:
        alt_key = key.replace("-", "_")
    elif "_" in key:
        alt_key = key.replace("_", "-")

    if not alt_key or alt_key == key:
        return

    try:
        config.set_property(alt_key, value)
    except Exception:
        pass


def callWithSignatures(func:object, signatures:list) -> tuple[object, str | None]:
    '''Tries a callable against multiple argument signatures and returns the first success.'''

    errors = []

    for args in signatures:
        try:
            return func(*args), None
        except Exception as exc:
            errors.append(f"args={args}: {exc}")

    return None, "; ".join(errors)



    ###################################################
    ##              GIMP RESULT PARSERS             ##
    ###################################################

def summarizeRequest(request:object) -> dict:
    '''Summarizes a request payload for concise logging.'''

    if not isinstance(request, dict):
        return {"request_type": type(request).__name__}

    return {
        "action": request.get("action") or request.get("command"),
        "keys": sorted(request.keys()),
    }


def extractLayerFromResult(rawResult:object) -> object | None:
    '''Extracts the first layer-like object from GI/PDB result values.'''

    for value in flattenValues(rawResult):
        if value is None:
            continue

        has_name = callable(getattr(value, "get_name", None))
        has_alpha = callable(getattr(value, "has_alpha", None))
        has_mode = callable(getattr(value, "get_mode", None))
        if has_name and (has_alpha or has_mode):
            return value

    return None


def extractImageFromResult(rawResult:object) -> object | None:
    '''Extracts the first image-like object from GI/PDB result values.'''

    for value in flattenValues(rawResult):
        if value is None:
            continue

        has_width = callable(getattr(value, "get_width", None))
        has_height = callable(getattr(value, "get_height", None))
        has_layers = callable(getattr(value, "get_layers", None))
        if (has_width and has_height) or has_layers:
            return value

    return None


def parseThumbnailResult(rawResult:object, width:int=0, height:int=0) -> dict | None:
    '''Tries parseThumbnailPayload first, then parsePixbufPayload as fallback.'''
    
    parsed = parseThumbnailPayload(rawResult, width, height)
    if not parsed:
        parsed = parsePixbufPayload(rawResult)
    return parsed


def parseThumbnailPayload(rawResult:object, fallback_width:int=0, fallback_height:int=0) -> dict | None:
    '''Parses thumbnail API/PDB payload into width/height/bpp/pixel-bytes.'''

    values = flattenValues(rawResult)

    ints = []
    pixel_bytes = b""

    for value in values:
        if value is None:
            continue

        if isinstance(value, bool):
            continue

        if isinstance(value, int):
            ints.append(value)
            continue

        converted = toBytes(value)
        if converted and not pixel_bytes:
            pixel_bytes = converted

    if not pixel_bytes:
        return None

    width = int(fallback_width or 0)
    height = int(fallback_height or 0)
    bpp = 0

    if len(ints) >= 3:
        width = max(width, int(ints[0]))
        height = max(height, int(ints[1]))
        bpp = int(ints[2])

    if bpp not in (3, 4):
        if width > 0 and height > 0:
            pixel_count = width * height
            if pixel_count > 0:
                derived_bpp = len(pixel_bytes) // pixel_count
                if derived_bpp in (3, 4):
                    bpp = derived_bpp

    if width <= 0 or height <= 0:
        if bpp in (3, 4) and fallback_width and fallback_height:
            expected = int(fallback_width) * int(fallback_height) * bpp
            if expected == len(pixel_bytes):
                width = int(fallback_width)
                height = int(fallback_height)

    if width <= 0 or height <= 0 or bpp not in (3, 4):
        return None

    expected_size = width * height * bpp
    if expected_size <= 0 or len(pixel_bytes) < expected_size:
        return None

    return {
        "width": width,
        "height": height,
        "bpp": bpp,
        "pixels": pixel_bytes[:expected_size],
    }


def parsePixbufPayload(rawResult:object) -> dict | None:
    '''Parses pixbuf-like payload into width/height/bpp/pixel-bytes.'''

    value = unpackValue(rawResult)

    if isinstance(value, (list, tuple)):
        for item in value:
            parsed = parsePixbufPayload(item)
            if parsed:
                return parsed
        return None

    if value is None:
        return None

    width_getter = getattr(value, "get_width", None)
    height_getter = getattr(value, "get_height", None)
    channels_getter = getattr(value, "get_n_channels", None)
    rowstride_getter = getattr(value, "get_rowstride", None)
    pixels_getter = getattr(value, "get_pixels", None)

    if not (callable(width_getter) and callable(height_getter) and callable(channels_getter) and callable(pixels_getter)):
        return None

    try:
        width = int(width_getter())
        height = int(height_getter())
        bpp = int(channels_getter())
        rowstride = int(rowstride_getter()) if callable(rowstride_getter) else width * bpp
        raw_pixels = toBytes(pixels_getter())
    except Exception:
        return None

    if width <= 0 or height <= 0 or bpp not in (3, 4) or rowstride <= 0:
        return None

    tight_stride = width * bpp
    expected_row_data = rowstride * height
    if len(raw_pixels) < expected_row_data:
        return None

    if rowstride == tight_stride:
        pixels = raw_pixels[: tight_stride * height]
    else:
        rows = []
        for row_index in range(height):
            start = row_index * rowstride
            end = start + tight_stride
            rows.append(raw_pixels[start:end])
        pixels = b"".join(rows)

    return {
        "width": width,
        "height": height,
        "bpp": bpp,
        "pixels": pixels,
    }
