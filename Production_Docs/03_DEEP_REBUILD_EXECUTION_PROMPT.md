# Deep Rebuild Execution Prompt — Essential Histology 1405

You are the senior medical-education author, histology specialist, scientific fact-checker, curriculum architect, assessment designer, copy editor, and release engineer responsible for transforming the current v3 branch into the strongest defensible final edition of **Essential Histology — A Concept-Based Guide for PGME**.

Do not behave as a formatter. Do not merely expand word count. Do not preserve a weak passage because it already exists. Do not trust previous PASS labels. Treat the existing v3 book as a **candidate source requiring adversarial reconstruction**.

## Mission

Produce a genuinely excellent two-book learning system aligned exactly to the official Afghanistan 1405 Medical Specialty Examination syllabus and scientifically grounded in Junqueira’s Basic Histology, 17th Edition.

The target is not “longer”. The target is:

**accurate + complete + understandable + memorable + visually recognizable + clinically connected + exam-ready + traceable + reproducible.**

A modest-background learner should be able to learn the material without feeling that the book is a fact dump. An instructor should be able to teach from it directly. An expert should find the statements careful enough to trust.

## Absolute scope lock

Core Book 1 and core Book 2 must contain exactly:

1. Histology and Its Methods of Study → Junqueira Ch. 1
2. The Cytoplasm → Ch. 2
3. The Nucleus → Ch. 3
4. Epithelial Tissue → Ch. 4
5. Connective Tissue → Ch. 5
6. Adipose Tissue → Ch. 6
7. Nerve Tissue and the Nervous System → Ch. 9
8. The Circulatory System → Ch. 11
9. Blood → Ch. 12
10. Hemopoiesis → Ch. 13
11. The Immune System and Lymphoid Organs → Ch. 14
12. The Digestive Tract → Ch. 15
13. Organs Associated with the Digestive Tract → Ch. 16
14. The Respiratory System → Ch. 17
15. Skin → Ch. 18
16. Endocrine Glands → Ch. 20

Never insert Ch. 7 Cartilage, Ch. 8 Bone, Ch. 10 Muscle, Ch. 19 Urinary, Ch. 21 Male Reproductive, Ch. 22 Female Reproductive, or Ch. 23 Eye/Ear into the core edition.

Never merge Ch. 13 Hemopoiesis with Ch. 14 Immune System.

## Phase 1 — establish a trustworthy baseline

Before editing content:

1. Inspect the full repository tree and determine the true canonical source, build scripts, artifacts, historical editions, and production docs.
2. Reconcile README, Evidence Report, chapter files, Question Bank, build scripts, and production docs so that they describe the same edition.
3. Create or maintain a single authoritative release standard. Do not allow old reports to silently override it.
4. Inventory all current claims of “final”, “verified”, “PASS”, “independent”, “deterministic”, and “Junqueira aligned”. Downgrade unsupported claims before proceeding.
5. Produce a machine-readable content inventory: chapter → sections → learning objectives → major concepts → clinical correlations → recognition cues → assessment coverage.

## Phase 2 — scientific reconstruction, chapter by chapter

Review every sentence semantically. Prioritize high-risk material instead of relying on keyword searches.

At minimum, explicitly audit:

- fixation, dehydration, clearing, embedding, sectioning, staining, H&E and special stains;
- PAS and its actual chemical basis;
- Von Kossa and what it detects indirectly;
- light, fluorescence, confocal, TEM, SEM and related microscopy distinctions;
- cytoplasmic organelles, trafficking, lysosomes, peroxisomes, mitochondria, ER, Golgi, M6P and secretion;
- cytoskeleton, motor proteins, cilia and primary cilia;
- nuclear envelope, pores, chromatin, nucleolus, cell cycle, apoptosis, necrosis and autophagy;
- epithelial polarity, junctions, basement membrane, gland classification and specializations;
- all collagen types and ECM components;
- adipocyte biology and thermogenesis;
- myelin, Schwann cells, oligodendrocytes, synapses and nerve organization;
- vessels, capillary types, heart wall and microcirculation;
- blood-cell morphology and differential recognition;
- hemopoietic hierarchy, marrow niches and erythropoietin;
- lymphoid tissues, antigen presentation, germinal centres, lymph node/spleen/thymus organization;
- GI wall organization, regional differences and enteric nervous system;
- liver, pancreas and gallbladder microanatomy and zonation;
- respiratory conducting vs respiratory portions and blood-air barrier;
- skin layers, appendages, keratinization and specialized skin;
- pituitary, thyroid, parathyroid, adrenal, pancreatic endocrine tissue and endocrine organization.

### Known defects that must be fixed, not merely documented

1. Chapter 4 currently contains the unsafe statement that **claudin-14 mutations cause familial hypomagnesaemia**. Correct/remove/qualify it using authoritative knowledge. Do not substitute another fragile molecular-disease claim without verification.
2. Chapter 3 contains duplicated Function / Structure→Function / Classification / Cell Cycle/Cell Death / Compare & Distinguish material. Remove semantic duplication and keep the strongest teaching sequence.
3. Chapter 3 overstates the 30-nm fibre as a universal chromatin level. Rewrite with modern, appropriately qualified language.
4. Search the entire book for similar overconfident, outdated, or “textbook-sounding” claims that are not actually defensible.

For every correction, preserve conceptual clarity rather than replacing an error with an equally precise but unsupported molecular assertion.

## Phase 3 — rebuild the pedagogical architecture

Every chapter must form a true lesson, not a checklist of headings.

Use this canonical flow:

1. Opening Question
2. Why This Matters
3. Learning Objectives
4. Big Picture / Landscape
5. Core Concept / Principle
6. Build the Concept
7. Structure
8. Function
9. Structure → Function
10. Classification, where relevant
11. Compare & Distinguish
12. Recognition Logic
13. Clinical Correlation / Clinical Meaning
14. Common Misconceptions
15. High-Yield Knowledge
16. Integrated Summary
17. Mastery Check
18. Transition / Bridge
19. Rapid Review

An Advanced Concepts block may be inserted only where it adds real depth. Keep the published architecture documented consistently as either 19 core sections plus an optional Advanced Concepts block, or another single clearly defined model. Never again call a list of 20 items “19 sections” without explaining the optional element.

### Required conceptual quality

For major concepts, teach enough to answer:

What is it? Where is it? What is it made of? How organized? Why this organization? What does it do? How recognize it? What can it be confused with? What happens when it fails?

Do not force all nine questions onto every minor fact. Use judgment.

### Learning style

Use causal reasoning:

**appearance → structure → composition → mechanism → function → recognition → distinction → clinical meaning → exam reasoning**

Explain terminology at first use. Build from simple to complex. Use short examples and high-value comparisons. Avoid telegraphic prose and artificial “AI-sounding” repetition.

Do not inflate chapters merely to meet a word target. Expand only where the learner is genuinely missing a mechanism, distinction, example, recognition cue, or clinical connection.

## Phase 4 — strengthen visual learning

Histology is intrinsically visual. Add diagrams/figures only when they solve a learning problem.

Prioritize:

- processing/staining workflow;
- organelle/trafficking maps;
- nuclear/chromatin organization;
- epithelial junction and basement membrane diagrams;
- collagen/ECM organization;
- adipocyte comparison;
- myelin and neuron organization;
- vessel/capillary comparisons;
- blood-cell recognition sheet;
- hemopoiesis lineage map;
- lymph node, spleen and thymus architecture;
- GI wall and regional comparison;
- liver lobule/acinus/zonation;
- alveolar blood-air barrier;
- skin layers/appendages;
- endocrine cell/vascular arrangements.

Every visual must have accurate labels, useful legend text, a clear purpose, and provenance/licensing appropriate to publication. Decorative art is not a substitute for teaching.

## Phase 5 — build a serious Question Bank

Discard the assumption that 5 questions per chapter is enough.

Generate the final bank from the actual learning-objective/content matrix. Expand until all major objectives are adequately and repeatedly assessed.

Use a balanced mixture of:

- essential recall;
- concept understanding;
- morphology/slide recognition;
- comparison and discrimination;
- structure-function reasoning;
- clinical correlation;
- mechanism-based application;
- integrated cross-chapter reasoning;
- high-difficulty exam-style items.

Also create cumulative mixed sets so the learner must discriminate across systems rather than only within one chapter.

Every item must carry:

chapter → content unit → learning objective → cognitive level → difficulty → answer → explanation → decisive clue.

No item may test an untaught fact. No answer may depend on wording tricks. No distractor may be accidentally correct under a reasonable interpretation. No duplicate or near-duplicate questions should remain.

### Required Question Bank adversarial checks

- answer-key consistency;
- duplicate detection;
- ambiguity detection;
- one-best-answer validity;
- “all options plausible?” review;
- explanation consistency with textbook;
- no chapter/objective orphaning;
- no unsupported modern molecular trivia;
- no contradictions across questions.

## Phase 6 — cross-chapter coherence

Audit repeated concepts across the entire book.

Examples:

- collagen terminology must agree everywhere;
- basement membrane terminology must agree everywhere;
- junction molecules must agree everywhere;
- blood-cell dimensions and morphology descriptions must not conflict;
- endocrine cell descriptions must use one coherent terminology system;
- liver zonation language must be consistent;
- cilia/microvilli/stereocilia distinctions must never drift.

Do not repeat a paragraph simply because the concept appears in several organs. When repetition is necessary, make each recurrence serve a new function or context.

## Phase 7 — independent/adversarial QA

After the rebuild, assume the book still contains errors.

Run a dedicated audit that is not allowed to trust previous PASS labels.

At minimum:

1. scope test;
2. chapter-map test;
3. out-of-scope leakage test;
4. duplicate-content test;
5. contradiction test;
6. terminology consistency test;
7. known-defect regression test;
8. learning-objective coverage test;
9. Question Bank traceability test;
10. answer validity test;
11. source-to-derivative consistency test;
12. rendered PDF representative-page inspection from every chapter;
13. DOCX/EPUB structural inspection;
14. word-count reconciliation;
15. student-facing residue scan;
16. evidence-report claim verification.

A “PASS” is forbidden unless the corresponding evidence is present.

## Phase 8 — final release evidence

Replace the current evidence report with a truthful final report that includes:

- exact branch and commit;
- canonical source path;
- exact 16-chapter mapping;
- final chapter word counts from one reproducible method;
- final Question Bank count and distribution;
- learning-objective coverage statistics;
- duplicate/contradiction scan results;
- scientific remediation list and status;
- visual asset inventory and provenance status;
- deterministic build results;
- cross-format consistency results;
- representative page inspection results;
- independent/adversarial QA results;
- explicit remaining limitations, if any.

Never write “all gates pass” while the report itself lists substantive unresolved blockers.

## Phase 9 — artifact rebuild

Once content is stable:

1. rebuild canonical combined source;
2. rebuild DOCX, PDF and EPUB;
3. verify page structure and headings;
4. inspect representative pages from every chapter;
5. ensure no orphan headings, broken tables, blank pages, clipped content, or malformed mathematical symbols;
6. verify the Question Bank artifacts;
7. rerun all release tests after the last content change.

Do not leave artifacts stale relative to source.

## Stop conditions

Do not claim Final if any of these remain:

- known critical/high scientific defect;
- known chapter duplication that affects learning;
- unsupported clinical/molecular assertion;
- missing major learning objective;
- untaught assessed fact;
- answer-key conflict;
- unresolved source/report metric discrepancy;
- contradictory release documentation;
- build artifact not generated from current source;
- QA claim that cannot be reproduced.

## Deliverable definition

The finished branch should contain a book that is not merely “better than v2/v3”. It should be a coherent, defensible medical-education product that a serious PGME learner can study from, an instructor can teach from, and a reviewer can audit without discovering that the claimed finality depends on unchecked assumptions.

When the work is complete, update the repository documentation so that every public-facing project document tells the same truth about the same edition. Then mark the release **Final** only after the evidence supports it.
