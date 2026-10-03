from __future__ import annotations

from time import perf_counter


class SentenceTransformerModel:
    def __init__(self,name:str):
        from sentence_transformers import SentenceTransformer
        started=perf_counter()
        self.name=name
        self.model=SentenceTransformer(name)
        self.load_seconds=perf_counter()-started

    def encode(self,texts:list[str],batch_size:int=32)->tuple[list[list[float]],dict]:
        started=perf_counter()
        vectors=self.model.encode(
            texts,
            normalize_embeddings=True,
            batch_size=batch_size,
            show_progress_bar=False,
        ).tolist()
        elapsed=perf_counter()-started
        dimension=0 if not vectors else len(vectors[0])
        return vectors,{
            "seconds":elapsed,
            "items_per_second":len(texts)/max(elapsed,1e-9),
            "dimension":dimension,
            "float32_bytes_per_vector":dimension*4,
            "float16_bytes_per_vector":dimension*2,
            "load_seconds":self.load_seconds,
            "batch_size":batch_size,
        }
