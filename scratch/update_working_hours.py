import os
import re

def update_working_hours(directory):
    # Mapping of various patterns to the new requested format: "Pzt - Cum, 08:00 - 17:00"
    replacements = [
        (r'Mon to Sat 08:00 - 17:00', r'Pzt - Cum, 08:00 - 17:00'),
        (r'Monday - Friday 08:00 - 17:00', r'Pzt - Cum, 08:00 - 17:00'),
        (r'Pazartesi - Cuma 08:00 - 17:00', r'Pzt - Cum, 08:00 - 17:00'),
        (r'Pazartesi - Cuma 08:00 - 18:00', r'Pzt - Cum, 08:00 - 17:00')
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
                    print(f"Updated working hours in {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    update_working_hours(".")
