# section_extractor.py

# nlp_service.py

import re

SECTION_HEADERS = {
    "skills": ["skills", "technical skills", "technologies"],
    "experience": ["experience", "work experience", "employment"],
    "projects": ["projects", "project"],
    "education": ["education", "academic background", "qualification"],
    "certifications": ["certifications", "certification", "licenses"],
    "achievements": ["achievements", "awards"],
}


JD_HEADERS = {
    "skills": [
        "required skills",
        "technical skills",
        "skills",
        "key skills",
        "core skills",
        "must have skills",
        "preferred skills",
        "desired skills"
    ],

    "experience": [
        "experience",
        "work experience",
        "professional experience",
        "responsibilities",
        "key responsibilities",
        "roles and responsibilities",
        "job responsibilities",
        "what you'll do",
        "what you will do"
    ],

    "education": [
        "education",
        "qualifications",
        "minimum qualifications",
        "preferred qualifications",
        "academic qualifications"
    ],

    "certifications": [
        "certifications",
        "required certifications",
        "preferred certifications"
    ],

    "requirements": [
        "requirements",
        "minimum requirements",
        "job requirements",
        "eligibility",
        "essential requirements"
    ],

    "benefits": [
        "benefits",
        "perks",
        "what we offer",
        "why join us"
    ],

    "about_company": [
        "about us",
        "company overview",
        "who we are",
        "about the company"
    ]
}

def extract_resume_sections(text:str):
    lines=text.split("\n")
    lines = [line.strip() for line in lines if line.strip()]
    sections={}
    current_section = "other"
    sections[current_section]=[]

    for line in lines:
        clean_line= line.lower()
        found=False

        for section, headings in SECTION_HEADERS.items():
            for heading in headings:
                if heading in clean_line:
                    current_section = section
                    if current_section not in sections:
                        sections[current_section]=[]
                    found = True
                    break
        if found:
            continue

        sections[current_section].append(line)

    for section in sections:
        sections[section]= " ".join(sections[section])

    return sections

def extract_jd_sections(text:str):
    lines= text.split("\n")
    lines=[line.strip() for line in lines if line.strip()]

    sections ={}
    current_section="other"
    sections[current_section]=[]

    for line in lines:
        clean_line = line.lower()
        found= False
        for section, headings in JD_HEADERS.items():
            for heading in headings:
                if heading in clean_line:
                    current_section=section
                    if current_section not in sections:
                        sections[current_section]=[]
                    found = True
                    break
            if found:
                break
        if found:
            continue

        sections[current_section].append(line)

    for section in sections:
        sections[section]= " ".join(sections[section])
    return sections