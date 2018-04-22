import os
import time
import subprocess
from .PathsFinder import PathsFinder
from .ProjectController import ProjectController
from .AndroidManifest import AndroidManifest

class Configurator(object):

    def __init__(self, vim):
        self.vim = vim
        self.ProjectController = ProjectController()
        self.PathsFinder = PathsFinder(vim)
        self.AndroidManifest = AndroidManifest()

    def setupCheckers(self):
        self.vim.command("compiler! gradle")

    def resetJavacomplete(self):
        try:
            self.vim.command("JCclasspathGenerate")
        except:
            print("Eat the error")

    def launchEmulator(self, emulator):
        if emulator in self.ProjectController.retrieveListOfEmulators():
            emulate = subprocess.Popen(
                "emulator @" + emulator,
                env=os.environ.copy(),
                cwd=os.getcwd(),
                stdout=subprocess.PIPE,
                stdin=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                shell=True,
                bufsize=1
            )
        else:
            self.vim.command("echom 'that emulator doesn't exist")

    def getApplicationDebuggingPort(self):
        package = self.AndroidManifest.getPackage()
        output = os.popen("adb shell ps | grep " + package + " | awk '{print $2}' | tr '\n' ' '")
        return output.read()

    def attachDebugger(self):
        time.sleep(2)
        port = self.getApplicationDebuggingPort()
        adb = subprocess.Popen(
                "adb forward tcp:9000 jdwp:" + port,
            env=os.environ.copy(),
            cwd=os.getcwd(),
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            shell=True,
            bufsize=1
        )
        adb.wait()
        self.vim.command("call vebugger#jdb#attach('localhost:9000')")

    def getDevices(self):
        devices = []
        output = os.popen("adb devices | grep device | grep -v devices | awk '{print $1}' | tr '\n' ' '")
        for device in output.read().split(" "):
            if device is not '':
                devices.append(device)
        return devices

    def installOnDevice(self, deviceID):
        apk = self.PathsFinder.getLatestApkFile()
        installation = subprocess.Popen(
            "adb -s " + deviceID + " install -r -d " + apk,
            env=os.environ.copy(),
            cwd=os.getcwd(),
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            shell=True,
            bufsize=1
        )
        installation.wait()
        if installation.returncode is 0:
            self.vim.command("echom 'Installation succeeded'")
        else:
            self.vim.command("echom 'Installation failed'")
        return installation.returncode

    def installOnAllDevices(self, deviceIDs=[]):
        if not deviceIDs:
            deviceIDs.extend(self.getDevices)
        for device in deviceIDs:
            self.installOnDevice(device)

    def launchMainActivity(self, deviceID, debugMode = False):
        package = self.AndroidManifest.getPackage()
        mainActivity = self.AndroidManifest.getMainActivity()
        command = "adb -d shell am start -D -n '" + package  + "/" + mainActivity + "' &"
        if debugMode:
            command = command[:-1] + "-D &"
        launchActivity = subprocess.Popen(
            command,
            env=os.environ.copy(),
            cwd=os.getcwd(),
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            shell=True,
            bufsize=1
        )
        launchActivity.wait()
        if launchActivity.returncode is 0:
            self.vim.command("echom 'launch MainActivity succeeded'")
        else:
            self.vim.command("echom 'launch MainActivity failed'")
        return launchActivity.returncode

    def launchAllMainActivity(self, deviceIDs=[]):
        if not deviceIDs:
            deviceIDs.extend(self.getDevices)
        for device in deviceIDs:
            self.launchMainActivity(device)
