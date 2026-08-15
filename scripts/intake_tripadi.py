from pathlib import Path
import json,sys

ROOT=Path(__file__).resolve().parents[1]
if len(sys.argv)<2:
    print("Usage: python scripts/intake_tripadi.py 1")
    raise SystemExit(2)
n=int(sys.argv[1])
if n<1:
    raise SystemExit("Tripadi number must be >= 1")

out=ROOT/f"data/sarvajna/tripadis/SAR-{n:04d}.json"
if out.exists():
    raise SystemExit(f"{out.name} already exists")

d={
 "id":f"SAR-{n:04d}",
 "author":"ಸರ್ವಜ್ಞ",
 "work":"ಸರ್ವಜ್ಞ ತ್ರಿಪದಿಗಳು",
 "tripadi_number":n,
 "original":"",
 "padartha":"",
 "bhavartha":"",
 "life_message":"",
 "category":"",
 "keywords":[],
 "source":{"source_id":"","title":"","publisher":"","year":None,"locator":"","url":None,"verified":False,"notes":""},
 "rights":{"status":"needs_review","license":None,"permission_reference":None},
 "youtube":{"title":"","hook":"","script":"","description":"","tags":[]},
 "instagram":{"caption":"","hashtags":[],"alt_text":""},
 "review_status":"draft",
 "version":"1.0.0",
 "created_at":"",
 "updated_at":""
}
out.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding="utf-8")
print(out)
