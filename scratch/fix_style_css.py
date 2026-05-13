import os

def fix_style_css():
    file_path = r'c:\Benim Web Sitem\solaria\madebydesignesia.com\themes\solaria\css\style.css'
    
    with open(file_path, 'r', encoding='utf-16', errors='ignore') as f:
        content = f.read()
    
    # We want to remove the mangled section and replace it with clean UTF-8 text.
    # The mangled section starts around " / *   L a n g u a g e"
    
    # Actually, a better way is to read the file as UTF-8, find the last clean part, and truncate.
    with open(file_path, 'rb') as f:
        raw_data = f.read()
    
    # Find the end of the clean part. The clean part ends with "  width: auto;\n  }\n}"
    search_term = b'  width: auto;\r\n    }\r\n  }\r\n}\r\n'
    if search_term not in raw_data:
        search_term = b'  width: auto;\n    }\n  }\n}\n'
    
    # Let's just find the last occurrence of "width: auto;" and then find the closing braces.
    # Or more simply, search for the first mangled character.
    # The mangled part has null bytes or spaces between characters.
    
    clean_data = raw_data.split(b' / *   L a n g u a g e')[0]
    
    new_styles = """
/* Language Switcher Custom Styles */
.de-switch-lang {
    position: relative;
    display: inline-block;
    cursor: pointer;
    font-size: 13px;
    font-weight: 600;
    color: #fff;
    padding: 5px 0;
}

.de-switch-lang:after {
    font-family: 'FontAwesome';
    content: '\\f078';
    font-size: 8px;
    margin-left: 8px;
    opacity: .5;
}

.de-switch-lang ul {
    position: absolute;
    top: 100%;
    right: 0;
    background: #fff;
    list-style: none;
    padding: 5px 0;
    margin: 0;
    min-width: 100px;
    box-shadow: 0 5px 15px rgba(0,0,0,.1);
    border-radius: 4px;
    opacity: 0;
    visibility: hidden;
    transition: all .3s ease;
    z-index: 1000;
}

.de-switch-lang:hover ul {
    opacity: 1;
    visibility: visible;
    top: calc(100% + 5px);
}

.de-switch-lang ul li {
    padding: 0;
}

.de-switch-lang ul li a {
    color: #333 !important;
    display: block;
    padding: 8px 15px;
    white-space: nowrap;
    transition: all .2s;
}

.de-switch-lang ul li a:hover {
    background: #f8f9fa;
    color: var(--primary-color) !important;
}

/* Adjust topbar for vertical alignment */
#topbar .d-flex {
    align-items: center;
}
"""
    
    with open(file_path, 'wb') as f:
        f.write(clean_data)
        f.write(new_styles.encode('utf-8'))

if __name__ == "__main__":
    fix_style_css()
