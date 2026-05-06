import os
import re

def update_copyright(directory):
    # List of patterns to identify and their replacements
    # We target both the Solaria branding and the already-updated Arüv Çevre branding for the year change.
    replacements = [
        (re.compile(r'&copy; 2025 - Solaria by Designesia'), '&copy; 2026 Arüv Çevre'),
        (re.compile(r'&copy; 2025 - Arüv Çevre'), '&copy; 2026 Arüv Çevre'),
        (re.compile(r'&copy; 2025 Arüv Çevre'), '&copy; 2026 Arüv Çevre'),
        (re.compile(r'© 2025 - Solaria by Designesia'), '© 2026 Arüv Çevre'),
        (re.compile(r'© 2025 - Arüv Çevre'), '© 2026 Arüv Çevre'),
        (re.compile(r'© 2025 Arüv Çevre'), '© 2026 Arüv Çevre'),
    ]

    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                new_content = content
                for pattern, replacement in replacements:
                    new_content = pattern.sub(replacement, new_content)

                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated copyright in {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    update_copyright(".")
