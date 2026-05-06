import os

def update_hours(directory):
    # The working hours string to search for
    target = 'Monday - Friday 08.00 - 18.00'
    # The new working hours string in Turkish
    replacement = 'Pazartesi - Cuma 08:00 - 17:00'

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
                    print(f"Updated working hours in {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    update_hours(".")
