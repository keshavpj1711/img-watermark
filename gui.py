from tkinter import *
from image_processing import ImageProcessing


class UserInterface:

  def __init__(self):
    self.root = Tk()
    self.root.maxsize(1800, 800)
    self.root.geometry("1600x800")
    self.root.resizable(0, 0)

    # Configuring bg
    self.root.config(bg='deep sky blue')
    # Setting image path
    self.img_path = "image.png"

    self.setup_gui()
    

  def setup_gui(self):
    self.left_frame = Frame(self.root, width=400, height=780, bg='white')
    self.left_frame.grid(row=0, column=0, padx=10, pady=10)

    self.right_frame = Frame(self.root, width=1160, height=780, bg='white')
    self.right_frame.grid(row=0, column=1, padx=10, pady=10)

    # Left frame
    self.resized_image = ImageProcessing.resize_image(self.img_path, 400, 225)
    Label(self.left_frame, image=self.resized_image).grid(row=0, column=0, padx=5, pady=5, columnspan=2)

    load_button = Button(self.left_frame, text="Load", width=20)
    load_button.grid(row=1, column=0, columnspan=2)

    # Adding a text box
    self.text_label = Label(self.left_frame, text="Enter your text", font=(
        "Arial", 12, "normal"), bg='white', fg='black')
    self.text_label.grid(row=2, column=0, pady=5)
    # For text entry
    self.text_entry = Entry(self.left_frame, width=20, bg='white', font=(
        "Arial", 12, "normal"), fg='black')
    self.text_entry.grid(row=2, column=1, pady=5)

  def load_path():
    # This will give a dialog box to select the image from the menu
    pass

  def run(self):
    self.root.mainloop()
