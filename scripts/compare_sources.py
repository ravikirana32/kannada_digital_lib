from difflib import SequenceMatcher
import re,sys
def norm(s):
    return re.sub(r"\s+","",s.replace("॥","।").replace("\u200c","").replace("\u200d",""))
if len(sys.argv)!=3:
    print("Usage: python scripts/compare_sources.py source_a.txt source_b.txt"); raise SystemExit(2)
a=norm(open(sys.argv[1],encoding="utf-8").read()); b=norm(open(sys.argv[2],encoding="utf-8").read())
score=SequenceMatcher(None,a,b).ratio()
status="exact_normalized" if score==1 else ("minor_variant" if score>=.98 else ("wording_variant" if score>=.90 else "major_variant"))
print(f"status={status}\nsimilarity={score:.4f}")
