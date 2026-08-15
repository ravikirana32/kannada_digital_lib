#!/usr/bin/env python3
import re, sys, unicodedata
from difflib import SequenceMatcher

def normalize(s):
    s=unicodedata.normalize("NFC",s or "")
    s=s.replace("\u200c","").replace("\u200d","")
    s=re.sub(r"\s+","",s)
    return s.replace("॥","।").strip()

def compare(a,b):
    na,nb=normalize(a),normalize(b)
    if not na or not nb: return {"class":"unresolved","similarity":None}
    if na==nb: return {"class":"exact","similarity":1.0}
    score=SequenceMatcher(None,na,nb).ratio()
    if score>=.98: c="minor_variant"
    elif score>=.90: c="wording_variant"
    else: c="major_variant"
    return {"class":c,"similarity":round(score,6)}

if len(sys.argv)!=3:
    print("Usage: python scripts/reconcile_texts.py source_a.txt source_b.txt")
    raise SystemExit(2)
a=open(sys.argv[1],encoding="utf-8").read()
b=open(sys.argv[2],encoding="utf-8").read()
print(compare(a,b))
