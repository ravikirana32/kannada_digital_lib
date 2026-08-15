from pathlib import Path
req=['api/package.json','api/src/server.js','api/src/routes/candidates.js','api/src/routes/comparisons.js','api/src/routes/publication.js','api/src/store/db.json','docs/API_V1.md']
m=[x for x in req if not Path(x).exists()]
if m: raise SystemExit('Missing: '+', '.join(m))
import json
d=json.loads(Path('api/src/store/db.json').read_text(encoding='utf-8'))
assert len(d['candidates'])==75
assert all(x['publication_ready'] is False for x in d['candidates'])
print('PASS: API V1 scaffold and 75 B001 candidate seed records are valid.')
print('Publication-ready candidates:',sum(x['publication_ready'] for x in d['candidates']))
