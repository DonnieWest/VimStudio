import re
import os
import sys
from .ProjectController import ProjectController

class PathsFinder:
    def __init__(self):
        sys.path.append(os.getcwd())
        self.ProjectController = ProjectController()

    def getAndroidHome(self):
        return os.environ.get('ANDROID_HOME')

    def getStaticPaths(self):
        staticPaths = []

        staticPaths.append('./src/main/java')
        staticPaths.append('./build/intermediates/classes/debug')

        return staticPaths


    def getDynamicPaths(self):
        dynamicPaths = []

        if self.ProjectController.isAndroidProject():
            dynamicPaths.append(self.getAndroidSdkJar())
            dynamicPaths.extend(self.getExplodedAarClasses())
        return dynamicPaths

    def getAllClassPaths(self):
        classPathsAndJars = []

        # classPathsAndJars.extend(self.getAllSourcePaths())
        classPathsAndJars.extend(self.getGradleClassPathsFromFile())
        classPathsAndJars.extend(self.getDynamicPaths())
        return classPathsAndJars

    def getAllSourcePaths(self):
        sourcePaths = []
        sourcePaths.extend(self.getStaticPaths())
        if self.ProjectController.isAndroidProject():
            sourcePaths.append(self.getAndroidSdkSourcePath())

        return sourcePaths



    def getGradleClassPathsFromFile(self):
        list = []

        filename = self.ProjectController.GRADLE_WRITE_FILE

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
        with open(ProjectController.GRADLE_BUILD_FILE, 'U') as f:
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

    def getExplodedAarClasses(self):
        foundJars = []
        for root, dirs, files in os.walk("./"):
            for file in files:
                if file.endswith(".jar"):
                    foundJars.append(os.path.join(root, file))
        return foundJars

    def getLatestApkFile(self):
        foundFiles = []
        for root, dirs, files in os.walk("./build/"):
            for file in files:
                if file.endswith(".apk"):
                    foundFiles.append(os.path.join(root, file))

        latestFile = max(foundFiles, key=os.path.getmtime)
        return latestFile

