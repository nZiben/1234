import os
from src.utils.image_extractor import ImageExtractor

class ImagePipeline:
    def __init__(self, image_dir: str):
        self.image_dir = image_dir
        self.image_extractor = ImageExtractor()

    def process_images(self):
        processed = []
        for root, dirs, files in os.walk(self.image_dir):
            for file in files:
                path = os.path.join(root, file)
                content = self.image_extractor.extract_text(path)
                processed.append({
                    'path': path,
                    'content': content,
                    'type': 'image'
                })
        return processed
