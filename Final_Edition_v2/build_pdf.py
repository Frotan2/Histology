#!/usr/bin/env python3
"""
Build the final PDF from canonical markdown source.
"""
import os
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.lib.colors import HexColor, white, black
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak,
    Table, TableStyle, NextPageTemplate, PageTemplate, Frame,
    KeepTogether, Flowable, BaseDocTemplate
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

# Paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(SCRIPT_DIR, 'source', 'Essential_Histology_Definitive_Final.md')
IMG_DIR = os.path.join(SCRIPT_DIR, 'source', 'images')
OUT = os.path.join(SCRIPT_DIR, 'Essential_Histology_v2.pdf')

# Colors
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
GUTTER = 0.25 * inch  # extra binding space

# Register fonts (use Helvetica/Times-Roman as base, with Times for serif)
from reportlab.pdfbase.pdfmetrics import registerFontFamily

# Try to register DejaVu fonts if available (better Unicode support)
def try_register_dejavu():
    font_paths = [
        '/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf',
        '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf',
        '/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf',
        '/usr/share/fonts/truetype/dejavu/DejaVuSerif-BoldItalic.ttf',
        '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
    ]
    fonts_ok = False
    for fp in font_paths:
        if os.path.exists(fp):
            try:
                fname = os.path.basename(fp).replace('.ttf', '')
                pdfmetrics.registerFont(TTFont(fname, fp))
                fonts_ok = True
            except Exception as e:
                print(f'Could not register {fp}: {e}')
    return fonts_ok

use_dejavu = try_register_dejavu()
if use_dejavu:
    BODY_FONT = 'DejaVuSerif'
    BODY_BOLD = 'DejaVuSerif-Bold'
    BODY_ITALIC = 'DejaVuSerif'  # Fallback to regular since italic not available
    BODY_BOLDITALIC = 'DejaVuSerif-Bold'  # Fallback
    HEAD_FONT = 'DejaVuSans'
    HEAD_BOLD = 'DejaVuSans-Bold'
    print('Using DejaVu fonts')
else:
    BODY_FONT = 'Times-Roman'
    BODY_BOLD = 'Times-Bold'
    BODY_ITALIC = 'Times-Italic'
    BODY_BOLDITALIC = 'Times-BoldItalic'
    HEAD_FONT = 'Helvetica'
    HEAD_BOLD = 'Helvetica-Bold'
    print('Using standard fonts')

# Register family
try:
    registerFontFamily(BODY_FONT, normal=BODY_FONT, bold=BODY_BOLD, italic=BODY_ITALIC, boldItalic=BODY_BOLDITALIC)
    registerFontFamily(HEAD_FONT, normal=HEAD_FONT, bold=HEAD_BOLD)
except Exception:
    pass


class NumberedCanvas(canvas.Canvas):
    """Canvas that adds page numbers and running header/footer."""
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        # Skip page numbers on title page
        page_num = self._pageNumber
        if page_num == 1:
            return
        # Footer: page number centered
        self.saveState()
        self.setFont(HEAD_FONT, 9)
        self.setFillColor(MED_GRAY)
        text = f'{page_num}'
        self.drawCentredString(PAGE_WIDTH / 2, 0.5 * inch, text)
        # Header: book title centered
        self.setFont(HEAD_FONT, 9)
        self.setFillColor(MED_GRAY)
        self.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 0.5 * inch, 'Essential Histology — Definitive Edition')
        self.restoreState()


def make_paragraph_style(name, font=BODY_FONT, size=11, leading=14, color=DARK_GRAY,
                         alignment=TA_JUSTIFY, space_before=0, space_after=4, bold=False, italic=False,
                         left_indent=0, bullet_indent=0, right_indent=0):
    return ParagraphStyle(
        name=name,
        fontName=font,
        fontSize=size,
        leading=leading,
        textColor=color,
        alignment=alignment,
        spaceBefore=space_before,
        spaceAfter=space_after,
        leftIndent=left_indent,
        rightIndent=right_indent,
        bulletIndent=bullet_indent,
        allowWidows=1,
        allowOrphans=1,
    )

# Define styles
styles = {
    'body': make_paragraph_style('body', size=11, leading=14),
    'body_left': make_paragraph_style('body_left', size=11, leading=14, alignment=TA_LEFT),
    'h1': make_paragraph_style('h1', font=HEAD_FONT, size=20, leading=24, color=NAVY, alignment=TA_LEFT, space_before=0, space_after=10, bold=True),
    'h2': make_paragraph_style('h2', font=HEAD_FONT, size=15, leading=20, color=ACCENT, alignment=TA_LEFT, space_before=12, space_after=6, bold=True),
    'h3': make_paragraph_style('h3', font=HEAD_FONT, size=12, leading=16, color=LIGHT_NAVY, alignment=TA_LEFT, space_before=8, space_after=4, bold=True),
    'h4': make_paragraph_style('h4', font=HEAD_FONT, size=11, leading=14, color=DARK_GRAY, alignment=TA_LEFT, space_before=6, space_after=3, bold=True, italic=True),
    'bullet': make_paragraph_style('bullet', size=11, leading=14, alignment=TA_LEFT, space_before=2, space_after=2, left_indent=20, bullet_indent=8),
    'numbered': make_paragraph_style('numbered', size=11, leading=14, alignment=TA_LEFT, space_before=2, space_after=2, left_indent=20, bullet_indent=8),
    'image_caption': make_paragraph_style('image_caption', size=10, leading=12, color=MED_GRAY, alignment=TA_CENTER, space_before=2, space_after=8, italic=True),
    'core_idea': make_paragraph_style('core_idea', size=11, leading=14, color=DARK_GRAY, alignment=TA_LEFT, space_before=4, space_after=4, left_indent=12, right_indent=12),
    'code': make_paragraph_style('code', font='Courier', size=9, leading=12, color=DARK_GRAY, alignment=TA_LEFT),
    'title_main': make_paragraph_style('title_main', font=HEAD_FONT, size=36, leading=44, color=NAVY, alignment=TA_CENTER, space_before=120, space_after=12, bold=True),
    'title_sub': make_paragraph_style('title_sub', font=HEAD_FONT, size=18, leading=22, color=ACCENT, alignment=TA_CENTER, space_before=4, space_after=24, italic=True),
    'title_tag': make_paragraph_style('title_tag', font=HEAD_FONT, size=12, leading=16, color=DARK_GRAY, alignment=TA_CENTER, space_before=2, space_after=2, italic=True),
    'title_def': make_paragraph_style('title_def', font=HEAD_FONT, size=14, leading=18, color=NAVY, alignment=TA_CENTER, space_before=24, space_after=4, bold=True),
    'title_pub': make_paragraph_style('title_pub', font=HEAD_FONT, size=12, leading=16, color=DARK_GRAY, alignment=TA_CENTER, space_before=0, space_after=24, italic=True),
    'title_meta': make_paragraph_style('title_meta', font=HEAD_FONT, size=10, leading=14, color=LIGHT_NAVY, alignment=TA_CENTER, space_before=24, space_after=4, italic=True),
    'contents': make_paragraph_style('contents', size=11, leading=18, alignment=TA_LEFT, space_before=2, space_after=4),
    'section_break': make_paragraph_style('section_break', size=10, leading=12, color=MED_GRAY, alignment=TA_CENTER, space_before=8, space_after=8, italic=True),
}

def parse_inline_to_html(text):
    """Convert markdown inline to ReportLab paragraph markup."""
    # Escape XML chars
    text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    # Bold-italic: ***text***
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<b><i>\1</i></b>', text)
    # Bold: **text**
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    # Italic: *text*
    text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
    # Code: `text`
    text = re.sub(r'`(.+?)`', r'<font face="Courier">\1</font>', text)
    # Restore escaped chars that we need
    return text


def build_title_page(story):
    """Build the title page."""
    story.append(Spacer(1, 60))
    story.append(Paragraph('Essential Histology', styles['title_main']))
    story.append(Paragraph('A Concept-Based Guide for PGME', styles['title_sub']))
    story.append(Spacer(1, 12))
    story.append(Paragraph('Understanding the structure. Seeing the pattern.', styles['title_tag']))
    story.append(Paragraph('Distinguishing the alternatives. Retrieving the logic.', styles['title_tag']))
    story.append(Spacer(1, 24))
    story.append(Paragraph('Definitive Edition', styles['title_def']))
    story.append(Paragraph('AREMS-HY Academic Series', styles['title_pub']))
    story.append(Spacer(1, 48))
    story.append(Paragraph('Primary scientific foundation', styles['title_meta']))
    story.append(Paragraph('Mescher AL. <b>Junqueira\'s Basic Histology: Text and Atlas.</b> 17th ed. McGraw Hill.', styles['body_left']))
    story.append(Spacer(1, 12))
    story.append(Paragraph('Official 16-Chapter Syllabus', styles['title_meta']))
    story.append(Paragraph('Aligned with Junqueira 17th Chapters 1, 2, 3, 4, 5, 6, 9, 11, 12, 13, 14, 15, 16, 17, 18, 20', styles['body_left']))
    story.append(Spacer(1, 12))
    story.append(Paragraph('Built for the Afghanistan 1405 Specialty Examination', styles['body_left']))
    story.append(PageBreak())


def render_table(story, rows):
    """Render markdown table rows as ReportLab Table."""
    if not rows or len(rows) < 2:
        return

    header = rows[0]
    data_rows = rows[1:]

    # Normalize column count
    max_cols = max(len(r) for r in rows)
    header = header + [''] * (max_cols - len(header))
    data_rows = [r + [''] * (max_cols - len(r)) for r in data_rows]

    # Convert to paragraphs
    header_cells = [Paragraph(parse_inline_to_html(c), make_paragraph_style('th', size=10, leading=12, color=DARK_GRAY, alignment=TA_LEFT, bold=True)) for c in header]
    data_cells = []
    for row in data_rows:
        cells = [Paragraph(parse_inline_to_html(c), make_paragraph_style('td', size=9, leading=11, color=DARK_GRAY, alignment=TA_LEFT)) for c in row]
        data_cells.append(cells)

    col_widths = [PAGE_WIDTH - LEFT_MARGIN - RIGHT_MARGIN - GUTTER] * 1
    if max_cols > 1:
        col_width = (PAGE_WIDTH - LEFT_MARGIN - RIGHT_MARGIN - GUTTER) / max_cols
        col_widths = [col_width] * max_cols

    t = Table([header_cells] + data_cells, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), LIGHT_GRAY),
        ('TEXTCOLOR', (0, 0), (-1, 0), DARK_GRAY),
        ('FONTNAME', (0, 0), (-1, 0), HEAD_FONT),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('FONTWEIGHT', (0, 0), (-1, 0), 'BOLD'),
        ('FONTNAME', (0, 1), (-1, -1), BODY_FONT),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#BDC3C7')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))

    story.append(t)
    story.append(Spacer(1, 8))


def process_markdown(story, lines, start_idx=0):
    """Process markdown lines into ReportLab flowables."""
    i = start_idx
    in_contents = False
    while i < len(lines):
        line = lines[i]
        line_stripped = line.strip()

        # Track when we're in Contents section
        if line_stripped.startswith('## Contents'):
            in_contents = True
            i += 1
            continue
        if in_contents and line_stripped.startswith('## ') and not line_stripped.startswith('## Contents'):
            in_contents = False

        # Skip empty
        if not line.strip():
            i += 1
            continue

        # Page break
        if line.strip() == '\\pagebreak':
            story.append(PageBreak())
            i += 1
            continue

        # Horizontal rule
        if line.strip() == '---':
            story.append(Spacer(1, 4))
            i += 1
            continue

        # Heading 1 (chapter)
        if line.startswith('# '):
            text = line[2:].strip()
            # Don't insert page break here - the \pagebreak before the heading handles it
            text_html = parse_inline_to_html(text)
            story.append(Paragraph(text_html, styles['h1']))
            i += 1
            continue

        # Heading 2
        if line.startswith('## '):
            text = line[3:].strip()
            text_html = parse_inline_to_html(text)
            story.append(Paragraph(text_html, styles['h2']))
            i += 1
            continue

        # Contents lines - special handling
        if in_contents and (line_stripped.startswith('1.') or line_stripped.startswith('2.') or
                            line_stripped.startswith('3.') or line_stripped.startswith('4.') or
                            line_stripped.startswith('5.') or line_stripped.startswith('6.') or
                            line_stripped.startswith('7.') or line_stripped.startswith('8.') or
                            line_stripped.startswith('9.') or re.match(r'^\d+\.', line_stripped)):
            text_html = parse_inline_to_html(line)
            contents_style = make_paragraph_style('cont', size=11, leading=18, alignment=TA_LEFT, space_before=2, space_after=4, left_indent=0)
            story.append(Paragraph(text_html, contents_style))
            i += 1
            continue

        # Heading 3
        if line.startswith('### '):
            text = line[4:].strip()
            text_html = parse_inline_to_html(text)
            story.append(Paragraph(text_html, styles['h3']))
            i += 1
            continue

        # Heading 4
        if line.startswith('#### '):
            text = line[5:].strip()
            text_html = parse_inline_to_html(text)
            story.append(Paragraph(text_html, styles['h4']))
            i += 1
            continue

        # Image
        img_match = re.match(r'!\[(.*?)\]\((.*?)\)', line)
        if img_match:
            alt = img_match.group(1)
            src = img_match.group(2)
            image_path = os.path.join(os.path.dirname(SRC), src) if not os.path.isabs(src) else src
            if not os.path.exists(image_path):
                fname = os.path.basename(src)
                image_path = os.path.join(IMG_DIR, fname)
            if os.path.exists(image_path):
                try:
                    img = Image(image_path)
                    # Scale to fit page width
                    max_w = PAGE_WIDTH - LEFT_MARGIN - RIGHT_MARGIN - GUTTER
                    if img.imageWidth > max_w:
                        scale = max_w / img.imageWidth
                        img.drawWidth = max_w
                        img.drawHeight = img.imageHeight * scale
                    # Center
                    img.hAlign = 'CENTER'
                    story.append(Spacer(1, 6))
                    story.append(img)
                    story.append(Paragraph(alt, styles['image_caption']))
                except Exception as e:
                    print(f'Image error: {e}')
                    story.append(Paragraph(f'[Image: {alt}]', styles['body_left']))
            else:
                story.append(Paragraph(f'[Image: {alt}]', styles['body_left']))
            i += 1
            continue

        # Table
        if line.strip().startswith('|'):
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

        # Bullet list
        bullet_match = re.match(r'^\s*-\s+(.*)', line)
        if bullet_match:
            text = bullet_match.group(1)
            text_html = parse_inline_to_html(text)
            bullet_style = make_paragraph_style('b', size=11, leading=14, alignment=TA_LEFT, space_before=2, space_after=2, left_indent=20, bullet_indent=8)
            bullet_style.bulletText = '•'
            story.append(Paragraph(text_html, bullet_style))
            i += 1
            continue

        # Numbered list
        num_match = re.match(r'^(\d+)\.\s+(.*)', line)
        if num_match:
            num = num_match.group(1)
            text = num_match.group(2)
            text_html = parse_inline_to_html(f'<b>{num}.</b> {text}')
            story.append(Paragraph(text_html, styles['numbered']))
            i += 1
            continue

        # Regular paragraph
        text_html = parse_inline_to_html(line)
        # Detect "Core Idea:" special blocks for nicer formatting
        if text_html.startswith('<b>Core Idea:</b>') or text_html.startswith('<b>Carry this forward'):
            story.append(Paragraph(text_html, styles['core_idea']))
        else:
            story.append(Paragraph(text_html, styles['body']))
        i += 1


def build_pdf():
    # Create document
    doc = SimpleDocTemplate(
        OUT,
        pagesize=A4,
        leftMargin=LEFT_MARGIN + GUTTER,
        rightMargin=RIGHT_MARGIN,
        topMargin=TOP_MARGIN,
        bottomMargin=BOTTOM_MARGIN,
        title='Essential Histology — A Concept-Based Guide for PGME',
        author='AREMS-HY Academic Series',
        subject='Histology Textbook for Afghanistan 1405 Specialty Examination',
    )

    story = []

    # Read source
    with open(SRC) as f:
        md_text = f.read()

    lines = md_text.split('\n')

    # Find the start of contents
    start = 0
    for i, line in enumerate(lines):
        if line.startswith('## Contents'):
            start = i
            break

    # Build title page first
    build_title_page(story)

    # Process from contents
    process_markdown(story, lines, start)

    # Build PDF
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f'Wrote {OUT}: {os.path.getsize(OUT)} bytes')


if __name__ == '__main__':
    build_pdf()
