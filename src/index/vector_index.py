import faiss
import numpy as np

class VectorIndex:
    def __init__(self, dim: int):
        self.index = faiss.IndexFlatL2(dim)
        self.docs = []

    def add(self, embeddings: np.ndarray, docs: list):
        self.index.add(embeddings.astype(np.float32))
        self.docs.extend(docs)

    def search(self, query_embedding: np.ndarray, top_k: int = 5):
        query_embedding = query_embedding.astype(np.float32).reshape(1, -1)
        distances, indices = self.index.search(query_embedding, top_k)
        results = [self.docs[i] for i in indices[0]]
        return results
