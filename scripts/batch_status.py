import json
from pathlib import Path
p=Path('data/sarvajna/review/historical-evidence-ledger-1-14.json')
d=json.loads(p.read_text(encoding='utf-8'))
rows=d['records']
print('Historical verification batch:',len(rows))
for r in rows:
    print(r['canonical_id'], '|', r['editorial_status'], '| authenticity=',r['authenticity_status'], '| canonical=',r['canonical_text_status'])
