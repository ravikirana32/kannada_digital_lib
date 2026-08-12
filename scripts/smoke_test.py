from pathlib import Path
import json, subprocess, sys

ROOT=Path(__file__).resolve().parents[1]
required=[
 "README.md","requirements.txt",
 "data/sarvajna/metadata/tripadi.schema.json",
 "data/sarvajna/categories/categories.json",
 "scripts/validate_all.py","scripts/build_book.py",
 "scripts/build_docx.py","scripts/build_pdf.py","scripts/build_epub.py",
 "website/package.json","website/src/App.jsx"
]
missing=[x for x in required if not (ROOT/x).exists()]
if missing:
    print("Missing files:", *missing, sep="\n- "); raise SystemExit(1)

subprocess.run([sys.executable,str(ROOT/"scripts/validate_all.py")],check=True)
print("Smoke test passed.")
