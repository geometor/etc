import re
from bs4 import BeautifulSoup

def extract_glossary_terms(html_content):
    """
    Extracts glossary terms and definitions from the HTML content.
    Returns a dictionary {term: definition_rst}.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    terms = {}
    
    # Find all h2 elements, as they seem to contain the terms
    for h2 in soup.find_all('h2'):
        term = h2.get_text().strip()
        
        # Skip empty terms or specific headers if any
        if not term:
            continue
            
        # The definition follows the h2
        definition_parts = []
        for sibling in h2.find_next_siblings():
            if sibling.name == 'h2':
                break
            # Convert HTML to simple RST (basic text for now, maybe improve later)
            text = sibling.get_text().strip()
            if text:
                definition_parts.append(text)
        
        definition = "\n\n".join(definition_parts)
        terms[term] = definition
        
    return terms

def generate_glossary_rst(terms):
    """
    Generates the content for glossary.rst.
    """
    rst = ":navigation: header footer\n:order: 2\n\n"
    rst += "Glossary\n========\n\n"
    rst += ".. glossary::\n\n"
    
    for term in sorted(terms.keys()):
        definition = terms[term]
        # Indent definition
        indented_def = "\n    ".join(definition.splitlines())
        rst += f"   {term}\n    {indented_def}\n\n"
        
    return rst

def wrap_glossary_terms(text, terms):
    """
    Wraps occurrences of glossary terms in the text with :term:`term`.
    terms is a list of strings.
    """
    # Sort terms by length descending to match longest phrases first
    sorted_terms = sorted(terms, key=len, reverse=True)
    
    # Create a regex pattern
    # We want to match whole words/phrases, case-insensitive?
    # The glossary terms are usually lowercase in text, but capitalized in headers.
    # Let's assume case-insensitive matching but preserve original case in text?
    # Or just use the term as defined.
    
    # For efficiency and to avoid nested replacements, we can use a single regex
    # But we need to be careful about not replacing inside existing tags or links.
    # For now, simple replacement on the text.
    
    # Escape terms for regex
    escaped_terms = [re.escape(t) for t in sorted_terms]
    pattern = re.compile(r'\b(' + '|'.join(escaped_terms) + r')\b', re.IGNORECASE)
    
    def replace_func(match):
        matched_text = match.group(0)
        # Find the canonical term (case-insensitive match)
        # This is slow if we iterate. 
        # But we can just use the matched text as the label if we want, 
        # or we need to find the actual term key.
        # :term:`matched_text <Actual Term>`
        
        # Find the actual term key that matches
        lower_matched = matched_text.lower()
        actual_term = next((t for t in terms if t.lower() == lower_matched), None)
        
        if actual_term:
             return f":term:`{matched_text} <{actual_term}>`"
        return matched_text

    return pattern.sub(replace_func, text)
