#from gui import *
from pynput import mouse, keyboard
from pynput.keyboard import Listener
from autoclicker import *


if __name__ == "__main__":

    # window = create_window(500, 500)

    ms = mouse.Controller()
    clicker = AutoClicker(0.01, mouse.Button.left, ms)
    clicker.start()

    def on_press(k):
        if k == keyboard.Key.shift:
            clicker.toggle()

        elif k == keyboard.Key.esc:
            clicker.stop()
            listener.stop()
            exit(0)


    with Listener(on_press=on_press) as listener:
        listener.join()
