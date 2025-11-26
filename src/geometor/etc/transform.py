import os
import re
from .glossary import wrap_glossary_terms


def format_rst_header(title, char='='):
    """
    Create an RST header.
    """
    line = char * len(title)
    return f"{title}\n{line}\n\n"

def wrap_refs(text):
    """
    Wrap X(n) references in :ref:`X.n`.
    """
    # Pattern to match X(n) where n is a number
    # We use a negative lookbehind to avoid double wrapping if already wrapped (though simple regex might suffice for raw text)
    # And we want to avoid matching the title definition itself if possible, but usually that's handled by context.
    # For now, simple substitution: X(1) -> :ref:`X.1`
    
    def replace_func(match):
        num = match.group(1)
        return f":ref:`X({num}) <X({num})>`"
        
    return re.sub(r'X\((\d+)\)', replace_func, text)

def transform_center_to_rst(data, glossary_terms=None):
    """
    Transform a center data dictionary into an RST string.
    """
    if not data or not data.get('key'):
        return ""

    key = data['key']
    title = data['title']
    
    # Extract number from key X(n)
    try:
        num = int(key.replace('X(', '').replace(')', ''))
    except ValueError:
        num = 0

    rst = ""
    
    # Metadata
    rst += f":order: {num}\n"
    rst += ":type: center\n\n"
    
    # Anchor
    rst += f".. _X({num}):\n\n"
    
    # Title: X(n) = Name
    full_title = f"{key} = {title}" if title else key
    rst += format_rst_header(full_title, '=')
    
    # Coordinates
    if data.get('trilinears'):
        rst += "**Trilinears**\n\n"
        for item in data['trilinears']:
            # Wrap refs in coordinates too if they appear? 
            # Usually coordinates are math, so maybe not inside math blocks.
            # But if they are text descriptions, yes.
            # For now, let's assume they might contain refs.
            item = wrap_refs(item)
            rst += f":math:`{item}`\n\n"
            
    if data.get('barycentrics'):
        rst += "**Barycentrics**\n\n"
        for item in data['barycentrics']:
            item = wrap_refs(item)
            rst += f":math:`{item}`\n\n"

    # Notes
    if data.get('notes'):
        rst += "**Notes**\n\n"
        for note in data['notes']:
            # Ensure X(n) = starts on a new line
            note = re.sub(r'(X\(\d+\)\s*=)', r'\n\n\1', note)
            
            note = wrap_refs(note)
            if glossary_terms:
                note = wrap_glossary_terms(note, glossary_terms)
            rst += f"{note}\n\n"
            
    return rst

def generate_rst_files(centers, output_dir, glossary_terms=None):
    """
    Generate RST files for a list of centers.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Index using collection directive
    index_content = ":navigation: header footer\n:order: 1\n\n"
    index_content += format_rst_header("Encyclopedia of Triangle Centers", "=")
    index_content += ".. collection::\n   :type: center\n   :sort: order\n"
    
    for center in centers:
        if not center:
            continue
            
        key = center['key']
        try:
            num = int(key.replace('X(', '').replace(')', ''))
            filename = f"x-{num:05d}.rst"
        except ValueError:
            filename = f"{key}.rst"
            
        filepath = os.path.join(output_dir, filename)
        
        rst_content = transform_center_to_rst(center, glossary_terms)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(rst_content)

    # Write index.rst
    with open(os.path.join(output_dir, "index.rst"), 'w', encoding='utf-8') as f:
        f.write(index_content)
