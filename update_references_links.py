import os
import re

patterns = [
    # Main Referanslarımız link
    (r'<li><a class="menu-item" href>Referanslarımız</a>', '<li><a class="menu-item" href="references.html">Referanslarımız</a>'),
    (r'<li><a class="menu-item" href=\"\">Referanslarımız</a>', '<li><a class="menu-item" href="references.html">Referanslarımız</a>'),
    
    # Sub-menu items
    (r'<li><a href>Müşavirlik\s+Referanslarımız</a></li>', '<li><a href="references.html">Müşavirlik Referanslarımız</a></li>'),
    (r'<li><a href>Taahhüt\s+Referanslarımız</a></li>', '<li><a href="references.html">Taahhüt Referanslarımız</a></li>'),
    (r'<li><a href>Peyzaj\s+Referanslarımız</a></li>', '<li><a href="references.html">Peyzaj Referanslarımız</a></li>'),
    (r'<li><a href>Danışmanlık\s+Referanslarımız</a></li>', '<li><a href="references.html">Danışmanlık Referanslarımız</a></li>'),
    
    # Alternative formats with quotes or spaces
    (r'<li><a href=\"\">Müşavirlik\s+Referanslarımız</a></li>', '<li><a href="references.html">Müşavirlik Referanslarımız</a></li>'),
    (r'<li><a href=\"\">Taahhüt\s+Referanslarımız</a></li>', '<li><a href="references.html">Taahhüt Referanslarımız</a></li>'),
    (r'<li><a href=\"\">Peyzaj\s+Referanslarımız</a></li>', '<li><a href="references.html">Peyzaj Referanslarımız</a></li>'),
    (r'<li><a href=\"\">Danışmanlık\s+Referanslarımız</a></li>', '<li><a href="references.html">Danışmanlık Referanslarımız</a></li>'),
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
                # Fallback to other encoding if utf-8 fails
                try:
                    with open(path, 'r', encoding='latin-1') as f:
                        content = f.read()
                    new_content = content
                    for p, r in patterns:
                        new_content = re.sub(p, r, new_content, flags=re.MULTILINE | re.IGNORECASE)
                    if new_content != content:
                        print(f'Updated (latin-1) {path}')
                        with open(path, 'w', encoding='latin-1') as f:
                            f.write(new_content)
                except:
                    print(f'Error reading {path}: {e}')
