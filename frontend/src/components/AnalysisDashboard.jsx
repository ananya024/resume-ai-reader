// AnalysisDashboard.jsx

import "../App.css";
import "../styles/Dashboard.css";
import "../styles/AnalysisDashboard.css";
import "../styles/Card.css"
import CandidateSummaryCard from "./analysis/CandidateSummaryCard";
import ResumeScoreCard from "./analysis/ResumeScoreCard";
import ATSAnalysisCard from "./analysis/ATSAnalysisCard";
import ResumeImprovementsCard from "./analysis/ResumeImprovementsCard";
import CareerRecommendationCard from "./analysis/CareerRecommendationCard";
import SkillGapCard from "./analysis/SkillGapCard";
import LearningRoadmapCard from "./analysis/LearningRoadmapCard";
import InterviewQuestionsCard from "./analysis/InterviewQuestionsCard";

function AnalysisDashboard({analysis}){
    if(!analysis)
        return null;
    return (<>
        <div>
            <p className="file-name">Resume Analysis</p>
        </div>
        <div className="dashboard">
            <CandidateSummaryCard
                candidate_summary={analysis.candidate_summary}
            />

            <ATSAnalysisCard
                ats_analysis={analysis.ats_analysis}
            />

            <CareerRecommendationCard
                recommendation={analysis.career_recommendation}
            />

            <SkillGapCard
                skill_gap={analysis.skill_gap_analysis}
            />

            <LearningRoadmapCard
                roadmap={analysis.learning_roadmap}
            />

            <InterviewQuestionsCard
                questions={analysis.interview_questions}
            />

            <ResumeScoreCard
                resume_score={analysis.resume_score}
            />

            <ResumeImprovementsCard
                improvements={analysis.resume_improvements}
            />
        </div>
    </>)
}

export default AnalysisDashboard;