// AnalysisDashboard.jsx

import "../App.css";
import "../styles/Dashboard.css";
import "../styles/AnalysisDashboard.css";
import "../styles/Card.css";
import OverallExplanationCard from "./analysis/OverallExplanationCard";
import SkillGapCard from "./analysis/SkillGapCard";
import ProjectMatcherCard from "./analysis/ProjectMatcherCard";
import ExperienceMatchCard from "./analysis/ExperienceMatchCard";
import EducationMatchCard from "./analysis/EducationMatchCard";

function AnalysisDashboard({ analysis }) {
    if (!analysis) return null;

    return (
        <>
            <div>
                <p className="file-name" style={{ fontSize: "1.25rem", color: "#4a5568", fontWeight: "bold" }}>
                    ATS Match & Analysis Dashboard
                </p>
            </div>
            
            <div className="dashboard">
                {/* 1. Overall Score & Summary Explanation Card */}
                <OverallExplanationCard 
                    overall_score={analysis.overall_score} 
                    overall_explanation={analysis.overall_explanation} 
                />

                {/* 2. Skills Match & Category Propagation Card */}
                <SkillGapCard 
                    skills={analysis.skills} 
                />

                {/* 3. Project to JD Responsibility Matcher Card */}
                <ProjectMatcherCard 
                    projects={analysis.projects} 
                />

                {/* 4. Experience Years Match Card */}
                <ExperienceMatchCard 
                    experience={analysis.experience} 
                />

                {/* 5. Education Level & Field Match Card */}
                <EducationMatchCard 
                    education={analysis.education} 
                />
            </div>
        </>
    );
}

export default AnalysisDashboard;