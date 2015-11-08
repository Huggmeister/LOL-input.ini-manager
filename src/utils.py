import ConfigParser
import os
import shutil

def readIni(path):
    try:
        config = ConfigParser.ConfigParser()
        config.read(path)
    except ConfigParser.MissingSectionHeaderError, e:
        raise WrongIniFormatError(`e`)

    dictionary = {}
    for section in config.sections():
        for option in config.options(section):
            dictionary[option] = config.get(section, option)

    return dictionary

def fileExists(path):
    return os.path.exists(path)

def removeFile(path):
    os.remove(path)

def makeFile(path):
    open(path, "w+")

def coppyFile(path, newPath):
    shutil.copyfile(path, newPath)

def clearConfigFiles(lolPath):
    removeFile(lolPath + "\League of Legends\Config\PersistedSettings.json")
    removeFile(lolPath + "\Config\input.ini")

def applyChanges(self):
        self.activeFile = self.inputFilesList.get(ACTIVE)
        tmp = 2
        if self.activeFile != "default input.ini file":
            if utils.fileExists(self.master.lolPath + "\League of Legends\Config\PersistedSettings.json"):
                tmp -= 1
                utils.removeFile(self.master.lolPath + "\League of Legends\Config\PersistedSettings.json")
            if utils.fileExists(self.master.lolPath + "\League of Legends\Config\input.ini"):
                tmp -= 1
                utils.removeFile(self.master.lolPath + "\Config\input.ini")
            self.result = utils.coppyFile(self.master.rootDir + "\input files\\" + self.activeFile,
                            self.master.lolPath + "\League of Legends\Config\input.ini")
            if self.result != 0:
                self.outputText.set("ERROR!! Failed to apply changes. Path to riota games folder is most likley missconfigured")
            if tmp != 0:
                self.outputText.set("NOTE! Some of files in LOL config folder where not found. This is probabbly not a problem.\n If settings wont change the path to riotgames folder might be missconfigured")
        else:
            if utils.fileExists(self.master.lolPath + "\League of Legends\Config\PersistedSettings.json"):
                tmp -= 1
                utils.removeFile(self.master.lolPath + "\League of Legends\Config\PersistedSettings.json")
            if utils.fileExists(self.master.lolPath + "\League of Legends\Config\input.ini"):
                tmp -= 1
                utils.removeFile(self.master.lolPath + "\League of Legends\Config\input.ini")
            if tmp != 0:
                self.outputText.set("NOTE! Some of files in LOL config folder where not found. This is probabbly not a problem.\n If settings wont change the path to riotgames folder might be missconfigured")
