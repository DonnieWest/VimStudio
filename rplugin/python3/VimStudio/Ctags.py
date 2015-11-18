import os
from .PathsFinder import PathsFinder

class Ctags:
    def __init__(self, vim):
        self.vim = vim

    tagsFile = ".tags"
    tempFile = ".TEMP_TAGS"
    ctagsCommandArray = []

    def generateCtags(self):
        if not self.isAlreadyRunning():
            self.runCtags()

    def isAlreadyRunning(self):
        if os.path.isfile(self.tempFile):
            return True
        else:
            return False

    def runCtags(self):
        os.system(self.constructCtagsCommand())

    def constructCtagsCommand(self):
        self.addBasicTagsCommand()
        self.addTagsTargetFile()
        self.addTagsReadSources()
        self.addCommandSeperator()
        self.addMvCommand()

        return ' '.join(self.ctagsCommandArray)

    def addBasicTagsCommand(self):
        self.ctagsCommandArray = ['ctags', '--recurse', '--fields=+l', '--langdef=XML', '--langmap=Java:.java,XML:.xml', '--languages=Java,XML', '--regex-XML=/id="([a-zA-Z0-9_]+)"/\\1/d,definition/']

    def addTagsTargetFile(self):
        self.ctagsCommandArray.extend(['-f', self.tempFile])

    def addTagsReadSources(self):
        self.ctagsCommandArray.extend(PathsFinder(self.vim).getAllSourcePaths())

    def addCommandSeperator(self):
        self.ctagsCommandArray.append('&&')

    def addMvCommand(self):
        self.ctagsCommandArray.extend(['mv', self.tempFile, self.tagsFile])
