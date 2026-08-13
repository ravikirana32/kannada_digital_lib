from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[1]
if len(sys.argv)!=3: print("Usage: python scripts/create_batch.py 1 75"); raise SystemExit(2)
start,end=map(int,sys.argv[1:]); out=ROOT/f"data/sarvajna/review/batch-{start:04d}-{end:04d}.json"
items=[{"tripadi_number":n,"status":"unassigned","source_id":"","reviewer":"","notes":""} for n in range(start,end+1)]
out.write_text(json.dumps({"batch":f"{start}-{end}","items":items},ensure_ascii=False,indent=2),encoding="utf-8"); print(out)
