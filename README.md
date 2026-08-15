# Kannada Digital Library

**ಸರ್ವಜ್ಞ ಸಮಗ್ರ ತ್ರಿಪದಿಗಳು — ಮೂಲ ಕನ್ನಡ • ಭಾವಾರ್ಥ • ಜೀವನ ಸಂದೇಶ**

A data-first, open-source foundation for preserving and publishing classical Kannada wisdom.

## Current milestone

**Phase 1 + Phase 2 + Phase 3 complete foundation**

- Repository/documentation foundation
- Structured JSON data model
- Validation and publishing pipeline
- PDF/DOCX/EPUB/Markdown generation
- React/Vite reader
- Search and category filtering
- Tripadi detail view
- Admin/editor foundation
- Review workflow model
- YouTube/Instagram export
- GitHub CI

## Core rule

JSON is the canonical source. Original/source text must never be invented or reconstructed from memory. Source and rights metadata are mandatory before publication.

## Quick validation

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
npm run dev
```

## PDF

Place a Unicode Kannada font at:

`books/sarvajna/assets/NotoSansKannada-Regular.ttf`

Then:

```bash
python scripts/build_pdf.py
```

## EPUB

```bash
python scripts/build_epub.py
```

## Content status

The repository contains no fabricated Sarvajna source text. The website uses a clearly marked demo record for UI testing only.

## Master index

```bash
python scripts/index_report.py
python scripts/intake_tripadi.py 1
```

The intake helper creates an empty record only; it never invents source text.

## Phase 4A tools

```bash
python scripts/index_report.py
python scripts/find_duplicates.py
python scripts/review_report.py
python scripts/publish_candidates.py
```

Research-only comparison template: `data/sarvajna/review/source-comparison.template.json`

Rights audit: `data/sarvajna/metadata/rights-audit.json`

Variant register: `data/sarvajna/review/variant-register.json`
