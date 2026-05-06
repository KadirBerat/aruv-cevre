import os
import re

def final_footer_fix(directory):
    # 1. Fix the .abs div to not block clicks
    # 2. Update text to "Kullanım Koşulları" (if preferred by user's prompt) and ensure links
    
    replacements = [
        # Make the background decoration non-interactive
        (r'<div class="abs w-50 end-0 bottom-0 op-3">', r'<div class="abs w-50 end-0 bottom-0 op-3" style="pointer-events: none;">'),
        
        # Ensure legal links are correct and use the requested terminology
        (r'<a href="terms.html">Kullanım Şartları</a>', r'<a href="terms.html">Kullanım Koşulları</a>'),
        (r'<a href="#">Kullanım Şartları</a>', r'<a href="terms.html">Kullanım Koşulları</a>'),
        (r'<a href="#">Kullanım Koşulları</a>', r'<a href="terms.html">Kullanım Koşulları</a>'),
        (r'<a href="#">Gizlilik Politikası</a>', r'<a href="privacy.html">Gizlilik Politikası</a>'),
        
        # Catch any plain text that might be sitting there without links (unlikely but possible)
        # We only do this if they are inside menu-simple
        (r'<ul class="menu-simple">\s*<li>Kullanım Şartları</li>\s*<li>Gizlilik Politikası</li>\s*</ul>', 
         r'<ul class="menu-simple"><li><a href="terms.html">Kullanım Koşulları</a></li><li><a href="privacy.html">Gizlilik Politikası</a></li></ul>')
    ]

    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                original_content = content
                for pattern, repl in replacements:
                    content = re.sub(pattern, repl, content, flags=re.IGNORECASE)

                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Fixed footer in {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    final_footer_fix(".")
