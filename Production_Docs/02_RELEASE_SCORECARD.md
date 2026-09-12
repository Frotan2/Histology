# Release Scorecard — Essential Histology 1405

This scorecard defines what must be measured before the edition can be called Final. Values must be generated from the current branch, not copied from an older report.

| Dimension | Minimum release evidence | Current status |
|---|---|---|
| Scope | Exact 16-chapter mapping, automated leakage check | PASS on scope; final leakage scan pending |
| Scientific accuracy | Zero known critical/high defects; semantic review of high-risk claims | BLOCKED |
| Source alignment | Explicit mapping to Junqueira 17th chapter scope and major teaching points; no fabricated citations | BLOCKED |
| Chapter completeness | Every LO taught, contextualized, retrieved, and assessed | BLOCKED |
| Duplication | No material semantic duplicates or contradictory repeated explanations | BLOCKED |
| Terminology | Consistent definitions for major histology structures/molecules across all chapters | BLOCKED |
| Recognition teaching | Major slide-identification patterns and common confusions taught | BLOCKED |
| Clinical integration | Major structure–function–disease links accurate and appropriately qualified | BLOCKED |
| Question Bank breadth | Adequate coverage of all major objectives with varied cognitive levels | BLOCKED |
| Question traceability | 100% chapter/content-unit/LO mapping | BLOCKED |
| Question validity | 100% one-best-answer and explanation consistency on audited set; no known answer conflicts | BLOCKED |
| Visual quality | Accurate, useful, provenance-tracked teaching visuals | BLOCKED |
| Build reproducibility | Clean regeneration from canonical source | PENDING |
| Cross-format consistency | PDF/DOCX/EPUB equivalent in content and order | PENDING |
| Render QA | Representative page inspection for every chapter + targeted problem pages | PENDING |
| Documentation integrity | README/reports/artifacts describe the same edition and status | IN PROGRESS |
| Adversarial verification | Separate verification pass not trusting prior PASS labels | BLOCKED |

## Quantitative checks to populate at finalization

The final evidence report must provide actual values for:

- canonical source word count;
- per-chapter word counts;
- number of learning objectives;
- number of objectives with complete teaching/retrieval/assessment mapping;
- Question Bank total;
- questions by chapter;
- questions by cognitive level;
- questions by difficulty;
- percentage with complete traceability;
- duplicate/near-duplicate question count;
- answer-key conflict count;
- unresolved contradiction count;
- unresolved high-severity scientific issue count;
- number of visual assets and provenance status;
- artifact hashes/sizes and PDF page count;
- deterministic rebuild result.

## Scoring philosophy

Do not optimize for a cosmetic score. A single critical scientific error can block release regardless of how many lower-level checks pass.

The strongest final score is therefore evidence-weighted:

**scientific integrity > scope integrity > learning integrity > assessment integrity > reproducibility > presentation polish.**
