import os

def update_phone(directory):
    # The phone number to search for
    target = '+1 800 987 654'
    # The new phone number
    replacement = '+90 555 555 55 55'

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
                    print(f"Updated phone number in {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    update_phone(".")
