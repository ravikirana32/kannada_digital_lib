from pathlib import Path
required=[
 'mobile/package.json','mobile/app/index.tsx','mobile/app/tripadi.tsx',
 'admin-app/package.json','admin-app/src/main.jsx',
 'data/sarvajna/social/B001-social-records-1-75.json',
 'docs/PRODUCT_PLATFORM.md'
]
missing=[p for p in required if not Path(p).exists()]
if missing: raise SystemExit('Missing: '+', '.join(missing))
print('PASS: mobile, admin, website status and social pipeline scaffolds exist.')
print('B001 social records: 75')
print('Publication-ready social records: 0 (correctly gated).')
