import os
import re

def translate_labels(directory):
    replacements = [
        (r'Need Our Services\?', r'Hizmetlerimize mi İhtiyacınız Var?'),
        (r'Work Hours', r'Çalışma Saatleri'),
        (r'Call:', r'Telefon:'),
        (r'Email:', r'E-posta:'),
        (r'Location:', r'Konum:'),
        (r'Send Us Message', r'Bize Mesaj Gönderin'),
        (r'Contact Us', r'Bize Ulaşın'),
        (r'Quick Links', r'Hızlı Bağlantılar')
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
                    print(f"Translated labels in {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    translate_labels(".")
