from __future__ import annotations
import re
import json

def remove_tags(text: str) -> str:
    """
    Remove HTML tags from text.

    Args:
        text (str): The input text with HTML tags.

    Returns:
        str: The text with tags removed.
    """
    return re.sub('<[^>]+>', '', text)

def clean_text(text: str) -> str:
    """
    Clean up text by removing tags and extra whitespace.

    Args:
        text (str): The input text.

    Returns:
        str: The cleaned text.
    """
    if not text:
        return ""
    text = text.replace('<br>', ' ').replace('<BR>', ' ')
    text = remove_tags(text)
    text = text.replace('&nbsp;', ' ')
    return " ".join(text.split())

def parse_coordinates(coord_type: str, html: str) -> list[str]:
    """
    Parse coordinates (Trilinears, Barycentrics, etc.) from the HTML.

    Args:
        coord_type (str): The type of coordinates to look for (e.g., "Trilinears").
        html (str): The HTML content to search.

    Returns:
        list: A list of parsed coordinate strings.
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

def parse_h3(html: str) -> tuple[str | None, str | None]:
    """
    Parse the <h3> tag to get the key (X number) and title.

    Args:
        html (str): The HTML content.

    Returns:
        tuple: A tuple containing the key (e.g., "X(1)") and the title.
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

def parse_notes(html: str) -> list[str]:
    """
    Extract paragraphs as notes.

    Args:
        html (str): The HTML content.

    Returns:
        list: A list of note strings.
    """
    # Find all <p> tags
    notes = re.findall(r"<p>(.*?)</p>", html, re.DOTALL)
    cleaned_notes = [clean_text(note) for note in notes]
    return cleaned_notes

def parse_center(html_content: str) -> dict | None:
    """
    Parse a center's HTML content into a structured dictionary.

    Args:
        html_content (str): The HTML content of the center definition.

    Returns:
        dict: A dictionary containing center data (key, title, coordinates, notes), or None if parsing fails.
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
