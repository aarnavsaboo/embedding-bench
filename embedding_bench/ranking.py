from math import sqrt


def normalize(v: list[float]) -> list[float]:
    norm = sqrt(sum(x * x for x in v))
    if norm == 0:
        raise ValueError("zero vector")
    return [x / norm for x in v]


def cosine(a: list[float], b: list[float]) -> float:
    if len(a) != len(b):
        raise ValueError("dimension mismatch")
    return sum(x * y for x, y in zip(normalize(a), normalize(b)))


def rank(query: list[float], documents: dict[str, list[float]]) -> list[str]:
    return [
        doc_id for doc_id, _ in sorted(
            ((doc_id, cosine(query, vector)) for doc_id, vector in documents.items()),
            key=lambda item: (-item[1], item[0]),
        )
    ]
