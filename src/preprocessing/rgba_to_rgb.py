from PIL import Image
import os
import yaml
import glob

def flatten_image_to_rgb(img_path, bg_color):
    """
    Flattens an RGBA image onto a solid background color, resulting in an RGB image.
    
    Args:
        img_path (str): Path to the RGBA image.
        bg_color (tuple): RGB color tuple for the background.
        
    Returns:
        PIL.Image: The flattened RGB image.
    """
    img = Image.open(img_path).convert("RGBA")
    
    # Create the solid background image
    bg_img = Image.new("RGB", img.size, bg_color)
    
    # Paste the RGBA image onto the background, using its alpha channel as a mask
    bg_img.paste(img, mask=img)
    return bg_img

def run_preprocessing(config_path="experiments/config.yaml"):
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
        
    adv_dir = config["paths"]["adversarial_images_dir"]
    proc_dir = config["paths"]["processed_images_dir"]
    os.makedirs(proc_dir, exist_ok=True)
    
    backgrounds = config["preprocessing"]["backgrounds"]
    adv_images = glob.glob(os.path.join(adv_dir, "*.png"))
    
    for img_path in adv_images:
        filename = os.path.basename(img_path)
        base_name, ext = os.path.splitext(filename)
        
        for bg_name, bg_color in backgrounds.items():
            flattened = flatten_image_to_rgb(img_path, tuple(bg_color))
            
            out_filename = f"{base_name}_{bg_name}{ext}"
            out_path = os.path.join(proc_dir, out_filename)
            flattened.save(out_path)
            print(f"Preprocessed {filename} -> {out_filename}")

if __name__ == "__main__":
    run_preprocessing()
