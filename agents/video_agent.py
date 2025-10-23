from PIL import Image
import pytesseract


def extract_text_from_image(image_path):
    """Extract text from a nutrition facts table image using OCR."""
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text
