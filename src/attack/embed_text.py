from PIL import Image, ImageDraw

def embed_hidden_text(base_image_path, text_payload, alpha, text_coord, text_color=(255, 255, 255)):
    """
    Embeds hidden text onto a given image using the specified alpha (opacity) level.
    
    Args:
        base_image_path (str): Path to the base image to modify.
        text_payload (str): The payload string to embed.
        alpha (int): Opacity level (0-255).
        text_coord (tuple): (x, y) coordinates for the text.
        text_color (tuple): (r, g, b) base color for the text layer.
        
    Returns:
        PIL.Image: The resulting adversarial image in RGBA format.
    """
    # Open the image and ensure it has an alpha channel (RGBA)
    img = Image.open(base_image_path).convert("RGBA")
    
    # Create an overlay for the text
    txt_layer = Image.new('RGBA', img.size, (255, 255, 255, 0))
    d = ImageDraw.Draw(txt_layer)
    
    # Set the text color with the specific alpha
    fill_color = (*text_color, alpha)
    
    # Draw the text onto the transparent layer
    d.text(text_coord, text_payload, fill=fill_color)
    
    # Composite the text layer over the base image
    adversarial_img = Image.alpha_composite(img, txt_layer)
    return adversarial_img
