#!/usr/bin/env python3
"""
Build the final EPUB from canonical markdown source.
"""
import os
import re
import zipfile
import shutil
from pathlib import Path
from ebooklib import epub
from PIL import Image

# Paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(SCRIPT_DIR, 'source', 'Essential_Histology_Canonical_Source.md')
IMG_DIR = os.path.join(SCRIPT_DIR, 'source', 'images')
OUT = os.path.join(SCRIPT_DIR, 'Essential_Histology_Definitive_Edition.epub')


def parse_inline_xhtml(text):
    """Convert markdown inline to XHTML."""
    # Escape HTML chars (but not for our intentional tags)
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;').replace('>', '&gt;')

    # Bold-italic
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<b><i>\1</i></b>', text)
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    # Italic
    text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
    # Code
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    return text


def render_table_xhtml(rows):
    """Render markdown table rows as XHTML."""
    if not rows or len(rows) < 2:
        return ''

    header = rows[0]
    data_rows = rows[1:]

    max_cols = max(len(r) for r in rows)
    header = header + [''] * (max_cols - len(header))
    data_rows = [r + [''] * (max_cols - len(r)) for r in data_rows]

    xhtml = '<table>\n<thead>\n<tr>\n'
    for cell in header:
        xhtml += f'<th>{parse_inline_xhtml(cell)}</th>\n'
    xhtml += '</tr>\n</thead>\n<tbody>\n'
    for row in data_rows:
        xhtml += '<tr>\n'
        for cell in row:
            xhtml += f'<td>{parse_inline_xhtml(cell)}</td>\n'
        xhtml += '</tr>\n'
    xhtml += '</tbody>\n</table>'
    return xhtml


def md_to_xhtml(md_text):
    """Convert markdown to XHTML."""
    lines = md_text.split('\n')
    output = []
    i = 0
    in_contents = False
    skip_to_contents = True

    # Skip the first "# Essential Histology" and front matter until "## Contents"
    found_contents = False
    for j, line in enumerate(lines):
        if line.strip().startswith('## Contents'):
            start_idx = j
            found_contents = True
            break

    if not found_contents:
        start_idx = 0

    i = start_idx
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Track contents section
        if stripped.startswith('## Contents'):
            in_contents = True
            i += 1
            continue
        if in_contents and stripped.startswith('## ') and not stripped.startswith('## Contents'):
            in_contents = False
            output.append(f'<h2>{parse_inline_xhtml(stripped[3:])}</h2>')
            i += 1
            continue

        if not stripped:
            output.append('')
            i += 1
            continue

        # Page break - just add a section break marker
        if stripped == '\\pagebreak':
            i += 1
            continue

        # Horizontal rule
        if stripped == '---':
            output.append('<hr/>')
            i += 1
            continue

        # Heading 1
        if stripped.startswith('# '):
            text = stripped[2:]
            output.append(f'<h1>{parse_inline_xhtml(text)}</h1>')
            i += 1
            continue

        # Heading 2
        if stripped.startswith('## '):
            text = stripped[3:]
            output.append(f'<h2>{parse_inline_xhtml(text)}</h2>')
            i += 1
            continue

        # Heading 3
        if stripped.startswith('### '):
            text = stripped[4:]
            output.append(f'<h3>{parse_inline_xhtml(text)}</h3>')
            i += 1
            continue

        # Heading 4
        if stripped.startswith('#### '):
            text = stripped[5:]
            output.append(f'<h4>{parse_inline_xhtml(text)}</h4>')
            i += 1
            continue

        # Image
        img_match = re.match(r'!\[(.*?)\]\((.*?)\)', stripped)
        if img_match:
            alt = img_match.group(1)
            src = img_match.group(2)
            fname = os.path.basename(src)
            output.append(f'<div class="figure"><img src="../images/{fname}" alt="{alt}"/><div class="caption">{alt}</div></div>')
            i += 1
            continue

        # Table
        if stripped.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                if re.match(r'^\|[\s\-\|:]+\|?$', lines[i].strip()):
                    i += 1
                    continue
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                rows.append(cells)
                i += 1
            output.append(render_table_xhtml(rows))
            output.append('')
            continue

        # Bullet list
        bullet_match = re.match(r'^\s*-\s+(.*)', line)
        if bullet_match:
            text = bullet_match.group(1)
            output.append(f'<ul><li>{parse_inline_xhtml(text)}</li></ul>')
            i += 1
            continue

        # Numbered list
        num_match = re.match(r'^(\d+)\.\s+(.*)', line)
        if num_match:
            num = num_match.group(1)
            text = num_match.group(2)
            # If in_contents, render as plain paragraph (with bold number) for cleaner TOC
            if in_contents:
                output.append(f'<p class="toc-item"><b>{num}.</b> {parse_inline_xhtml(text)}</p>')
            else:
                output.append(f'<p><b>{num}.</b> {parse_inline_xhtml(text)}</p>')
            i += 1
            continue

        # Regular paragraph
        output.append(f'<p>{parse_inline_xhtml(line)}</p>')
        i += 1

    return '\n'.join(output)


def build_epub():
    # Create EPUB book
    book = epub.EpubBook()

    # Metadata
    book.set_identifier('urn:uuid:essential-histology-1405-definitive')
    book.set_title('Essential Histology — A Concept-Based Guide for PGME')
    book.set_language('en')
    book.add_author('AREMS-HY Academic Series')
    book.add_metadata('DC', 'description',
                      'A concept-based histology textbook for the Afghanistan 1405 Medical Specialty Examination, aligned with Junqueira 17th edition, official 16-chapter syllabus.')
    book.add_metadata('DC', 'subject', 'Histology, Medical Textbook, PGME, 1405 Examination')
    book.add_metadata('DC', 'publisher', 'AREMS-HY Academic Series')

    # CSS
    css = '''
@namespace epub "http://www.idpf.org/2007/ops";

body {
  font-family: Georgia, serif;
  line-height: 1.5;
  color: #1a1a1a;
  margin: 0 1em;
}

h1 {
  font-family: 'Helvetica', sans-serif;
  font-size: 1.8em;
  font-weight: bold;
  color: #0A3D62;
  margin: 2em 0 1em 0;
  page-break-before: always;
  page-break-after: avoid;
}

h2 {
  font-family: 'Helvetica', sans-serif;
  font-size: 1.4em;
  font-weight: bold;
  color: #1F4E79;
  margin: 1.5em 0 0.6em 0;
  page-break-after: avoid;
}

h3 {
  font-family: 'Helvetica', sans-serif;
  font-size: 1.2em;
  font-weight: bold;
  color: #2C3E50;
  margin: 1.2em 0 0.5em 0;
  page-break-after: avoid;
}

h4 {
  font-family: 'Helvetica', sans-serif;
  font-size: 1.05em;
  font-weight: bold;
  font-style: italic;
  margin: 1em 0 0.4em 0;
}

p {
  margin: 0.8em 0;
  text-align: justify;
}

.toc-item {
  margin: 0.3em 0;
}

ul {
  margin: 0.5em 0;
  padding-left: 1.5em;
}

ul li {
  margin: 0.2em 0;
}

table {
  border-collapse: collapse;
  width: 100%;
  margin: 1em 0;
}

th {
  background-color: #EAEDED;
  font-weight: bold;
  padding: 0.4em 0.6em;
  border: 1px solid #BDC3C7;
  text-align: left;
}

td {
  padding: 0.3em 0.6em;
  border: 1px solid #BDC3C7;
  vertical-align: top;
  font-size: 0.95em;
}

.figure {
  margin: 1.5em 0;
  text-align: center;
  page-break-inside: avoid;
}

.figure img {
  max-width: 100%;
  height: auto;
}

.caption {
  font-style: italic;
  font-size: 0.9em;
  color: #555;
  margin-top: 0.3em;
}

code {
  font-family: Menlo, Monaco, 'Lucida Console', Consolas, monospace;
  font-size: 0.9em;
  background-color: #f4f4f4;
  padding: 0.1em 0.3em;
  border-radius: 2px;
}

hr {
  border: none;
  border-top: 1px solid #ccc;
  margin: 2em 0;
}

.title-page {
  text-align: center;
  padding: 4em 0;
}

.title-page h1 {
  font-size: 2.5em;
  color: #0A3D62;
  margin-bottom: 0.3em;
  page-break-before: avoid;
}

.title-page .subtitle {
  font-style: italic;
  font-size: 1.3em;
  color: #1F4E79;
  margin-bottom: 2em;
}

.title-page .tagline {
  font-style: italic;
  color: #333;
  margin: 0.2em 0;
}

.title-page .def-edition {
  font-size: 1.2em;
  font-weight: bold;
  color: #0A3D62;
  margin: 1.5em 0 0.3em 0;
}

.title-page .publisher {
  font-style: italic;
  margin-bottom: 2em;
}

.title-page .meta {
  font-size: 0.95em;
  margin: 0.8em 0;
}

.title-page .meta-label {
  font-style: italic;
  color: #2C3E50;
  margin-bottom: 0.2em;
}

.contents-list p {
  margin: 0.4em 0;
}

nav#toc {
  margin: 2em 0;
}

nav#toc ol {
  list-style-type: none;
  padding-left: 0;
}

nav#toc ol li {
  margin: 0.4em 0;
}

nav#toc a {
  text-decoration: none;
  color: #1a1a1a;
}

sup, sub {
  font-size: 0.8em;
}
'''

    # Add CSS
    css_item = epub.EpubItem(
        uid='style',
        file_name='styles/style.css',
        media_type='text/css',
        content=css.encode('utf-8')
    )
    book.add_item(css_item)

    # Add images
    if os.path.exists(IMG_DIR):
        for fname in sorted(os.listdir(IMG_DIR)):
            if fname.endswith('.png'):
                img_path = os.path.join(IMG_DIR, fname)
                with open(img_path, 'rb') as f:
                    img_content = f.read()
                img_item = epub.EpubItem(
                    uid=f'image_{fname}',
                    file_name=f'images/{fname}',
                    media_type='image/png',
                    content=img_content
                )
                book.add_item(img_item)

    # Read source
    with open(SRC) as f:
        md_text = f.read()

    # Build title page
    title_page = epub.EpubHtml(
        title='Essential Histology',
        file_name='text/title_page.xhtml',
        lang='en'
    )
    title_page.add_link(href='../styles/style.css', rel='stylesheet', type='text/css')
    title_page.content = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en">
<head>
<title>Essential Histology</title>
<link rel="stylesheet" type="text/css" href="../styles/style.css"/>
</head>
<body epub:type="frontmatter">
<section class="title-page">
<h1>Essential Histology</h1>
<div class="subtitle">A Concept-Based Guide for PGME</div>
<div class="tagline">Understanding the structure. Seeing the pattern.</div>
<div class="tagline">Distinguishing the alternatives. Retrieving the logic.</div>
<div class="def-edition">Definitive Edition</div>
<div class="publisher">AREMS-HY Academic Series</div>

<div class="meta"><div class="meta-label">Primary scientific foundation</div>
Mescher AL. <b>Junqueira's Basic Histology: Text and Atlas.</b> 17th ed. McGraw Hill.</div>

<div class="meta"><div class="meta-label">Official 16-Chapter Syllabus</div>
Aligned with Junqueira 17th Chapters 1, 2, 3, 4, 5, 6, 9, 11, 12, 13, 14, 15, 16, 17, 18, 20</div>

<div class="meta">Built for the Afghanistan 1405 Specialty Examination</div>
</section>
</body>
</html>'''.encode('utf-8')
    book.add_item(title_page)

    # Convert markdown to XHTML, then split into chapters
    full_xhtml = md_to_xhtml(md_text)

    # Split into chapters by Heading 1
    chapter_pattern = re.compile(r'<h1>(.+?)</h1>')
    parts = chapter_pattern.split(full_xhtml)

    # parts[0] is preamble (Contents), then alternating title/content
    chapters_data = []
    preamble = parts[0]
    for i in range(1, len(parts), 2):
        title = parts[i]
        content = parts[i+1] if i+1 < len(parts) else ''
        chapters_data.append((title, content))

    # Add each chapter
    chapter_items = []
    for idx, (title, content) in enumerate(chapters_data, 1):
        # Generate file name
        if 'Final Integrated Review' in title:
            fname = 'ch_final_review.xhtml'
            num = 'Final'
        elif 'Examination Practice' in title:
            fname = 'ch_exam_practice.xhtml'
            num = 'Practice'
        elif 'Recognition Drills' in title:
            fname = 'ch_recognition_drills.xhtml'
            num = 'Drills'
        elif 'Final Preparation' in title:
            fname = 'ch_final_preparation.xhtml'
            num = 'Last'
        else:
            ch_num = re.search(r'Chapter (\d+)', title)
            num = ch_num.group(1) if ch_num else str(idx)
            fname = f'ch{idx:02d}.xhtml'

        chapter = epub.EpubHtml(
            title=title,
            file_name=f'text/{fname}',
            lang='en'
        )
        chapter.add_link(href='../styles/style.css', rel='stylesheet', type='text/css')

        # Build chapter content
        chapter_xhtml = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en">
<head>
<title>{title}</title>
<link rel="stylesheet" type="text/css" href="../styles/style.css"/>
</head>
<body epub:type="bodymatter">
<section>
<h1>{title}</h1>
{content}
</section>
</body>
</html>'''
        chapter.content = chapter_xhtml.encode('utf-8')
        book.add_item(chapter)
        chapter_items.append(chapter)

    # Add Contents page (after title page)
    contents_chapter = epub.EpubHtml(
        title='Contents',
        file_name='text/contents.xhtml',
        lang='en'
    )
    contents_chapter.add_link(href='../styles/style.css', rel='stylesheet', type='text/css')

    # Build TOC items
    toc_links = []
    toc_html_items = []
    for ch in chapter_items:
        toc_links.append(ch)
        toc_html_items.append(f'<li><a href="{ch.file_name.replace("text/", "")}">{ch.title}</a></li>')

    contents_xhtml = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en">
<head>
<title>Contents</title>
<link rel="stylesheet" type="text/css" href="../styles/style.css"/>
</head>
<body epub:type="frontmatter">
<section class="contents-list">
<h1>Contents</h1>
<nav id="toc">
<ol>
{"".join(toc_html_items)}
</ol>
</nav>
</section>
<p></p>
</body>
</html>'''
    contents_chapter.content = contents_xhtml.encode('utf-8')
    book.add_item(contents_chapter)

    # Set Table of Contents (NCX)
    book.toc = tuple(
        epub.Link(ch.file_name.replace('text/', ''), ch.title, ch.id)
        for ch in chapter_items
    )

    # Navigation - use only EpubNcx; create nav separately
    book.add_item(epub.EpubNcx())

    # Set spine (reading order)
    book.spine = [title_page, contents_chapter] + chapter_items

    # Write EPUB
    epub.write_epub(OUT, book)
    print(f'Wrote {OUT}: {os.path.getsize(OUT)} bytes')


if __name__ == '__main__':
    build_epub()
