# education_matcher.py

# Numeric ranks for comparing degree levels bottom-up
DEGREE_LEVELS = {
    "phd": 3,
    "doctorate": 3,
    "master": 2,
    "ms": 2,
    "mtech": 2,
    "bachelor": 1,
    "btech": 1,
    "be": 1,
    "bs": 1,
    "diploma": 0
}

def extract_degree_level(text: str):
    """
    Extracts the highest degree level mentioned in the text.
    Returns (canonical_name, numeric_rank).
    """
    text_lower = text.lower()
    
    # PhD
    if any(x in text_lower for x in ["phd", "ph.d", "doctorate"]):
        return "PhD", 3
        
    # Master's
    if any(x in text_lower for x in ["master", "ms", "mtech", "m.tech", "m.s.", "mba"]):
        return "Master", 2
        
    # Bachelor's
    if any(x in text_lower for x in ["bachelor", "btech", "b.tech", "be", "b.e.", "bs", "b.s.", "bsc", "b.sc"]):
        return "Bachelor", 1
        
    # Diploma
    if "diploma" in text_lower:
        return "Diploma", 0
        
    return "None", -1

def match_field_of_study(resume_text: str, jd_text: str) -> bool:
    """
    Checks if the field of study in the resume matches the JD requirement.
    Uses normalization and containment logic.
    """
    resume_lower = resume_text.lower()
    jd_lower = jd_text.lower()
    
    # If JD does not specify any field of study, it is a default match
    field_keywords = ["computer science", "cs", "cse", "engineering", "math", "statistics", "science", "physics"]
    if not any(k in jd_lower for k in field_keywords):
        return True
        
    # Standard Computer Science matches
    if any(x in jd_lower for x in ["computer science", "cs", "cse"]):
        # Check if resume contains CS, AI/ML, or IT
        cs_aliases = [
            "computer science", "cs", "cse", "computer engineering", 
            "information technology", "it", "artificial intelligence", 
            "ai", "ml", "machine learning"
        ]
        if any(x in resume_lower for x in cs_aliases):
            return True
            
    # Category alias mapping checks
    field_aliases = {
        "computer science": ["computer science", "cs", "cse", "computer engineering", "it"],
        "data science": ["data science", "data analytics", "statistics"],
        "artificial intelligence": ["artificial intelligence", "ai", "machine learning", "ml"]
    }
    
    for key, aliases in field_aliases.items():
        if any(a in jd_lower for a in aliases):
            if any(a in resume_lower for a in aliases):
                return True
                
    # Direct substring word intersection fallback
    words = [w for w in jd_lower.split() if len(w) > 3 and w not in ["degree", "required", "preferred", "minimum"]]
    for w in words:
        if w in resume_lower:
            return True
            
    return False

def match_education(resume_edu: str, jd_edu: str) -> dict:
    """
    Compares resume education section against the JD education required.
    Normalizes levels/fields and outputs a detailed score and explanation.
    """
    if not jd_edu or jd_edu.strip() == "":
        return {
            "resume": resume_edu.strip() if resume_edu else "Not Specified",
            "required": "Not Specified",
            "matched": True,
            "reason": "No education requirements specified in the job description.",
            "score": 100.0
        }
        
    if not resume_edu or resume_edu.strip() == "":
        return {
            "resume": "Not Specified",
            "required": jd_edu.strip(),
            "matched": False,
            "reason": "Resume does not contain education details to verify against requirements.",
            "score": 0.0
        }

    # Extract degree levels
    jd_degree, jd_rank = extract_degree_level(jd_edu)
    res_degree, res_rank = extract_degree_level(resume_edu)
    
    # Degree match checks
    degree_matched = False
    if jd_rank == -1:
        # No explicit degree level requirement (e.g. "Computer Science background preferred")
        degree_matched = True
    elif res_rank >= jd_rank:
        # Candidate meets or exceeds the required level (e.g., Master satisfies Bachelor)
        degree_matched = True
        
    # Field of study match checks
    field_matched = match_field_of_study(resume_edu, jd_edu)
    
    matched = degree_matched and field_matched
    score = 100.0 if matched else (50.0 if degree_matched or field_matched else 0.0)
    
    # Construct explanation reason
    if matched:
        reason = f"B.Tech/Bachelor satisfies required degree level '{jd_degree}' and fields of study align."
    elif degree_matched:
        reason = f"Degree level satisfies requirements, but the field of study does not match."
    elif field_matched:
        reason = f"Field of study aligns, but degree level is lower than the required '{jd_degree}'."
    else:
        reason = f"Neither the degree level nor the field of study matches the required '{jd_edu}'."
        
    return {
        "resume": resume_edu.strip(),
        "required": jd_edu.strip(),
        "matched": matched,
        "reason": reason,
        "score": score
    }
