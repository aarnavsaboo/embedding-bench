from __future__ import annotations

from .dataset import Dataset
from .metrics import evaluate
from .models import SentenceTransformerModel
from .ranking import rank


def run_model(dataset:Dataset,model_name:str,batch_size:int=32,k:int=10)->list[dict]:
    model=SentenceTransformerModel(model_name)
    doc_text=[x.text for x in dataset.documents]
    doc_ids=[x.id for x in dataset.documents]
    doc_vectors,doc_stats=model.encode(doc_text,batch_size)
    docs=dict(zip(doc_ids,doc_vectors))

    query_vectors,query_stats=model.encode([x.text for x in dataset.queries],batch_size)
    rows=[]
    for query,vector in zip(dataset.queries,query_vectors):
        ranking=rank(vector,docs)
        rows.append({
            "model":model_name,
            "query_id":query.id,
            "ranking":ranking[:k],
            "metrics":evaluate(ranking,set(query.relevant),k),
            "system":{
                "dimension":doc_stats["dimension"],
                "corpus_items_per_second":doc_stats["items_per_second"],
                "query_items_per_second":query_stats["items_per_second"],
                "model_load_seconds":doc_stats["load_seconds"],
                "batch_size":batch_size,
                "float32_bytes_per_vector":doc_stats["float32_bytes_per_vector"],
            },
        })
    return rows
