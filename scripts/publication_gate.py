import json,sys
from pathlib import Path
p=Path("data/sarvajna/review/source-acquisition-manifest-1-14.json")
d=json.loads(p.read_text(encoding="utf-8"))
failed=[]
for r in d["records"]:
    g=r["publication_gate"]
    if not (g["text_verified"] and g["rights_verified"] and g["editorial_approved"]):
        failed.append(r["canonical_id"])
if failed:
    print("NOT READY:",", ".join(failed))
    raise SystemExit(1)
print("ALL RECORDS READY")
