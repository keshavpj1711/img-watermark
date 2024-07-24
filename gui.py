from tkinter import *


class UserInterface:

    def __init__(self):
        self.root = Tk()
        self.root.maxsize(1800, 800)
        self.root.geometry("1600x800")
        self.root.resizable(0, 0)

        # Configuring bg
        self.root.config(bg='deep sky blue')
        self.setup_gui()

    def setup_gui(self):
        self.left_frame = Frame(self.root, width=400, height=780, bg='white')
        self.left_frame.grid(row=0, column=0, padx=10, pady=10)

        self.right_frame = Frame(self.root, width=1160, height=780, bg='white')
        self.right_frame.grid(row=0, column=1, padx=10, pady=10)

        # Left frame
        self.

    def run(self):
        self.root.mainloop()
