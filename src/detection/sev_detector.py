import pytesseract
from PIL import Image

def extract_text(image_path):
    """
    Extracts text from an image using pytesseract OCR.
    
    Args:
        image_path (str): The path to the image file.
        
    Returns:
        str: Extracted text, stripped of leading/trailing whitespace.
    """
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text.strip()

def check_semantic_drift(base_text, proc_text, threshold=0):
    """
    Checks if semantic drift occurred by comparing the length of strings 
    extracted from the human-visible image vs the preprocessed (flattened) image.
    
    Args:
        base_text (str): Test from the original (human-visible) image.
        proc_text (str): Text from the preprocessed image.
        threshold (int): Minimum length difference to flag as drift.
        
    Returns:
        int: 1 if drift is detected, 0 otherwise.
    """
    # Simple heuristic: if the preprocessed image reveals more text than the original, it's semantic drift.
    return int((len(proc_text) - len(base_text)) > threshold)
