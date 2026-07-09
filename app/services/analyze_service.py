# analyze_service.py

from app.services.pdf_reader import read_pdf
from app.services.gemini_service import parse_resume, analyze_json
from app.services.SAMPLE_RESPONSE import SAMPLE_RESPONSE

def analyze_resume(path:str):
    text,links= read_pdf(path)
    return SAMPLE_RESPONSE
    parsed= parse_resume(text, links)

    if "error" in parsed:
        return SAMPLE_RESPONSE

    analyzed = analyze_json(parsed)

    if(analyzed):
        return {parsed, analyzed}
    else:
        return SAMPLE_RESPONSE