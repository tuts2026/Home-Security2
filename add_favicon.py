import os

# 1. Create a simple shield SVG for the favicon
svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="#E8A317">
  <path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm0 10.99h7c-.53 4.12-3.28 7.79-7 8.94V12H5V6.3l7-3.11v8.8z"/>
</svg>"""
with open('favicon.svg', 'w', encoding='utf-8') as f:
    f.write(svg_content)

# 2. Add the favicon link to the HTML files
files_to_update = ['index.html', 'privacy.html', 'terms.html']
favicon_tag = '<link rel="icon" type="image/svg+xml" href="/favicon.svg" />\n'

for filename in files_to_update:
    if not os.path.exists(filename):
        continue
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    
    if '<link rel="icon"' not in html:
        # Insert right after the title tag
        html = html.replace('</title>\n', '</title>\n' + favicon_tag)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
