from tkinter import *
from PIL import Image, ImageTk

# Resizing image with PIL
def resize_image(image_path, width, height):
  # Opening image
  image = Image.open(image_path)
  # Resizing
  rszd_image = image.resize((width, height))

  return rszd_image


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

# Adding buttons 
font_style = Button(left_frame, text='Font Style', width=20)
font_style.grid(row=2, column=0, pady=5)
font_color = Button(left_frame, text='Font Color', width=20)
font_color.grid(row=2, column=1, pady=5)
font_size = Button(left_frame, text='Font Size', width=20)
font_size.grid(row=3, column=0, pady=5)
types = Button(left_frame, text='Types', width=20)
types.grid(row=3, column=1, pady=5)
rotate = Button(left_frame, text='Rotate', width=20)
rotate.grid(row=4, column=0, pady=(5, 10))
generate = Button(left_frame, text='Generate', width=20, bg='deep sky blue', activebackground='dodger blue', fg='white', activeforeground='white')
generate.grid(row=4, column=1, pady=(5, 10))

root.mainloop()