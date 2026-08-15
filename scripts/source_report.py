import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=root/"data/sarvajna/sources/sources.json"
d=json.loads(p.read_text(encoding="utf-8"))
print("Sarvajna source-role report")
for s in d["sources"]:
    print(f"{s['source_id']}: {s['title']} | {s['role'] if 'role' in s else s['source_type']} | rights={s['rights_status']}")
