import utils
import os
from Tkinter import *
import settingsScreen
import time
from subprocess import call

class StartScreen:
    def display(self, master):

        # not ui stuff
        self.master = master
        self.setup()
                

        # ui stuff
        
        self.container = Frame(master.root)
        self.container.grid(row=0, column=0, sticky=W+N+S+E)
        Grid.rowconfigure(master.root, 0, weight=1)
        Grid.columnconfigure(master.root, 0, weight=1)
                            
        # top text
        self.topText = Label(self.container, text="select input file to use")
        self.topText.grid(row=0, column=0, sticky=W+E+S+N)
        Grid.rowconfigure(self.container, 0, weight=1)
        Grid.columnconfigure(self.container, 0, weight=1)

        # listBox with input files
        self.inputFilesList = Listbox(self.container, selectmode=BROWSE)
        self.inputFilesList.insert(END, "previously used file")
        self.inputFilesList.insert(END, "default input.ini file")
        for f in self.inputFiles:
            if f != "previously used file":
                self.inputFilesList.insert(END, f)
        self.inputFilesList.grid(row=1, column=0, sticky=W+E+S+N, columnspan=3)
        Grid.rowconfigure(self.container, 1, weight=1)

        # buttons....
        self.applyButton = Button(self.container, text="refresh",
                                  command=lambda: self.refresh())
        self.applyButton.grid(row=0, column=2, sticky=W+E+S+N)
        
        self.applyButton = Button(self.container, text="apply",
                         command=lambda: self.applyChanges())
        self.applyButton.grid(row=2, column=0, sticky=W+E+S+N)
        Grid.rowconfigure(self.container, 2, weight=1)
    
        self.launchLolButton = Button(self.container, text="launch\n LOL",
                             command=lambda: self.launchLol())
        self.launchLolButton.grid(row=2, column=1, sticky=W+E+S+N)
        Grid.columnconfigure(self.container, 1, weight=1)

        self.settingsButton = Button(self.container, text="settings",
                            command=lambda: self.gotoSettings())
        self.settingsButton.grid(row=2, column=2, sticky=W+E+S+N)
        Grid.columnconfigure(self.container, 2, weight=1)

        self.out = Label(self.container, textvariable=self.outputText)
        self.out.grid(row=3, column=0, columnspan=3)    

        while self.running:
            master.root.update()

    def setup(self):
        self.running = True

        self.activeFile="previously used file"

        # contents of variable is displayed by the bottom label
        self.outputText = StringVar()
        self.outputText.set("\n")

        # coppy input.ini file in lol config to lol settings manager input files
        try:
            utils.coppyFile(self.master.lolPath + "\League of Legends\Config\input.ini",
                                     self.master.rootDir + "\input files\previously used file")
        except IOError:
            self.outputText.set("NOTE! No input.ini file found in lol config folder. Either the file have been removed(no problem)\n or the path to the riotgames folder is misconfigured. Set the path to riotgames folder in settings ")
    

        # list containg name of all availible input files
        self.inputFiles = os.listdir(self.master.rootDir + "\input files")


    def close(self):
        self.running = False

    # button actions
    def refresh(self):
        # coppy input.ini file in lol config to lol settings manager input files
        try:
            utils.coppyFile(self.master.lolPath + "\League of Legends\Config\input.ini",
                            self.master.rootDir + "\input files\previously used file")
        except IOError:
            utils.makeFile(self.master.rootDir + "\input files\previously used file")
            self.outputText.set("NOTE! No input.ini file found in lol config folder. Either the file have been removed(no problem)\n or the path to the riotgames folder is misconfigured. Set the path to riotgames folder in settings ")

        # list containg name of all availible input files
        self.inputFiles = os.listdir(self.master.rootDir + "\input files")

        # refresh listbox
        self.inputFilesList.delete(0, END)
        self.inputFilesList.insert(END, "previously used file")
        self.inputFilesList.insert(END, "default input.ini file")
        for f in self.inputFiles:
            if f != "previously used file":
                self.inputFilesList.insert(END, f)

        self.activeFile="previously used file"
    
    def applyChanges(self):
        self.activeFile = self.inputFilesList.get(ACTIVE)
        try:
            utils.clearConfigFiles(self.master.lolPath)
        except OSError:
            pass
        if self.activeFile != "default input.ini file":
            try:
                utils.coppyFile(self.master.rootDir + "\input files\\" + self.activeFile,
                          self.master.lolPath + "\League of Legends\config\input.ini")
                self.outputText.set("settings sucsessfully applied\n")
            except IOError:
                self.outputText.set("ERROR! settings could not be applied. path to Riot Games folder is probably missconfigured")
        
        
    def launchLol(self):
        self.outputText.set("launching LOL with " + self.activeFile + " as input.ini file\n")
        try:
            call(self.master.lolPath + "\League of Legends\lol.launcher.exe")
            if self.master.closeAfterLaunch != 0:
                time.sleep(0.6)
                self.close()
        except WindowsError:
            self.outputText.set("ERROR! could not launch lol. The path to Riot Games folder might be missconfigured.\n configure in settings")
        
    def gotoSettings(self):
        self.running = False
        self.master.setDisplay(settingsScreen.SettingsScreen())
