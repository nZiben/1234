import json
import os

class MetadataExtractor:
    def extract_metadata(self, metadata_path: str) -> dict:
        if os.path.splitext(metadata_path)[1].lower() == '.json':
            with open(metadata_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
