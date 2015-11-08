from Tkinter import *
import tkFileDialog
import startScreen
import ConfigParser

class SettingsScreen:
    def display(self, master):

        # not ui stuff
        self.running = True
        self.master = master
        self.lolPath = StringVar()
        self.lolPath.set(master.lolPath)
        self.checkBoxVar = IntVar()
        self.checkBoxVar.set(master.closeAfterLaunch)

        # ui stuff

        self.container = Frame(master.root)
        self.container.grid(row=0, column=0, sticky=W+N+S+E)
        Grid.rowconfigure(master.root, 0, weight=1)
        Grid.columnconfigure(master.root, 0, weight=1)
        
        self.lolPathLabel = Label(self.container, text="Path to Riot Games")
        self.lolPathLabel.grid(row=0, column=0, columnspan=2,
                               padx=(75,0), pady=(50,0), sticky=W)

        self.pathField = Entry(self.container, textvariable=self.lolPath)
        Grid.columnconfigure(self.container, 1, weight=1)
        self.pathField.grid(row=1, column=0, columnspan=3, padx=(75,0),
                            sticky=W+E)

        self.browseButton = Button(self.container, text="browse",
                                   command=lambda: self.browse())
        self.browseButton.grid(row=1, column=3, padx=(0,100))

        self.closeAfterLaunchLabel = Label(self.container,
                                           text="close after launch")
        self.closeAfterLaunchLabel.grid(row=2, column=0, padx=(75,0), sticky=N,
                                        pady=(25,0))
        
        self.closeAfterLaunch = Checkbutton(self.container,
                                            variable=self.checkBoxVar)
        self.closeAfterLaunch.grid(row=2, column=1, sticky=W+N, pady=(25,0))


        self.container2 = Frame(self.container, bg="red")
        self.container2.grid(row=3, column=0, columnspan=4, sticky=W+S+E)
        Grid.rowconfigure(self.container, 2, weight=1)

        self.applyButton = Button(self.container2, text="  apply  ",
                                  command=lambda: self.applyChanges())
        self.applyButton.grid(row=0, column=0, sticky=W+E)
        Grid.columnconfigure(self.container2, 0, weight=1)

        self.resetButton = Button(self.container2, text="reset changes",
                                  command=lambda: self.reset())
        self.resetButton.grid(row=0, column=1, sticky=W+E)
        Grid.columnconfigure(self.container2, 1, weight=1)

        self.backButton = Button(self.container2, text="    back    ",
                                 command=lambda: self.gotoStart())
        self.backButton.grid(row=0, column=2, sticky=W+E)
        Grid.columnconfigure(self.container2, 2, weight=1)

                             
        while self.running:
            master.root.update()
          
    def close(self):
        self.running=False

    # button actions
    def browse(self):
        self.lolPath.set(tkFileDialog.askdirectory())

    def applyChanges(self):
        Config = ConfigParser.ConfigParser()
        cfgfile = open(self.master.rootDir + "\config\settings.ini","w")
        Config.add_section("main")
        Config.set("main", "lolPath", self.lolPath.get())
        Config.set("main", "closeAfterLaunch", self.checkBoxVar.get())
        Config.write(cfgfile)
        cfgfile.close()
        self.master.lolPath = self.lolPath.get()
        self.master.closeAfterLaunch = self.checkBoxVar.get()

    def reset(self):
        self.lolPath.set(self.master.lolPath)
        self.checkBoxVar.set(self.master.closeAfterLaunch)

    def gotoStart(self):
        self.runnig = False
        self.master.setDisplay(startScreen.StartScreen())
