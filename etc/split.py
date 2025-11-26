import re
import os
import glob


def slugify(text):
    return re.sub(r'\W+', '-', text.lower()).strip('-')


def unique_filename(output_folder, base_name):
    counter = 1
    file_name = base_name
    while os.path.exists(os.path.join(output_folder, file_name)):
        file_name = f"{base_name}-{counter}.html"
        counter += 1
    return file_name


def split_html_files(input_folder, output_folder):
    html_files = glob.glob(os.path.join(input_folder, '*.html'))

    os.makedirs(output_folder, exist_ok=True)

    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Replace all &nbsp; occurrences with a space
        html_content = html_content.replace('&nbsp;', ' ')

        h3_parts = re.split(r'(?=<h3)', html_content)

        for part in h3_parts:
            h3_title_match = re.search(r'<h3[^>]*>(.*?)<\/h3>', part)
            if h3_title_match:
                h3_title = h3_title_match.group(1)
                output_file_name = slugify(h3_title) + '.html'
            else:
                # Ensure unique filename for parts without valid h3 text
                output_file_name = unique_filename(output_folder, '_')

            output_path = os.path.join(output_folder, output_file_name)
            with open(output_path, 'w', encoding='utf-8') as output_file:
                print(output_file_name)
                output_file.write(part)


if __name__ == '__main__':
    input_folder = 'source'
    output_folder = 'split'
    split_html_files(input_folder, output_folder)

