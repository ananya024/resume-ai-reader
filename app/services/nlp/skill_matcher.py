# skill_matcher.py

from app.services.nlp.embedding_service import generate_embedding
from app.services.nlp.similarity_service import calculate_similarities
from app.services.nlp.skill_normalizer import normalize_skill

# In-memory embedding cache to avoid regenerating embeddings for repeated skills (e.g. Python, JavaScript, SQL)
EMBEDDING_CACHE = {}

def get_cached_embedding(skill: str):
    """
    Returns the embedding for a skill, using the in-memory cache if available.
    """
    skill_lower = skill.strip().lower()
    if skill_lower not in EMBEDDING_CACHE:
        EMBEDDING_CACHE[skill_lower] = generate_embedding(skill)
    return EMBEDDING_CACHE[skill_lower]

def match_skills(resume_skills, jd_skills):
    """
    Compares resume skills to JD skills:
    1. Normalize both lists.
    2. Perform exact matching.
    3. Remove exact matches.
    4. Generate embeddings ONLY for remaining unmatched skills.
    5. Perform cosine similarity with threshold 0.55.
    6. Return matched, missing, extra, and score.
    """
    # Step 1: Normalize both lists and remove duplicates
    normalized_resume = sorted(list(set(normalize_skill(s) for s in resume_skills if s)))
    normalized_jd = sorted(list(set(normalize_skill(s) for s in jd_skills if s)))

    if not normalized_resume or not normalized_jd:
        return {
            "matched": [],
            "missing": normalized_jd,
            "extra": normalized_resume,
            "score": 0.0
        }

    matched = []
    matched_resume = set()
    matched_jd = set()

    # Step 2 & 3: Perform exact matching and remove exact matches
    exact_matches = set(normalized_resume) & set(normalized_jd)
    for skill in exact_matches:
        matched.append({
            "resume_skill": skill,
            "jd_skill": skill,
            "similarity": 1.0
        })
        matched_resume.add(skill)
        matched_jd.add(skill)

    # Step 4: Identify remaining unmatched skills
    unmatched_resume = [s for s in normalized_resume if s not in matched_resume]
    unmatched_jd = [s for s in normalized_jd if s not in matched_jd]

    # Step 5: Perform cosine similarity on unmatched skills
    if unmatched_resume and unmatched_jd:
        # Retrieve embeddings using cache
        resume_embeddings = [get_cached_embedding(s) for s in unmatched_resume]
        jd_embeddings = [get_cached_embedding(s) for s in unmatched_jd]

        # Compare unmatched resume skills with unmatched JD skills
        for r_skill, r_emb in zip(unmatched_resume, resume_embeddings):
            best_score = 0.0
            best_match = None
            
            for j_skill, j_emb in zip(unmatched_jd, jd_embeddings):
                # Calculate cosine similarity using the similarity service
                score = float(calculate_similarities([r_emb], [j_emb])[0][0])
                if score > best_score:
                    best_score = score
                    best_match = j_skill

            # Apply threshold of 0.55
            if best_score >= 0.55:
                matched.append({
                    "resume_skill": r_skill,
                    "jd_skill": best_match,
                    "similarity": round(best_score, 2)
                })
                matched_resume.add(r_skill)
                matched_jd.add(best_match)

    # Step 6: Calculate final lists and score
    missing = [skill for skill in normalized_jd if skill not in matched_jd]
    extra = [skill for skill in normalized_resume if skill not in matched_resume]

    # Score is the percentage of JD skills matched
    score = (len(matched_jd) / len(normalized_jd)) * 100 if normalized_jd else 0.0

    return {
        "matched": matched,
        "missing": missing,
        "extra": extra,
        "score": round(score, 2)
    }
