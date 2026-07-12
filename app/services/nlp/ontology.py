# ontology.py

# Hierarchical skill ontology representing relations between engineering categories, concepts, and technologies.
ONTOLOGY = {
    "Software Engineering": {
        "children": ["Backend", "Frontend", "Databases", "Version Control", "Testing", "REST API", "Object-Oriented Programming", "System Design"],
        "min_children_to_match": 3
    },
    "Backend": {
        "children": ["Node.js", "Express", "NestJS", "Spring Boot", "Django", "Flask", "FastAPI"],
        "min_children_to_match": 1
    },
    "Frontend": {
        "children": ["React", "Angular", "Vue", "HTML", "CSS", "JavaScript"],
        "min_children_to_match": 1
    },
    "Databases": {
        "children": ["PostgreSQL", "MySQL", "MongoDB", "SQL", "Database Management Systems"],
        "min_children_to_match": 1
    },
    "Version Control": {
        "children": ["Git", "GitHub", "GitLab"],
        "min_children_to_match": 1
    },
    "Testing": {
        "children": ["Unit Testing", "Integration Testing", "TDD", "BDD", "Debugging"],
        "min_children_to_match": 1
    },
    "Operating Systems": {
        "children": ["Linux", "Processes", "Threads", "Scheduling", "Memory Management", "Concurrency", "Kernel"],
        "min_children_to_match": 1
    },
    "Networking": {
        "children": ["TCP/IP", "DNS", "HTTP", "HTTPS", "Routing", "Switching", "Sockets"],
        "min_children_to_match": 1
    }
}

def evaluate_ontology(skills_list):
    """
    Evaluates category matches bottom-up from a set of direct candidate skills.
    Returns a dictionary mapping ontology parent categories to boolean match indicators.
    """
    current_matches = set(skills_list)
    category_matches = {}
    
    # Run multiple propagation passes (propagating matching states up the graph)
    for _ in range(3):
        changes = False
        for parent, config in ONTOLOGY.items():
            if parent in current_matches:
                category_matches[parent] = True
                continue
                
            # Count matched children or subcategories
            matched_children = [c for c in config["children"] if c in current_matches]
            min_required = config["min_children_to_match"]
            
            if len(matched_children) >= min_required:
                current_matches.add(parent)
                category_matches[parent] = True
                changes = True
                
        if not changes:
            break
            
    # Explicitly set False for any categories that weren't matched
    for parent in ONTOLOGY.keys():
        if parent not in category_matches:
            category_matches[parent] = False
            
    return category_matches
