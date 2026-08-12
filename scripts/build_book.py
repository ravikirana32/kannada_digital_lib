from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
out=ROOT/"books/sarvajna/manuscript/part-001.md"
rows=[]
for p in (ROOT/"data/sarvajna/tripadis").glob("SAR-*.json"):
    if p.name.endswith(".template.json"): continue
    d=json.loads(p.read_text(encoding="utf-8"))
    if d["review_status"] in {"approved","published"}: rows.append(d)
rows.sort(key=lambda x:x["tripadi_number"])
lines=["# ಸರ್ವಜ್ಞ ಸಮಗ್ರ ತ್ರಿಪದಿಗಳು","## ಮೂಲ ಕನ್ನಡ • ಭಾವಾರ್ಥ • ಜೀವನ ಸಂದೇಶ",""]
for d in rows:
    lines += [f"## ತ್ರಿಪದಿ {d['tripadi_number']}","",f"> {d['original']}","",
              "**ಭಾವಾರ್ಥ**","",d["bhavartha"],"","**ಜೀವನ ಸಂದೇಶ**","",d.get("life_message",""),"",
              f"**ವರ್ಗ:** {d['category']}","",f"**ಮುಖ್ಯ ಪದಗಳು:** {', '.join(d['keywords'])}","", "---",""]
out.write_text("\n".join(lines),encoding="utf-8")
print(out)
