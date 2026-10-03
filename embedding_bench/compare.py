def paired(rows:list[dict],left:str,right:str,metric:str="ndcg")->dict:
    a={x["query_id"]:x for x in rows if x["model"]==left}
    b={x["query_id"]:x for x in rows if x["model"]==right}
    keys=sorted(set(a)&set(b))
    deltas=[
        (key,float(b[key]["metrics"][metric])-float(a[key]["metrics"][metric]))
        for key in keys
    ]
    ordered=sorted(deltas,key=lambda x:x[1])
    return {
        "metric":metric,
        "pairs":len(deltas),
        "mean_delta_right_minus_left":0.0 if not deltas else sum(x[1] for x in deltas)/len(deltas),
        "right_wins":sum(x[1]>0 for x in deltas),
        "ties":sum(x[1]==0 for x in deltas),
        "right_losses":sum(x[1]<0 for x in deltas),
        "largest_regressions":ordered[:5],
        "largest_improvements":list(reversed(ordered[-5:])),
    }
