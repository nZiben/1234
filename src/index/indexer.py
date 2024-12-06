import numpy as np
from src.models.colpali_wrapper import ColpaliEmbedder
from src.index.vector_index import VectorIndex
import pickle

class Indexer:
    def __init__(self):
        self.embedder = ColpaliEmbedder()
        self.vector_index = None

    def build_index(self, documents: list):
        embeddings = []
        for doc in documents:
            content = doc.get('content', '')
            if content:
                emb = self.embedder.get_embedding(content)
            else:
                # Если контент отсутствует, используем метаданные
                md = doc.get('metadata', '')
                emb = self.embedder.get_embedding(str(md))
            embeddings.append(emb)
        embeddings = np.array(embeddings)
        dim = embeddings.shape[1] if len(embeddings.shape) > 1 else len(embeddings)
        self.vector_index = VectorIndex(dim)
        self.vector_index.add(embeddings, documents)

    def get_vector_index(self):
        return self.vector_index

    def save_index(self, filepath: str):
        with open(filepath, 'wb') as f:
            pickle.dump(self.vector_index, f)
        print(f"Индекс сохранён в {filepath}")

    def load_index(self, filepath: str):
        with open(filepath, 'rb') as f:
            self.vector_index = pickle.load(f)
        print(f"Индекс загружен из {filepath}")
