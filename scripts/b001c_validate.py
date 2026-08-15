import json
from pathlib import Path
p=Path('data/sarvajna/batches/B001/B001-C-source-records-51-75.json')
r=json.loads(p.read_text(encoding='utf-8'))['records']
assert len(r)==25 and [x['source_number'] for x in r]==list(range(51,76))
assert all(x['canonical_status']=='pending' for x in r)
assert r[9]['section']=='ಜಾತಿಸ್ಮರಣ ಪದ್ದತಿ'
assert r[10]['section']=='ಲಿಂಗಾತಿಶಯ ಪದ್ಧತಿ'
print('PASS: B001-C contains 25 source-backed records (51-75).')
print('PASS: section transition at 61 preserved.')
print('B001 source acquisition: 75/75.')
