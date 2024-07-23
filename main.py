from tkinter import *

root = Tk()  # create root window
root.title("Basic GUI Layout")  # title of the GUI window

# Setting a maxsize to open floating windows in tiling wm
root.maxsize(1800, 900)
root.geometry("1800x900")

# bg color
root.config(bg="skyblue")  

# Creating left frame
left_frame = Frame(root, width=400, height=880, bg='white')
left_frame.grid(row=0, column=0, padx=10, pady=10)

# Original image 
image_path = "image.png"
org_image = PhotoImage(image_path)
org_image = org_image.subsample(3,3)
Label(left_frame, image=org_image).grid(row=0, column=0, padx=5, pady=5)




root.mainloop()