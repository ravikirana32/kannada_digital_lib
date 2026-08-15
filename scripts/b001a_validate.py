import json
from pathlib import Path
p=Path('data/sarvajna/batches/B001/B001-A-source-records-6-25.json')
r=json.loads(p.read_text(encoding='utf-8'))['records']
assert len(r)==20 and [x['source_number'] for x in r]==list(range(6,26))
assert all(x['canonical_status']=='pending' for x in r)
print('PASS: B001-A contains 20 source-backed records (6-25); none promoted to canonical.')
