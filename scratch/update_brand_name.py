import os

def update_brand_name(directory):
    # The brand name to search for (case-sensitive)
    target = 'Solaria'
    # The new brand name
    replacement = 'Arüv Çevre'

    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            try:
                # Read file content
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Perform the replacement if the target exists
                if target in content:
                    new_content = content.replace(target, replacement)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated brand name in {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    update_brand_name(".")
