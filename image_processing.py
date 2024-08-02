from PIL import Image, ImageTk, ImageDraw, ImageFont


class ImageProcessing:
  def resize_image(image_path, width, height):
    image = Image.open(image_path)
    image = image.resize((width, height))
    image = ImageTk.PhotoImage(image)

    return image

  def draw_image(image_path, text="", font_size=10, font_color="black", type=None, rotation=None):
    # Open the image
    image = Image.open(image_path).convert("RGBA")
    txt_layer = Image.new("RGBA", image.size, (255, 255, 255, 0))

    # Load a font
    try:
      font_size = int(font_size) if font_size else 10
      font = ImageFont.truetype("arial.ttf", font_size)
    except (OSError, ValueError):
      # If arial.ttf is not found, use the default PIL font
      font = ImageFont.load_default()
    
    # Initialize ImageDraw
    draw = ImageDraw.Draw(txt_layer)

    # Draw the text
    if text:
      # Center the text if type is specified as 'center'
      if type == 'center':
        width, height = image.size
        text_width, text_height = draw.textsize(text, font=font)
        position = ((width - text_width) // 2, (height - text_height) // 2)
      else:
        position = (10, 10)  # Default position at the top-left corner
      
      draw.text(position, text, font=font, fill=font_color)
  
    # Combine the image with the text layer
    combined = Image.alpha_composite(image, txt_layer)
    
    # Apply rotation if specified
    if rotation:
      combined = combined.rotate(rotation, expand=True)

    # Convert combined image back to RGB mode
    combined = combined.convert("RGB")

    return combined
