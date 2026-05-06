import os

def update_footer_links(directory):
    target = '<ul class="menu-simple">\n                      <li><a href="#">Terms &amp; Conditions</a></li>\n                      <li><a href="#">Privacy Policy</a></li>\n                    </ul>'
    
    # Variations in whitespace can happen, so let's use a more flexible approach or multiple targets
    targets = [
        '<ul class="menu-simple">\n                      <li><a href="#">Terms &amp; Conditions</a></li>\n                      <li><a href="#">Privacy Policy</a></li>\n                    </ul>',
        '<ul class="menu-simple">\n                                            <li><a href="#">Terms &amp; Conditions</a></li>\n                                            <li><a href="#">Privacy Policy</a></li>\n                                        </ul>'
    ]
    
    replacement = '<ul class="menu-simple">\n                      <li><a href="terms.html">Kullanım Şartları</a></li>\n                      <li><a href="privacy.html">Gizlilik Politikası</a></li>\n                    </ul>'

    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                updated = False
                for t in targets:
                    if t in content:
                        content = content.replace(t, replacement)
                        updated = True
                
                # If exact match fails, try a regex or simpler match
                if not updated and 'Terms &amp; Conditions' in content:
                    import re
                    # Match the ul block more flexibly
                    pattern = r'<ul class="menu-simple">.*?Terms &amp; Conditions.*?Privacy Policy.*?</ul>'
                    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
                    if new_content != content:
                        content = new_content
                        updated = True

                if updated:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Updated footer links in {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    update_footer_links(".")
