import json
from pathlib import Path

p=Path("data/sarvajna/canonical/canonical-records-1-5.json")
d=json.loads(p.read_text(encoding="utf-8"))
assert len(d["records"]) == 5
required={"canonical_id","source_evidence","canonical_text","variants","authenticity","bhavartha","rights","editorial","publication","social"}
for r in d["records"]:
    missing=required-set(r)
    assert not missing, (r["canonical_id"],missing)
    assert r["publication"]["approved"] is False, r["canonical_id"]
print("PASS: Phase 5A canonical records 1-5 are schema-valid and publication-gated.")
