import json
from pathlib import Path
p=Path('data/sarvajna/acquisition/corpus-acquisition-manifest-1-2100.json')
d=json.loads(p.read_text(encoding='utf-8'))
rows=d['records']
from collections import Counter
c=Counter(r['match_status'] for r in rows)
print('Phase 6 corpus candidates:',len(rows))
for k,v in sorted(c.items()): print(f'{k}: {v}')
print('source-backed:',sum(bool(r['source_evidence']) for r in rows))
print('canonical:',sum(bool(r['canonical_id']) for r in rows))
