import argparse
import sys
import os

# Workaround to allow importing src module since this script lives in scripts/
# by ensuring the project root is in sys.path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from scripts.generate_dataset import generate_base_images
from src.attack.generate_adversarial import generate_adversarial_images
from src.preprocessing.rgba_to_rgb import run_preprocessing
from src.evaluation.run_experiments import run_evaluation

def main():
    parser = argparse.ArgumentParser(description="Run the full Semantic Drift evaluation pipeline.")
    parser.add_argument("--config", type=str, default="experiments/config.yaml", help="Path to configuration file")
    args = parser.parse_args()
    
    config_path = args.config
    
    print("=== Step 1: Generating Base Images ===")
    generate_base_images(config_path)
    
    print("\n=== Step 2: Generating Adversarial Images ===")
    generate_adversarial_images(config_path)
    
    print("\n=== Step 3: Running Preprocessing ===")
    run_preprocessing(config_path)
    
    print("\n=== Step 4: SEV Detect & Evaluate ===")
    run_evaluation(config_path)
    
    print("\nPipeline complete.")

if __name__ == "__main__":
    # Workaround to allow importing src module since this script lives in scripts/
    # by ensuring the project root is in sys.path
    import os
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
        
    main()
