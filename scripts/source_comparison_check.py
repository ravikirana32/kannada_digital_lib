import json
from pathlib import Path
req=[
 'admin-app/src/main.jsx',
 'mobile/app/compare.tsx',
 'data/sarvajna/reconciliation/comparison-record-schema.json',
 'data/sarvajna/reconciliation/B001-comparison-queue-1-75.json',
 'docs/SOURCE_COMPARISON_WORKFLOW.md'
]
m=[x for x in req if not Path(x).exists()]
if m: raise SystemExit('Missing: '+', '.join(m))
q=json.loads(Path(req[3]).read_text(encoding='utf-8'))
assert len(q['records'])==75
assert all(x['decision']=='pending' for x in q['records'])
print('PASS: source-comparison workflow ready for all 75 B001 candidates.')
