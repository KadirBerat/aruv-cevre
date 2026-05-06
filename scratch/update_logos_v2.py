import os
import re

def update_logo(directory):
    # Regex to match the logo block from <!-- logo begin --> to <!-- logo end -->
    # We use non-greedy matching .*? with re.DOTALL to capture everything between the comments
    logo_block_pattern = re.compile(
        r'<!-- logo begin -->.*?<!-- logo end -->',
        re.DOTALL
    )

    # The user's exact "after" snippet
    new_logo_content = """<!-- logo begin -->
                                <div id="logo">
                                    <a href="index.html">
                                        <!-- <img class="logo-main" src="images/logo-white.webp" alt="" > -->
                                        <img class="logo-main" src="images/aruvcevre.png" alt="" >
                                        <!-- <img class="logo-mobile" src="images/logo-white.webp" alt="" > -->
                                        <img class="logo-mobile" src="images/aruvcevre.png" alt="" >
                                    </a>
                                </div>
                                <!-- logo end -->"""

    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                new_content = logo_block_pattern.sub(new_logo_content, content)

                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    update_logo(".")
