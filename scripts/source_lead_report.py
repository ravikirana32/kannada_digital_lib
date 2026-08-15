import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=root/"data/sarvajna/sources/1924-source-leads.json"
d=json.loads(p.read_text(encoding="utf-8"))
print("1924 source discovery")
print("Exact scan found:", d["exact_1924_scan_found"])
for x in d["leads"]:
    print(f"{x['lead_id']}: {x['name']} [{x['confidence']}]")
