from pathlib import Path
import json
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[1]
schema=json.loads((ROOT/"data/sarvajna/metadata/tripadi.schema.json").read_text(encoding="utf-8"))
errors=[]
for p in (ROOT/"data/sarvajna/tripadis").glob("SAR-*.json"):
    if p.name.endswith(".template.json"): continue
    try: data=json.loads(p.read_text(encoding="utf-8"))
    except Exception as e: errors.append(f"{p}: {e}"); continue
    for e in Draft202012Validator(schema).iter_errors(data):
        errors.append(f"{p}: {e.message}")
if errors:
    print("\n".join(errors)); raise SystemExit(1)
print("Validation passed.")
