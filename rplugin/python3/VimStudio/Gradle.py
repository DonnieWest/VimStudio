import os

class Gradle(object):

    def __init__(self, vim):
        self.vim = vim

    def setGradleCompiler(self):
        self.vim.command("let g:gradleBin = '" + self.gradleCommand() + "'")
        self.vim.command("compiler! gradle")


    def runGradleCommand(self, command, async=False):
        gradle = self.gradleCommand()
        if async == True:
            gradle = "Dispatch! " + gradle
        else:
            gradle = "!" + gradle
        self.vim.command("%s %s" % (gradle, command))

    def outputPaths(self, async=False):
        self.runGradleCommand("outputPaths", async)

    def gradleCommand(self):
        if os.path.isfile("./gradlew") and os.access("./gradlew", os.X_OK):
            return "./gradlew"
        else:
            return "gradle"
    
    def lint(self):
        self.vim.command(self.gradleCommand() + " lint")
