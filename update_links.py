import os
import re

patterns = [
    (r'<li>\s*<a href=\"[^\"]*\">\s*Basın\s+Odası\s*</a>\s*</li>', '<li><a href=\"news.html\">Basın Odası</a></li>'),
    (r'<li>\s*<a href\s*>\s*Basın\s+Odası\s*</a>\s*</li>', '<li><a href=\"news.html\">Basın Odası</a></li>'),
    (r'<li>\s*<a href=\"[^\"]*\">\s*Basın\s*Odası\s*</a>\s*</li>', '<li><a href=\"news.html\">Basın Odası</a></li>'),
    # Case with line breaks
    (r'<li>\s*<a href=\"[^\"]*\">\s*Basın\s*\n\s*Odası\s*</a>\s*</li>', '<li><a href=\"news.html\">Basın Odası</a></li>')
]

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = content
                for p, r in patterns:
                    new_content = re.sub(p, r, new_content, flags=re.MULTILINE | re.IGNORECASE)
                
                if new_content != content:
                    print(f'Updated {path}')
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
            except Exception as e:
                print(f'Error reading {path}: {e}')
