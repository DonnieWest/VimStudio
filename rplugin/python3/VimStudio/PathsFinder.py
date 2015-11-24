import re
import os
import sys
import glob
from .ProjectController import ProjectController

class PathsFinder:
    def __init__(self, vim):
        self.vim = vim
        sys.path.append(os.getcwd())
        self.ProjectController = ProjectController()

    def getAndroidHome(self):
        return os.environ.get('ANDROID_HOME')

    def getStaticPaths(self):
        staticPaths = []

        staticPaths.extend(glob.glob(os.getcwd() + '/**/build/intermediates/classes/debug'))
        sources = self.vim.eval("g:JavaComplete_SourcesPath")[1:].replace("//", "/").split(":")
        for each in sources:
            if each.find("src"):
                staticPaths.append(each + "/main/java")
        return staticPaths

    def getAllClassPaths(self):
        classPathsAndJars = self.vim.eval("g:JavaComplete_LibsPath")
        classPathsAndJars = classPathsAndJars.split(":")
        return classPathsAndJars

    def getAllSourcePaths(self):
        sourcePaths = []
        sourcePaths.extend(self.getStaticPaths())
        if self.ProjectController.isAndroidProject():
            sourcePaths.append(self.getAndroidSdkSourcePath())

        return sourcePaths

    def getGradleClassPathsFromFile(self, filename):
        list = []

        if os.path.isfile(filename):
            with open(filename, 'U') as f:
                for line in f:
                    list.append(line.rstrip())
        return list

    def getAndroidSdkJar(self):
        androidHome = os.environ.get('ANDROID_HOME')
        currentPlatformDir = 'android-' + self.getAndroidVersionFromBuildGradle()

        sdkJarPath = androidHome +os.sep+ 'platforms' +os.sep+ currentPlatformDir +os.sep+ 'android.jar'
        return sdkJarPath

    def getAndroidSdkSourcePath(self):
        androidHome = os.environ.get('ANDROID_HOME')
        currentPlatformDir = 'android-' + self.getAndroidVersionFromBuildGradle()

        sdkSourcePath = androidHome +os.sep+ 'sources' +os.sep+ currentPlatformDir +os.sep

        return sdkSourcePath


    def getAndroidVersionFromBuildGradle(self):
        buildFiles = self.ProjectController.findFile(os.getcwd(), ProjectController.GRADLE_BUILD_FILE)
        for gradle in buildFiles:
            with open(gradle, 'U') as f:
                for line in f:
                    result = self.getAndroidVersionFromLine(line)
                    if result != None:
                        return result

    def getAndroidVersionFromLine(self, line):
        matchObj = re.search(r'compileSdkVersion\W*(\d*)', line, re.M|re.I)
        if matchObj != None:
            version = matchObj.group(1)
            return version
        return None


    def getLatestApkFile(self):
        foundFiles = []
        for root, dirs, files in os.walk("./build/"):
            for file in files:
                if file.endswith(".apk"):
                    foundFiles.append(os.path.join(root, file))

        latestFile = max(foundFiles, key=os.path.getmtime)
        return latestFile

