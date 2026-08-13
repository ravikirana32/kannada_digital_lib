from pathlib import Path
import json
from collections import Counter
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/"data/sarvajna/tripadis"; SOURCE=ROOT/"data/sarvajna/sources/sources.json"
errors=[]; warnings=[]; ids=[]; nums=[]
for p in sorted(DATA.glob("SAR-*.json")):
    if p.name.endswith(".template.json"): continue
    d=json.loads(p.read_text(encoding="utf-8")); ids.append(d["id"]); nums.append(d["tripadi_number"])
    if d["review_status"] in {"source_verified","editorial_review","approved","published"}:
        if not d["source"].get("verified"): errors.append(f"{p.name}: verified/reviewed status but source.verified=false")
        if not d["source"].get("source_id"): errors.append(f"{p.name}: missing source_id")
        if not d["source"].get("locator"): errors.append(f"{p.name}: missing source locator")
    if d["review_status"] in {"approved","published"}:
        if d["rights"]["status"]=="needs_review": errors.append(f"{p.name}: approved/published with rights=needs_review")
        if not d["bhavartha"].strip(): errors.append(f"{p.name}: approved/published without bhavartha")
    if d["original"].strip().startswith("[DEMO"): errors.append(f"{p.name}: demo text in canonical content")
for v,c in Counter(ids).items():
    if c>1: errors.append(f"duplicate id: {v}")
for v,c in Counter(nums).items():
    if c>1: warnings.append(f"duplicate tripadi number: {v}")
if not SOURCE.exists(): errors.append("source registry missing")
else:
    source_ids={s["source_id"] for s in json.loads(SOURCE.read_text(encoding="utf-8"))["sources"]}
    for p in DATA.glob("SAR-*.json"):
        if p.name.endswith(".template.json"): continue
        sid=json.loads(p.read_text(encoding="utf-8"))["source"].get("source_id")
        if sid and sid not in source_ids: errors.append(f"{p.name}: source_id {sid} not found in registry")
print("Phase 4 audit")
print(f"Tripadi records: {len(ids)}")
print(f"Source records: {len(source_ids) if SOURCE.exists() else 0}")
for w in warnings: print("WARNING:",w)
if errors:
    print("\nERRORS:\n"+"\n".join(errors)); raise SystemExit(1)
print("Phase 4 audit passed.")
