# concept_matcher.py

from app.services.nlp.skill_matcher import get_cached_embedding
from app.services.nlp.similarity_service import calculate_similarities
from app.services.nlp.skill_normalizer import normalize_skill
from app.services.nlp.ontology import evaluate_ontology

def match_concepts(resume_skills, jd_skills) -> dict:
    """
    Implements concept-level matching flow:
    1. Normalize both lists.
    2. Perform exact matching.
    3. Perform semantic embedding matching for unmatched skills.
    4. Propagate matches through the ontology concept graph.
    5. Return matched list, missing, extra, category_matches, and score.
    """
    # Step 1: Normalize both lists
    normalized_resume = sorted(list(set(normalize_skill(s) for s in resume_skills if s)))
    normalized_jd = sorted(list(set(normalize_skill(s) for s in jd_skills if s)))

    if not normalized_resume or not normalized_jd:
        category_matches = evaluate_ontology(normalized_resume)
        return {
            "matched": [],
            "missing": normalized_jd,
            "extra": normalized_resume,
            "category_matches": category_matches,
            "score": 0.0,
            "details": []
        }

    matched_jd = set()
    matched_resume = set()
    match_details = []

    # Step 2: Exact matching
    exact_matches = set(normalized_resume) & set(normalized_jd)
    for skill in exact_matches:
        matched_jd.add(skill)
        matched_resume.add(skill)
        match_details.append({
            "resume_skill": skill,
            "jd_skill": skill,
            "similarity": 1.0,
            "type": "exact"
        })

    # Step 3: Identify remaining unmatched skills
    unmatched_resume = [s for s in normalized_resume if s not in matched_resume]
    unmatched_jd = [s for s in normalized_jd if s not in matched_jd]

    # Step 4: Semantic matching on unmatched skills
    if unmatched_resume and unmatched_jd:
        resume_embeddings = [get_cached_embedding(s) for s in unmatched_resume]
        jd_embeddings = [get_cached_embedding(s) for s in unmatched_jd]

        for r_skill, r_emb in zip(unmatched_resume, resume_embeddings):
            best_score = 0.0
            best_match = None
            
            for j_skill, j_emb in zip(unmatched_jd, jd_embeddings):
                # Calculate cosine similarity
                score = float(calculate_similarities([r_emb], [j_emb])[0][0])
                if score > best_score:
                    best_score = score
                    best_match = j_skill

            # Apply semantic threshold of 0.55
            if best_score >= 0.55:
                matched_jd.add(best_match)
                matched_resume.add(r_skill)
                match_details.append({
                    "resume_skill": r_skill,
                    "jd_skill": best_match,
                    "similarity": round(best_score, 2),
                    "type": "semantic"
                })

    # Step 5: Evaluate ontology propagation
    # We combine normalized resume skills and matched JD skills
    candidate_skills = set(normalized_resume) | matched_jd
    category_matches = evaluate_ontology(candidate_skills)

    # Step 6: Adjust scores with parent category matches
    # If a parent category is matched in the ontology and is required in the JD, mark it matched!
    for category, is_matched in category_matches.items():
        if is_matched:
            if category in normalized_jd and category not in matched_jd:
                matched_jd.add(category)
                match_details.append({
                    "resume_skill": "Ontology Inference",
                    "jd_skill": category,
                    "similarity": 1.0,
                    "type": "ontology"
                })

    # Re-calculate missing and extra skill lists
    missing = [skill for skill in normalized_jd if skill not in matched_jd]
    extra = [skill for skill in normalized_resume if skill not in matched_jd and skill not in matched_resume]

    # Calculate final matching score
    score = (len(matched_jd) / len(normalized_jd)) * 100 if normalized_jd else 0.0

    return {
        "matched": sorted(list(matched_jd)),
        "missing": missing,
        "extra": extra,
        "category_matches": category_matches,
        "score": round(score, 2),
        "details": match_details
    }
