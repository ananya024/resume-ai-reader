# analyze_service.py

from app.services.pdf_reader import read_pdf
from app.services.gemini_service import parse_resume, analyze_json

def analyze_resume(path:str):
    text,links= read_pdf(path)
    parsed= parse_resume(text, links)

    if "error" in parsed:
        return {
            "parsed_resume": parsed,
            "analysis": None
        }

    analyzed = analyze_json(parsed)

    return {
        "parsed_resume": parsed,
        "analysis": analyzed
    }