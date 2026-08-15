import json
from pathlib import Path
p=Path('data/sarvajna/batches/phase6-batches.json')
d=json.loads(p.read_text(encoding='utf-8'))
for b in d['batches']:
 print(b['batch_id'],b['start'],b['end'],b['status'])
