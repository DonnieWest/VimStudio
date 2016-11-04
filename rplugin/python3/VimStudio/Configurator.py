import os
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
        self.vim.command("JCclasspathGenerate")

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

    def launchMainActivity(self, deviceID):
        package = self.AndroidManifest.getPackage()
        command = "adb -s " + deviceID + " shell monkey -p " + package + " -c android.intent.category.LAUNCHER 1 &"
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
