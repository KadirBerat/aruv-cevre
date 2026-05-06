import os
import re

def update_extra_logo(directory):
    # Regex to match <div id="extra-content"> followed by the specific img tag
    # We use \s* to handle potential whitespace/newlines between tags
    # We capture the indentation to preserve it
    pattern = re.compile(
        r'([ \t]*)<div id="extra-content">\s*\n([ \t]*)<img src="images/logo-white\.webp" class="w-150px" alt="">',
        re.MULTILINE
    )

    def replacer(match):
        indent1 = match.group(1)
        indent2 = match.group(2)
        return (f'{indent1}<div id="extra-content">\n'
                f'{indent2}<!-- <img src="images/logo-white.webp" class="w-150px" alt=""> -->\n'
                f'{indent2}<img src="images/aruvcevre.png" class="w-150px" alt="">')

    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                new_content = pattern.sub(replacer, content)

                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    update_extra_logo(".")
