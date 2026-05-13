import os
import re

def update_portal_text():
    directory = r'c:\Benim Web Sitem\solaria\madebydesignesia.com\themes\solaria'
    # Use a broad regex to handle potential whitespace variations
    target_pattern = re.compile(r'<span>Bize Ulaşın</span>', re.IGNORECASE)
    replacement = '<span>Arüv Portal</span>'
    
    updated_files = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    if target_pattern.search(content):
                        new_content = target_pattern.sub(replacement, content)
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        updated_files.append(file)
                except Exception as e:
                    print(f"Error processing {file}: {e}")
    
    if updated_files:
        print(f"Updated {len(updated_files)} files: {', '.join(updated_files)}")
    else:
        print("No files were updated.")

if __name__ == "__main__":
    update_portal_text()
