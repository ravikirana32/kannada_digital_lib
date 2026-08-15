from pathlib import Path
req=['admin-app/src/main.jsx','website/src/App.jsx','scripts/build_social_production.py','docs/API_CONTRACT_V1.md']
m=[x for x in req if not Path(x).exists()]
if m: raise SystemExit('Missing: '+', '.join(m))
print('PASS: Admin V2, Website reader V2, Social production generator and API contract exist.')
