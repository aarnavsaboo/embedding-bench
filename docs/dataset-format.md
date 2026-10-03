# Dataset format

The benchmark uses JSONL with explicit document and query records.

```json
{"type":"document","id":"d1","text":"Reciprocal-rank fusion combines ranked lists."}
{"type":"query","text":"How can ranked retrieval results be combined?","relevant":["d1"]}
```

A query may have multiple relevant documents. Keep labels independent of the embedding model being compared; otherwise the evaluation leaks the retrieval method into the target.
