# experience_matcher.py

from app.services.nlp.experience_parser import extract_experience, parse_year

# Terms that signify a junior/entry-level role requiring 0 years of experience
ENTRY_LEVEL_KEYWORDS = [
    "entry level", "fresh graduate", "campus hiring", "internship", 
    "no experience", "0 years", "fresher", "intern", "graduate program"
]

def check_entry_level(text: str) -> bool:
    """
    Checks if the job description indicates an entry-level or no experience role.
    """
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in ENTRY_LEVEL_KEYWORDS)

def match_experience(resume_text: str, jd_experience_text: str) -> dict:
    """
    Compares candidate experience against JD experience required:
    1. Extracts candidate experience years using regex.
    2. Parses required experience, returning 0 if entry-level.
    3. Computes the match status, reason, and score.
    """
    # 1. Candidate years
    resume_exp = extract_experience(resume_text)
    resume_mentions = resume_exp["experience_mentions"]
    resume_years = (max(parse_year(x) for x in resume_mentions) if resume_mentions else 0)
    
    # 2. Required years
    jd_years = 0
    is_entry_level = False
    
    if jd_experience_text:
        # Check if entry level indicators are present
        if check_entry_level(jd_experience_text):
            is_entry_level = True
            jd_years = 0
        else:
            # Extract required years using parser regex
            jd_exp_extracted = extract_experience(jd_experience_text)
            if jd_exp_extracted["experience_mentions"]:
                jd_years = max(parse_year(x) for x in jd_exp_extracted["experience_mentions"])
            else:
                # Fallback to direct parsing if it is just a number like "3"
                jd_years = parse_year(jd_experience_text)
                
    # 3. Match checking and score computation
    matched = resume_years >= jd_years
    
    if jd_years == 0 or is_entry_level:
        matched = True
        score = 100.0
        reason = f"Entry level role. Candidate has {resume_years} years of experience."
    elif matched:
        score = 100.0
        reason = f"Candidate has {resume_years} years of experience, satisfying the required {jd_years} years."
    else:
        score = (resume_years / jd_years) * 100.0 if jd_years else 0.0
        reason = f"Candidate has {resume_years} years of experience, which is less than the required {jd_years} years."
        
    return {
        "resume_years": resume_years,
        "required_years": jd_years,
        "matched": matched,
        "reason": reason,
        "score": round(score, 2)
    }
