import json
from pathlib import Path
p=Path('data/sarvajna/editorial/phase5B-evidence-decision-packet-1-5.json')
d=json.loads(p.read_text(encoding='utf-8'))
for r in d['records']:
    print(r['canonical_id'], '|', r['correspondence_status'], '| canonical=',r['canonical_selection'], '| authenticity=',r['authenticity_status'])
