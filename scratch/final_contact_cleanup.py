import os
import re

def final_contact_cleanup(directory):
    # Mapping of legacy patterns (regex) to new values
    replacements = [
        (r'100 Solar\s+Ave,\s+San Diego,\s+CA', 'Muratpaşa / Antalya'),
        (r'Monday\s*-\s*Friday\s+08\.00\s*-\s*18\.00', 'Pazartesi - Cuma 08:00 - 17:00'),
        (r'Monday\s*-\s*Friday', 'Pazartesi - Cuma'),
        (r'08\.00\s*-\s*18\.00', '08:00 - 17:00'),
        (r'support@solaria\.com', 'info@test.com'),
        (r'\+1 800 987 654', '+90 555 555 55 55'),
        (r'© 2025 - Solaria by Designesia', '© 2026 Arüv Çevre'),
        (r'© 2025 - Arüv Çevre by Designesia', '© 2026 Arüv Çevre')
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
                    print(f"Cleaned up contact info in {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    final_contact_cleanup(".")
