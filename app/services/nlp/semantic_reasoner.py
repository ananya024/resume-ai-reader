# semantic_reasoner.py

from app.services.gemini_service import client

def get_strongest_weakest_areas(skills_score, projects_score, education_score, experience_score):
    """
    Identifies candidate's strongest and weakest matching dimensions based on scores.
    """
    scores = {
        "Technical Skills": skills_score,
        "Project Alignment": projects_score,
        "Education": education_score,
        "Experience": experience_score
    }
    
    # Sort areas by score
    sorted_areas = sorted(scores.items(), key=lambda x: x[1])
    
    strongest = []
    weakest = []
    
    max_score = sorted_areas[-1][1]
    for area, score in scores.items():
        if score == max_score or score >= 75.0:
            strongest.append(area)
            
    min_score = sorted_areas[0][1]
    for area, score in scores.items():
        if score == min_score or score < 60.0:
            weakest.append(area)
            
    # Guarantee sets are populated and don't overlap
    strongest = list(set(strongest))
    weakest = list(set(weakest) - set(strongest))
    
    if not strongest:
        strongest = [sorted_areas[-1][0]]
    if not weakest:
        weakest = [sorted_areas[0][0]]
        
    return sorted(strongest), sorted(weakest)

def explain_overall_score(skills_score, projects_score, education_score, experience_score, overall_score, strongest, weakest):
    """
    Generates a natural language explanation of the overall score using Gemini.
    Falls back to a local template if Gemini fails.
    """
    prompt = f"""You are an ATS Resume Analyzer.
Synthesize the candidate's matching scores into a concise, professional summary (2-3 sentences max) explaining their overall compatibility.

Scores:
- Overall Score: {overall_score}/100
- Technical Skills Match: {skills_score}/100
- Project Alignment: {projects_score}/100
- Education Alignment: {education_score}/100
- Experience Alignment: {experience_score}/100

Strongest Areas: {", ".join(strongest)}
Weakest Areas: {", ".join(weakest)}

Explain why the candidate received the overall score of {overall_score}/100. Write it as a single cohesive paragraph. Do not return JSON or markdown formatting.
"""
    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt
        )
        text = response.text.strip()
        if text:
            return text
    except Exception as e:
        print(f"Gemini explanation generation failed: {e}")
        
    # Local template fallback
    return (
        f"The candidate achieved an overall match score of {overall_score}/100. "
        f"Their strongest match lies in {', '.join(strongest)}, showing good alignment. "
        f"However, their profile is limited by {', '.join(weakest)}, which represents their weakest areas and areas for improvement."
    )
