# Changelog

## 0.10.0
- Added JWT authentication.
- Added researcher/reviewer/editor/admin RBAC.
- Protected candidate, comparison and publication routes.
- Added PostgreSQL User model and migration.
- Added audit helper and RBAC documentation.
- Added secure environment variables for JWT and admin bootstrap.



## 0.9.4
- Added API V1 development backend.
- Added candidate, comparison and publication endpoints.
- Added development JSON store seeded with B001 1–75.
- Added publication gate endpoint.
- Added API validation script and production-upgrade roadmap.



## 0.9.3
- Added Admin source-comparison workspace.
- Added B001 1–75 comparison queue.
- Added source comparison record schema.
- Added explicit variant/duplicate decision options.
- Added mobile source-comparison screen.
- Added source-comparison workflow documentation.
- Kept canonical publication gated by backend evidence checks.



## 0.9.2
- Upgraded Admin app to functional editorial review prototype.
- Upgraded Website to searchable Kannada reader prototype.
- Added API Contract V1 for shared canonical source of truth.
- Added production social generator gated by canonical/publication approval.
- Added shared review-state and canonical-record contracts.



## 0.9.1
- Added mobile Expo/React Native application scaffold.
- Added editorial admin Vite/React scaffold.
- Added B001 social metadata records for all 75 candidates.
- Added website B001 status data.
- Added product platform architecture documentation.
- Kept social publication blocked until canonical approval.



## 0.9.0
- Completed B001 source-acquisition reconciliation package for 1–75.
- Added full reconciliation JSON and decision matrix.
- Added source-specific numbering map.
- Added within-source exact/near-duplicate detection.
- Added section-boundary preservation.
- Kept canonical approval at 0/75 pending independent historical/critical evidence.



## 0.8.4
- B001-C: collected 25 source readings for candidates 51–75.
- Completed source acquisition for all B001 candidates 1–75.
- Preserved Wikisource section boundary at item 61.
- Preserved apparent source transcription/OCR irregularities.
- Added complete B001 source-acquisition status.
- Kept all 75 records canonicalization-blocked pending reconciliation and historical verification.



## 0.8.1
- Started operational Batch B001 (candidate slots 1–75).
- Seeded 5 records with existing source evidence.
- Added 70 explicit acquisition-pending records.
- Added B001 source references, import template, status and validation scripts.
- Added B001 research log.



## 0.8.0
- Consolidated Phase 6 corpus acquisition and reconciliation engineering.
- Added 2,100 candidate-slot manifest without fabricated text.
- Added batch configuration starting at 1–75.
- Added candidate schema and canonical promotion gate.
- Added progress, missing-source, batch-status and validation scripts.
- Added complete Phase 6 documentation.



## 0.7.0
- Consolidated Phase 5A and 5B into one Phase 5 release.
- Added final Phase 5 status and content gates.
- Added book publication schema.
- Added YouTube and Instagram output schemas.
- Added bhavartha record schema.
- Added phase5_final_check.py.
- Closed Phase 5 as an engineering milestone; unresolved content remains explicitly gated.



## 0.6.2
- Added Phase 5B historical verification evidence packets for SAR-0001 to SAR-0005.
- Added canonical selection rules and human review checklist.
- Added blocked canonical candidates.
- Added explicit historical/critical evidence status.
- Prevented premature canonical text selection.



## 0.6.1
- Started Phase 5A: canonical Sarvagna corpus foundation.
- Added canonical record schema.
- Initialized canonical records 1–5 from Phase 4 source evidence.
- Added editorial approval gates.
- Added publication output schema.
- Added bhavartha and social-output rules.
- Added Phase 5 validation script.
- Kept all five records publication-blocked pending verification.



## 0.6.0
- Consolidated Phase 4 into one replaceable release.
- Added final phase status and acceptance gates.
- Added research evidence URL manifest.
- Added phase4_final_check.py.
- Explicitly separated engineering completion from textual/copyright approval.



## 0.5.5
- Added first pairwise cross-source reconciliation for SAR-0001 to SAR-0005.
- Added similarity classifications and correspondence candidates.
- Confirmed source-order/numbering discrepancies.
- Prevented automatic global numbering.
- Kept canonical and authenticity decisions unresolved pending historical/critical evidence.



## 0.5.4
- Added actual source readings for pilot 1–5 from accessible online traditions.
- Added normalized SHA-256 fingerprints for each source reading.
- Added WEB-ALT-001 as secondary ordering/variant reference.
- Documented concrete numbering and wording discrepancies.
- Kept canonical text and authenticity unresolved.



## 0.5.3
- Added source acquisition manifest for records 1–14.
- Added automated normalized text reconciliation.
- Added variant register.
- Added authenticity register.
- Added source coverage reporting.
- Added publication approval gate.
- Added reconciliation unit test.



## 0.5.2
- Added Phase 4J historical verification ledger for records 1–14.
- Added separate authenticity and canonical-text gates.
- Added Sarvajna Sanchaya as SRC-005 discovery/reference source.
- Extended master index to research records 6–14.
- Added batch status reporting.



## 0.5.1
- Added Phase 4I pilot 1–5 reconciliation report.
- Documented source-numbering discrepancies across online transcriptions.
- Added authenticity-status model.
- Added source-numbering validation script.
- Kept pilot records unresolved and prevented premature canonical numbering.



## 0.4.9
- Added Phase 4G library/catalog discovery results.
- Added ranked bibliographic leads for the 1924 Uttangi edition.
- Kept SRC-003 unverified until an exact scan is located.
- Added source lead reporting tool.
- Updated pilot 1–5 status to await exact 1924 scan.



## 0.4.8
- Added Phase 4F 1924 Uttangi source-discovery audit.
- Marked SRC-003 as exact digital copy not yet located.
- Added bibliographic evidence record.
- Added source discovery status tool.
- Prevented later editions from being silently substituted for the 1924 edition.
- Updated pilot 1–5 status to await exact 1924 source.



## 0.4.7
- Added SRC-004 critical scholarly reference: L. Basavaraju's Paramartha.
- Expanded reconciliation from three to four source roles.
- Added corpus-count research and discrepancy documentation.
- Added rights-chain qualification for the 1924 Uttangi edition.
- Added pilot 1–5 four-source reconciliation manifest.
- Added source-role reporting.



## 0.4.6
- Added SRC-003: Uttangi 1924 historical-edition candidate.
- Added corpus reconciliation model.
- Added rights matrix.
- Added reconciliation utility.
- Added legal/source research notes for India.
- Expanded pilot source mapping to three-source reconciliation.



## 0.4.5
- Added SRC-001 vs SRC-002 comparison audit for Tripadis 1–5.
- Located pilot material in the 1957 Archive scan.
- Classified Archive OCR as unreliable for Kannada text comparison.
- Added visual-page review checklist.
- Prevented OCR from being treated as canonical source text.
- Updated master-index status to source-comparison.



## 0.4.3
- Added Phase 4B pilot records SAR-0001 through SAR-0005.
- Added Kannada bhavartha and life-message drafts.
- Added Wikisource attribution and licensing notes.
- Kept pilot records in editorial review pending Archive/Uttangi cross-check.
- Updated master index for pilot status.



## 0.4.2
- Completed Phase 4A source/corpus foundation.
- Added rights audit.
- Added variant register.
- Added source-comparison template.
- Added Phase 4A completion documentation.


## 0.4.1
- Added master source index for research queue 1–75.
- Added index progress report.
- Added controlled Tripadi intake helper.
- Added pilot 1–5 checklist.
- Explicitly separated research index from canonical published text.



## 0.3.0
- Consolidated Phase 1, 2 and 3 foundation.
- Added publishing pipeline.
- Added web reader/search/category/detail UI.
- Added admin/editor workflow foundation.
- Added social export.
- Added GitHub CI and smoke tests.

## 0.2.0
- Added JSON schema, validation and generators.

## 0.1.0
- Initial repository foundation.

## 0.4.0
- Added source registry and Phase 4 review pipeline.
- Added source/rights/review schemas.
- Added batch queue, duplicate check, review report and publish-candidate tools.
