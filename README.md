# embedding-bench

A local retrieval benchmark for comparing embedding models on the same corpus and labelled query set.

The benchmark keeps retrieval quality, encoding throughput, vector dimension and storage cost in the same experiment record. It is intended for choosing embedding models for RAG pipelines where a smaller local encoder can be attractive even if it gives up a small amount of retrieval quality.

The runner separates corpus encoding from query encoding so both costs remain visible.

## Measurements

### Retrieval

- Recall@k
- MRR@k
- nDCG@k
- per-query ranked document IDs
- query-level wins and regressions between models

### Systems

- corpus documents/second
- query encodes/second
- vector dimension
- estimated float32 / float16 vector bytes
- model load + encode wall time
- batch size
- vector-cache size
- corpus size and query count

## Workflow

```text
dataset.jsonl
      |
      +--> documents
      +--> labelled queries
      |
      v
model matrix
      |
      v
batched local encoding
      |
      +--> corpus vectors -> cache
      +--> query vectors
      |
      v
cosine ranking
      |
      v
per-query metrics
      |
      +--> aggregate report
      +--> paired model comparison
```

## Example

```bash
python -m embedding_bench run examples/dataset.jsonl \
  --models sentence-transformers/all-MiniLM-L6-v2 BAAI/bge-small-en-v1.5 \
  --batch-size 32 \
  --out runs/results.jsonl

python -m embedding_bench report runs/results.jsonl
python -m embedding_bench compare runs/results.jsonl model-a model-b
```

## Vector cache

Corpus embeddings can be cached in JSONL for small experiments. The cache stores model ID, document ID, dimension and vector values.

This is intentionally not a vector database. It keeps experiments portable and makes the cost/shape of the vectors visible.

## Why query-level comparisons?

Two embedding models can have nearly identical average Recall@10 while failing on different queries. Pairwise comparison reports the largest gains and regressions by query ID so a model change can be inspected rather than reduced to one number.

## Repository layout

- `dataset.py` — labelled corpus/query format
- `models.py` — local embedding adapters
- `batching.py` — deterministic batches
- `cache.py` — simple vector cache
- `ranking.py` — cosine ranking
- `metrics.py` — Recall/MRR/nDCG
- `runner.py` — end-to-end benchmark
- `report.py` — grouped summaries
- `compare.py` — paired model deltas
- `tests/` — deterministic tests

Maintained by **Aarnav Saboo**.
