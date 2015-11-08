from master import Master
from displays import *

def main():
    master = Master()
    master.setup()
    master.setDisplay(startScreen.StartScreen())
    
if __name__ == "__main__":
    main()
