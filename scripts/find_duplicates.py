from pathlib import Path
import json,re
from collections import defaultdict
ROOT=Path(__file__).resolve().parents[1]; groups=defaultdict(list)
for p in (ROOT/"data/sarvajna/tripadis").glob("SAR-*.json"):
    if p.name.endswith(".template.json"): continue
    d=json.loads(p.read_text(encoding="utf-8")); t=re.sub(r"\s+"," ",d["original"].strip())
    if t: groups[t].append((d["id"],p.name))
dupes={k:v for k,v in groups.items() if len(v)>1}
if not dupes: print("No duplicate original-text records found.")
else:
    for text,items in dupes.items(): print("DUPLICATE:",items,"\n",text)
