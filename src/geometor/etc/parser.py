import re
import json

def remove_tags(text):
    """Remove HTML tags from text."""
    return re.sub('<[^>]+>', '', text)

def clean_text(text):
    """Clean up text by removing tags and extra whitespace."""
    if not text:
        return ""
    text = text.replace('<br>', ' ').replace('<BR>', ' ')
    text = remove_tags(text)
    text = text.replace('&nbsp;', ' ')
    return " ".join(text.split())

def parse_coordinates(coord_type, html):
    """
    Parse coordinates (Trilinears, Barycentrics, etc.) from the HTML.
    Looks for patterns like "Trilinears ... <br>"
    """
    # Regex to find the line starting with the coord_type
    # It captures everything until the next <br> or end of string
    pattern = rf"{coord_type}\s+(.+?)(?:<br>|$)"
    matches = re.findall(pattern, html, re.IGNORECASE | re.DOTALL)
    
    parsed_coords = []
    for match in matches:
        # Sometimes there are multiple sets or notes
        # We'll try to split by comma if it looks like a list of values, 
        # but often it's a formula.
        # For now, we store the raw string but cleaned up.
        cleaned = clean_text(match)
        parsed_coords.append(cleaned)
        
    return parsed_coords

def parse_h3(html):
    """
    Parse the <h3> tag to get the key (X number) and title.
    """
    match = re.search(r'<h3[^>]*>(.*?)<\/h3>', html, re.DOTALL)
    if not match:
        return None, None
    
    content = match.group(1)
    content = content.replace('&nbsp;', ' ')
    clean_content = remove_tags(content).strip()
    
    # Try to extract X(n)
    key_match = re.search(r'X\((\d+)\)', clean_content)
    key = f"X({key_match.group(1)})" if key_match else ""
    
    # Title is the rest
    if '=' in clean_content:
        _, title = clean_content.split('=', 1)
        title = title.strip()
    else:
        title = clean_content
        
    return key, title

def parse_notes(html):
    """
    Extract paragraphs as notes.
    """
    # Find all <p> tags
    notes = re.findall(r"<p>(.*?)</p>", html, re.DOTALL)
    cleaned_notes = [clean_text(note) for note in notes]
    return cleaned_notes

def parse_center(html_content):
    """
    Main function to parse a center's HTML content.
    """
    key, title = parse_h3(html_content)
    
    if not key:
        # If no key found, it might not be a center definition
        return None

    data = {
        'key': key,
        'title': title,
        'trilinears': parse_coordinates("Trilinears", html_content),
        'barycentrics': parse_coordinates("Barycentrics", html_content),
        'tripolars': parse_coordinates("Tripolars", html_content),
        'notes': parse_notes(html_content),
        # 'raw': html_content # Optional: keep raw for debugging
    }
    
    return data
