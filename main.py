import tkinter as tk

# Creating the window
window = tk.Tk()
window.title("img_watermark")
window.config(bg="skyblue")


# Creating the main preview window
preview_frame = tk.Frame(window, width=500, height=350, bg="white")
preview_frame.grid(row=0, column=1, padx=10, pady=10)

# Creating a frame for tool/edit area
tool_frame = tk.Frame(window, width=500, height=550, bg="white")
tool_frame.grid(row=1, column=1, padx=10, pady=10)

# To prevent screen from shutting off 
tk.mainloop()