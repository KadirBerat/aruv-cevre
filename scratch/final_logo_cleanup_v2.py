import os
import re

def final_logo_cleanup(directory):
    # Global regex for any <img> with images/logo-white.webp
    tag_pattern = re.compile(r'([ \t]*)<img\s+([^>]*src="images/logo-white\.webp"[^>]*)>', re.DOTALL)

    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                new_content = content
                matches = list(tag_pattern.finditer(content))
                
                # Process matches in reverse to maintain string indices
                for match in reversed(matches):
                    start = match.start()
                    
                    # Check if this match is inside a comment
                    prefix = content[:start]
                    last_comment_start = prefix.rfind('<!--')
                    last_comment_end = prefix.rfind('-->')
                    
                    if last_comment_start > last_comment_end:
                        # It's inside a comment, skip it
                        continue
                    
                    # Replacement logic
                    indent = match.group(1)
                    full_attrs = match.group(2)
                    
                    # Extract class
                    class_match = re.search(r'class="([^"]*)"', full_attrs)
                    img_class = class_match.group(1) if class_match else ""
                    
                    # Create the replacement block
                    # We'll normalize the attributes for the comment to keep it on one line if possible,
                    # or just keep it as is. Let's keep it as is but wrap in comments.
                    old_tag_commented = f'<!-- <img {full_attrs}> -->'
                    new_tag = f'<img src="images/aruvcevre.png" class="{img_class}" alt="">'
                    
                    # The full replacement string
                    replacement = f'{indent}{old_tag_commented}\n{indent}{new_tag}'
                    
                    # Perform the replacement
                    new_content = new_content[:match.start()] + replacement + new_content[match.end():]

                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Final cleanup (v2) updated {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    final_logo_cleanup(".")
