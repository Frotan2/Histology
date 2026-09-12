# Production Docs — Essential Histology 1405

These documents are the authoritative quality and release controls for the current Essential Histology edition.

## Reading order

1. `00_FINAL_EDITION_STANDARD.md` — the non-negotiable scope, scientific, pedagogical, assessment, evidence, and release standard.
2. `01_V3_CRITICAL_AUDIT.md` — the concrete defects and blockers found in the current v3 branch.
3. `03_DEEP_REBUILD_EXECUTION_PROMPT.md` — the execution specification for the deep content rebuild and final verification.
4. `02_RELEASE_SCORECARD.md` — release metrics and evidence to be populated during remediation/final QA.

## Authority rule

Older production reports may be preserved for provenance, but they are not authoritative when they conflict with `00_FINAL_EDITION_STANDARD.md`.

A document may not declare the edition Final merely because the files build or because an automated heading/keyword scan succeeds.

## Current release state

**Candidate / Release Blocked.**

The branch is not permitted to claim finality until all blockers in `01_V3_CRITICAL_AUDIT.md` are resolved and the evidence required by the final standard is produced.
