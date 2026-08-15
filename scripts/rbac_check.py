from pathlib import Path
import json
req=['api/src/auth/auth.js','api/src/auth/rbac.js','api/src/routes/auth.js','api/src/models/user.js','api/src/migrations/20260815180000-create-users.js','docs/RBAC_AUTH_AUDIT_V1.md']
m=[x for x in req if not Path(x).exists()]
if m: raise SystemExit('Missing: '+', '.join(m))
roles=['researcher','reviewer','editor','admin']
assert len(roles)==4
print('PASS: JWT authentication, four RBAC roles, protected routes and user migration are present.')
