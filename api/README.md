# Sarvajna API V1

Development backend connecting the website, mobile and admin workflows.

## Endpoints

GET `/health`

GET `/api/candidates?q=`

GET `/api/candidates/:id`

POST `/api/candidates/:id/decision`

GET `/api/comparisons?candidate_id=`

POST `/api/comparisons`

GET `/api/publication/ready`

POST `/api/publication/check`

## Safety

This V1 uses a JSON development store. It does not yet provide authentication, PostgreSQL persistence, audit-grade permissions or production deployment.

Publication checks require:
- original Kannada
- bhavartha
- historical gate
- authenticity gate
- rights gate
- editorial gate

No source text is promoted merely because it exists in the development store.
