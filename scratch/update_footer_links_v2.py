import os
import re

def update_footer_links(directory):
    # Professional replacement content
    replacement = '<ul class="menu-simple">\n                      <li><a href="terms.html">Kullanım Şartları</a></li>\n                      <li><a href="privacy.html">Gizlilik Politikası</a></li>\n                    </ul>'

    # Regex to find the menu-simple list with Terms and Privacy, handling whitespace and line breaks
    pattern = re.compile(r'<ul class="menu-simple">.*?Terms &amp;.*?Conditions.*?Privacy Policy.*?</ul>', re.DOTALL | re.IGNORECASE)

    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                if "Terms &amp;" in content or "Privacy Policy" in content:
                    new_content = pattern.sub(replacement, content)
                    if new_content != content:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Updated footer links in {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    update_footer_links(".")
