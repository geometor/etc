import os
import glob
import json
import re
from rich import print


def parse_coordinates(coord_type, s):
    coordinates = re.findall(rf"{coord_type}\s+(.+?)\s*<br>", s)
    coordinates_split = []
    for coord in coordinates:
        note = ''
        if ',' in coord:
            values, note = coord.split(",", 1)
        else:
            values = coord
        values = values.split(":")
        values = [value.strip() for value in values]
        coordinates_split.append({"values": values, "note": note.strip()})
    return coordinates_split


def parse_trilinears(s):
    return parse_coordinates("Trilinears", s)


def parse_barycentrics(s):
    return parse_coordinates("Barycentrics", s)


def parse_tripolars(s):
    return parse_coordinates("Tripolars", s)


def parse_algebraic_expressions(s):
    # get first b block
    expressions = re.findall(r"<b>(.*?)</b>", s, re.DOTALL)
    if expressions:
        expressions = expressions[0]
        if '<br>' in expressions:
            expressions = expressions[0].split('<br>')
        else:
            expressions = [expressions]
        expressions = [exp.strip() for exp in expressions]
        parsed_expressions = []
        for exp in expressions:
            note = ''
            if ',' in exp:
                exp, note = exp.split(",", 1)
            parsed_expressions.append({'expression': exp, 'note': note.strip()})

        return parsed_expressions


def parse_notes(s):
    notes = re.findall(r"<p>(.*?)</p>", s, re.DOTALL)
    #  return [note.strip().replace("<br>\n", "\n") for note in notes]
    return [note.strip() for note in notes]


def remove_tags(text):
    return re.sub('<[^>]+>', '', text)

def parse_h3(s):
    title = re.findall(r'<h3[^>]*>(.*?)<\/h3>', s, re.DOTALL)[0]
    title = remove_tags(title)
    #  title = re.findall(r"<h3.*>(.*?)</h3>", s, re.DOTALL)[0]
    #  title = title.replace('&nbsp;', ' ')
    key = ''
    if '=' in title:
        key, title = title.strip().split('=', 1)
    return key.strip(), title.strip()


def parse_relations(notes):
    #relations are in the last note and all start with 'X(n) ='
    if not notes:
        return

    relations = notes[-1]
    relations = relations.split('<br>\n')
    for i in range(len(relations)):
        relation = relations[i].strip()
        if '=' in relation:
            key, relation = relation.split('=', 1)
        relations[i] = relation.strip()

    return relations


def parse_html(html):
    html = html.replace('&nbsp;', ' ')
    key, title = parse_h3(html)
    notes = parse_notes(html)
    relations = parse_relations(notes)
    notes = notes[:-1]

    parsed_data = {
            'key': key,
            "title": title,
            "trilinears": parse_trilinears(html),
            "barycentrics": parse_barycentrics(html),
            "tripolars": parse_tripolars(html),
            "algebraic_expressions": parse_algebraic_expressions(html),
            'relations': relations,
            "notes": notes,
            }

    return parsed_data


def read_files_with_prefix(folder, prefix):
    files_with_prefix = glob.glob(os.path.join(folder, f'{prefix}*.html'))

    max = 10
    i = 1

    for file_path in files_with_prefix:
        print(file_path)

        with open(file_path, 'r', encoding='utf-8') as file:
            file_contents = file.read()
            parsed_data = parse_html(file_contents)

        with open(file_path + '.json', "w") as outfile:
            json.dump(parsed_data, outfile, indent=4)
        if i > max:
            break
        else:
            i += 1

if __name__ == '__main__':
    folder = 'test'
    prefix = 'x-'
    read_files_with_prefix(folder, prefix)

