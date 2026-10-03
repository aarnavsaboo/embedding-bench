from pathlib import Path
import json


def write(path:str,model:str,ids:list[str],vectors:list[list[float]]):
    if len(ids)!=len(vectors):
        raise ValueError("ids and vectors must align")
    target=Path(path)
    target.parent.mkdir(parents=True,exist_ok=True)
    with target.open("w",encoding="utf-8") as handle:
        for item_id,vector in zip(ids,vectors):
            handle.write(json.dumps({
                "model":model,
                "id":item_id,
                "dimension":len(vector),
                "vector":vector,
            },separators=(",",":"))+"\n")


def read(path:str,model:str)->dict[str,list[float]]:
    out={}
    for line in Path(path).read_text().splitlines():
        if not line.strip():
            continue
        row=json.loads(line)
        if row["model"]!=model:
            raise ValueError("cache model does not match requested model")
        out[str(row["id"])]=[float(x) for x in row["vector"]]
    return out
