from pathlib import Path
import json
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parents[1]
schema=json.loads((ROOT/"data/sarvajna/metadata/tripadi.schema.json").read_text(encoding="utf-8"))
validator=Draft202012Validator(schema)
errors=[]
for p in sorted((ROOT/"data/sarvajna/tripadis").glob("SAR-*.json")):
    if p.name.endswith(".template.json"):
        continue
    try:
        d=json.loads(p.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{p}: invalid JSON: {exc}")
        continue
    for e in validator.iter_errors(d):
        errors.append(f"{p}: {'/'.join(map(str,e.absolute_path))}: {e.message}")
if errors:
    print("\n".join(errors)); raise SystemExit(1)
print("JSON validation passed.")
