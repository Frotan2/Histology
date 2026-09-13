# Production Docs — Essential Histology 1405

These documents are the authoritative quality and release controls for the current Essential Histology edition.

## Reading order

1. `00_FINAL_EDITION_STANDARD.md` — the non-negotiable scope, scientific, pedagogical, assessment, evidence, and release standard.
2. `01_V3_CRITICAL_AUDIT.md` — the concrete defects and blockers found in the current v3 branch.
3. `03_DEEP_REBUILD_EXECUTION_PROMPT.md` — the execution specification for the deep content rebuild and final verification.
4. `02_RELEASE_SCORECARD.md` — release metrics and evidence to be populated during remediation/final QA.
5. `14_Final_Release_Audit.md` — first remediation audit.
6. `15_Second_Adversarial_Audit.md` — **authoritative: second adversarial audit, defects found and fixed, final metrics, stated limitations.**

## Authority rule

Older production reports may be preserved for provenance, but they are not authoritative when they conflict with `00_FINAL_EDITION_STANDARD.md`.

A document may not declare the edition Final merely because the files build or because an automated heading/keyword scan succeeds.

## Current release state

**Release Approved** — see `15_Second_Adversarial_Audit.md` (latest pass) and `14_Final_Release_Audit.md`.

All blockers in `01_V3_CRITICAL_AUDIT.md` are resolved with evidence. The final audit also records two defects found by adversarial review that the earlier gate missed, the reproducible metrics for both books, and the residual limitations, which are stated as limitations rather than labelled PASS.
