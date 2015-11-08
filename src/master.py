import os
import utils
from Tkinter import *

class Master:
    def setup(self):
        self.rootDir = os.path.dirname(os.path.realpath(__file__))[:len(os.path.dirname(os.path.realpath(__file__))) - 4]
        #self.rootDir = os.path.join(sys.path[0][:len(sys.path[0]) - 3 -13])
        self.settings = utils.readIni(self.rootDir + "\config\settings.ini")
        self.lolPath = self.settings["lolpath"]
        self.closeAfterLaunch = int(self.settings["closeafterlaunch"])
        
        self.scale = 4
        self.screenWidth = 160 * self.scale
        self.screenHeight = self.screenWidth * 9 / 16
        self.title = "LOL settings manager"

        self.root = Tk()
        self.root.minsize(width=self.screenWidth, height=self.screenHeight)
        self.root.maxsize(width=self.screenWidth, height=self.screenHeight)
        self.root.wm_title(self.title)
        self.root.protocol('WM_DELETE_WINDOW', lambda: self.close())

        self.activeScreen = None
        
    def setDisplay(self, display):
        for widget in self.root.winfo_children():
            widget.destroy()
        if self.activeScreen != None:
            self.activeScreen.close()
        self.activeScreen = display
        self.activeScreen.display(self)

    def close(self):
        if self.activeScreen != None:
            self.activeScreen.close()
        else:
            root.destroy()
