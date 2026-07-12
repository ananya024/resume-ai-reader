# gemini_service.py

import os
import json
from dotenv import load_dotenv
from google.genai import Client
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

def extract_jd(text:str):
    prompt = EXTRACT_PROMPT+text
    return generate_json(prompt)