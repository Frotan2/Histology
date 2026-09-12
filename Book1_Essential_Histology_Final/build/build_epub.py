#!/usr/bin/env python3
"""Build EPUB from canonical markdown source."""
import os
import re
import sys
import zipfile
from ebooklib import epub


def to_xhtml(text):
    text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<b><i>\1</i></b>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    text = re.sub(r'\*(.+?)\*', r'<i>\1</i>', text)
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    return text


def render_table_xhtml(rows):
    if not rows or len(rows) < 2:
        return ''
    header = rows[0]
    data = rows[1:]
    max_c = max(len(r) for r in rows)
    header = header + [''] * (max_c - len(header))
    data = [r + [''] * (max_c - len(r)) for r in data]
    x = '<table>\n<thead>\n<tr>\n'
    for c in header:
        x += f'<th>{to_xhtml(c)}</th>\n'
    x += '</tr>\n</thead>\n<tbody>\n'
    for r in data:
        x += '<tr>\n'
        for c in r:
            x += f'<td>{to_xhtml(c)}</td>\n'
        x += '</tr>\n'
    x += '</tbody>\n</table>'
    return x


def md_to_xhtml(md_text):
    lines = md_text.split('\n')
    out = []
    i = 0
    # skip front matter
    for j, line in enumerate(lines):
        if line.startswith('# Chapter 1 —'):
            i = j
            break
    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if not s:
            out.append('')
            i += 1
            continue
        if s == '---':
            out.append('<hr/>')
            i += 1
            continue
        if line.startswith('# ') and not line.startswith('## '):
            out.append(f'<h1>{to_xhtml(s[2:])}</h1>')
            i += 1
            continue
        if line.startswith('## '):
            out.append(f'<h2>{to_xhtml(s[3:])}</h2>')
            i += 1
            continue
        if line.startswith('### '):
            out.append(f'<h3>{to_xhtml(s[4:])}</h3>')
            i += 1
            continue
        if line.startswith('#### '):
            out.append(f'<h4>{to_xhtml(s[5:])}</h4>')
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
            out.append(render_table_xhtml(rows))
            out.append('')
            continue
        b = re.match(r'^\s*-\s+(.*)', line)
        if b:
            out.append(f'<ul><li>{to_xhtml(b.group(1))}</li></ul>')
            i += 1
            continue
        n = re.match(r'^(\d+)\.\s+(.*)', line)
        if n:
            out.append(f'<p><b>{n.group(1)}.</b> {to_xhtml(n.group(2))}</p>')
            i += 1
            continue
        out.append(f'<p>{to_xhtml(line)}</p>')
        i += 1
    return '\n'.join(out)


def build_epub(src_md, out_epub):
    book = epub.EpubBook()
    book.set_identifier('urn:uuid:essential-histology-1405-definitive-final')
    book.set_title('Essential Histology - A Concept-Based Guide for PGME')
    book.set_language('en')
    book.add_author('AREMS-HY Academic Series')
    book.add_metadata('DC', 'description',
                      'A concept-based histology textbook for the Afghanistan 1405 Specialty Examination, aligned with Junqueira 17th Edition official 16-chapter syllabus.')
    book.add_metadata('DC', 'subject', 'Histology, Medical Textbook, PGME, 1405 Examination, Junqueira')
    book.add_metadata('DC', 'publisher', 'AREMS-HY Academic Series')

    css = '''
body { font-family: Georgia, serif; line-height: 1.5; color: #1a1a1a; margin: 0 1em; }
h1 { font-family: Helvetica, sans-serif; font-size: 1.8em; color: #0A3D62; margin: 2em 0 1em 0; page-break-before: always; }
h2 { font-family: Helvetica, sans-serif; font-size: 1.4em; color: #1F4E79; margin: 1.5em 0 0.6em 0; }
h3 { font-family: Helvetica, sans-serif; font-size: 1.2em; color: #2C3E50; margin: 1.2em 0 0.5em 0; }
h4 { font-family: Helvetica, sans-serif; font-size: 1.05em; font-style: italic; margin: 1em 0 0.4em 0; }
p { margin: 0.8em 0; text-align: justify; }
ul { margin: 0.5em 0; padding-left: 1.5em; }
table { border-collapse: collapse; width: 100%; margin: 1em 0; }
th { background-color: #EAEDED; font-weight: bold; padding: 0.4em 0.6em; border: 1px solid #BDC3C7; }
td { padding: 0.3em 0.6em; border: 1px solid #BDC3C7; vertical-align: top; font-size: 0.95em; }
code { font-family: monospace; background-color: #f4f4f4; padding: 0.1em 0.3em; }
hr { border: none; border-top: 1px solid #ccc; margin: 2em 0; }
.title-page { text-align: center; padding: 4em 0; }
.title-page h1 { font-size: 2.5em; page-break-before: avoid; }
'''

    css_item = epub.EpubItem(uid='style', file_name='styles/style.css', media_type='text/css', content=css.encode('utf-8'))
    book.add_item(css_item)

    # Title page
    title_page = epub.EpubHtml(title='Essential Histology', file_name='text/title_page.xhtml', lang='en')
    title_page.add_link(href='../styles/style.css', rel='stylesheet', type='text/css')
    title_page.content = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en">
<head><title>Essential Histology</title><link rel="stylesheet" type="text/css" href="../styles/style.css"/></head>
<body epub:type="frontmatter">
<section class="title-page">
<h1>Essential Histology</h1>
<div style="font-style: italic; font-size: 1.3em; color: #1F4E79;">A Concept-Based Guide for PGME</div>
<div style="font-style: italic; color: #333;">Understanding the structure. Seeing the pattern.</div>
<div style="font-style: italic; color: #333;">Distinguishing the alternatives. Retrieving the logic.</div>
<div style="font-size: 1.2em; font-weight: bold; color: #0A3D62; margin-top: 1.5em;">Definitive Edition</div>
<div style="font-style: italic;">AREMS-HY Academic Series</div>
<div style="margin-top: 2em; font-size: 0.95em;">Primary scientific foundation: Mescher AL. <b>Junqueira's Basic Histology: Text and Atlas.</b> 17th ed. McGraw Hill.</div>
<div style="font-size: 0.95em;">Official 16-Chapter Syllabus: Aligned with Junqueira 17th Chapters 1, 2, 3, 4, 5, 6, 9, 11, 12, 13, 14, 15, 16, 17, 18, 20</div>
<div style="font-size: 0.95em;">Built for the Afghanistan 1405 Specialty Examination</div>
</section>
</body>
</html>'''.encode('utf-8')
    book.add_item(title_page)

    with open(src_md) as f:
        md = f.read()
    full_xhtml = md_to_xhtml(md)
    # Split by h1
    parts = re.split(r'(<h1>.+?</h1>)', full_xhtml)
    chapters_data = []
    for j in range(1, len(parts), 2):
        title_match = re.search(r'<h1>(.+?)</h1>', parts[j])
        title = title_match.group(1) if title_match else f'Chapter {j//2 + 1}'
        content = parts[j + 1] if j + 1 < len(parts) else ''
        chapters_data.append((title, content))

    chapter_items = []
    for idx, (title, content) in enumerate(chapters_data, 1):
        ch_num = re.search(r'Chapter (\d+)', title)
        num = ch_num.group(1) if ch_num else str(idx)
        fname = f'ch{idx:02d}.xhtml'
        ch = epub.EpubHtml(title=title, file_name=f'text/{fname}', lang='en')
        ch.add_link(href='../styles/style.css', rel='stylesheet', type='text/css')
        ch.content = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en">
<head><title>{title}</title><link rel="stylesheet" type="text/css" href="../styles/style.css"/></head>
<body epub:type="bodymatter">
<section>
{re.sub(r"<h1>.+?</h1>", "", parts[2*idx-1] + content)}
</section>
</body>
</html>'''.encode('utf-8')
        book.add_item(ch)
        chapter_items.append(ch)

    # Contents
    contents = epub.EpubHtml(title='Contents', file_name='text/contents.xhtml', lang='en')
    contents.add_link(href='../styles/style.css', rel='stylesheet', type='text/css')
    toc_html = '\n'.join(f'<li><a href="{ch.file_name.replace("text/", "")}">{ch.title}</a></li>' for ch in chapter_items)
    contents.content = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en">
<head><title>Contents</title><link rel="stylesheet" type="text/css" href="../styles/style.css"/></head>
<body epub:type="frontmatter">
<section><h1>Contents</h1>
<nav id="toc"><ol>{toc_html}</ol></nav>
</section></body>
</html>'''.encode('utf-8')
    book.add_item(contents)

    book.toc = tuple(epub.Link(ch.file_name.replace('text/', ''), ch.title, ch.id) for ch in chapter_items)
    book.add_item(epub.EpubNcx())
    book.spine = [title_page, contents] + chapter_items
    epub.write_epub(out_epub, book)


if __name__ == '__main__':
    src = sys.argv[1] if len(sys.argv) > 1 else '../Essential_Histology_Combined.md'
    out = sys.argv[2] if len(sys.argv) > 2 else '../Essential_Histology_Final.epub'
    build_epub(src, out)
    print(f'Wrote {out}')
