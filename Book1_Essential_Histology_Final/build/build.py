#!/usr/bin/env python3
"""
Build the canonical Book 1 source, then generate PDF, DOCX, EPUB.

Single source of truth: Essential_Histology_Combined.md
"""
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC_MD = ROOT / 'Essential_Histology_Combined.md'
OUT_PDF = ROOT / 'Essential_Histology_Final.pdf'
OUT_DOCX = ROOT / 'Essential_Histology_Final.docx'
OUT_EPUB = ROOT / 'Essential_Histology_Final.epub'

# 1. Build combined source if not present or stale
def ensure_combined():
    combined = ROOT / 'Essential_Histology_Combined.md'
    if not combined.exists():
        main = ROOT / 'Essential_Histology_Textbook.md'
        chapters = sorted((ROOT / 'chapters').glob('Chapter*.md'))
        content = main.read_text() + '\n\n'
        for ch in chapters:
            content += ch.read_text() + '\n\n'
        combined.write_text(content)
    return combined


def main():
    src = ensure_combined()
    print(f'Source: {src} ({src.stat().st_size:,} bytes, {len(src.read_text().split()):,} words)')

    # 2. Build DOCX
    print('\n[1] Building DOCX...')
    sys.path.insert(0, str(ROOT / 'build'))
    import build_docx
    build_docx.build_docx(str(src), str(OUT_DOCX))
    print(f'  DOCX: {OUT_DOCX.stat().st_size:,} bytes')

    # 3. Build PDF
    print('\n[2] Building PDF...')
    import build_pdf
    build_pdf.build_pdf(str(src), str(OUT_PDF))
    print(f'  PDF: {OUT_PDF.stat().st_size:,} bytes')

    # 4. Build EPUB
    print('\n[3] Building EPUB...')
    import build_epub
    build_epub.build_epub(str(src), str(OUT_EPUB))
    print(f'  EPUB: {OUT_EPUB.stat().st_size:,} bytes')

    print('\nAll artifacts built from', src)


if __name__ == '__main__':
    main()
