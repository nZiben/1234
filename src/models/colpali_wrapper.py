from sentence_transformers import SentenceTransformer

class ColpaliEmbedder:
    def __init__(self, model_path: str = "models/colpali"):
        self.model = SentenceTransformer(model_path)

    def get_embedding(self, text: str):
        return self.model.encode(text)
