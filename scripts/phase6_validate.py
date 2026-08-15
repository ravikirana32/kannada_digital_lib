import json
from pathlib import Path
required=[
 'data/sarvajna/review/PHASE6-FINAL-STATUS.json',
 'data/sarvajna/acquisition/corpus-acquisition-manifest-1-2100.json',
 'data/sarvajna/batches/phase6-batches.json',
 'data/sarvajna/corpus/candidate-record-schema.json',
 'data/sarvajna/canonical/CANONICAL_PROMOTION_GATE.md'
]
missing=[x for x in required if not Path(x).exists()]
if missing:
 print('MISSING'); print('\n'.join(missing)); raise SystemExit(1)
d=json.loads(Path(required[1]).read_text(encoding='utf-8'))
assert len(d['records'])==2100
assert all(r['canonical_id'] is None and r['publication_ready'] is False for r in d['records'])
print('PASS: Phase 6 corpus manifest and promotion gates are valid.')
print('Candidate slots:',len(d['records']))
print('Canonical records created by Phase 6:',sum(bool(r['canonical_id']) for r in d['records']))
