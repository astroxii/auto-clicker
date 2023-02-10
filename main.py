from GUI import *
from autoclicker import *
from pynput import keyboard


if __name__ == "__main__":

    clicker = AutoClicker(0, 0.5, mouse.Button.left)
    clicker.start()

    window = Window(700, 500, clicker)

    def on_press(k):
        if k == keyboard.Key.ctrl_l:
            clicker.toggle()
            window.update()

    with keyboard.Listener(on_press=on_press) as kbm_listener:
        window.create_window()
        kbm_listener.join()
