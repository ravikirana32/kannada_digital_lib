from pathlib import Path
import json
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
ROOT=Path(__file__).resolve().parents[1]
font=ROOT/"books/sarvajna/assets/NotoSansKannada-Regular.ttf"
if not font.exists(): raise SystemExit("Add NotoSansKannada-Regular.ttf to books/sarvajna/assets/")
pdfmetrics.registerFont(TTFont("Kannada",str(font)))
styles=getSampleStyleSheet()
for n in ["Normal","Title","Heading1","Heading2"]: styles[n].fontName="Kannada"
out=ROOT/"books/sarvajna/generated/pdf/sarvajna-samagra.pdf"; out.parent.mkdir(parents=True,exist_ok=True)
story=[Paragraph("ಸರ್ವಜ್ಞ ಸಮಗ್ರ ತ್ರಿಪದಿಗಳು",styles["Title"]),Paragraph("ಮೂಲ ಕನ್ನಡ • ಭಾವಾರ್ಥ • ಜೀವನ ಸಂದೇಶ",styles["Normal"]),Spacer(1,12)]
rows=[]
for p in (ROOT/"data/sarvajna/tripadis").glob("SAR-*.json"):
    if p.name.endswith(".template.json"): continue
    d=json.loads(p.read_text(encoding="utf-8"))
    if d["review_status"] in {"approved","published"}: rows.append(d)
for d in sorted(rows,key=lambda x:x["tripadi_number"]):
    story += [Paragraph(f"ತ್ರಿಪದಿ {d['tripadi_number']}",styles["Heading1"]),Paragraph(d["original"],styles["Normal"]),Paragraph("ಭಾವಾರ್ಥ",styles["Heading2"]),Paragraph(d["bhavartha"],styles["Normal"]),Paragraph("ಜೀವನ ಸಂದೇಶ",styles["Heading2"]),Paragraph(d.get("life_message",""),styles["Normal"]),Spacer(1,10)]
SimpleDocTemplate(str(out),pagesize=A4).build(story); print(out)
