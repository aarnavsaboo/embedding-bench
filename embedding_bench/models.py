from time import perf_counter


class SentenceTransformerModel:
    def __init__(self, name: str):
        from sentence_transformers import SentenceTransformer
        self.name = name
        self.model = SentenceTransformer(name)

    def encode(self, texts: list[str]) -> tuple[list[list[float]], dict]:
        started = perf_counter()
        vectors = self.model.encode(texts, normalize_embeddings=True).tolist()
        elapsed = perf_counter() - started
        dimension = 0 if not vectors else len(vectors[0])
        return vectors, {
            "seconds": elapsed,
            "items_per_second": len(texts) / max(elapsed, 1e-9),
            "dimension": dimension,
            "float32_bytes_per_vector": dimension * 4,
        }
