#!/usr/bin/env python3
"""Check built output for broken local links and accidental publication."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else '_site').resolve()
errors = []

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for attr in ('href', 'src'):
            if attrs.get(attr):
                self.urls.append(attrs[attr])

for page in root.rglob('*.html'):
    text = page.read_text()
    if any(term in text for term in ('Your Sidebar Name', 'GitHub University', 'Citation Ledger', 'ityuval@bgu.ac.il', '43 different slack teams', 'personal description')):
        errors.append(f'{page.relative_to(root)}: stale content')
    rel = page.relative_to(root).as_posix()
    if rel.startswith('photography/') and rel != 'photography/index.html' and 'data-pswp-width=' not in text:
        errors.append(f'{rel}: empty gallery')
    parser = Links()
    parser.feed(text)
    for url in parser.urls:
        parts = urlsplit(url)
        if parts.scheme and parts.scheme not in ('http', 'https'):
            continue
        if parts.netloc and parts.netloc != 'yuvalyitz.github.io':
            continue
        if not parts.path or parts.path.startswith('/parameterized-scheduling-zoo/'):
            continue
        target = (root / unquote(parts.path).lstrip('/')) if parts.path.startswith('/') else (page.parent / unquote(parts.path))
        if not target.exists() and not target.with_suffix(".html").exists():
            errors.append(f'{page.relative_to(root)}: missing {url}')
    if text.count('gtag/js?id=') > 1:
        errors.append(f'{page.relative_to(root)}: duplicate analytics')
for path in root.rglob('*'):
    rel = path.relative_to(root)
    if path.name == '.DS_Store' or path.suffix in ('.ipynb', '.db') or rel.parts[0] in ('local', 'scripts', 'anaconda_projects', 'markdown_generator') or 'demo-docs-website' in rel.parts:
        errors.append(f'Unexpected published file: {rel}')
for url in ('markdown', 'non-menu-page', 'archive-layout-with-content', 'collection-archive', 'page-archive', 'categories', 'tags', 'year-archive'):
    if (root / url).exists():
        errors.append(f'Unexpected demo page: {url}')
if errors:
    print('\n'.join(sorted(set(errors))))
    sys.exit(1)
print(f'Passed: {len(list(root.rglob("*.html")))} HTML files; local links, stale content, analytics, and output exclusions.')
