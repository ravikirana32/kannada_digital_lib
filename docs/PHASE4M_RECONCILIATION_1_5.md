# Phase 4M — First Cross-Source Reconciliation 1–5

## Result

The first reconciliation pass confirms that the accessible online traditions have **different ordering and numbering**.

This is not a simple text-cleaning problem. Several source numbers point to entirely different verses.

### Decision

We will not map source number `N` to canonical ID `SAR-N` automatically.

Instead:
- source numbers remain source-specific,
- candidate correspondence IDs are separate,
- exact/near-text similarity is only supporting evidence,
- historical/critical source evidence is required for canonical identity.

## Reconciliation classes

- `exact`
- `minor_variant`
- `wording_variant`
- `major_or_different`
- `unresolved`

## Important limitation

The first five are **not approved**. The 1924 Uttangi edition has not been directly inspected, the 1957 OCR is unreliable, and the critical edition locations are not yet established.

## Outcome

The project has now demonstrated that its reconciliation engine must handle:
1. reordering,
2. source-specific numbering,
3. variants,
4. possible corpus differences,
5. authenticity uncertainty.

This is a successful Phase 4M result even though no canonical decisions were made.
