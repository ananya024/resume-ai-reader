# project_matcher.py

import numpy as np
from app.services.nlp.embedding_service import generate_embedding
from app.services.nlp.similarity_service import calculate_similarities

def split_projects(projects_text: str) -> list[str]:
    """
    Splits the projects section of a resume into individual project descriptions.
    """
    if not projects_text:
        return []
    
    # Normalize newlines
    normalized = projects_text.replace("\r\n", "\n").strip()
    
    # Split by double newlines first (common for paragraphs)
    paragraphs = [p.strip() for p in normalized.split("\n\n") if p.strip()]
    
    if len(paragraphs) <= 1:
        # Try splitting by single newlines and look for header lines
        lines = [line.strip() for line in normalized.split("\n") if line.strip()]
        projects = []
        current = []
        for line in lines:
            # If line is short and does not start with bullet, treat as header
            if not line.startswith(('-', '*', '•', '1', '2', '3', '4', '5')) and len(line) < 60:
                if current:
                    projects.append("\n".join(current))
                    current = []
            current.append(line)
        if current:
            projects.append("\n".join(current))
        return [p for p in projects if p.strip()]
        
    return paragraphs

def match_projects(projects_text: str, responsibilities: list[str]) -> dict:
    """
    Compares individual projects against individual JD responsibilities.
    Computes a similarity matrix, maps project strengths, and lists missing themes.
    """
    projects = split_projects(projects_text)
    
    if not projects or not responsibilities:
        return {
            "matched_topics": [],
            "missing_topics": responsibilities,
            "top_matches": [],
            "similarity": 0.0,
            "reason": "No projects or responsibilities found to match.",
            "score": 0.0
        }
        
    # Generate embeddings for each project and responsibility statement
    proj_embeddings = [generate_embedding(p) for p in projects]
    resp_embeddings = [generate_embedding(r) for r in responsibilities]
    
    # Compute similarity matrix
    similarity_matrix = []
    for p_emb in proj_embeddings:
        row = []
        for r_emb in resp_embeddings:
            # calculate_similarities expects 2D inputs
            sim = float(calculate_similarities(p_emb.reshape(1, -1), r_emb.reshape(1, -1))[0][0])
            row.append(round(sim, 4))
        similarity_matrix.append(row)
        
    matrix_np = np.array(similarity_matrix)
    
    # Find matches and top-K
    top_matches = []
    matched_topics = set()
    
    for i, project in enumerate(projects):
        # Extract title from first line of project text
        title = project.split('\n')[0].strip("- *•")
        best_idx = int(np.argmax(matrix_np[i]))
        best_sim = float(matrix_np[i][best_idx])
        best_resp = responsibilities[best_idx]
        
        # Consider it matched if similarity is >= 0.50
        is_matched = best_sim >= 0.50
        
        match_info = {
            "project": title,
            "matched_responsibility": best_resp,
            "similarity": round(best_sim * 100, 2),
            "matched": is_matched,
            "reason": f"Project matches: '{best_resp[:60]}...' with similarity {round(best_sim*100, 1)}%"
        }
        top_matches.append(match_info)
        
        if is_matched:
            matched_topics.add(best_resp)
            
    missing_topics = [r for r in responsibilities if r not in matched_topics]
    matched_topics_list = list(matched_topics)
    
    # Calculate score using max similarity and topic coverage
    max_sim = float(matrix_np.max()) if matrix_np.size > 0 else 0.0
    coverage_ratio = len(matched_topics_list) / len(responsibilities) if responsibilities else 0.0
    
    # Blended score: 60% max similarity + 40% responsibility coverage ratio
    score = (max_sim * 0.60) + (coverage_ratio * 0.40)
    score_scaled = min(max(score * 100, 0.0), 100.0)
    
    # Construct explanation reason
    if coverage_ratio >= 0.7:
        reason = f"Candidate projects cover {len(matched_topics_list)} out of {len(responsibilities)} key job responsibilities, showing high alignment (Max similarity: {round(max_sim*100, 1)}%)."
    elif coverage_ratio >= 0.3:
        reason = f"Candidate projects cover {len(matched_topics_list)} out of {len(responsibilities)} key job responsibilities, showing moderate alignment (Max similarity: {round(max_sim*100, 1)}%)."
    else:
        reason = f"Candidate projects cover only {len(matched_topics_list)} out of {len(responsibilities)} key responsibilities. Project descriptions lack details matching JD requirements."
        
    return {
        "matched_topics": matched_topics_list,
        "missing_topics": missing_topics,
        "top_matches": top_matches,
        "similarity": round(max_sim * 100, 2),
        "reason": reason,
        "score": round(score_scaled, 2)
    }
