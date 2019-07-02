#!/usr/bin/env python3

import markdown 

with open('README.md') as f:
    content = f.read()
    html = markdown.markdown(content, extensions=['extra', 'codehilite'])

with open('README.html', 'w') as f:
    f.write('<html><head><link rel="stylesheet" type="text/css" href="github-markdown.css" /><link rel="stylesheet" type="text/css" href="codehilite.css" /></head><body><div id="main" class="markdown-body">')
    f.write(html)
    f.write('</div></body></html>')

