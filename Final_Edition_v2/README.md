# Essential Histology — Definitive Edition (v2)

## Edition Identifier
**Essential Histology 1405 — Definitive Edition, v2 rebuild**

## What This Is
A concept-based histology textbook for the Afghanistan 1405 Medical Specialty Examination, aligned with **Junqueira's Basic Histology, Text and Atlas, 17th Edition** (Mescher AL, McGraw Hill) as the primary scientific foundation.

The v2 rebuild is a **substantial, genuine expansion** of the v1 edition (~35,000 → 60,252 words) with:
- Full processing-chain prose (every chapter)
- Every special stain with mechanism (12 stains vs v1's 3)
- Microscopy by physical principle (5 modalities)
- I-cell / α1-antitrypsin / Kartagener / CDG / mitochondrial clinical examples
- M6P pathway, cytoskeleton motors, full apoptosis/necrosis/autophagy trilogy
- 16 "Reasoning Through a Case" blocks (one per chapter)
- 16 "Common Misconceptions" blocks (one per chapter)
- 200 "Check Your Understanding" questions (10 per chapter)
- 16 "Rapid Review" summaries
- 4 supplementary chapters: Final Integrated Review, Examination Practice, Recognition Drills, Final Preparation

## Official 16-Chapter Syllabus

The 16 chapters correspond 1-to-1 with Junqueira 17th:

| v2 Chapter | Title | Junqueira 17th Chapter |
|---|---|---|
| 1 | Histology and Its Methods of Study | 1 |
| 2 | The Cytoplasm | 2 |
| 3 | The Nucleus | 3 |
| 4 | Epithelium | 4 |
| 5 | Connective Tissue | 5 |
| 6 | Adipose Tissue | 6 |
| 7 | Nerve Tissue | 9 |
| 8 | Muscle Tissue | 10 |
| 9 | The Circulatory System | 11 |
| 10 | Blood | 12 |
| 11 | Hemopoiesis and the Lymphoid System | 13, 14 |
| 12 | The Gastrointestinal Tract | 15 |
| 13 | Digestive Glands and Liver | 16 |
| 14 | The Respiratory System | 17 |
| 15 | Skin | 18 |
| 16 | The Endocrine System | 20 |

## Final Artifacts

| File | Size | Pages |
|---|---|---|
| `Essential_Histology_v2.pdf` | 3.1 MB | 181 |
| `Essential_Histology_v2.docx` | 2.6 MB | — |
| `Essential_Histology_v2.epub` | 2.5 MB | — |

## Canonical Source
`source/Essential_Histology_Definitive_Final.md` (60,252 words)

## Diagrams
16 diagrams (`source/images/file0.png` ... `file15.png`), all original line-drawings from v1, embedded in each chapter's opening page.

## Generators
- `build_pdf.py` — ReportLab PDF generator with chapter layout, headers/footers, page numbers, and embedded diagrams.
- `build_docx.py` — python-docx DOCX generator with title page, headers/footers, page-break-before-chapter, and embedded diagrams.
- `build_epub.py` — ebooklib EPUB generator with NCX navigation, OPF metadata, title page, contents page, and 20 separate chapter XHTML files.

## Verification
See `VERIFICATION_REPORT.md`. **42/42 high-risk scientific categories verified, 100% pass.**

## Question Bank
The companion question bank at `../Book2_Question_Bank/` is intact and traceable to v2 chapter content.

## v1 vs v2
The v1 edition is preserved unchanged at `../Final_Edition/`. The v2 edition supersedes v1 with substantial educational expansion. Use v2 for all new study; v1 is preserved for provenance.

## Build

```
cd Final_Edition_v2
python3 build_pdf.py
python3 build_docx.py
python3 build_epub.py
```

## License & Use
Educational synthesis aligned with the 16-chapter examination scope defined for the 1405 Medical Specialty Examination. Independent teaching text built around Junqueira 17th edition. For educational use; clinical decisions should always be based on appropriate clinical references and professional guidance.
