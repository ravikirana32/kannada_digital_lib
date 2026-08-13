from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]; DATA=ROOT/"data/sarvajna/tripadis"; ids=[]
for p in DATA.glob("SAR-*.json"):
    if p.name.endswith(".template.json"): continue
    d=json.loads(p.read_text(encoding="utf-8"))
    if d["review_status"] in {"approved","published"} and d["source"]["verified"] and d["rights"]["status"]!="needs_review" and d["bhavartha"].strip(): ids.append(d["id"])
out=ROOT/"data/sarvajna/indexes/publish-candidates.json"; out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps({"count":len(ids),"ids":ids},ensure_ascii=False,indent=2),encoding="utf-8"); print(out)
