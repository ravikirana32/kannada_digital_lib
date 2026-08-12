# Admin Portal Foundation

The Phase 3 repository includes the admin contract and workflow. The web reader is the public UI; a production admin UI can be added behind authentication.

## Screens
- Dashboard
- Tripadi list
- Create/Edit
- Source verification
- Editorial review
- Approval
- Categories
- Export

## Workflow
draft → source_verified → editorial_review → approved → published

## Security
Do not expose an unauthenticated production editor. Authentication and role-based access belong in the production backend phase.
