# skill_inference.py

from app.services.nlp.extractor import extract_skills

# Inference mapping rules matching lowercase keyword to list of inferred concepts/skills
INFERENCE_RULES = {
    "react": ["Frontend Development", "Web Development"],
    "angular": ["Frontend Development", "Web Development"],
    "vue": ["Frontend Development", "Web Development"],
    "node.js": ["Backend Development", "Server-Side Development"],
    "express": ["Backend Development", "API Development"],
    "nestjs": ["Backend Development", "API Development"],
    "spring boot": ["Backend Development", "Server-Side Development"],
    "django": ["Backend Development", "Web Development"],
    "flask": ["Backend Development", "Web Development"],
    "fastapi": ["Backend Development", "API Development"],
    "postgresql": ["Database Development", "Relational Databases"],
    "mysql": ["Database Development", "Relational Databases"],
    "mongodb": ["Database Development", "NoSQL Databases"],
    "sqlite": ["Database Development", "Relational Databases"],
    "rest api": ["API Design", "REST API", "Backend Development"],
    "jwt": ["Authentication", "Authorization", "Security"],
    "socket.io": ["Client-Server Architecture", "Real-Time Communication"],
    "websockets": ["Client-Server Architecture", "Real-Time Communication"],
    "docker": ["DevOps", "Containerization"],
    "kubernetes": ["DevOps", "Container Orchestration", "Cloud Infrastructure"],
    "aws": ["Cloud Infrastructure", "Cloud Computing"],
    "gcp": ["Cloud Infrastructure", "Cloud Computing"],
    "azure": ["Cloud Infrastructure", "Cloud Computing"],
    "git": ["Version Control", "Collaborative Development"],
    "github": ["Version Control", "Collaborative Development"],
    "jenkins": ["CI/CD", "DevOps", "Automation"]
}

def infer_skills_from_text(text: str) -> list[str]:
    """
    Scans the text (such as a project description) for explicit skills and
    infers associated high-level skills, concepts, and architectures.
    """
    if not text:
        return []
        
    # Extract explicit skills first using our regex boundary extractor
    explicit_skills = extract_skills(text)
    inferred = set()
    
    # Check rules against explicit skills (case-insensitive key match)
    for skill in explicit_skills:
        skill_lower = skill.lower()
        if skill_lower in INFERENCE_RULES:
            for inf_skill in INFERENCE_RULES[skill_lower]:
                inferred.add(inf_skill)
                
    # Logic rule checks on combinations of skills
    has_frontend = "Frontend Development" in inferred
    has_backend = "Backend Development" in inferred
    has_db = "Database Development" in inferred
    
    if has_frontend and has_backend:
        inferred.add("Software Engineering")
        inferred.add("Full Stack Development")
        
    if has_backend and has_db:
        inferred.add("Database Design")
        
    return sorted(list(inferred))
