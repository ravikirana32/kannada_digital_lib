# Publication Gate

A Tripadi can become `approved` or `published` only when all are true:

- source_id exists in the source registry
- source locator is recorded
- source wording has been checked against the source
- `source.verified = true`
- rights status is not `needs_review`
- Kannada bhavartha is present
- editorial review passes
- duplicate/variant issues are resolved or documented

Until then, keep the entry in research/review state.
