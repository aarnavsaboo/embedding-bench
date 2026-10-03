# Benchmark methodology

The benchmark evaluates embedding models on two independent axes: retrieval quality and systems cost.

## Evaluation unit

A dataset contains documents and labelled queries. Corpus vectors are encoded once per model/configuration, while query vectors are measured separately.

```text
documents --------> corpus encoder ----> vector cache
                                           |
queries ----------> query encoder ---------+
                                           |
                                           v
                                      cosine ranking
                                           |
                                           v
                                  per-query metrics
```

Keeping corpus and query encoding separate prevents a single throughput number from hiding different workload costs.

## Retrieval metrics

The benchmark stores ranked document IDs per query and derives Recall@k, MRR@k and nDCG@k from those rankings. Pairwise model comparisons operate on the same query IDs and should retain the largest gains and regressions, not only aggregate averages.

## Systems measurements

Useful model-selection data includes:

- corpus documents/second
- query encodes/second
- vector dimension
- batch size
- model load/encode wall time
- estimated vector storage

Storage estimates describe embedding vectors only; they are not full index-size estimates.

## Reproducibility

Keep dataset revision, model revision, normalization behavior, batch size and numerical precision attached to results. Hardware and runtime versions matter for throughput comparisons.

The vector cache is an experiment artifact, not a production vector database. Its purpose is portability and traceability.

## Adding model adapters

Adapters should expose deterministic batched encoding and report the resulting vector dimension. Ranking and metric code should remain independent of the model library so stored vectors can be reevaluated without loading the encoder again.
