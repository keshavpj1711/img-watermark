from PIL import Image, ImageTk


class ImageProcessing:
  def resize_image(image_path, width, height):
    image = Image.open(image_path)
    image = image.resize((width, height))
    image = ImageTk.PhotoImage(image)

    return image

  def draw_image(image_path, text, font_size, font_color, type, rotation):
    pass
