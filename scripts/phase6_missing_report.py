import json
from pathlib import Path
p=Path('data/sarvajna/acquisition/corpus-acquisition-manifest-1-2100.json')
d=json.loads(p.read_text(encoding='utf-8'))
missing=[r['source_number'] for r in d['records'] if not r['source_evidence']]
print('Unpopulated candidate slots:',len(missing))
print('First 100:',missing[:100])
