from src.models.colpali_wrapper import ColpaliEmbedder

class Searcher:
    def __init__(self, vector_index):
        self.vector_index = vector_index
        self.embedder = ColpaliEmbedder()

    def search(self, query: str, top_k: int = 5):
        query_emb = self.embedder.get_embedding(query)
        results = self.vector_index.search(query_emb, top_k=top_k)
        return results
