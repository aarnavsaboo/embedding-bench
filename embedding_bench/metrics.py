from math import log2


def evaluate(ranked: list[str], relevant: set[str], k: int = 10) -> dict[str, float]:
    top = ranked[:k]
    recall = 0.0 if not relevant else len(set(top) & relevant) / len(relevant)
    rr = next((1 / i for i, x in enumerate(top, 1) if x in relevant), 0.0)
    dcg = sum(1 / log2(i + 1) for i, x in enumerate(top, 1) if x in relevant)
    ideal = sum(1 / log2(i + 1) for i in range(1, min(k, len(relevant)) + 1))
    return {"recall": recall, "mrr": rr, "ndcg": 0.0 if ideal == 0 else dcg / ideal}
