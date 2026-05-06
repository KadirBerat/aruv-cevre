import os
import re

def final_logo_cleanup(directory):
    # Target tag pattern for any uncommented images/logo-white.webp
    tag_pattern = re.compile(r'<img\s+([^>]*src="images/logo-white\.webp"[^>]*)>')

    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    lines = f.readlines()

                new_lines = []
                changed = False
                for line in lines:
                    # Check if the logo is present and NOT already commented out
                    if 'images/logo-white.webp' in line and '<!--' not in line:
                        # Extract indentation from the line
                        stripped = line.lstrip()
                        indent = line[:len(line) - len(stripped)]
                        
                        def replacer(match):
                            full_attrs = match.group(1)
                            # Extract class
                            class_match = re.search(r'class="([^"]*)"', full_attrs)
                            img_class = class_match.group(1) if class_match else ""
                            
                            # Comment out old, add new
                            old_comment = f'<!-- <img {full_attrs}> -->'
                            new_tag = f'<img src="images/aruvcevre.png" class="{img_class}" alt="">'
                            
                            # Return the replacement with proper line breaks and indentation
                            # Note: indent is already captured from the original line
                            return f'{old_comment}\n{indent}{new_tag}'
                        
                        new_line = tag_pattern.sub(replacer, line)
                        if new_line != line:
                            new_lines.append(new_line)
                            changed = True
                            continue
                    
                    new_lines.append(line)

                if changed:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.writelines(new_lines)
                    print(f"Cleaned up {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    final_logo_cleanup(".")
