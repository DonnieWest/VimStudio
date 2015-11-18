import os

class Gradle(object):

    def __init__(self, vim):
        self.vim = vim
        self.gradleInit = vim.eval("g:VimStudioDirectory") + "/init.gradle"
    
    def setGradleCompiler(self):
        self.vim.command("let g:gradleBin = '" + self.gradleCommand().replace(" ", "\ ") + "'")
        self.vim.command("compiler! gradle")

    def runGradleCommand(self, command, async=False):
        gradle = self.gradleCommand()
        if async == True:
            gradle = "Dispatch! " + gradle
        else:
            gradle = "!" + gradle
        self.vim.command("%s %s" % (gradle, command))

    def gradleCommand(self):
        if os.path.isfile("./gradlew") and os.access("./gradlew", os.X_OK):
            return "./gradlew -I " + self.gradleInit
        else:
            return "gradle -I " + self.gradleInit
    
    def lint(self):
        self.vim.command("cexpr system('" + self.gradleCommand() + " lint')")
