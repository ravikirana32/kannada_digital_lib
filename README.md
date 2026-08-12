# Kannada Digital Library

## Phase 3 — Platform Engineering Foundation

Book 1: **ಸರ್ವಜ್ಞ ಸಮಗ್ರ ತ್ರಿಪದಿಗಳು**

The project is data-first: JSON is the canonical source. The platform can run with verified content or demo records; demo content is clearly marked.

### Architecture
- `data/` canonical content
- `books/` publishing outputs
- `scripts/` validation/build automation
- `website/` React/Vite reader/search foundation
- `admin/` editor foundation
- `docs/` standards

### Validate
```bash
python -m pip install -r requirements.txt
python scripts/validate_all.py
python scripts/smoke_test.py
python scripts/generate_all.py
```

### Website
```bash
cd website
npm install
npm run dev
npm run build
```

No real Sarvajna source text is fabricated in this repository.
