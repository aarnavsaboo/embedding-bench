from pathlib import Path
import json


def load_jsonl(path: str):
    docs: dict[str, str] = {}
    queries = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if row["type"] == "document":
            docs[row["id"]] = row["text"]
        elif row["type"] == "query":
            queries.append((row["text"], set(row["relevant"])))
        else:
            raise ValueError(f"unknown row type: {row['type']}")
    return docs, queries
