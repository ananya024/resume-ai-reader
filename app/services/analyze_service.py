# analyze_service.py

import time
from app.services.pdf_reader import read_pdf
from app.services.gemini_service import extract_jd
from app.services.nlp.section_extractor import extract_resume_sections
from app.services.nlp.extractor import extract_skills
from app.services.nlp.skill_inference import infer_skills_from_text
from app.services.nlp.concept_matcher import match_concepts
from app.services.nlp.project_matcher import match_projects
from app.services.nlp.education_matcher import match_education
from app.services.nlp.experience_matcher import match_experience
from app.services.nlp.semantic_reasoner import get_strongest_weakest_areas, explain_overall_score

def analyze_resume(path_res: str, path_jd: str):
    """
    Main orchestration service for comparing a Resume PDF against a Job Description PDF.
    Uses local NLP, Regex, and a Knowledge Graph for matching, and Gemini for summary reasoning.
    """

    textres, linksres = read_pdf(path_res)
    textjd, linksjd = read_pdf(path_jd)

    # Segment the resume text into sections
    resume_sections = extract_resume_sections(textres)

    # Retrieve the parsed fields from the Job Description using Gemini
    for _ in range(3):
        jd_extract = extract_jd(textjd)
        if "error" not in jd_extract:
            break
        time.sleep(2)

    if "error" in jd_extract:
        print("Gemini JD Extraction error:", jd_extract)
        return {
            "overall_score": 0.0,
            "error": jd_extract["error"]
        }
    
    # 1. SKILLS EXTRACTION & INFERENCE
    # Extract explicit skills from the resume's skills section
    resume_skills_raw = extract_skills(resume_sections.get("skills", ""))
    
    # Infer additional skills from project descriptions (concept/architecture matching)
    inferred_skills = infer_skills_from_text(resume_sections.get("projects", ""))
    
    # Combine explicit and inferred skills
    augmented_resume_skills = list(set(resume_skills_raw) | set(inferred_skills))
    
    # Extract JD skills directly from the raw JD text
    jd_skills_raw = extract_skills(textjd)
    
    # Run the concept matcher (Exact + Semantic + Ontology matches)
    skill_result = match_concepts(augmented_resume_skills, jd_skills_raw)

    # 2. PROJECTS MATCHING (Fine-grained itemized comparison)
    project_result = match_projects(
        resume_sections.get("projects", ""), 
        jd_extract.get("responsibilities", [])
    )

    # 3. EXPERIENCE MATCHING (Entry-level normalization + years comparison)
    experience_result = match_experience(
        textres, 
        jd_extract.get("experience_required", "")
    )

    # 4. EDUCATION MATCHING (Degree/Field normalization)
    education_result = match_education(
        resume_sections.get("education", ""), 
        jd_extract.get("education_required", "")
    )

    # 5. OVERALL SCORE & WEIGHTED CALCULATIONS
    skills_score = skill_result["score"]
    projects_score = project_result["score"]
    experience_score = experience_result["score"]
    education_score = education_result["score"]

    # Contributions based on weights: Skills (45%), Experience (25%), Projects (20%), Education (10%)
    skills_contrib = round(skills_score * 0.45, 2)
    experience_contrib = round(experience_score * 0.25, 2)
    projects_contrib = round(projects_score * 0.20, 2)
    education_contrib = round(education_score * 0.10, 2)

    overall_score = round(skills_contrib + experience_contrib + projects_contrib + education_contrib, 2)

    # 6. STRENGTHS/WEAKNESSES AND EXPLANATION
    strongest_areas, weakest_areas = get_strongest_weakest_areas(
        skills_score, projects_score, education_score, experience_score
    )

    final_explanation = explain_overall_score(
        skills_score, projects_score, education_score, experience_score,
        overall_score, strongest_areas, weakest_areas
    )

    # Debug logs on backend console
    print("--- Analysis Verification ---")
    print(f"Candidate Skills: {skill_result['matched']}")
    print(f"Missing Skills: {skill_result['missing']}")
    print(f"Overall Match Score: {overall_score}")

    return {
        "overall_score": overall_score,
        "overall_explanation": {
            "weighted_calculation": "Skills (45%) + Experience (25%) + Projects (20%) + Education (10%)",
            "final_explanation": final_explanation,
            "strongest_areas": strongest_areas,
            "weakest_areas": weakest_areas,
            "contributions": {
                "skills": skills_contrib,
                "experience": experience_contrib,
                "projects": projects_contrib,
                "education": education_contrib
            }
        },
        "skills": {
            "matched": skill_result["matched"],
            "missing": skill_result["missing"],
            "extra": skill_result["extra"],
            "category_matches": skill_result["category_matches"],
            "score": skill_result["score"]
        },
        "projects": {
            "matched_topics": project_result["matched_topics"],
            "missing_topics": project_result["missing_topics"],
            "top_matches": project_result["top_matches"],
            "similarity": project_result["similarity"],
            "reason": project_result["reason"],
            "score": project_result["score"]
        },
        "experience": {
            "resume_years": experience_result["resume_years"],
            "required_years": experience_result["required_years"],
            "matched": experience_result["matched"],
            "reason": experience_result["reason"],
            "score": experience_result["score"]
        },
        "education": {
            "resume": education_result["resume"],
            "required": education_result["required"],
            "matched": education_result["matched"],
            "reason": education_result["reason"],
            "score": education_result["score"]
        }
    }