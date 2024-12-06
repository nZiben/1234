import os
from src.utils.metadata_extractor import MetadataExtractor

class MetadataPipeline:
    def __init__(self, metadata_dir: str):
        self.metadata_dir = metadata_dir
        self.extractor = MetadataExtractor()

    def process_metadata(self):
        processed = []
        for root, dirs, files in os.walk(self.metadata_dir):
            for file in files:
                path = os.path.join(root, file)
                md = self.extractor.extract_metadata(path)
                processed.append({
                    'path': path,
                    'content': "",
                    'metadata': md,
                    'type': 'metadata'
                })
        return processed
