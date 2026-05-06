import os
import re

def update_logo(directory):
    # Regex to match the logo block with flexible indentation
    # It looks for <!-- logo begin --> followed by optional whitespace and the logo div,
    # then the old image tags, and finally <!-- logo end -->.
    
    # Target pattern:
    # <!-- logo begin -->
    # <div id="logo">
    #     <a href="index.html">
    #         <img class="logo-main" src="images/logo-white.webp" alt="" >
    #         <img class="logo-mobile" src="images/logo-white.webp" alt="" >
    #     </a>
    # </div>
    # <!-- logo end -->

    logo_pattern = re.compile(
        r'(?P<indent>\s*)<!-- logo begin -->\s*\n'
        r'(?P<logo_indent>\s*)<div id="logo">\s*\n'
        r'(?P<link_indent>\s*)<a href="index.html">\s*\n'
        r'(?P<img_indent>\s*)<img class="logo-main" src="images/logo-white.webp" alt="" >\s*\n'
        r'(?P<img_indent2>\s*)<img class="logo-mobile" src="images/logo-white.webp" alt="" >\s*\n'
        r'(?P<link_end_indent>\s*)</a>\s*\n'
        r'(?P<logo_end_indent>\s*)</div>\s*\n'
        r'(?P<comment_end_indent>\s*)<!-- logo end -->'
    )

    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            def replace_logo(match):
                indent = match.group('indent')
                logo_indent = match.group('logo_indent')
                link_indent = match.group('link_indent')
                img_indent = match.group('img_indent')
                link_end_indent = match.group('link_end_indent')
                logo_end_indent = match.group('logo_end_indent')
                comment_end_indent = match.group('comment_end_indent')

                return (
                    f"{indent}<!-- logo begin -->\n"
                    f"{logo_indent}<div id=\"logo\">\n"
                    f"{link_indent}<a href=\"index.html\">\n"
                    f"{img_indent}<!-- <img class=\"logo-main\" src=\"images/logo-white.webp\" alt=\"\" > -->\n"
                    f"{img_indent}<img class=\"logo-main\" src=\"images/aruvcevre.png\" alt=\"\" >\n"
                    f"{img_indent}<!-- <img class=\"logo-mobile\" src=\"images/logo-white.webp\" alt=\"\" > -->\n"
                    f"{img_indent}<img class=\"logo-mobile\" src=\"images/aruvcevre.png\" alt=\"\" >\n"
                    f"{link_end_indent}</a>\n"
                    f"{logo_end_indent}</div>\n"
                    f"{comment_end_indent}<!-- logo end -->"
                )

            new_content = logo_pattern.sub(replace_logo, content)

            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filename}")
            else:
                # If the exact pattern above didn't match, maybe it's already updated or slightly different
                # Let's try a more lenient match if needed, but first let's see if this works.
                pass

if __name__ == "__main__":
    update_logo(".")
