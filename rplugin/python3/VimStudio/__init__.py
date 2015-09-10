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
        

    @neovim.command("VimStudioCtags")
    def ctags(self):
        Ctags().generateCtags

    @neovim.command("SetupVimStudio")
    def setupVimStudio(self):
        if self.ProjectController.isGradleProject():
            self.Configurator.genPathsAndSetup()
            self.Gradle.setGradleCompiler()
    
    @neovim.command("VimStudioLint")
    def lint(self):
        self.Gradle.lint()

    @neovim.autocmd("BufWritePost", pattern="*.java")
    def autoCtags(self):
        self.ctags()

    @neovim.autocmd("VimEnter")
    def setup(self):
        self.setupVimStudio()

    @neovim.autocmd("BufWritePost", pattern="build.gradle")
    def refreshPaths(self):
        self.Configurator.generatePaths()
        self.setupVimStudio()

    
