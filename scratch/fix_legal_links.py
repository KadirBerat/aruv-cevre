import os
import re

def fix_legal_links(directory):
    # Mapping of target text patterns to the correct file links
    # We use regex to handle potential multi-line tags or extra spaces
    replacements = [
        (r'href="#"[^>]*>\s*(Kullanım Şartları|Kullanım Koşulları|Terms &amp; Conditions)\s*</a>', 'href="terms.html">\\1</a>'),
        (r'href="#"[^>]*>\s*(Gizlilik Politikası|Privacy Policy)\s*</a>', 'href="privacy.html">\\1</a>')
    ]

    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                original_content = content
                for pattern, repl in replacements:
                    content = re.sub(pattern, repl, content, flags=re.IGNORECASE | re.DOTALL)

                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Fixed legal links in {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    fix_legal_links(".")
