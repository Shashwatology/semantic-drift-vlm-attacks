import os
import yaml
import glob
from src.attack.embed_text import embed_hidden_text

def generate_adversarial_images(config_path="experiments/config.yaml"):
    # Load configuration
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
        
    base_dir = config["paths"]["base_images_dir"]
    adv_dir = config["paths"]["adversarial_images_dir"]
    os.makedirs(adv_dir, exist_ok=True)
    
    alphas = config["attack"]["alphas"]
    text_payload = config["dataset"]["payload_text"]
    text_coord = tuple(config["attack"]["text_coordinate"])
    text_color = tuple(config["attack"]["text_color"])
    
    base_images = glob.glob(os.path.join(base_dir, "*.png"))
    
    for img_path in base_images:
        filename = os.path.basename(img_path)
        base_name, ext = os.path.splitext(filename)
        
        for alpha in alphas:
            adv_img = embed_hidden_text(
                base_image_path=img_path,
                text_payload=text_payload,
                alpha=alpha,
                text_coord=text_coord,
                text_color=text_color
            )
            
            out_filename = f"{base_name}_alpha{alpha}{ext}"
            out_path = os.path.join(adv_dir, out_filename)
            adv_img.save(out_path)
            print(f"Generated adversarial image: {out_path}")

if __name__ == "__main__":
    generate_adversarial_images()
