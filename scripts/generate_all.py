import subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
for s in ["validate_all.py","build_book.py","build_docx.py","build_social.py"]:
    subprocess.run([sys.executable,str(ROOT/"scripts"/s)],check=True)
print("Core generation completed.")
print("PDF: python scripts/build_pdf.py (requires Kannada TTF)")
print("EPUB: python scripts/build_epub.py")
