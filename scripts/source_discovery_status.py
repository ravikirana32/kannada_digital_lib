import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=root/"data/sarvajna/sources/sources.json"
d=json.loads(p.read_text(encoding="utf-8"))
for s in d["sources"]:
    if s["source_id"]=="SRC-003":
        print("SRC-003 — Uttangi 1924")
        print("verification_status:", s["verification_status"])
        print("rights_status:", s["rights_status"])
        print("url:", s.get("url") or "(not located)")
        break
