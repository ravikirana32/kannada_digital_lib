# Phase 4I — Pilot 1–5 Reconciliation Findings

## Major finding

The first five cannot safely be assigned a universal number based on web pages alone.

The current Kannada Wikisource page has a section-specific sequence under **ಜಾತಿಸ್ಮರಣ ಪದ್ದತಿ**. Other online transcriptions use a different global sequence. For example, one online list begins with `ನಂದಿಯನು ಏರಿದನ...`, followed by the Pushpadatta verse, while the current Wikisource page begins the displayed section with the Pushpadatta verse.

This is strong evidence that **source-specific numbering must be preserved**.

## Editorial consequence

Do not write:

`Sarvajna Tripadi #1 = whatever source calls #1`

Instead write:

`canonical_id = SAR-0001`
`source_id = SRC-002`
`source_number = 1`
`section = ಜಾತಿಸ್ಮರಣ ಪದ್ದತಿ`

A canonical/global number will only be assigned after edition reconciliation.

## Authenticity warning

Secondary scholarship and modern summaries caution that the first biographical poems are of uncertain authenticity and may contain interpolations. Therefore "appears first in a source" is not equivalent to "authentic Sarvajna poem."

## Current pilot status

1–5 remain `unresolved`.

The project has successfully demonstrated the need for:
- edition-specific numbering,
- source-specific locators,
- variant preservation,
- authenticity flags,
- and a separate canonical identifier.

## Next evidence needed

The exact 1924 Uttangi edition or a page-level trusted facsimile is still the most important missing evidence.
