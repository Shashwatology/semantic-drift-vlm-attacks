import os
import yaml
from PIL import Image

def generate_base_images(config_path="experiments/config.yaml"):
    # Load configuration
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    
    output_dir = config["paths"]["base_images_dir"]
    os.makedirs(output_dir, exist_ok=True)
    
    num_images = config["dataset"]["num_images"]
    width, height = config["dataset"]["image_size"]
    base_color = tuple(config["dataset"]["base_color"])
    
    for i in range(num_images):
        img = Image.new('RGB', (width, height), base_color)
        filepath = os.path.join(output_dir, f"base_{i:03d}.png")
        img.save(filepath)
        print(f"Generated base image: {filepath}")

if __name__ == "__main__":
    generate_base_images()
