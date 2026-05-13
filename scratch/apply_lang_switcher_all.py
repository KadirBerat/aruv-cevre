import os
import re

topbar_lang_code = """                                    <div class="topbar-widget me-4">
                                        <div class="de-switch-lang">
                                            <i class="fa fa-globe"></i> TR
                                            <ul>
                                                <li><a href="#"><img src="https://flagcdn.com/w20/tr.png" alt=""> Türkçe</a></li>
                                                <li><a href="#"><img src="https://flagcdn.com/w20/us.png" alt=""> English</a></li>
                                                <li><a href="#"><img src="https://flagcdn.com/w20/de.png" alt=""> Deutsch</a></li>
                                            </ul>
                                        </div>
                                    </div>"""

mobile_lang_code = """                                    <div class="de-switch-lang d-lg-none d-inline-block me-3">
                                        <i class="fa fa-globe"></i> TR
                                        <ul>
                                            <li><a href="#"><img src="https://flagcdn.com/w20/tr.png" alt=""> Türkçe</a></li>
                                            <li><a href="#"><img src="https://flagcdn.com/w20/us.png" alt=""> English</a></li>
                                            <li><a href="#"><img src="https://flagcdn.com/w20/de.png" alt=""> Deutsch</a></li>
                                        </ul>
                                    </div>"""

def update_file(filepath):
    if filepath.endswith("faq.html"):
        return
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='latin-1') as f:
            content = f.read()

    if 'de-switch-lang' in content:
        return

    # 1. Update Topbar
    # We want to insert inside the d-flex that contains social-icons
    topbar_pattern = r'(<div class="d-flex">\s*<div class="social-icons">)'
    if re.search(topbar_pattern, content, re.IGNORECASE | re.DOTALL):
        content = re.sub(topbar_pattern, r'<div class="d-flex">\n' + topbar_lang_code + r'\n                                    <div class="social-icons">', content, flags=re.IGNORECASE | re.DOTALL, count=1)
    
    # 2. Update Mobile Side Area
    mobile_pattern = r'(<div class="menu_side_area">)'
    if re.search(mobile_pattern, content, re.IGNORECASE):
        content = re.sub(mobile_pattern, r'\1' + '\n' + mobile_lang_code, content, flags=re.IGNORECASE, count=1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    directory = r'c:\Benim Web Sitem\solaria\madebydesignesia.com\themes\solaria'
    files = [f for f in os.listdir(directory) if f.endswith(".html")]
    for filename in files:
        filepath = os.path.join(directory, filename)
        update_file(filepath)
        print(f"Updated {filename}")

if __name__ == "__main__":
    main()
