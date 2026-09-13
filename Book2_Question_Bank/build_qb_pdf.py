#!/usr/bin/env python3
"""Build the Question Bank PDF from the canonical markdown source."""
import os, sys
ROOT = os.path.dirname(os.path.abspath(__file__))
BOOK1 = os.path.normpath(os.path.join(ROOT, '..', 'Book1_Essential_Histology_Final', 'build'))
sys.path.insert(0, BOOK1)
import build_pdf as B
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak

SRC = os.path.join(ROOT, 'Essential_Histology_Question_Bank.md')
OUT = os.path.join(ROOT, 'Essential_Histology_Question_Bank.pdf')

def main():
    doc = SimpleDocTemplate(
        OUT, pagesize=A4,
        leftMargin=B.LEFT_MARGIN + B.GUTTER, rightMargin=B.RIGHT_MARGIN,
        topMargin=B.TOP_MARGIN, bottomMargin=B.BOTTOM_MARGIN,
        title='Essential Histology - Question Bank',
        author='AREMS-HY Academic Series',
        subject='Question Bank for the Afghanistan 1405 Specialty Examination',
    )
    story = []
    story.append(Spacer(1, 70))
    story.append(Paragraph('Essential Histology', B.S['title_main']))
    story.append(Paragraph('Question Bank', B.S['title_sub']))
    story.append(Paragraph('400 single-best-answer questions with full rationales', B.S['title_tag']))
    story.append(Paragraph('Definitive Edition', B.S['title_def']))
    story.append(Spacer(1, 30))
    story.append(Paragraph('Companion to <b>Essential Histology — A Concept-Based Guide for PGME</b>', B.S['title_meta']))
    story.append(PageBreak())
    lines = open(SRC).read().split('\n')
    B.process_md(story, lines, 0)
    doc.build(story, canvasmaker=B.NumberedCanvas)
    print('  PDF: {:,} bytes'.format(os.path.getsize(OUT)))

if __name__ == '__main__':
    main()
