import json
from pathlib import Path
p=Path('data/sarvajna/review/pilot-1-5-reconciliation-report.json')
d=json.loads(p.read_text(encoding='utf-8'))
for r in d['records']:
    nums=[x['source_number'] for x in r['candidate_mappings'] if x.get('source_number') is not None]
    assert all(isinstance(n,int) for n in nums)
print('OK: source-specific numbering is represented independently.')
print('Records:',len(d['records']))
