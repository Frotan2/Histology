#!/usr/bin/env python3
"""Build PDF from canonical markdown source using ReportLab."""
import os
import re
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

NAVY = HexColor('#0A3D62')
DARK_GRAY = HexColor('#1A1A1A')
ACCENT = HexColor('#1F4E79')
LIGHT_NAVY = HexColor('#2C3E50')
LIGHT_GRAY = HexColor('#EAEDED')
MED_GRAY = HexColor('#7F8C8D')

PAGE_WIDTH, PAGE_HEIGHT = A4
LEFT_MARGIN = 1.0 * inch
RIGHT_MARGIN = 1.0 * inch
TOP_MARGIN = 1.0 * inch
BOTTOM_MARGIN = 1.0 * inch
GUTTER = 0.25 * inch

from reportlab.pdfbase.pdfmetrics import registerFontFamily


def try_register_dejavu():
    paths = [
        '/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf',
        '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf',
        '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf',
        '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
    ]
    ok = False
    for p in paths:
        if os.path.exists(p):
            try:
                pdfmetrics.registerFont(TTFont(os.path.basename(p).replace('.ttf', ''), p))
                ok = True
            except Exception:
                pass
    return ok


use_dejavu = try_register_dejavu()
BODY = 'DejaVuSerif' if use_dejavu else 'Times-Roman'
BODY_B = 'DejaVuSerif-Bold' if use_dejavu else 'Times-Bold'
BODY_I = 'DejaVuSerif' if use_dejavu else 'Times-Italic'
HEAD = 'DejaVuSans' if use_dejavu else 'Helvetica'
HEAD_B = 'DejaVuSans-Bold' if use_dejavu else 'Helvetica-Bold'

try:
    registerFontFamily(BODY, normal=BODY, bold=BODY_B, italic=BODY_I, boldItalic=BODY_B)
    registerFontFamily(HEAD, normal=HEAD, bold=HEAD_B)
except Exception:
    pass


class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved = []

    def showPage(self):
        self._saved.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        n = len(self._saved)
        for st in self._saved:
            self.__dict__.update(st)
            self.draw_pgnum(n)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_pgnum(self, total):
        if self._pageNumber == 1:
            return
        self.saveState()
        self.setFont(HEAD, 9)
        self.setFillColor(MED_GRAY)
        self.drawCentredString(PAGE_WIDTH / 2, 0.5 * inch, str(self._pageNumber))
        self.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 0.5 * inch, 'Essential Histology — Definitive Edition')
        self.restoreState()


def style(name, **kw):
    return ParagraphStyle(name=name, **kw)


S = {
    'body': style('body', fontName=BODY, fontSize=11, leading=14, textColor=DARK_GRAY, alignment=TA_JUSTIFY, spaceAfter=4),
    'h1': style('h1', fontName=HEAD, fontSize=20, leading=24, textColor=NAVY, alignment=TA_LEFT, spaceBefore=0, spaceAfter=10),
    'h2': style('h2', fontName=HEAD, fontSize=15, leading=20, textColor=ACCENT, alignment=TA_LEFT, spaceBefore=12, spaceAfter=6),
    'h3': style('h3', fontName=HEAD, fontSize=12, leading=16, textColor=LIGHT_NAVY, alignment=TA_LEFT, spaceBefore=8, spaceAfter=4),
    'h4': style('h4', fontName=HEAD, fontSize=11, leading=14, textColor=DARK_GRAY, alignment=TA_LEFT, spaceBefore=6, spaceAfter=3, fontStyle='italic'),
    'bullet': style('bullet', fontName=BODY, fontSize=11, leading=14, alignment=TA_LEFT, spaceBefore=1, spaceAfter=1, leftIndent=20, bulletIndent=8),
    'numbered': style('numbered', fontName=BODY, fontSize=11, leading=14, alignment=TA_LEFT, spaceBefore=1, spaceAfter=1, leftIndent=20, bulletIndent=8),
    'cap': style('cap', fontName=BODY, fontSize=10, leading=12, textColor=MED_GRAY, alignment=TA_CENTER, spaceAfter=8, fontStyle='italic'),
    'title_main': style('title_main', fontName=HEAD, fontSize=36, leading=44, textColor=NAVY, alignment=TA_CENTER, spaceBefore=120, spaceAfter=12),
    'title_sub': style('title_sub', fontName=HEAD, fontSize=18, leading=22, textColor=ACCENT, alignment=TA_CENTER, fontStyle='italic', spaceAfter=24),
    'title_tag': style('title_tag', fontName=HEAD, fontSize=12, leading=16, textColor=DARK_GRAY, alignment=TA_CENTER, fontStyle='italic'),
    'title_def': style('title_def', fontName=HEAD, fontSize=14, leading=18, textColor=NAVY, alignment=TA_CENTER, spaceBefore=24, spaceAfter=4),
    'title_meta': style('title_meta', fontName=HEAD, fontSize=10, leading=14, textColor=LIGHT_NAVY, alignment=TA_CENTER, fontStyle='italic'),
}


def to_html(text):
    text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<b><i>\1</i></b>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
    text = re.sub(r'`(.+?)`', r'<font face="Courier">\1</font>', text)
    return text


def render_table(story, rows):
    if not rows or len(rows) < 2:
        return
    header = rows[0]
    data = rows[1:]
    max_c = max(len(r) for r in rows)
    header = header + [''] * (max_c - len(header))
    data = [r + [''] * (max_c - len(r)) for r in data]
    h_cells = [Paragraph(to_html(c), style('th', fontName=HEAD, fontSize=9, leading=11, textColor=DARK_GRAY)) for c in header]
    d_cells = [[Paragraph(to_html(c), style('td', fontName=BODY, fontSize=8, leading=10, textColor=DARK_GRAY)) for c in r] for r in data]
    col_w = (PAGE_WIDTH - LEFT_MARGIN - RIGHT_MARGIN - GUTTER) / max_c
    t = Table([h_cells] + d_cells, colWidths=[col_w] * max_c, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), LIGHT_GRAY),
        ('FONTNAME', (0, 0), (-1, 0), HEAD),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('FONTWEIGHT', (0, 0), (-1, 0), 'BOLD'),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#BDC3C7')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(t)
    story.append(Spacer(1, 6))


def process_md(story, lines, start=0):
    i = start
    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if not s:
            i += 1
            continue
        if s == '---':
            i += 1
            continue
        if line.startswith('# ') and not line.startswith('## '):
            story.append(PageBreak())
            story.append(Paragraph(to_html(s[2:]), S['h1']))
            i += 1
            continue
        if line.startswith('## '):
            story.append(Paragraph(to_html(s[3:]), S['h2']))
            i += 1
            continue
        if line.startswith('### '):
            story.append(Paragraph(to_html(s[4:]), S['h3']))
            i += 1
            continue
        if line.startswith('#### '):
            story.append(Paragraph(to_html(s[5:]), S['h4']))
            i += 1
            continue
        m_img = re.match(r'^!\[[^\]]*\]\(([^)]+)\)\s*$', s)
        if m_img:
            ipath = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', m_img.group(1))
            ipath = os.path.normpath(ipath)
            if os.path.exists(ipath):
                try:
                    from reportlab.lib.utils import ImageReader
                    iw, ih = ImageReader(ipath).getSize()
                    max_w = PAGE_WIDTH - (LEFT_MARGIN + GUTTER) - RIGHT_MARGIN
                    max_h = 3.6 * inch
                    scale = min(max_w / iw, max_h / ih)
                    story.append(Spacer(1, 8))
                    story.append(Image(ipath, width=iw * scale, height=ih * scale))
                    story.append(Spacer(1, 4))
                except Exception:
                    pass
            i += 1
            continue
        if s.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                if re.match(r'^\|[\s\-\|:]+\|?$', lines[i].strip()):
                    i += 1
                    continue
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                rows.append(cells)
                i += 1
            render_table(story, rows)
            continue
        b = re.match(r'^\s*-\s+(.*)', line)
        if b:
            text = b.group(1)
            pstyle = style('b', fontName=BODY, fontSize=11, leading=14, alignment=TA_LEFT, leftIndent=20, bulletIndent=8)
            pstyle.bulletText = '•'
            story.append(Paragraph(to_html(text), pstyle))
            i += 1
            continue
        n = re.match(r'^(\d+)\.\s+(.*)', line)
        if n:
            story.append(Paragraph(f'<b>{n.group(1)}.</b> {to_html(n.group(2))}', S['numbered']))
            i += 1
            continue
        story.append(Paragraph(to_html(line), S['body']))
        i += 1


def build_pdf(src_md, out_pdf):
    doc = SimpleDocTemplate(
        out_pdf,
        pagesize=A4,
        leftMargin=LEFT_MARGIN + GUTTER,
        rightMargin=RIGHT_MARGIN,
        topMargin=TOP_MARGIN,
        bottomMargin=BOTTOM_MARGIN,
        title='Essential Histology - A Concept-Based Guide for PGME',
        author='AREMS-HY Academic Series',
        subject='Histology Textbook for Afghanistan 1405 Specialty Examination',
    )
    story = []
    # Title page
    story.append(Spacer(1, 60))
    story.append(Paragraph('Essential Histology', S['title_main']))
    story.append(Paragraph('A Concept-Based Guide for PGME', S['title_sub']))
    story.append(Paragraph('Understanding the structure. Seeing the pattern.', S['title_tag']))
    story.append(Paragraph('Distinguishing the alternatives. Retrieving the logic.', S['title_tag']))
    story.append(Paragraph('Definitive Edition', S['title_def']))
    story.append(Paragraph('AREMS-HY Academic Series', style('tp', fontName=HEAD, fontSize=12, leading=16, textColor=DARK_GRAY, alignment=TA_CENTER, fontStyle='italic')))
    story.append(Spacer(1, 36))
    story.append(Paragraph('Primary scientific foundation', S['title_meta']))
    story.append(Paragraph('Mescher AL. <b>Junqueira\'s Basic Histology: Text and Atlas.</b> 17th ed. McGraw Hill.', style('ml', fontName=BODY, fontSize=10, leading=14, textColor=DARK_GRAY, alignment=TA_LEFT)))
    story.append(Paragraph('Official 16-Chapter Syllabus', S['title_meta']))
    story.append(Paragraph('Aligned with Junqueira 17th Chapters 1, 2, 3, 4, 5, 6, 9, 11, 12, 13, 14, 15, 16, 17, 18, 20', style('ml', fontName=BODY, fontSize=10, leading=14, textColor=DARK_GRAY, alignment=TA_LEFT)))
    story.append(Paragraph('Built for the Afghanistan 1405 Specialty Examination', style('ml', fontName=BODY, fontSize=10, leading=14, textColor=DARK_GRAY, alignment=TA_LEFT)))
    story.append(PageBreak())

    with open(src_md) as f:
        md = f.read()
    lines = md.split('\n')
    start = 0
    for i, line in enumerate(lines):
        if line.startswith('# Chapter 1 —'):
            start = i
            break
    process_md(story, lines, start)
    doc.build(story, canvasmaker=NumberedCanvas)


if __name__ == '__main__':
    src = sys.argv[1] if len(sys.argv) > 1 else '../Essential_Histology_Combined.md'
    out = sys.argv[2] if len(sys.argv) > 2 else '../Essential_Histology_Final.pdf'
    build_pdf(src, out)
    print(f'Wrote {out}')
