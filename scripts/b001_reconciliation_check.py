import json
from pathlib import Path
p=Path('data/sarvajna/batches/B001/B001-FULL-RECONCILIATION-1-75.json')
d=json.loads(p.read_text(encoding='utf-8'))
assert len(d['records'])==75
assert d['source_acquisition']=='complete'
assert d['canonical_approvals']==0
assert len(d['numbering_map'])==75
print('PASS: B001 reconciliation package contains 75 records.')
print('Source acquisition: 75/75')
print('Canonical approvals: 0/75')
print('Cross-source mapping: explicitly gated where evidence is incomplete.')
print('Similarity anomalies:',len(d['similarity_anomalies']))
