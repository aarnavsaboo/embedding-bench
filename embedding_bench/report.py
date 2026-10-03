from collections import defaultdict


def summarize(rows:list[dict])->list[dict]:
    groups=defaultdict(list)
    for row in rows:
        groups[row["model"]].append(row)
    output=[]
    for model,group in sorted(groups.items()):
        first=group[0]["system"]
        output.append({
            "model":model,
            "queries":len(group),
            "recall":sum(x["metrics"]["recall"] for x in group)/len(group),
            "mrr":sum(x["metrics"]["mrr"] for x in group)/len(group),
            "ndcg":sum(x["metrics"]["ndcg"] for x in group)/len(group),
            "dimension":first["dimension"],
            "corpus_items_per_second":first["corpus_items_per_second"],
            "query_items_per_second":first["query_items_per_second"],
            "model_load_seconds":first["model_load_seconds"],
            "float32_bytes_per_vector":first["float32_bytes_per_vector"],
        })
    return output
