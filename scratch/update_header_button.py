import os

def update_header_button(directory):
    # The exact HTML snippet to replace
    target = '<a href="get-a-quote.html" class="btn-main btn-line fx-slide hover-white"><span>Get a Quote</span></a>'
    # The new HTML snippet
    replacement = '<a href="contact.html" class="btn-main btn-line fx-slide hover-white"><span>Bize Ulaşın</span></a>'

    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            try:
                # Read file content
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Replace the target string if it exists
                if target in content:
                    new_content = content.replace(target, replacement)
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated header button in {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    update_header_button(".")
