import subprocess,sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
for s in ["validate_all.py","build_book.py","build_docx.py"]:
    subprocess.run([sys.executable,str(R/"scripts"/s)],check=True)
print("Core generation complete.")
print("PDF requires NotoSansKannada-Regular.ttf; EPUB can be run separately.")
