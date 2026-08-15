from pathlib import Path
req=['api/package.json','api/.sequelizerc','api/src/config/database.js','api/src/models/index.js','api/src/migrations/20260815170000-create-core.js','docker-compose.yml','.env.example']
m=[x for x in req if not Path(x).exists()]
if m: raise SystemExit('Missing: '+', '.join(m))
print('PASS: PostgreSQL + Sequelize V1 schema package is present.')
