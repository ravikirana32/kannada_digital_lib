from pathlib import Path
import json
from collections import Counter
ROOT=Path(__file__).resolve().parents[1]; DATA=ROOT/"data/sarvajna/tripadis"; rows=[]
for p in DATA.glob("SAR-*.json"):
    if not p.name.endswith(".template.json"): rows.append(json.loads(p.read_text(encoding="utf-8")))
status=Counter(x["review_status"] for x in rows); rights=Counter(x["rights"]["status"] for x in rows)
lines=["# Sarvajna Content Review Report","",f"Total canonical Tripadis: {len(rows)}","","## Status"]
for k in ["draft","source_verified","editorial_review","approved","published"]: lines.append(f"- {k}: {status[k]}")
lines += ["","## Rights"]
for k,v in rights.items(): lines.append(f"- {k}: {v}")
out=ROOT/"data/sarvajna/review/CONTENT-REPORT.md"; out.write_text("\n".join(lines)+"\n",encoding="utf-8"); print(out)
