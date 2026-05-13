import os
import re

def update_portal_text():
    directory = r'c:\Benim Web Sitem\solaria\madebydesignesia.com\themes\solaria'
    target_pattern = re.compile(r'<span>Bize Ulaşın</span>')
    replacement = '<span>Arüv Portal</span>'
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    if target_pattern.search(content):
                        new_content = target_pattern.sub(replacement, content)
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"Updated: {file_path}")
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    update_portal_text()
