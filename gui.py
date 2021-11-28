from tkinter import *
from autoclicker import *


class Window(Thread):

    def __init__(self, width, height, clicker):

        super().__init__()

        self.width = width
        self.height = height
        self.clicker = clicker
        self.window = Tk()
        self.run_status = None

        self.create_window()

    def create_window(self):

        # Window Basics

        self.window.title("astroxii | Auto Clicker")
        x = int((self.window.winfo_screenwidth() / 2) - (self.width / 2))
        y = int((self.window.winfo_screenheight() / 2) - (self.height / 2))
        self.window.geometry(f'{self.width}x{self.height}+{x}+{y}')
        self.window.resizable(False, False)

        # Window Controls

        title_label = Label(self.window, text="Auto Clicker")
        title_label.pack()

        exit_button = Button(self.window, text="Exit", command=self.exit, padx=35, pady=10)
        exit_button.pack(side=BOTTOM, ipadx=25, ipady=10)

        run_buttom = Button(self.window, text="Start/Stop", command=self.toggle_clicker, padx=35, pady=10)
        run_buttom.pack(side=TOP, ipadx=20, ipady=7.5)
        self.run_status = Label(self.window, text="Clicker is off.")
        self.run_status.pack(side=TOP, ipadx=2, ipady=2)

        # Events

        self.window.protocol("WM_DELETE_WINDOW", self.exit)

        # Main Loop

        self.window.mainloop()

    def toggle_clicker(self):

        sleep(3)
        self.run_status.configure(text="Clicking, press [CTRL] to stop.")
        self.window.iconify()
        self.clicker.toggle()

    def exit(self):

        self.clicker.stop()
        exit(0)
