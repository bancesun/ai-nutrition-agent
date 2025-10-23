from pyzbar.pyzbar import decode
from PIL import Image
import requests

def get_qr_text(image_path):
    data = decode(Image.open(image_path))
    if not data:
        return None
    return data[0].data.decode('utf-8')

def lookup_nutrition_from_qr(qr_text):
    url = f"https://world.openfoodfacts.org/api/v2/product/{qr_text}.json"
    r = requests.get(url)
    if r.status_code == 200:
        prod = r.json().get("product", {})
        return prod.get("nutriments", {})
    return {}
