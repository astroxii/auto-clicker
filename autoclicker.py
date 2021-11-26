from time import sleep
from threading import Thread


class AutoClicker(Thread):

    def __init__(self, delay, button, mouse):
        super().__init__()

        self.delay = delay
        self.button = button
        self.mouse = mouse
        self.isClicking = False
        self.isAppRunning = True

    def run(self):
        while self.isAppRunning:
            print(" ")
            while self.isClicking:
                self.mouse.click(self.button)
                sleep(self.delay)

    def toggle(self):
        if self.isClicking:
            self.isClicking = False
        else:
            self.isClicking = True

    def stop(self):
        self.isAppRunning = False
        self.isClicking = False
