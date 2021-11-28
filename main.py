from gui import *
from autoclicker import *
#from listener import *


if __name__ == "__main__":

    clicker = AutoClicker(0, 0.01, mouse.Button.left)
    clicker.start()

    window = Window(500, 500, clicker)
    window.start()

    #listener = Listener(clicker)
    #listener.start()
