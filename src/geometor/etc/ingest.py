import re
import os
import glob
from pathlib import Path

def slugify(text):
    """
    Simple slugify function to create safe filenames.
    """
    text = re.sub(r'<[^>]+>', '', text)  # Remove HTML tags
    text = text.replace('&nbsp;', ' ')
    return re.sub(r'\W+', '-', text.lower()).strip('-')

def unique_filename(output_folder, base_name):
    """
    Return the filename, allowing overwrites.
    """
    return f"{base_name}.html"

def split_html_file(input_path, output_folder):
    """
    Splits a single HTML file into multiple files based on <h3> tags.
    """
    print(f"Processing: {input_path}")
    with open(input_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    html_content = html_content.replace('&nbsp;', ' ')
    
    # Split by <h3> tags, keeping the delimiter
    # The regex lookahead (?=<h3) splits before the tag, so the tag stays with the content
    parts = re.split(r'(?=<h3)', html_content)

    os.makedirs(output_folder, exist_ok=True)

    count = 0
    for part in parts:
        if not part.strip():
            continue

        h3_match = re.search(r'<h3[^>]*>(.*?)<\/h3>', part, re.DOTALL)
        if h3_match:
            h3_content = h3_match.group(1)
            # Extract the X number if possible for better sorting/naming
            # Expected format often: X(1) = ...
            x_match = re.search(r'X\((\d+)\)', h3_content)
            if x_match:
                num = x_match.group(1)
                # Pad with zeros for sorting, e.g., x-00001
                filename = f"x-{int(num):05d}"
            else:
                filename = slugify(h3_content)
            
            if not filename:
                filename = "unknown"
        else:
            # Content before the first <h3> or without <h3>
            filename = "preamble"

        output_filename = unique_filename(output_folder, filename)
        output_path = os.path.join(output_folder, output_filename)
        
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(part)
        
        count += 1
    
    print(f"  -> Split into {count} files.")

def ingest_folder(input_folder, output_folder):
    """
    Ingests all HTML files in the input folder.
    """
    input_path = Path(input_folder)
    html_files = sorted(input_path.glob('*.html'))
    
    for file_path in html_files:
        split_html_file(file_path, output_folder)

if __name__ == '__main__':
    # Default behavior for testing
    import sys
    if len(sys.argv) > 2:
        ingest_folder(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python -m geometor.etc.ingest <input_folder> <output_folder>")
