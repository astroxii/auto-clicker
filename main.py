from pynput import mouse, keyboard
from pynput.keyboard import Listener
from time import sleep

ms = mouse.Controller()
kbm = keyboard.Controller()


def auto_click():
    global ms

    i = 1000

    while i > 0:
        sleep(0.01)

        i -= 1
        ms.click(mouse.Button.left)
        ms.click(mouse.Button.left)


if __name__ == "__main__":

    def on_press(key):
        if key == keyboard.KeyCode(char="-"):
            exit(0)
        elif key == keyboard.KeyCode(char="="):
            auto_click()


    with Listener(on_press=on_press) as listener:
        listener.join()
