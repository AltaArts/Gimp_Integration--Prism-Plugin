#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
#
#   This script implements the Prism Host process for the Gimp integration.  It
#   is launched by the Prism Bridge service running inside Gimp as a separate
#   process, and runs a Qt event loop that provides a UI window and handles
#   incoming socket commands from the Bridge.
#


import argparse
import atexit
import json
import os
import socket
import sys
import threading
import traceback

scriptDir = os.path.dirname(os.path.abspath(__file__))
if scriptDir not in sys.path:
    sys.path.insert(0, scriptDir)

import Prism_Helper as Helper


PRISM_ROOT = r"@PRISMROOTREPLACE@"


#   Redirects Writes to the Log File
class RotatingLogStream:
    def __init__(self, runtime:"PrismHostRuntime"):
        self.runtime = runtime

    #   Write Text Data into Rotating Host Log
    def write(self, data):
        if not data:
            return 0

        text = str(data)
        if not text:
            return 0

        self.runtime.appendLogText(text)
        return len(text)

    #   Flush Stream Interface for Compatibility
    def flush(self):
        return None



#####################################################
#   Main Runtime Class for the Prism Host Process   #
#####################################################
class PrismHostRuntime:
    def __init__(self):
        self.settings = Helper.loadSettings()

        self.bridgePort_out = self.settings["bridgePort_out"]
        self.bridgePort_in = self.settings["bridgePort_in"]
        self.log_maxBytes = self.settings["log_maxBytes"]

        self.logLock = threading.Lock()
        self.logComponent = "HOST"

        self.args = self.parseArgs()

        self.prismRoot = self.args.prism_root or self.getPrismRoot()
        self.hostWindow = None
        self.prismCoreModule = None

        self.serverSocket = None
        self.serverThread = None
        self.shutdownEvent = threading.Event()

        self.pendingActions = []
        self.pendingActionsLock = threading.Lock()


    #   Parses Command Line Arguments Passed to the Host Process by the Bridge
    def parseArgs(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--parent-pid", type=int, required=True, help="PID of the parent process (GIMP).")
        parser.add_argument("--prism-root", type=str, required=True, help="Path to the Prism root directory.")
        return parser.parse_args()


    ###########################
    #         PATHS           #
    ###########################

    def getPrismRoot(self):
        if "PRISM_ROOT" in os.environ:
            return os.environ["PRISM_ROOT"]

        configured_root = PRISM_ROOT
        if configured_root and not configured_root.startswith("@"):
            return configured_root

        else:
            self.appendLogText("ERROR: Unable to Get Prism Root Path")
            return None


    #   Return Host Log File Path
    def getLogPath(self):
        return os.environ.get("PRISM_GIMP_LOG_PATH", Helper.getLogPath())


    #   Return Host Backup Log File Path
    def getBackupLogPath(self):
        return os.environ.get("PRISM_GIMP_LOG_BACKUP_PATH", Helper.getBackupLogPath())


    #   Return Max Log Size with Environment Override
    def getLogMaxBytes(self):
        try:
            return int(os.environ.get("PRISM_GIMP_log_maxBytes", self.log_maxBytes))
        
        except Exception:
            return self.log_maxBytes


    #   Return Outbound Bridge Port with Override
    def getBridgePort_out(self):
        try:
            return int(os.environ.get("PRISM_GIMP_BRIDGE_PORT_OUT", self.bridgePort_out))
        
        except Exception:
            return self.bridgePort_out


    #   Return Inbound Bridge Port with Override
    def getBridgePort_in(self):
        try:
            return int(os.environ.get("PRISM_GIMP_BRIDGE_PORT_IN", self.bridgePort_in))
        
        except Exception:
            return self.bridgePort_in


    ###########################
    #        LOGGING          #
    ###########################

    #   Rotates the Log File if at Max Size by Renaming the Current File to a Backup and Starting a New Log
    def rotateLogIfNeeded(self, incoming_bytes=0):
        log_path = self.getLogPath()

        with self.logLock:
            try:
                currSize = os.path.getsize(log_path)
            except OSError:
                currSize = 0

            if currSize + incoming_bytes < self.getLogMaxBytes():
                return

            backup_path = self.getBackupLogPath()
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


    #   Appends Text to the Log File, Rotating if Needed
    def appendLogText(self, text):
        encoded_text = text.encode("utf-8", errors="replace")
        self.rotateLogIfNeeded(len(encoded_text))

        with self.logLock:
            with open(self.getLogPath(), "a", encoding="utf-8") as handle:
                handle.write(text)


    #   Append Formatted Message to Host Log
    def addToLog(self, message, **fields):
        self.appendLogText(Helper.formatLogLine(message, self.logComponent, **fields))


    #   Configures Logging by Redirecting stdout and stderr to the Log File
    def configureLogging(self):
        sys.stdout = RotatingLogStream(self)
        sys.stderr = RotatingLogStream(self)

        self.addToLog(
            "Configured rotating log streams",
            log_path=self.getLogPath(),
            backup_path=self.getBackupLogPath(),
            max_bytes=self.getLogMaxBytes(),
        )


    #############################
    #      COMMUNICATIONS       #
    #############################

    #   Starts a Socket Server to Receive Commands from Gimp
    def startCommandServer(self):
        if self.serverThread is not None:
            return

        host = "127.0.0.1"
        port = self.getBridgePort_out()

        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serverSocket.bind((host, port))
        self.serverSocket.listen(5)
        self.serverSocket.settimeout(0.5)

        self.serverThread = threading.Thread(target=self.runCommandServer, name="PrismHostCommandServer", daemon=True)
        self.serverThread.start()

        self.addToLog("Started host command server", host=host, port=port, thread_name=self.serverThread.name)


    #   Stops the Socket Server
    def stopCommandServer(self):
        self.shutdownEvent.set()

        if self.serverSocket:
            try:
                self.serverSocket.close()
            except Exception:
                pass
            self.serverSocket = None

        self.addToLog("Stopped host command server")


    #   Server Loop which Receives Command Requests from Gimp
    def runCommandServer(self):
        while not self.shutdownEvent.is_set():
            try:
                client, _address = self.serverSocket.accept()
            except socket.timeout:
                continue
            except OSError:
                break

            with client:
                client.settimeout(1)

                try:
                    #   Receive Raw Data from Socket and Parse as JSON Command Request
                    rawData = client.recv(65536)
                    if not rawData:
                        continue

                    request = json.loads(rawData.decode("utf-8"))
                    response = self.handleIncomingRequest(request)

                except Exception as exc:
                    self.addToLog("Host command request failed before dispatch", error=str(exc))
                    response = {
                        "ok": False,
                        "error": str(exc),
                        "traceback": traceback.format_exc(),
                    }

                try:
                    #   Send JSON Response Back to Gimp Bridge
                    client.sendall(json.dumps(response).encode("utf-8"))
                    if not response.get("ok"):
                        self.addToLog("Sent failed host command response", ok=False, action=request.get("action") if isinstance(request, dict) else None)

                except Exception:
                    self.addToLog("Failed to send host command response")


    #   Handles Parsed Command Request from Gimp
    def handleIncomingRequest(self, request:dict):
        action = request.get("action") or request.get("command")
        payload = request.get("data") if isinstance(request.get("data"), dict) else {}

        #   Simple Ping Request to Check if Host is Alive and Respond with Connection Info
        if action == "ping":
            return {"ok": True, "data": {"host": "prism-gimp-host", "port": self.getBridgePort_out()}}

        #   Request for Host Status, Respond with Connection Info and PIDs
        if action == "get-host-status":
            return {
                "ok": True,
                "data": {
                    "host": "prism-gimp-host",
                    "port": self.getBridgePort_out(),
                    "parent_pid": self.args.parent_pid,
                    "host_pid": os.getpid(),
                },
            }

        #   Request to Shutdown the Host Process, which will be Sent by the Bridge when Gimp is Closing
        if action == "shutdown-host":
            self.addToLog("Received host shutdown request")
            self.QT_QApplication.quit()
            return {"ok": True}

        #   For Other Commands, Emit as Qt Signal to be Handled on the Main Event Loop Thread by the Prism Host
        if self.hostWindow is None:
            with self.pendingActionsLock:
                self.pendingActions.append((action, payload))

            return {
                "ok": True,
                "accepted": True,
                "action": action,
                "queued": True,
            }

        #   Emit as Qt signal So it Runs on the Main Event Loop Thread.
        self.hostWindow.commandDispatcher.commandRequested.emit(action, payload)

        return {
            "ok": True,
            "accepted": True,
            "action": action,
        }


    #############################
    #         ENVIRONMENT       #
    #############################

    #   Write Host PID to the Settings State so that it can be Monitored by the Bridge
    def writeHostPidFile(self):
        Helper.updateSettingState(HOST_PID=os.getpid())
        self.addToLog("Wrote host pid state", process_id=os.getpid())


    #   Set up the Environ for the Host Process
    def setupEnvironment(self):
        pythonlibs_root = os.path.join(self.prismRoot, "PythonLibs")
        pythonlibs_py3 = os.path.join(pythonlibs_root, "Python3")
        pythonlibs_cross = os.path.join(pythonlibs_root, "CrossPlatform")
        pyside_root = os.path.join(pythonlibs_py3, "PySide")
        pyside6_root = os.path.join(pyside_root, "PySide6")
        shiboken6_root = os.path.join(pyside_root, "shiboken6")

        sys.path.append(self.prismRoot)
        sys.path.insert(0, os.path.join(self.prismRoot, "Scripts"))
        sys.path.append(pythonlibs_py3)
        sys.path.append(pythonlibs_cross)
        sys.path.insert(0, pyside_root)

        os.environ["PATH"] = os.pathsep.join([
            shiboken6_root,
            pyside6_root,
            pyside_root,
            pythonlibs_py3,
            pythonlibs_cross,
            os.environ.get("PATH", ""),
        ])

        if hasattr(os, "add_dll_directory"):
            for dll_dir in [shiboken6_root, pyside6_root, pyside_root]:
                if os.path.isdir(dll_dir):
                    os.add_dll_directory(dll_dir)

        os.environ.setdefault("QT_API", "pyside6")
        self.addToLog("Configured Prism host environment", prismRoot=self.prismRoot)


    #   Imports Required PrismCore and Qt Modules
    def importRuntimeModules(self):
        import PrismCore
        from qtpy.QtCore import Qt, QObject, QTimer, Signal
        from qtpy.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

        class HostCommandDispatcher(QObject):
            commandRequested = Signal(str, object)

        self.prismCoreModule = PrismCore
        self.QT_Qt = Qt
        self.QT_QObject = QObject
        self.QT_QTimer = QTimer
        self.QT_Signal = Signal
        self.QT_QApplication = QApplication
        self.QT_QMainWindow = QMainWindow
        self.QT_QPushButton = QPushButton
        self.QT_QVBoxLayout = QVBoxLayout
        self.QT_QWidget = QWidget
        self.QT_HostCommandDispatcher = HostCommandDispatcher
        
        self.addToLog("Imported Prism host runtime modules")


    #   Run the Main Host Process, Setting up Logging, Environment, and UI, then Entering the Qt Event Loop
    def run(self):
        self.configureLogging()
        atexit.register(Helper.removeHostPidState, os.getpid(), self.addToLog)
        self.setupEnvironment()
        self.importRuntimeModules()

        existing_instance = self.QT_QApplication.instance()
        app = existing_instance or self.QT_QApplication(sys.argv)
        app.setQuitOnLastWindowClosed(False)

        self.writeHostPidFile()
        try:
            self.startCommandServer()
            self.hostWindow = PrismToolsWindow(self, parent_pid=self.args.parent_pid)

            with self.pendingActionsLock:
                queued_actions = list(self.pendingActions)
                self.pendingActions.clear()

            for queued_action in queued_actions:
                if isinstance(queued_action, tuple) and len(queued_action) == 2:
                    action, payload = queued_action
                else:
                    action, payload = queued_action, {}

                self.hostWindow.commandDispatcher.commandRequested.emit(action, payload)

            result = app.exec_()

            self.addToLog("Prism Host shutting down", exit_code=result)
            return result
        
        finally:
            self.stopCommandServer()
            Helper.removeHostPidState(os.getpid(), addToLog=self.addToLog)




##################################################
#   Container Created by PrismHostRuntime for    #
#   the Prism Qt UI and Command Handling Logic   #
##################################################
class PrismToolsWindow:
    def __init__(self, runtime:"PrismHostRuntime", parent_pid=None):
        self.runtime = runtime
        self.parent_pid = parent_pid
        self.core = None
        self.gimpFuncts = None

        self.buttons = {}
        self.monitorTimer = None
        self.window = runtime.QT_QMainWindow()
        self.commandDispatcher = runtime.QT_HostCommandDispatcher()

        self.runtime.addToLog("Creating PrismToolsWindow", parent_pid=parent_pid)
        self.core = self.runtime.prismCoreModule.create(app="Gimp", prismArgs=["noProjectBrowser", "splash"])
        self.runtime.addToLog("Created PrismCore instance", plugin_app="Gimp")

        self.gimpFuncts = self.core.getPlugin("Gimp")

        if self.gimpFuncts is None:
            raise RuntimeError("Unable to load the Prism Gimp plugin.")

        #   Route Incoming Socket Commands to executeAction on the Qt UI thread.
        self.commandDispatcher.commandRequested.connect(
            self.executeAction,
            runtime.QT_Qt.QueuedConnection,
        )

        self.setupUi()
        self.startMonitor()


    #   Adds a Line to the Log File with the Host Runtime
    def addToLog(self, message, **fields):
        self.runtime.addToLog(message, **fields)


    #   Sets up the Qt UI of the Host Window (hidden normally)
    def setupUi(self):
        window = self.window
        rt = self.runtime

        window.setObjectName("MainWindow")
        window.setAttribute(rt.QT_Qt.WA_StyledBackground, True)
        window.setAttribute(rt.QT_Qt.WA_DeleteOnClose, False)
        window.setWindowTitle("Prism Tools")
        window.setGeometry(100, 100, 260, 300)
        window.setWindowFlags(window.windowFlags() | rt.QT_Qt.WindowStaysOnTopHint)

        central_widget = rt.QT_QWidget(window)
        window.setCentralWidget(central_widget)
        layout = rt.QT_QVBoxLayout(central_widget)

        button_map = [
            ("saveVersion", "Save Version"),
            ("saveComment", "Save Version with Comment"),
            ("open_ProjectBrowser", "Project Browser"),
            ("open_StateManager", "State Manager"),
            ("open_PrismSettings", "Prism Settings"),
        ]

        for method_name, label in button_map:
            button = rt.QT_QPushButton(label)
            button.setObjectName("b_%s" % method_name)
            button.setFixedHeight(40)
            button.clicked.connect(getattr(self, method_name))
            layout.addWidget(button)
            self.buttons[method_name] = button


    #   Starts the Gimp Monitor Timer to Check if Gimp is Still Running
    def startMonitor(self):
        if not self.parent_pid:
            self.addToLog("Skipping Qt parent monitor because no parent pid was provided")
            return

        self.monitorTimer = self.runtime.QT_QTimer(self.window)
        self.monitorTimer.timeout.connect(self.checkParentProcess)
        self.monitorTimer.start(1000)
        self.addToLog("Started Gimp parent monitor timer", parent_pid=self.parent_pid, interval_ms=1000)


    #   Checks if the Parent Gimp Process is Still Running, and Quits the Host if it is Not
    def checkParentProcess(self):
        parent_alive = Helper.isProcessRunning(self.parent_pid)
        if not parent_alive:
            self.addToLog("Gimp process missing during monitor check", parent_pid=self.parent_pid)
            self.runtime.QT_QApplication.quit()


    ###########################################
    ##    Handles Gimp Prism Menu Commands   ##  

    def saveVersion(self, payload=None):
        self.gimpFuncts.saveVersion(requestData=payload or {})

    def saveComment(self, payload=None):
        self.gimpFuncts.saveComment(requestData=payload or {})

    def open_ProjectBrowser(self, payload=None):
        self.gimpFuncts.open_ProjectBrowser()

    def open_StateManager(self, payload=None):
        self.gimpFuncts.open_StateManager(requestData=payload or {})

    def open_PrismSettings(self, payload=None):
        self.gimpFuncts.open_PrismSettings()


    #   Executes a Supported Host Action by Name
    def executeAction(self, actionName:str, payload=None):
        actionMap = {
            "saveVersion": self.saveVersion,
            "saveComment": self.saveComment,
            "open_ProjectBrowser": self.open_ProjectBrowser,
            "open_StateManager": self.open_StateManager,
            "open_PrismSettings": self.open_PrismSettings,
        }

        try:
            actionCallable = actionMap.get(actionName)

            if not actionCallable:
                raise RuntimeError("Unknown host action: %s" % actionName)

            actionCallable(payload)

        except Exception as exc:
            self.addToLog("Host action execution failed", action=actionName, error=str(exc))




###############################################
#   Creates and Runs the Prism Host Runtime   #
###############################################

def main():
    runtime = PrismHostRuntime()
    return runtime.run()


if __name__ == "__main__":
    sys.exit(main())


