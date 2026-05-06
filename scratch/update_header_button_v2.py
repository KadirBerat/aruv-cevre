import os
import re

def update_header_button(directory):
    # Regex to match the button even with newlines/whitespace
    # Specifically targeting the header button structure
    pattern = re.compile(r'<a\s+href="get-a-quote\.html"\s+class="btn-main\s+btn-line\s+fx-slide\s+hover-white"><span>\s*Get\s+a\s+Quote\s*</span></a>', re.IGNORECASE | re.DOTALL)
    
    replacement = '<a href="contact.html" class="btn-main btn-line fx-slide hover-white"><span>Bize Ulaşın</span></a>'

    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                if pattern.search(content):
                    new_content = pattern.sub(replacement, content)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated header button in {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    update_header_button(".")
