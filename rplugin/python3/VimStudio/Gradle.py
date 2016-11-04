import os
import subprocess
import shutil

class Gradle(object):

    def __init__(self, vim):
        self.vim = vim
        self.gradleInit = vim.eval("g:VimStudioDirectory") + "/init.gradle"
        self.tasks = []

    def setGradleCompiler(self):
        gradle = self.gradleCommand()
        if gradle is not None:
            self.vim.command("let g:gradleBin = '" + self.gradleCommand().replace(" ", "\ ") + "'")
        else:
            self.vim.command("echom 'No gradle wrapper found or gradle binary in Path'")

    def runGradleCommand(self, command):
        gradle = self.gradleCommand()
        if gradle is None:
            self.vim.command("echom 'No gradle wrapper found or gradle binary in Path'")
        else:
            gradleCommand = subprocess.Popen(
                gradle + " " + command,
                env=os.environ.copy(),
                cwd=os.getcwd(),
                stdout=subprocess.PIPE,
                stdin=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                shell=True,
                bufsize=1
            )
            gradleCommand.wait()
            if gradleCommand.returncode is 0:
                self.vim.command("echom 'Gradle command " + command + " succeeded'")
            else:
                self.vim.command("echom 'Gradle " + command + " failed'")
            return gradleCommand.returncode

    def gradleCommand(self):
        if os.path.isfile("./gradlew") and os.access("./gradlew", os.X_OK):
            return "./gradlew -I " + self.gradleInit
        elif shutil.which('gradle') is not None:
            return "gradle -I " + self.gradleInit
        else:
            return None

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
                if task is "assemble":
                    flavors.append(task)
                else:
                    flavors.append(task.replace("assemble", ""))
        return flavors
