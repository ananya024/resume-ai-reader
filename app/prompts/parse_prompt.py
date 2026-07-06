# parse_prompt.py
PARSE_PROMPT="""
    You are an expert resume parser.

    Your task is to extract structured information from the resume provided below.

    Rules:

    1. Return ONLY valid JSON.
    2. Do NOT include markdown.
    3. Do NOT wrap the JSON inside triple backticks.
    4. Do NOT add explanations.
    5. If a field is unavailable, return null.
    6. If a list is unavailable, return an empty array [].
    7. Preserve the wording from the resume whenever possible.
    8. Do not invent information.
    9. Extract all information exactly as written.

    Return the following JSON schema:

    {
    "name": "",
    "email": "",
    "phone": "",
    "location": "",
    "linkedin": "",
    "github": "",
    "portfolio": "",

    "professional_summary": "",

    "skills": {
        "programming_languages": [],
        "frameworks": [],
        "libraries": [],
        "databases": [],
        "tools": [],
        "cloud": [],
        "other": []
    },

    "education": [
        {
        "institution": "",
        "degree": "",
        "field_of_study": "",
        "start_date": "",
        "end_date": "",
        "cgpa": ""
        }
    ],

    "experience": [
        {
        "company": "",
        "position": "",
        "location": "",
        "start_date": "",
        "end_date": "",
        "description": []
        }
    ],

    "projects": [
        {
        "title": "",
        "technologies": [],
        "description": []
        }
    ],

    "certifications": [
        {
        "name": "",
        "issuer": "",
        "date": ""
        }
    ],

    "achievements": [],

    "languages": [],

    "interests": []
    }

    Resume:
"""