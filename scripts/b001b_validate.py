import json
from pathlib import Path
p=Path('data/sarvajna/batches/B001/B001-B-source-records-26-50.json')
r=json.loads(p.read_text(encoding='utf-8'))['records']
assert len(r)==25 and [x['source_number'] for x in r]==list(range(26,51))
assert all(x['canonical_status']=='pending' for x in r)
print('PASS: B001-B contains 25 source-backed records (26-50); none promoted to canonical.')
