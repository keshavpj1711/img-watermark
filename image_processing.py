from PIL import Image, ImageTk, ImageDraw, ImageFont


class ImageProcessing:
  def resize_image(image_path, width, height):
    image = Image.open(image_path)
    image = image.resize((width, height))
    image = ImageTk.PhotoImage(image)

    return image

  def draw_image(image_path, text, font_size, font_color, type, rotation):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", font_size)

    draw.text((10, 10), text, fill=font_color, font=font)

    return image
