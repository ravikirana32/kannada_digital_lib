import json
from pathlib import Path
p=Path("data/sarvajna/review/source-acquisition-manifest-1-14.json")
d=json.loads(p.read_text(encoding="utf-8"))
print("Source coverage — 1 to 14")
for r in d["records"]:
    ready=sum(1 for x in r["sources"].values() if x["status"] in {"checked","verified"})
    print(f"{r['canonical_id']}: {ready}/5 sources text-ready")
