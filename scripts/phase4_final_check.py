from pathlib import Path
import json
required=[
 'data/sarvajna/editions/edition-registry.json',
 'data/sarvajna/review/source-acquisition-manifest-1-14.json',
 'data/sarvajna/review/variant-register.json',
 'data/sarvajna/review/authenticity-register.json',
 'data/sarvajna/review/PHASE4-FINAL-STATUS.json',
 'data/sarvajna/review/reconciliation/reconciliation-1-5.json',
 'docs/PHASE4_FINAL_COMPLETION.md'
]
missing=[p for p in required if not Path(p).exists()]
if missing:
 print('MISSING:')
 for p in missing: print(' -',p)
 raise SystemExit(1)
d=json.loads(Path('data/sarvajna/review/PHASE4-FINAL-STATUS.json').read_text(encoding='utf-8'))
print('Phase 4 consolidated package:', d['version'])
print('Engineering complete:', len(d['completed']))
print('Open evidence gates:', len(d['blocked_gates']))
print('PASS: package structure is complete; content approval remains gated.')
