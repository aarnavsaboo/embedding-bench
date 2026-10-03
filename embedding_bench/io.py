from pathlib import Path
import json


def read_rows(path:str)->list[dict]:
    return [json.loads(x) for x in Path(path).read_text().splitlines() if x.strip()]


def write_rows(path:str,rows:list[dict],append:bool=True):
    target=Path(path)
    target.parent.mkdir(parents=True,exist_ok=True)
    with target.open("a" if append else "w",encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row,sort_keys=True)+"\n")
