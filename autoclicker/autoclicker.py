from time import sleep
from threading import Thread
from pynput import mouse


class AutoClicker(Thread):

    def __init__(self, start_delay, delay, button):

        super().__init__()

        self.delay = delay
        self.start_delay = start_delay
        self.button = button
        self.mouse = mouse.Controller()
        self.isClicking = False
        self.isAppRunning = True

    def run(self):
        while self.isAppRunning:
            sleep(0)

            if self.isClicking and self.start_delay > 0:
                sleep(self.start_delay)

            while self.isClicking:
                self.mouse.click(self.button)
                sleep(self.delay)

    def toggle(self):
        self.isClicking = not self.isClicking

    def stop(self):
        self.isAppRunning = False
        self.isClicking = False
