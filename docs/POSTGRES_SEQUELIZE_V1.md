# PostgreSQL + Sequelize V1

Core tables: sources, candidates, source_readings, comparisons, bhavarthas, editorial_decisions, audit_logs.

Local:
1. `cp .env.example .env`
2. `docker compose up -d postgres`
3. `cd api && npm install`
4. `npx sequelize-cli db:migrate`

This is a development schema; production still needs authentication, RBAC, backups, monitoring and migration review.
