# RBAC + Authentication + Audit V1

## Roles

- researcher: read candidates/sources; create comparisons
- reviewer: researcher + comparison approval
- editor: reviewer + bhavartha/canonical/publication approval
- admin: all permissions

## Authentication

JWT bearer tokens. Passwords are bcrypt-hashed.

## Audit

Editorial actions are persisted through `audit_logs`. Production should make audit writes transactional with the business operation.

## Important security note

`users.json` is a development bootstrap only. Production credentials must live in PostgreSQL/secret management, not in source control.

## Login

`POST /api/auth/login`

Then send:

`Authorization: Bearer <token>`
