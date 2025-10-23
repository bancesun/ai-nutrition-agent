from pyzbar.pyzbar import decode
from PIL import Image
import requests


def get_barcode(image_path):
    """Decode a barcode from a food packaging image and return the code string."""
    data = decode(Image.open(image_path))
    if not data:
        return None
    return data[0].data.decode('utf-8')


def lookup_nutrition_from_barcode(barcode_text):
    """Look up nutrition info using a product barcode via OpenFoodFacts API."""
    url = f"https://world.openfoodfacts.org/api/v2/product/{barcode_text}.json"
    r = requests.get(url)
    if r.status_code == 200:
        product = r.json().get("product", {})
        return product.get("nutriments", {})
    return {}
