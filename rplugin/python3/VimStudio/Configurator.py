from .PathsFinder import PathsFinder
from .ProjectController import ProjectController
import os

class Configurator(object):

    def __init__(self, vim):
        self.vim = vim

    def setupCheckers(self):
        classpath = []
        classpath.extend(PathsFinder(self.vim).getAllClassPaths())
        sources = PathsFinder(self.vim).getAllSourcePaths()

        classpath.extend(sources)
        sourcepath = ':'.join(classpath)
        self.vim.command("let g:syntastic_java_javac_classpath = '" + sourcepath + "'")
        self.vim.command("let g:neomake_java_javac_classpath = '" + sourcepath + "'")
        self.vim.command("let g:gradleClasspath = '" + sourcepath + "'")
        self.vim.command("compiler! gradle")
        self.vim.command("let g:neomake_java_javac_autoload_gradle_classpath = 1")

    def resetJavacomplete(self):
        self.vim.command("JCcacheClear")
        classpath = self.vim.eval("g:JavaComplete_BaseDir") + "/javacomplete2/classpath/" + self.vim.eval("g:JavaComplete_ProjectKey")
        os.remove(classpath)
        self.vim.command("call javacomplete#classpath#classpath#BuildClassPath()")
