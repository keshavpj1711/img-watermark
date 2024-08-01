from tkinter import *
from tkinter import filedialog
from image_processing import ImageProcessing
from PIL import ImageTk


class UserInterface:

  def __init__(self):
    self.root = Tk()
    self.root.maxsize(1800, 800)
    self.root.geometry("1600x800")
    self.root.resizable(0, 0)

    # Configuring bg
    self.root.config(bg='deep sky blue')
    # Setting image path
    self.img_path = None

    self.setup_gui()
    

  def setup_gui(self):
    self.left_frame = Frame(self.root, width=400, height=780, bg='white')
    self.left_frame.grid(row=0, column=0, padx=10, pady=10)

    self.right_frame = Frame(self.root, width=1150, height=780, bg='white')
    self.right_frame.grid(row=0, column=1, padx=10, pady=10)

    self.display_org()

    load_button = Button(self.left_frame, text="Load", width=20, command=self.load_path, bg="deep sky blue", fg="white", activebackground="dodger blue", activeforeground="white")
    load_button.grid(row=1, column=0, columnspan=2)

    # Adding a text box
    self.text_label = Label(self.left_frame, text="Enter your text", font=("Arial", 12, "normal"), bg='white', fg='black')
    self.text_label.grid(row=2, column=0, pady=5)
    # For text entry
    self.text_entry = Entry(self.left_frame, width=20, bg='white', font=("Arial", 12, "normal"), fg='black')
    self.text_entry.grid(row=2, column=1, pady=5)

    self.font_size = Label(self.left_frame, text="Font Size", width=20, font=("Arial", 12, "normal"), bg='white', fg='black')
    self.font_size.grid(row=3, column=0, pady=5)
    self.font_size_entry = Entry(self.left_frame, width=20, bg='white', font=("Arial", 12, "normal"), fg='black')
    self.font_size_entry.grid(row=3, column=1, pady=5)

    self.font_color = Label(self.left_frame, text="Font Color", width=20, font=("Arial", 12, "normal"), bg='white', fg='black')
    self.font_color.grid(row=4, column=0)
    self.font_color_entry = Entry(self.left_frame, width=20, bg='white', font=("Arial", 12, "normal"), fg='black')
    self.font_color_entry.grid(row=4, column=1, pady=5)

    self.type = Label(self.left_frame, text="Type", width=20 , bg='white', fg='black', font=("Arial", 12, "normal"))
    self.type.grid(row=5, column=0, pady=5)

    self.rotate = Label(self.left_frame, text="Rotate", width=20 , bg='white', fg='black', font=("Arial", 12, "normal"))
    self.rotate.grid(row=6, column=0, pady=5)

    preview_button = Button(self.left_frame, text="Preview", width=20, command=self.load_path, bg="deep sky blue", fg="white", activebackground="dodger blue", activeforeground="white")
    preview_button.grid(row=7, column=0, pady=5)

    generate_button = Button(self.left_frame, text="Generate`", width=20, command=self.load_path, bg="deep sky blue", fg="white", activebackground="dodger blue", activeforeground="white")
    generate_button.grid(row=7, column=1, pady=5)

  def load_path(self):
    # This will give a dialog box to select the image from the menu
    self.img_path = filedialog.askopenfilename(
        initialdir="./", 
        title="Select file", 
        filetypes=(("all files", "*.*"), ("Image files", "*.jpg;*.jpeg;*.png;*.bmp"))
    )
    self.display_org()

    self.setup_gui()

  def display_org(self):
    try:
      # This is to display the image on original image pane
      self.resized_image = ImageProcessing.resize_image(self.img_path, 400, 225)
      Label(self.left_frame, image=self.resized_image).grid(row=0, column=0, padx=5, pady=5, columnspan=2)
    except:
      self.img_path = "white.png"
      self.resized_image = ImageProcessing.resize_image(self.img_path, 400, 225)
      Label(self.left_frame, image=self.resized_image).grid(row=0, column=0, padx=5, pady=5, columnspan=2)

  def display_prev(self):
    font_size_text = self.font_size_entry.get()
    font_color_text = self.font_color_entry.get()
    text = self.text_entry.get()
    image = ImageProcessing.draw_image(self.img_path, text, font_size_text, font_color_text)
    self.prev_img = ImageTk.PhotoImage(image)
    

  def save_image(self):
    # To save image in the current directory
    pass
    
  def run(self):
    self.root.mainloop()
