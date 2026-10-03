# Benchmark design

Embedding comparisons should freeze the corpus, queries and relevance labels before changing models.

Corpus encoding is usually a batch/offline cost while query encoding is an online cost. The runner therefore records them separately.

Vector dimension matters because it changes storage and similarity-computation cost. A model with slightly higher retrieval quality can produce much larger vectors, so the report keeps dimension and estimated vector bytes beside retrieval metrics.

The pairwise comparison is especially useful when two models have similar aggregate scores. It shows whether the newer model makes consistent small gains or simply swaps one group of failures for another.
