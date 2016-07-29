import neovim
from .Configurator import Configurator
from .Ctags import Ctags
from .ProjectController import ProjectController
from .Gradle import Gradle

@neovim.plugin
class VimStudio(object):
    def __init__(self, vim):
        self.vim = vim
        self.Configurator = Configurator(vim)
        self.ProjectController = ProjectController()
        self.Gradle = Gradle(self.vim)
        self.Ctags = Ctags(self.vim)

    @neovim.command("SetupVimStudio")
    def setupVimStudio(self):
        if self.ProjectController.isGradleProject():
            self.Gradle.setGradleCompiler()
            self.Configurator.setupCheckers()
            if not self.ProjectController.isBuilt() and self.ProjectController.isAndroidProject():
                self.Gradle.runGradleCommand("assembleDebug")
                self.Configurator.resetJavacomplete()



    @neovim.command("Gradle", complete='customlist,GradleComplete', range='', nargs='*')
    def runGradleCommand(self, args, range):
        if self.ProjectController.isGradleProject():
            command = " ".join(args)
            self.Gradle.runGradleCommand(command)
            if "install" in command:
                self.Configurator.launchAllMainActivity()
        else:
            self.vim.command("echo 'this is not a gradle project'")

    @neovim.command("VimStudioInstall", complete='customlist,FlavorComplete', nargs="?", sync=True)
    def install(self, args):
        flavor = "Debug"
        if args:
            flavor = args[0]
        devices = self.Configurator.getDevices()
        device = ""
        if devices:
            if len(devices) > 1:
                device = self.vim.funcs.input("Which device? ", "all", "customlist,DeviceComplete")
                if device is "":
                    return
                elif device is not "all":
                    self.Gradle.runGradleCommand("assemble" + flavor)
                    self.Configurator.installOnDevice(device)
                    self.Configurator.launchMainActivity(device)
                else:
                    self.Gradle.runGradleCommand("install" + flavor)
                    self.Configurator.launchAllMainActivity()
            else:
                device = devices[0]
                self.Gradle.runGradleCommand("install" + flavor)
                self.Configurator.launchMainActivity(device)
        else:
            self.vim.command("echo 'no devices available'")


    @neovim.command("VimStudioCtags")
    def ctags(self):
        self.Ctags.generateCtags()

    @neovim.command("VimStudioLint")
    def lint(self):
        self.Gradle.lint()

    @neovim.command("VimStudioEmulator", complete='customlist,EmulatorComplete', nargs="1", sync=True)
    def launchEmulator(self, args):
        self.Configurator.launchEmulator(args[0])

    @neovim.autocmd("BufReadPost", pattern="*.java")
    def setup(self):
        self.setupVimStudio()

    @neovim.autocmd("BufWritePost", pattern="*.java")
    def autoCtags(self):
        self.ctags()

    @neovim.autocmd("BufEnter", pattern="*.xml")
    def layoutCompletion(self):
        if self.ProjectController.isAndroidProject():
            self.vim.command("XMLns android")

    @neovim.autocmd("BufEnter", pattern="AndroidManifest.xml")
    def manifestCompletion(self):
        if self.ProjectController.isAndroidProject():
            self.vim.command("XMLns manifest")

    @neovim.autocmd("BufWritePost", pattern="build.gradle")
    def sync(self):
        self.Configurator.resetJavacomplete()
        self.setupVimStudio()

    @neovim.function("EmulatorComplete", sync=True)
    def EmulatorComplete(self, *args, **kwargs):
        return self.ProjectController.retrieveListOfEmulators()

    @neovim.function("GradleComplete", sync=True)
    def GradleComplete(self, *args, **kwargs):
        tasks = []
        tasks.extend(self.Gradle.getAllTasks())
        filter = args[0][0]
        if (filter):
            tasks = [task for task in tasks if filter in task]
        return tasks

    @neovim.function("FlavorComplete", sync=True)
    def FlavorComplete(self, *args, **kwargs):
        flavors = []
        flavors.extend(self.Gradle.getAllFlavors())
        filter = args[0][0]
        if (filter):
            flavors = [flavor for flavor in flavors if filter in flavor]
        return flavors

    @neovim.function("DeviceComplete", sync=True)
    def DeviceComplete(self, *args, **kwargs):
        devices = []
        devices.extend(self.Configurator.getDevices())
        if devices and len(devices) > 1:
            devices.append("all")
        return devices
