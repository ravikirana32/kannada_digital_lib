import json,sys
from pathlib import Path

src=Path("data/sarvajna/batches/B001/B001-candidates-1-75.json")
out=Path("data/sarvajna/social/B001-production")
out.mkdir(parents=True,exist_ok=True)
data=json.loads(src.read_text(encoding="utf-8"))["records"]
ready=[]
for r in data:
    approved=(r.get("editorial_status")=="approved" and r.get("publication_ready") is True)
    item={"candidate_id":r["candidate_id"],"approved_for_publish":approved}
    if approved:
        text=(r.get("source_readings") or [{}])[0].get("text","")
        item.update({
          "youtube":{"title":f"ಸರ್ವಜ್ಞ ತ್ರಿಪದಿ | {r['candidate_id']}","voiceover_kannada":text,
                     "description":text,"tags":["ಸರ್ವಜ್ಞ","ಸರ್ವಜ್ಞನ ವಚನಗಳು","ಕನ್ನಡ ಸಾಹಿತ್ಯ","Sarvajna"]},
          "instagram":{"hook":"ಇಂದಿನ ಸರ್ವಜ್ಞನ ವಚನ","on_screen_text":text,
                       "caption":text,"hashtags":["#ಸರ್ವಜ್ಞ","#ಕನ್ನಡಸಾಹಿತ್ಯ","#Kannada","#Sarvajna"]}
        })
    else:
        item["blocked_reason"]="Canonical/editorial/publication approval is not complete."
    ready.append(item)
(out/"B001-social-production.json").write_text(json.dumps({"records":ready},ensure_ascii=False,indent=2),encoding="utf-8")
print("Generated:",len(ready),"records; publishable:",sum(x["approved_for_publish"] for x in ready))
