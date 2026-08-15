import json
from pathlib import Path
p=Path('data/sarvajna/batches/B001/B001-candidates-1-75.json')
d=json.loads(p.read_text(encoding='utf-8'))
assert d['batch_id']=='B001' and len(d['records'])==75
assert [r['source_number'] for r in d['records']]==list(range(1,76))
assert all(not r['publication_ready'] for r in d['records'])
print('PASS: B001 contains exactly 75 controlled candidate records.')
