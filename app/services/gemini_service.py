# gemini_service.py

import os
import json
from dotenv import load_dotenv
from google.genai import Client
from app.prompts.parse_prompt import PARSE_PROMPT
from app.prompts.analyze_prompt import ANALYZE_PROMPT
from app.prompts.jd_extract import EXTRACT_PROMPT

load_dotenv() 
# reads .env

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("NO API KEY!")

client= Client(api_key=api_key)
# makes a connection

def generate_json(prompt:str)->dict:
    try:
        response= client.models.generate_content(
            model="gemini-2.5-flash",
            contents= prompt
        )
        text=response.text.strip()
        if text.startswith("```json"):
            text=text.replace("```json","",1)
        if text.endswith("```"):
            text=text[:-3]
        text=text.strip()
        parsed = json.loads(text)
        return parsed
    except json.JSONDecodeError:
        return {
            "error": "Gemini returned invalid JSON.",
            "raw_response": text
        }
    except Exception as e:
        return {
            "error": str(e)
        }


def parse_resume(text:str, link:list[str]):
    link_text = "\n".join(link)
    prompt=(PARSE_PROMPT
        +text
        +"\n\nThe following hyperlinks were extracted from the PDF. Use them to populate the github, linkedin, and portfolio fields if applicable.\n\n"
        +link_text)
    return generate_json(prompt)

def analyze_json(parsed: dict):
    prompt = ANALYZE_PROMPT + json.dumps(parsed, indent=2)
    return generate_json(prompt)

def extract_jd(text:str):
    prompt = EXTRACT_PROMPT+text
    return generate_json(prompt)