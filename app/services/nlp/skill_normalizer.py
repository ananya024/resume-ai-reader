# skill_normalizer.py

# Normalization mapping for standardizing skill aliases. Easy to extend.
NORMALIZATION_MAPPING = {
    "js": "JavaScript",
    "javascript": "JavaScript",
    "node": "Node.js",
    "nodejs": "Node.js",
    "node.js": "Node.js",
    "restful apis": "REST API",
    "restful api": "REST API",
    "rest apis": "REST API",
    "rest api": "REST API",
    "postgres": "PostgreSQL",
    "postgresql": "PostgreSQL",
    "postgresql database": "PostgreSQL",
    "oop": "Object-Oriented Programming",
    "object oriented programming": "Object-Oriented Programming",
    "object-oriented programming": "Object-Oriented Programming",
    "os": "Operating Systems",
    "operating systems": "Operating Systems",
    "operating system": "Operating Systems",
    "cn": "Computer Networks",
    "computer networks": "Computer Networks",
    "computer network": "Computer Networks",
    "dbms": "Database Management Systems",
    "database management systems": "Database Management Systems",
    "reactjs": "React",
    "react": "React",
    "aws": "AWS",
    "amazon web services": "AWS",
    "gcp": "GCP",
    "google cloud platform": "GCP",
    "google cloud": "GCP",
    "azure": "Azure",
    "microsoft azure": "Azure",
    "k8s": "Kubernetes",
    "kubernetes": "Kubernetes",
    "git": "Git",
    "github": "Git",
    "gitlab": "Git",
    "golang": "Go",
    "go": "Go",
    "mac os": "macOS",
    "macos": "macOS",
    "vs code": "VS Code",
    "vscode": "VS Code"
}

def normalize_skill(skill: str) -> str:
    """
    Normalizes a skill string to its canonical form.
    If no canonical mapping exists, returns standard title case or uppercase acronym.
    """
    if not skill:
        return ""
        
    skill_clean = skill.strip().lower()
    
    # Try mapping
    if skill_clean in NORMALIZATION_MAPPING:
        return NORMALIZATION_MAPPING[skill_clean]
        
    # Upper-case acronyms (e.g. SQL, XML, HTML, CSS, BDD, TDD, VPN, DNS, VPC, SSL, TLS)
    if len(skill_clean) <= 4 and skill_clean.isalpha():
        return skill_clean.upper()
        
    # Default is title case
    return skill.strip().title()
