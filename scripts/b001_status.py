import json
from pathlib import Path
p=Path('data/sarvajna/batches/B001/B001-candidates-1-75.json')
d=json.loads(p.read_text(encoding='utf-8'))
from collections import Counter
c=Counter(r['collection_status'] for r in d['records'])
print('B001:',d['batch_id'],'slots=',len(d['records']))
for k,v in sorted(c.items()): print(k,':',v)
print('source readings:',sum(bool(r['source_readings']) for r in d['records']))
print('canonical approved:',sum(r['editorial_status']=='approved' for r in d['records']))
