import os

class Gradle(object):

    def __init__(self, vim):
        self.vim = vim
        self.gradleInit = vim.eval("g:VimStudioDirectory") + "/init.gradle"
        self.tasks = []

    def setGradleCompiler(self):
        self.vim.command("let g:gradleBin = '" + self.gradleCommand().replace(" ", "\ ") + "'")

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
        self.vim.command("make lint")

    def rebuildProject(self):
        self.runGradleCommand("assembleDebug")

    def getAllTasks(self):
        if not self.tasks:
            taskCommand = self.gradleCommand() + " --console=plain --quiet tasks | grep ' - ' | awk '{print $1}' | tr '\n' ' '"
            output = os.popen(taskCommand)
            self.tasks = sorted(output.read().split(" "))
        return self.tasks

    def getAllFlavors(self):
        flavors = []
        for task in self.getAllTasks():
            if "assemble" in task:
                flavors.append(task.replace("assemble", ""))
        return flavors
