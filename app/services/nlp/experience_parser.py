# experience_parser.py

import re

def extract_experience(text: str):
    """
    Extracts experience mentions and minimum experience from text using regex.
    """
    if not text:
        return {
            "experience_mentions": [],
            "minimum_experience": None
        }
        
    pattern = r'(\d+(?:\s*-\s*\d+)?\+?)\s*(?:years?|yrs?)\b'
    matches = re.findall(pattern, text, re.IGNORECASE)
    return {
        "experience_mentions": matches,
        "minimum_experience": matches[0] if matches else None
    }

def parse_year(value: str) -> int:
    """
    Parses a string representation of years of experience to an integer.
    E.g., "5+" -> 5, "3-5" -> 5, "2" -> 2.
    """
    if not value:
        return 0
        
    value_clean = value.replace(" ", "").replace("+", "")
    
    try:
        if "-" in value_clean:
            return int(value_clean.split("-")[-1])  # Use upper bound
        return int(value_clean)
    except ValueError:
        # Graceful fallback in case of unexpected text formatting
        return 0
