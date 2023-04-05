import os
import re
import copy
from bs4 import BeautifulSoup
from slugify import slugify
from rich import print, inspect

def make_safe_filename(title):
    #  safe_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    #  safe_title = ''.join(c for c in title if c in safe_chars)
    return slugify(title)


def split_html_file(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html5lib')
    #  print(soup)
    head = soup.head
    print(head)
    print(soup.body)
    hr_elements = soup.find_all('hr')
    print(hr_elements)
    print(len(hr_elements))
    breakpoint()

    if not hr_elements:
        print("No <hr> tags found in the document.")
        return

    # Add a dummy <hr> at the end to include the last section
    last_hr = soup.new_tag('hr')
    soup.body.append(last_hr)

    base_name, _ = os.path.splitext(input_file)
    os.makedirs(base_name, exist_ok=True)

    start = soup.body
    for index, hr in enumerate(hr_elements):
        # Extract the content between the <hr> tags
        content = []
        for elem in start.find_next_siblings():
            if len(hr_elements) == index + 1:
                break

            if elem is hr_elements[index+1]:
                break
            content.append(elem.extract())

        if content:
            # Find the first h tag
            first_h = content[0].find(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

            if first_h:
                title = first_h.text
            else:
                title = f"Part {index+1}"

            safe_filename = make_safe_filename(title)
            output_file = os.path.join(base_name, f"{index:05}-{safe_filename}.html")

            # Create a new soup for the output file
            new_soup = BeautifulSoup("<!DOCTYPE html><html></html>", 'html.parser')
            #  inspect(new_soup)
            new_head = copy.copy(head)
            new_soup.html.append(new_head)  # Use a copy of the head to avoid modifying the original
            new_soup.html.append(soup.new_tag('body'))

            # Set the title in the <head> using the title from the first_h tag
            new_soup.title = title

            for elem in content:
                new_soup.body.append(elem)

            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(str(new_soup))

            print(f'{title=}')
            print(f'{output_file=}')
            print()
            

        # Update the start position for the next iteration
        start = hr

    # Clean up by removing the dummy <hr> tag
    soup.body.hr.decompose()

if __name__ == "__main__":
    filename = "./faculty.evansville.edu/ck6/encyclopedia/ETC.html"

    split_html_file(filename)
