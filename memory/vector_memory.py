# memory/vector_memory.py

from sentence_transformers import SentenceTransformer
import numpy as np

class VectorMemory:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        print("🔧 Loading embedding model...")
        self.embedder = SentenceTransformer(model_name)

        # Stores memory as →  { "text": str, "vector": np.array }
        self.memory = []

    def embed(self, text: str):
        """Convert text to vector embeddings."""
        vector = self.embedder.encode([text])[0]
        return np.array(vector)

    def add_memory(self, text: str):
        """Store a memory chunk with its vector."""
        vector = self.embed(text)
        self.memory.append({
            "text": text,
            "vector": vector
        })
        print("🧠 Memory stored:", text[:40], "...")

    def similarity(self, v1, v2):
        """Cosine similarity."""
        return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

    def search(self, query: str, top_k=3):
        """Retrieve the most relevant memories."""
        query_vec = self.embed(query)

        results = []
        for item in self.memory:
            sim = self.similarity(query_vec, item["vector"])
            results.append((sim, item["text"]))

        results.sort(reverse=True, key=lambda x: x[0])
        return results[:top_k]

