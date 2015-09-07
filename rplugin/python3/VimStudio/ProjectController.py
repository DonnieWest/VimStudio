import os
import glob
import fnmatch

class ProjectController:

    ANDROID_MANIFEST_FILE = 'AndroidManifest.xml'
    GRADLE_BUILD_FILE = "build.gradle"
    GRADLE_WRITE_FILE = ".output_paths_result"  #Also defined in gradle config
    PATH_FILE = ".grand_source_paths"

    def fileExistsInCwd(self, filename, maxDepth):
        current_directory = os.getcwd()
        return self.fileExistsInDir(filename, current_directory, maxDepth)

    def fileExistsInDir(self, filename, directory, maxDepth):
        top = directory
        matches = self.fileNamesRetrieve(top, maxDepth, filename)

        if len(matches) > 0:
            return True
        else:
            return False

    def fileNamesRetrieve(self, top, maxDepth, fnMask):
        someFiles = []

        for d in range(1, maxDepth+1):
            maxGlob = "/".join("*" * d)
            topGlob = os.path.join(top, maxGlob)
            allFiles = glob.glob(topGlob)

            someFiles.extend([f for f in allFiles if fnmatch.fnmatch(os.path.basename(f), fnMask )])

        
        for d in range(1, maxDepth+1):
            maxGlob = ".*".join("/" * (d + 1))[1:-1]
            topGlob = os.path.join(top, maxGlob)
            allFiles = glob.glob(topGlob)

            someFiles.extend([f for f in allFiles if fnmatch.fnmatch(os.path.basename(f), fnMask )])
        return someFiles

    def isGradleProject(self):
        return self.fileExistsInCwd(self.GRADLE_BUILD_FILE, 1)

    def isAndroidProject(self):
        return self.fileExistsInCwd(self.ANDROID_MANIFEST_FILE, 10)

    def isVimStudioReady(self):
        return self.fileExistsInCwd(self.GRADLE_WRITE_FILE, 1)

    def isGradleSetup(self):
        home_directory = os.path.expanduser("~")
        return self.fileExistsInDir("VimStudio.gradle", home_directory + "/.gradle/init.d/", 1)

    def setupEnvironment(self):
        d = os.path.expanduser("~")


        if not os.path.exists(d + "/.gradle/init.d/VimStudio.gradle"):
            if not os.path.exists(d + "/.gradle/init.d"):
                if not os.path.exists(d + "/.gradle"):
                    os.makedirs(d + "/.gradle")
                os.makedirs(d + "/.gradle/init.d")
        
        if not os.path.exists(d + "/.gradle/init.d/VimStudio.gradle"):
            with open(d + "/.gradle/init.d/VimStudio.gradle", "a+") as f:
                write("allprojects { apply from: 'https://raw.githubusercontent.com/DonnieWest/VimStudio/master/VimStudio.gradle'}")
