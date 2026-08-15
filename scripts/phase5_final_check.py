import json
from pathlib import Path
required=[
 'data/sarvajna/canonical/canonical-record-schema.json',
 'data/sarvajna/canonical/canonical-records-1-5.json',
 'data/sarvajna/editorial/editorial-gate-matrix-1-5.json',
 'data/sarvajna/editorial/phase5B-evidence-decision-packet-1-5.json',
 'data/sarvajna/publication/book-record-schema.json',
 'data/sarvajna/publication/youtube-record-schema.json',
 'data/sarvajna/publication/instagram-reel-schema.json',
 'data/sarvajna/bhavartha/bhavartha-record-schema.json',
 'data/sarvajna/review/PHASE5-FINAL-STATUS.json'
]
missing=[p for p in required if not Path(p).exists()]
if missing:
    print('MISSING:')
    print('\n'.join(missing))
    raise SystemExit(1)
status=json.loads(Path('data/sarvajna/review/PHASE5-FINAL-STATUS.json').read_text(encoding='utf-8'))
records=json.loads(Path('data/sarvajna/canonical/canonical-records-1-5.json').read_text(encoding='utf-8'))['records']
assert len(records)==5
assert all(not r['publication']['approved'] for r in records)
print('PASS: Phase 5 consolidated package is structurally complete.')
print('Canonical pilot records:',len(records))
print('Open content gates:',len(status['open_content_gates']))
print('Publication remains safely gated.')
