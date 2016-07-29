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

    @neovim.command("VimStudioCtags")
    def ctags(self):
        self.Ctags.generateCtags()

    @neovim.command("SetupVimStudio")
    def setupVimStudio(self):
        if self.ProjectController.isGradleProject():
            self.Gradle.setGradleCompiler()
            self.Configurator.setupCheckers()

    @neovim.command("VimStudioLint")
    def lint(self):
        self.Gradle.lint()

    @neovim.autocmd("BufWritePost", pattern="*.java")
    def autoCtags(self):
        self.ctags()

    @neovim.command("Gradle", range='', nargs='*')
    def runGradleCommand(self, args, range):
        command = " ".join(args)
        self.Gradle.runGradleCommand(command)

    @neovim.autocmd("BufWritePost", pattern="build.gradle")
    def sync(self):
        self.Configurator.resetJavacomplete()

    @neovim.autocmd("BufReadPost", pattern="*.java")
    def setup(self):
        self.setupVimStudio()

    @neovim.autocmd("BufEnter", pattern="*.xml")
    def layoutCompletion(self):
        if self.ProjectController.isAndroidProject():
            self.vim.command("XMLns android")

    @neovim.autocmd("BufEnter", pattern="AndroidManifest.xml")
    def manifestCompletion(self):
        if self.ProjectController.isAndroidProject():
            self.vim.command("XMLns manifest")
