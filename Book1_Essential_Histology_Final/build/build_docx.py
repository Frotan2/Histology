#!/usr/bin/env python3
"""Build DOCX from canonical markdown source."""
import os
import re
import sys
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK

NAVY = RGBColor(0x0A, 0x3D, 0x62)
DARK_GRAY = RGBColor(0x1A, 0x1A, 0x1A)
ACCENT = RGBColor(0x1F, 0x4E, 0x79)
LIGHT_NAVY = RGBColor(0x2C, 0x3E, 0x50)
MED_GRAY = RGBColor(0x7F, 0x8C, 0x8D)
HEAD_FONT = 'Calibri'
BODY_FONT = 'Georgia'


def add_run(p, text, bold=False, italic=False, size=11, color=DARK_GRAY, font=BODY_FONT):
    run = p.add_run(text)
    run.font.name = font
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    run.font.color.rgb = color
    return run


def parse_inline(text, p, base_size=11, base_color=DARK_GRAY, base_font=BODY_FONT):
    pattern = re.compile(r'(\*\*\*(.+?)\*\*\*|\*\*(.+?)\*\*|\*(.+?)\*|`(.+?)`)')
    pos = 0
    for m in pattern.finditer(text):
        if m.start() > pos:
            add_run(p, text[pos:m.start()], size=base_size, color=base_color, font=base_font)
        if m.group(3):
            add_run(p, m.group(3), bold=True, size=base_size, color=base_color, font=base_font)
        elif m.group(4):
            add_run(p, m.group(4), italic=True, size=base_size, color=base_color, font=base_font)
        elif m.group(2):
            add_run(p, m.group(2), bold=True, italic=True, size=base_size, color=base_color, font=base_font)
        elif m.group(5):
            add_run(p, m.group(5), size=max(base_size - 1, 9), color=base_color, font='Consolas')
        pos = m.end()
    if pos < len(text):
        add_run(p, text[pos:], size=base_size, color=base_color, font=base_font)


def add_paragraph(doc, text, *, size=11, bold=False, italic=False, color=DARK_GRAY,
                  alignment=WD_ALIGN_PARAGRAPH.JUSTIFY, font=BODY_FONT,
                  space_before=2, space_after=4):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(space_after)
    pf.line_spacing = 1.15
    p.alignment = alignment
    parse_inline(text, p, base_size=size, base_color=color, base_font=font)
    if bold or italic:
        for r in p.runs:
            if bold: r.bold = True
            if italic: r.italic = True
    return p


def render_table(doc, rows):
    if not rows or len(rows) < 2:
        return
    header = rows[0]
    data = rows[1:]
    max_cols = max(len(r) for r in rows)
    header = header + [''] * (max_cols - len(header))
    data = [r + [''] * (max_cols - len(r)) for r in data]
    table = doc.add_table(rows=1 + len(data), cols=max_cols)
    table.autofit = True
    for j, cell_text in enumerate(header):
        cell = table.rows[0].cells[j]
        cell.text = ''
        p = cell.paragraphs[0]
        parse_inline(cell_text, p, base_size=10, base_color=DARK_GRAY)
        for r in p.runs:
            r.bold = True
    for ri, row in enumerate(data):
        for j, cell_text in enumerate(row):
            cell = table.rows[ri + 1].cells[j]
            cell.text = ''
            p = cell.paragraphs[0]
            parse_inline(cell_text, p, base_size=10, base_color=DARK_GRAY)


def process_md(doc, lines, start=0):
    i = start
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if stripped == '---':
            i += 1
            continue

        if line.startswith('# ') and not line.startswith('## '):
            text = stripped[2:]
            p = doc.add_paragraph()
            r = add_run(p, text, bold=True, size=22, color=NAVY, font=HEAD_FONT)
            pf = p.paragraph_format
            pf.space_before = Pt(18)
            pf.space_after = Pt(12)
            pf.keep_with_next = True
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            i += 1
            continue

        if line.startswith('## '):
            text = stripped[3:]
            p = doc.add_paragraph()
            add_run(p, text, bold=True, size=14, color=ACCENT, font=HEAD_FONT)
            pf = p.paragraph_format
            pf.space_before = Pt(10)
            pf.space_after = Pt(6)
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            i += 1
            continue

        if line.startswith('### '):
            text = stripped[4:]
            p = doc.add_paragraph()
            add_run(p, text, bold=True, size=12, color=LIGHT_NAVY, font=HEAD_FONT)
            pf = p.paragraph_format
            pf.space_before = Pt(8)
            pf.space_after = Pt(4)
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            i += 1
            continue

        if line.startswith('#### '):
            text = stripped[5:]
            p = doc.add_paragraph()
            add_run(p, text, bold=True, italic=True, size=11, color=DARK_GRAY, font=HEAD_FONT)
            pf = p.paragraph_format
            pf.space_before = Pt(6)
            pf.space_after = Pt(3)
            i += 1
            continue

        m_img = re.match(r'^!\[[^\]]*\]\(([^)]+)\)\s*$', line.strip())
        if m_img:
            ipath = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', m_img.group(1)))
            if os.path.exists(ipath):
                try:
                    doc.add_picture(ipath, width=Inches(6.0))
                    doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
                except Exception:
                    pass
            i += 1
            continue
        if line.strip().startswith('|'):
            rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                if re.match(r'^\|[\s\-\|:]+\|?$', lines[i].strip()):
                    i += 1
                    continue
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                rows.append(cells)
                i += 1
            render_table(doc, rows)
            continue

        bullet = re.match(r'^\s*-\s+(.*)', line)
        if bullet:
            text = bullet.group(1)
            p = doc.add_paragraph(style='List Bullet')
            pf = p.paragraph_format
            pf.space_before = Pt(1)
            pf.space_after = Pt(1)
            parse_inline(text, p, base_size=11)
            i += 1
            continue

        num = re.match(r'^(\d+)\.\s+(.*)', line)
        if num:
            text = num.group(2)
            p = doc.add_paragraph()
            pf = p.paragraph_format
            pf.space_before = Pt(1)
            pf.space_after = Pt(1)
            add_run(p, f"{num.group(1)}. ", bold=True, size=11)
            parse_inline(text, p, base_size=11)
            i += 1
            continue

        add_paragraph(doc, line, size=11, color=DARK_GRAY)
        i += 1


def build_docx(src_md, out_docx):
    doc = Document()
    style = doc.styles['Normal']
    style.font.name = BODY_FONT
    style.font.size = Pt(11)
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Header / footer
    for section in doc.sections:
        header = section.header
        h_p = header.paragraphs[0]
        h_p.text = ''
        h_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        add_run(h_p, 'Essential Histology — Definitive Edition', italic=True, size=9, color=LIGHT_NAVY)

        footer = section.footer
        f_p = footer.paragraphs[0]
        f_p.text = ''
        f_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        add_run(f_p, 'Page ', size=9, color=LIGHT_NAVY)
        # Page number field
        run = f_p.add_run()
        fldChar1 = run._r.makeelement('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}fldChar', {'{http://schemas.openxmlformats.org/wordprocessingml/2006/main}fldCharType': 'begin'})
        run._r.append(fldChar1)
        instrText = run._r.makeelement('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}instrText', {'{http://www.w3.org/XML/1998/namespace}space': 'preserve'})
        instrText.text = 'PAGE'
        run._r.append(instrText)
        fldChar2 = run._r.makeelement('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}fldChar', {'{http://schemas.openxmlformats.org/wordprocessingml/2006/main}fldCharType': 'end'})
        run._r.append(fldChar2)
        for r in f_p.runs:
            r.font.size = Pt(9)
            r.font.color.rgb = LIGHT_NAVY

    # Title page
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pf = p.paragraph_format
    pf.space_before = Pt(120)
    pf.space_after = Pt(12)
    add_run(p, 'Essential Histology', bold=True, size=36, color=NAVY, font=HEAD_FONT)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    add_run(p, 'A Concept-Based Guide for PGME', italic=True, size=18, color=ACCENT, font=HEAD_FONT)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pf = p.paragraph_format
    pf.space_before = Pt(12)
    pf.space_after = Pt(12)
    add_run(p, 'Understanding the structure. Seeing the pattern.', italic=True, size=12, color=DARK_GRAY)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    add_run(p, 'Distinguishing the alternatives. Retrieving the logic.', italic=True, size=12, color=DARK_GRAY)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pf = p.paragraph_format
    pf.space_before = Pt(24)
    pf.space_after = Pt(4)
    add_run(p, 'Definitive Edition', bold=True, size=14, color=NAVY, font=HEAD_FONT)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    add_run(p, 'AREMS-HY Academic Series', italic=True, size=12, color=DARK_GRAY)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pf = p.paragraph_format
    pf.space_before = Pt(48)
    pf.space_after = Pt(4)
    add_run(p, 'Primary scientific foundation', italic=True, size=10, color=LIGHT_NAVY)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    add_run(p, 'Mescher AL. Junqueira\'s Basic Histology: Text and Atlas. 17th ed. McGraw Hill.', size=10, color=DARK_GRAY)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pf = p.paragraph_format
    pf.space_before = Pt(12)
    pf.space_after = Pt(4)
    add_run(p, 'Official 16-Chapter Syllabus', italic=True, size=10, color=LIGHT_NAVY)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    add_run(p, 'Aligned with Junqueira 17th Chapters 1, 2, 3, 4, 5, 6, 9, 11, 12, 13, 14, 15, 16, 17, 18, 20', size=10, color=DARK_GRAY)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pf = p.paragraph_format
    pf.space_before = Pt(12)
    pf.space_after = Pt(24)
    add_run(p, 'Built for the Afghanistan 1405 Specialty Examination', size=10, color=DARK_GRAY)

    # Page break before front matter content
    p = doc.add_paragraph()
    p.add_run().add_break(WD_BREAK.PAGE)

    with open(src_md) as f:
        md = f.read()
    lines = md.split('\n')

    # Skip front matter (YAML + title) - start at first # Chapter
    start = 0
    for i, line in enumerate(lines):
        if line.startswith('# Chapter 1 —'):
            start = i
            break
    process_md(doc, lines, start)
    doc.save(out_docx)


if __name__ == '__main__':
    src = sys.argv[1] if len(sys.argv) > 1 else '../Essential_Histology_Combined.md'
    out = sys.argv[2] if len(sys.argv) > 2 else '../Essential_Histology_Final.docx'
    build_docx(src, out)
    print(f'Wrote {out}')
