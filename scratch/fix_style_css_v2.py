import os

def fix_style_css():
    file_path = r'c:\Benim Web Sitem\solaria\madebydesignesia.com\themes\solaria\css\style.css'
    
    with open(file_path, 'rb') as f:
        data = f.read()
    
    # The bad part starts with something like " / *   L a n g u a g e" 
    # But it might have different encodings. 
    # Let's search for the last clean part which is "} \r\n }" or similar.
    # The clean part ends at line 13122.
    
    # We'll just look for the first occurrence of " / * " (with spaces)
    bad_part_start = data.find(b' / *   L a n g u a g e')
    if bad_part_start == -1:
        bad_part_start = data.find(b'\x00/\x00*\x00') # UTF-16 style
    
    if bad_part_start != -1:
        clean_data = data[:bad_part_start]
        
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
        print("Fixed successfully.")
    else:
        print("Could not find bad part.")

if __name__ == "__main__":
    fix_style_css()
