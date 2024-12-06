import os
from src.utils.pdf_extractor import PDFExtractor
from src.utils.docx_extractor import DocxExtractor

class TextPipeline:
    def __init__(self, text_dir: str):
        self.text_dir = text_dir
        self.pdf_extractor = PDFExtractor()
        self.docx_extractor = DocxExtractor()

    def process_documents(self):
        processed = []
        for root, dirs, files in os.walk(self.text_dir):
            for file in files:
                path = os.path.join(root, file)
                ext = os.path.splitext(file)[1].lower()

                if ext == '.pdf':
                    content = self.pdf_extractor.extract_text(path)
                elif ext == '.docx':
                    content = self.docx_extractor.extract_text(path)
                elif ext == '.txt':
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                else:
                    continue

                processed.append({
                    'path': path,
                    'content': content,
                    'type': 'text'
                })
        return processed
