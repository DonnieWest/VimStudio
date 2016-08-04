import os
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
        self.vim.command("JCcacheClear")
        classpath = self.vim.eval("g:JavaComplete_BaseDir") + "/javacomplete2/classpath/" + self.vim.eval("g:JavaComplete_ProjectKey")
        os.remove(classpath)
        self.vim.command("call javacomplete#classpath#classpath#BuildClassPath()")

    def launchEmulator(self, emulator):
        if emulator in self.ProjectController.retrieveListOfEmulators():
            self.vim.command("silent !emulator @" + emulator + " &")
        else:
            self.vim.command("echo 'that emulator doesn't exist")

    def getDevices(self):
        devices = []
        output = os.popen("adb devices | grep device | grep -v devices | awk '{print $1}' | tr '\n' ' '")
        devices.extend(output.read().split(" "))
        return devices

    def installOnDevice(self, deviceID):
        apk = self.PathsFinder.getLatestApkFile()
        self.vim.command("silent !adb -s " + deviceID + " install -r -d " + apk)

    def installOnAllDevices(self, deviceIDs=[]):
        if not deviceIDs:
            deviceIDs.extend(self.getDevices)
        for device in deviceIDs:
            self.installOnDevice(device)

    def launchMainActivity(self, deviceID):
        package = self.AndroidManifest.getPackage()
        command = "silent !adb -s " + deviceID + " shell monkey -p " + package + " -c android.intent.category.LAUNCHER 1 &"
        self.vim.command(command)

    def launchAllMainActivity(self, deviceIDs=[]):
        if not deviceIDs:
            deviceIDs.extend(self.getDevices)
        for device in deviceIDs:
            self.launchMainActivity(device)
