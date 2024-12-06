import PyPDF2

class PDFExtractor:
    def extract_text(self, pdf_path: str) -> str:
        text = ""
        with open(pdf_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        return text
