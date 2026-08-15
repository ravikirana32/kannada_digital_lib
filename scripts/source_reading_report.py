import json
from pathlib import Path
p=Path('data/sarvajna/review/actual_text/pilot-1-5-actual-source-readings.json')
d=json.loads(p.read_text(encoding='utf-8'))
for r in d['records']:
    print(r['canonical_id'], 'sources=', len(r['source_readings']), 'status=', r['editorial_status'])
    for s in r['source_readings']:
        print('  ',s['source_id'], 'number=',s['source_number'], 'sha256=',s['normalized_sha256'][:12])
