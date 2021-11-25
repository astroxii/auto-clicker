from pynput import mouse, keyboard
from pynput.keyboard import Listener
from autoclicker import AutoClicker


def on_press(k):
    if k == keyboard.Key.space:
        clicker.toggle()

    elif k == keyboard.Key.esc:
        clicker.exit()
        listener.stop()
        exit(0)


if __name__ == "__main__":

    ms = mouse.Controller()
    clicker = AutoClicker(0.01, mouse.Button.left, ms)
    clicker.start()

    with Listener(on_press=on_press) as listener:
        listener.join()
