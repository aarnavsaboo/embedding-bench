from argparse import ArgumentParser
import json

from .compare import paired
from .dataset import load
from .io import read_rows,write_rows
from .report import summarize
from .runner import run_model


def main():
    parser=ArgumentParser()
    sub=parser.add_subparsers(dest="cmd",required=True)

    run=sub.add_parser("run")
    run.add_argument("dataset")
    run.add_argument("--models",nargs="+",required=True)
    run.add_argument("--batch-size",type=int,default=32)
    run.add_argument("-k",type=int,default=10)
    run.add_argument("--out",required=True)

    report=sub.add_parser("report")
    report.add_argument("path")

    compare=sub.add_parser("compare")
    compare.add_argument("path")
    compare.add_argument("left")
    compare.add_argument("right")
    compare.add_argument("--metric",choices=["recall","mrr","ndcg"],default="ndcg")

    args=parser.parse_args()
    if args.cmd=="run":
        dataset=load(args.dataset)
        first=True
        for model in args.models:
            rows=run_model(dataset,model,args.batch_size,args.k)
            write_rows(args.out,rows,append=not first)
            first=False
        print(json.dumps({"models":len(args.models),"queries":len(dataset.queries)}))
    elif args.cmd=="report":
        print(json.dumps(summarize(read_rows(args.path)),indent=2))
    else:
        print(json.dumps(paired(read_rows(args.path),args.left,args.right,args.metric),indent=2))


if __name__=="__main__":
    main()
