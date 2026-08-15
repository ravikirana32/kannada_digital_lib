# Source Research — 2026-08-13

## Decision

We will use a **two-source strategy**.

### SRC-001 — Internet Archive / Uttangi 1957
Historical/reference source:
- https://archive.org/details/in.ernet.dli.2015.363853/mode/2up
- Use for discovery, comparison and textual verification.
- Keep `rights_status = needs_review`.
- Do not treat the 1957 edition itself as an unrestricted redistribution source.

### SRC-002 — Kannada Wikisource
Reference/machine-readable candidate:
- https://kn.wikisource.org/wiki/ಸರ್ವಜ್ಞನ_ವಚನಗಳು
- It contains numbered Tripadis and topical sections.
- Wikisource's general copyright policy says user contributions are normally released under CC BY-SA/GFDL unless otherwise noted.
- However, the underlying source/edition of a transcription must still be traced before we make it our canonical redistribution source.
- Therefore it remains `rights_review`, not `public_domain`.

## Historical basis

Kannada scholarly material on Channappa Uttangi states that his 1924 edited *Sarvajna Vachanagalu* was the result of work from 1915–1924 and involved approximately 2,000 vachanas. It also describes his examination of manuscript/printed sources and his organization of the material into spiritual, ethical and worldly sections.

## Project rule

**Reference widely, publish conservatively.**

No canonical Tripadi text is published until:
1. the source is identified,
2. the exact locator is recorded,
3. the wording is checked,
4. rights are cleared or otherwise documented as permitted,
5. source review passes,
6. editorial review passes.

## Next content milestone

Do not bulk-import 1–75 yet.

First:
1. resolve the canonical rights/source basis,
2. build the master source index,
3. verify Tripadis 1–5 against selected source(s),
4. then scale the 1–75 research batch.
