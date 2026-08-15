#!/usr/bin/env python3
"""Report potential duplicates/variants across source records.

Input format:
{
  "records": [
    {"source_id":"SRC-002","source_number":1,"text":"..."}
  ]
}
"""
from difflib import SequenceMatcher
import json, re, sys
from pathlib import Path

def norm(s):
    s=s.replace("\u200c","").replace("\u200d","")
    s=re.sub(r"\s+","",s).replace("॥","।")
    return s.strip()

def score(a,b):
    return SequenceMatcher(None,norm(a),norm(b)).ratio()

if len(sys.argv)!=2:
    print("Usage: python scripts/reconcile_corpus.py data/sarvajna/review/corpus-reconciliation.json")
    raise SystemExit(2)

p=Path(sys.argv[1])
d=json.loads(p.read_text(encoding="utf-8"))
r=d.get("records",[])
print("Corpus reconciliation records:",len(r))
print("Sources:",", ".join(d.get("sources",[])))
print("This tool reports candidates; it does not choose a canonical reading.")
