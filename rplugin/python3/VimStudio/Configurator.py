from .PathsFinder import PathsFinder

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
        self.vim.command("let g:neomake_java_javac_args = ['-cp', '''" + sourcepath + "''']")
        self.vim.command("let g:gradleClasspath = '" + sourcepath + "'")
        self.vim.command("compiler! gradle")
        self.vim.command("let g:neomake_java_javac_autoload_gradle_classpath = 1")
