from pathlib import Path
import json
from ebooklib import epub
ROOT=Path(__file__).resolve().parents[1]; DATA=ROOT/"data/sarvajna/tripadis"; OUT=ROOT/"books/sarvajna/generated/epub/sarvajna-samagra.epub"
book=epub.EpubBook(); book.set_identifier("kannada-digital-library-sarvajna"); book.set_title("ಸರ್ವಜ್ಞ ಸಮಗ್ರ ತ್ರಿಪದಿಗಳು"); book.set_language("kn")
rows=[]
for p in DATA.glob("SAR-*.json"):
    if p.name.endswith(".template.json"): continue
    d=json.loads(p.read_text(encoding="utf-8"))
    if d["review_status"] in {"approved","published"}: rows.append(d)
chapters=[]
for d in sorted(rows,key=lambda x:x["tripadi_number"]):
    c=epub.EpubHtml(title=f"ತ್ರಿಪದಿ {d['tripadi_number']}",file_name=f"SAR-{d['tripadi_number']:04d}.xhtml",lang="kn")
    c.content=f"<html><body><h1>ತ್ರಿಪದಿ {d['tripadi_number']}</h1><p>{d['original']}</p><h2>ಭಾವಾರ್ಥ</h2><p>{d['bhavartha']}</p><h2>ಜೀವನ ಸಂದೇಶ</h2><p>{d.get('life_message','')}</p></body></html>"
    book.add_item(c); chapters.append(c)
book.add_item(epub.EpubNcx()); book.add_item(epub.EpubNav()); book.spine=["nav"]+chapters
OUT.parent.mkdir(parents=True,exist_ok=True); epub.write_epub(str(OUT),book); print("EPUB generated:",OUT)
