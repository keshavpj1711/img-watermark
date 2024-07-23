from tkinter import *
from PIL import Image, ImageTk


# Resizing image with PIL
def resize_image(image_path, width, height):
  # Opening image
  image = Image.open(image_path)
  # Resizing
  rszd_image = image.resize((width, height))

  return rszd_image


# A funtion to update the image by calling all the function with the respective info in the text boxes
def update_img():
  # 1. Take text from text_entry and update on the image
  # 2. Apply the font color 
  # 3. Apply the font size
  # 4. Apply the types
  # 5. Add the rotation to the text
  pass


def generate_img():
  # Save the image in the same directory where the program was ran
  pass


root = Tk()  # create root window
root.title("Basic GUI Layout")  # title of the GUI window

# Setting a maxsize to open floating windows in tiling wm
root.maxsize(1600, 800)
root.geometry("1800x900")
root.resizable(0, 0)

# bg color
root.config(bg="deep sky blue")  

# Creating left frame
left_frame = Frame(root, width=400, height=780, bg='white')
left_frame.grid(row=0, column=0, padx=10, pady=10)

# Creating right frame
right_frame = Frame(root, width=1140, height=780, bg='grey')
right_frame.grid(row=0, column=1, padx=10, pady=10)

# Original image 
img_path = "image.png"
resized_image = resize_image(img_path, 400, 225)
tk_image = ImageTk.PhotoImage(resized_image)
Label(left_frame, image=tk_image).grid(row=0, column=0, padx=5, pady=5, columnspan=2)

# Adding a text box
text_label = Label(left_frame, text="Enter your text", font=("Arial", 12, "normal"), bg='white', fg='black')
text_label.grid(row=1, column=0, pady=5)
# For text entry 
text_entry = Entry(left_frame, width=20, bg='white', font=("Arial", 12, "normal"), fg='black')
text_entry.grid(row=1, column=1, pady=5)

# Adding functionalities
font_style_label = Label(left_frame, text="Font color", font=("Arial", 12, "normal"), bg='white', fg='black')
font_style_label.grid(row=2, column=0, pady=5)
# For text entry 
font_style_entry = Entry(left_frame, width=20, bg='white', font=("Arial", 12, "normal"), fg='black')
font_style_entry.grid(row=2, column=1, pady=5)

font_size_label = Label(left_frame, text="Font size", font=("Arial", 12, "normal"), bg='white', fg='black')
font_size_label.grid(row=3, column=0, pady=5)
# For text entry 
font_size_entry = Entry(left_frame, width=20, bg='white', font=("Arial", 12, "normal"), fg='black')
font_size_entry.grid(row=3, column=1, pady=5)

types = Label(left_frame, text='Types', font=("Arial", 12, "normal"), bg='white', fg='black')
types.grid(row=4, column=0, pady=5)
# A dropdown to select type is to be added

rotate = Label(left_frame, text='Rotate', font=("Arial", 12, "normal"), bg='white', fg='black')
rotate.grid(row=5, column=0, pady=5)
# A dropdown to select type is to be added

preview = Button(left_frame, text='Preview', width=20, bg='deep sky blue', activebackground='dodger blue', fg='white', activeforeground='white', command=update_img)
preview.grid(row=6, column=0, pady=(5, 10))

generate = Button(left_frame, text='Generate', width=20, bg='deep sky blue', activebackground='dodger blue', fg='white', activeforeground='white')
generate.grid(row=6, column=1, pady=(5, 10))

root.mainloop()