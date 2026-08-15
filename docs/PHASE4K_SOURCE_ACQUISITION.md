# Phase 4K — Source Acquisition & Reconciliation

## Purpose

Create a repeatable pipeline for acquiring, comparing and reviewing source text for records 1–14.

### Pipeline

1. Acquire source text.
2. Record edition/source locator.
3. Normalize Unicode/whitespace.
4. Compare text.
5. Register variants.
6. Assess authenticity separately.
7. Verify rights.
8. Editorial approval.
9. Only then create canonical text and bhavartha.

### Current source state

- SRC-001: Archive OCR available but unreliable for canonical transcription.
- SRC-002: Wikisource checked for 1–5; 6–14 pending.
- SRC-003: Exact 1924 scan not located.
- SRC-004: Critical-edition locators pending.
- SRC-005: Discovery/reference source; exact source mapping pending.

## Publication gate

A record cannot be published as canonical unless:
`text_verified = true`
AND `rights_verified = true`
AND `editorial_approved = true`.

No script should bypass this gate.
