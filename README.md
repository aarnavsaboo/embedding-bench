# embedding-bench

A small retrieval benchmark for comparing embedding models on the same labelled query set.

The benchmark records model dimension, encoding latency, corpus throughput and ranking quality. It is intended for local sentence-transformer style models where a smaller embedding model may be substantially faster while producing nearly the same retrieval quality on a particular corpus.

## Metrics

- Recall@k
- MRR@k
- nDCG@k
- queries/second
- documents/second during corpus encoding
- embedding dimension
- serialized vector size estimate

```bash
python -m embedding_bench run dataset.jsonl \
  --models sentence-transformers/all-MiniLM-L6-v2 BAAI/bge-small-en-v1.5
```

Results are dataset-specific. The project keeps the query labels and timing metadata next to each run instead of presenting one model as universally best.

Maintained by **Aarnav Saboo**.
