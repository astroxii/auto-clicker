from tkinter import *
from time import sleep


class Window:

    def __init__(self, width, height, clicker):

        self.width = width
        self.height = height
        self.clicker = clicker
        self.window = Tk()
        self.run_status = None

    def create_window(self):

        # Window Basics

        self.window.title("astroxii | Auto Clicker")
        #icon = PhotoImage(file="/res/images/clickerIcon.png")
        #self.window.iconphoto(True, icon)

        x = int((self.window.winfo_screenwidth() / 2) - (self.width / 2))
        y = int((self.window.winfo_screenheight() / 2) - (self.height / 2))
        self.window.geometry(f'{self.width+4}x{self.height+4}+{x}+{y-25}')
        self.window.resizable(False, False)

        # Window Controls

        background = Canvas(self.window, width=self.width, height=self.height, bg="black")
        background.grid(columnspan=9, rowspan=9)

        title_label = Label(self.window, text="astroxii | Auto Clicker", bg="black", fg="#b300b3", font="Arial 25")
        title_label.grid(column=4, row=0)

        exit_button = Button(self.window, text="Exit",
                             command=self.exit, padx=10, pady=2.5, bg="red", fg="white", font="Arial 15")
        exit_button.grid(column=0, row=8)

        run_buttom = Button(self.window, text="Start / Stop",
                            command=self.toggle_clicker, padx=15, pady=5, bg="#005ce6", fg="white", font="Arial 15")
        run_buttom.grid(column=4, row=4)
        
        self.run_status = Label(self.window, text="Clicker is off, press [CTRL] to toggle.",
                                bg="black", fg="white", font="Arial 16")
        self.run_status.grid(column=4, row=5)

        # Events

        self.window.protocol("WM_DELETE_WINDOW", self.exit)

        # Main Loop

        self.window.mainloop()

    def toggle_clicker(self):

        self.clicker.toggle()

        if self.clicker.isClicking:
            self.run_status.configure(text="Clicking, press [CTRL] to toggle.")
            self.window.iconify()
        else:
            self.run_status.configure(text="Clicker is off, press [CTRL] to toggle.")

    def update(self):
        if self.clicker.isClicking:
            self.run_status.configure(text="Clicking, press [CTRL] to toggle.")
            self.window.iconify()
        else:
            self.run_status.configure(text="Clicker is off, press [CTRL] to toggle.")

    def exit(self):

        self.clicker.stop()
        exit(0)
