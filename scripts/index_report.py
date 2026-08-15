from pathlib import Path
import json
from collections import Counter

ROOT=Path(__file__).resolve().parents[1]
p=ROOT/"data/sarvajna/review/master-source-index.json"
d=json.loads(p.read_text(encoding="utf-8"))
records=d["records"]
status=Counter(x["status"] for x in records)
verified=sum(x["source_text_verified"] for x in records)
rights=sum(x["rights_cleared"] for x in records)
print("Master Source Index")
print("Records:",len(records))
print("Source-text verified:",verified)
print("Rights cleared:",rights)
print("Status:")
for k,v in sorted(status.items()):
    print(f"  {k}: {v}")
