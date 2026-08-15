# API Contract V1

## GET /api/tripadis?query=
Returns only public/published canonical records.

## GET /api/tripadis/:canonicalId
Returns:
- original Kannada
- bhavartha
- source summary
- approved variants
- publication metadata

## Admin endpoints
- GET /api/admin/review-queue
- GET /api/admin/candidates/:id
- POST /api/admin/candidates/:id/decision
- POST /api/admin/candidates/:id/source
- POST /api/admin/candidates/:id/variant
- POST /api/admin/candidates/:id/bhavartha

## Publication
Social/book exports must consume approved canonical records only.
