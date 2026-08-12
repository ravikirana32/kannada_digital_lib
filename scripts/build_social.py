from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data/sarvajna/tripadis"; OUT=ROOT/"data/sarvajna/indexes/social-export.json"
rows=[]
for p in DATA.glob("SAR-*.json"):
    if p.name.endswith(".template.json"): continue
    d=json.loads(p.read_text(encoding="utf-8"))
    if d["review_status"] in {"approved","published"}:
        rows.append({"id":d["id"],"tripadi_number":d["tripadi_number"],"youtube":d.get("youtube",{}),"instagram":d.get("instagram",{})})
OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding="utf-8")
print("Social export generated:",OUT)
