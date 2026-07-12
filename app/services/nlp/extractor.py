# extractor.py

import re

# Canonical single master skill dictionary containing all skills across categories
ALL_SKILLS = {
    # High-level Categories and Concepts
    "software engineering", "backend", "frontend", "databases", "version control",
    "testing", "operating systems", "networking", "os", "dbms",
    
    # Inferred Concepts & Architectures
    "backend development", "frontend development", "web development",
    "server-side development", "api development", "enterprise architecture",
    "database development", "relational databases", "nosql databases",
    "api design", "restful web services", "authentication", "authorization",
    "security", "real-time communication", "client-server architecture",
    "websockets", "devops", "containerization", "container orchestration",
    "cloud infrastructure", "cloud computing", "collaborative development",
    "ci/cd", "automation",

    # Programming Languages
    "python", "java", "c++", "c#", "c", "javascript", "typescript", "ruby", "go", "golang",
    "rust", "php", "swift", "kotlin", "scala", "r", "dart", "perl", "haskell", "objective-c",
    "bash", "shell", "powershell", "sql", "html", "css", "matlab", "assembly", "julia", "f#",
    
    # Frameworks
    "react", "reactjs", "angular", "angularjs", "vue", "vuejs", "next.js", "nextjs",
    "nuxt.js", "nuxtjs", "svelte", "node.js", "nodejs", "express", "expressjs", "django",
    "flask", "fastapi", "nestjs", "spring boot", "spring", "laravel", "asp.net", "net core",
    "ruby on rails", "rails", "jquery", "bootstrap", "tailwind", "tailwind css", "ember",
    "backbone", "meteor",
    
    # Libraries
    "pandas", "numpy", "matplotlib", "seaborn", "scikit-learn", "tensorflow", "pytorch", "keras",
    "spacy", "nltk", "opencv", "huggingface", "langchain", "stl", "scipy", "sympy",
    
    # Databases
    "postgresql", "postgres", "mysql", "sqlite", "mongodb", "redis", "oracle", "sql server",
    "cassandra", "dynamodb", "mariadb", "neo4j", "firebase", "elasticsearch", "dbms",
    "database management systems", "couchdb", "influxdb", "snowflake", "redshift",
    
    # Cloud
    "aws", "amazon web services", "azure", "microsoft azure", "gcp", "google cloud",
    "google cloud platform", "heroku", "digitalocean", "cloudflare", "openstack", "lambda",
    
    # Operating Systems Concepts
    "linux", "windows", "macos", "mac os", "unix", "ubuntu", "centos", "redhat", "red hat",
    "android", "ios", "debian", "processes", "threads", "scheduling", "memory management",
    "concurrency", "kernel",
    
    # Developer Tools
    "git", "github", "gitlab", "docker", "kubernetes", "k8s", "jenkins", "terraform",
    "ansible", "maven", "gradle", "webpack", "npm", "yarn", "pip", "postman", "jira",
    "vs code", "vscode", "intellij", "eclipse", "pycharm", "docker compose", "bitbucket",
    
    # Networking Concepts
    "tcp/ip", "dns", "http", "https", "ssh", "ftp", "vpn", "ssl", "tls", "routing",
    "switching", "load balancing", "vpc", "subnetting", "ipsec", "computer networks", 
    "computer network", "dhcp", "lan", "wan", "firewall", "firewalls", "sockets",
    
    # Engineering & CS concepts
    "data structures", "algorithms", "system design", "distributed systems",
    "microservices", "rest api", "restful api", "restful apis", "rest apis", "graphql",
    "soap", "agile", "scrum", "tdd", "bdd", "unit testing", "integration testing",
    "debugging", "multithreading", "design patterns", "version control", "database design",
    "test automation",
    
    # Soft skills
    "communication", "problem solving", "leadership", "teamwork", "collaboration",
    "critical thinking", "time management", "mentoring", "presentation", "adaptability",
    "active listening", "negotiation", "conflict resolution", "interpersonal skills",
    "organization", "work ethic", "problem-solving"
}

def extract_skills(text: str):
    """
    Extracts skills from text (works for both resume text and JD text)
    using a boundary-aware regex search against the canonical master skill dictionary.
    """
    if not text:
        return []
        
    text_lower = text.lower()
    found = set()

    for skill in ALL_SKILLS:
        # Build custom regex boundary pattern to support C++, C#, .NET, Node.js etc.
        if re.match(r'^\w', skill):
            prefix = r'\b'
        else:
            prefix = r'(?:^|(?<=\s|[,.;:!?()[\]{}]))'
            
        if re.match(r'.*\w$', skill):
            suffix = r'\b'
        else:
            suffix = r'(?:$|(?=\s|[,.;:!?()[\]{}]))'
            
        pattern = prefix + re.escape(skill) + suffix
        if re.search(pattern, text_lower):
            found.add(skill)

    return sorted(list(found))
