from .PathsFinder import PathsFinder

class Configurator(object):

    def __init__(self, vim):
        self.vim = vim

    def setupSyntastic(self):
        classpath = []
        classpath.extend(PathsFinder(self.vim).getAllClassPaths())
        classpath.extend(PathsFinder(self.vim).getAllSourcePaths())
        sourcepath = ':'.join(classpath)
        self.vim.command("let g:syntastic_java_javac_classpath = '" + sourcepath + "'")
        self.vim.comamnd("let g:neomake_java_javac_args = neomake#makers#ft#java#javac()['args'] + ['-cp', '" + sourcepath + "']")
