import pytesseract
from PIL import Image

class ImageExtractor:
    def extract_text(self, image_path: str) -> str:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img, lang='eng')
        return text
