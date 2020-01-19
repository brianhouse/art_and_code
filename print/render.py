#!/usr/bin/env python3

import markdown, os

with open(os.path.join(os.path.dirname(__file__), "..", "README.md")) as f:
    content = f.read()
    html = markdown.markdown(content, extensions=['extra', 'codehilite'])

with open(os.path.join(os.path.dirname(__file__), "README.html"), 'w') as f:
    f.write('<!doctype html><head><meta charset="utf-8"/><link rel="stylesheet" type="text/css" href="github-markdown.css" /><link rel="stylesheet" type="text/css" href="codehilite.css" /></head><body><div id="main" class="markdown-body">')
    f.write(html)
    f.write('</div></body></html>')

