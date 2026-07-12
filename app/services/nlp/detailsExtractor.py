# detailsExtractor.py

import re

EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
PHONE_PATTERN = r"(\+?\d[\d\s\-]{8,}\d)"

def extract_details(text: str, links: list):

    details = {
        "name": "",
        "email": "",
        "phone": "",
        "location": "",
        "linkedin": "",
        "github": "",
        "portfolio": ""
    }

    email = re.search(EMAIL_PATTERN, text)
    if email:
        details["email"] = email.group()

    phone = re.search(PHONE_PATTERN, text)
    if phone:
        details["phone"] = phone.group().strip()

    for link in links:
        lower = link.lower()

        if "linkedin.com" in lower:
            details["linkedin"] = link

        elif "github.com" in lower:
            details["github"] = link

        else:
            details["portfolio"] = link

    lines = [line.strip() for line in text.split("\n") if line.strip()]

    for line in lines[:8]:

        if details["email"] and details["email"] in line:
            continue

        if details["phone"] and details["phone"] in line:
            continue

        if "linkedin" in line.lower():
            continue

        if "github" in line.lower():
            continue

        if len(line.split()) >= 2 and len(line.split()) <= 4:
            details["name"] = line
            break

    return details