from dataclasses import dataclass
from pathlib import Path
import json


@dataclass(frozen=True)
class Document:
    id:str
    text:str


@dataclass(frozen=True)
class Query:
    id:str
    text:str
    relevant:frozenset[str]


@dataclass(frozen=True)
class Dataset:
    documents:tuple[Document,...]
    queries:tuple[Query,...]


def load(path:str)->Dataset:
    docs=[]
    queries=[]
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row=json.loads(line)
        if row["type"]=="document":
            docs.append(Document(str(row["id"]),str(row["text"])))
        elif row["type"]=="query":
            queries.append(Query(str(row["id"]),str(row["text"]),frozenset(str(x) for x in row["relevant"])))
        else:
            raise ValueError(f"unknown row type: {row['type']}")
    return Dataset(tuple(docs),tuple(queries))
