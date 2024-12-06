import docx

class DocxExtractor:
    def extract_text(self, docx_path: str) -> str:
        doc = docx.Document(docx_path)
        return "\n".join([p.text for p in doc.paragraphs])
