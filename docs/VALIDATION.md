# Validation

## Backend/data
```bash
python -m pip install -r requirements.txt
python scripts/validate_all.py
python scripts/smoke_test.py
python scripts/generate_all.py
```

## Website
```bash
cd website
npm install
npm run build
```

## PDF
Add `NotoSansKannada-Regular.ttf` to:
`books/sarvajna/assets/`

Then:
```bash
python scripts/build_pdf.py
```

## EPUB
```bash
python scripts/build_epub.py
```
