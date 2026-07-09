// ResumeScoreCard.jsx

import "../../styles/Card.css"

function ResumeScoreCard({ resume_score }) {

    return (<>
        <div className="card">
            <h1>Resume Score</h1>
            <h2>{resume_score.overall_score.score}/100</h2>
            <p><strong>Reason</strong></p>
            <p>{resume_score.overall_score.reason}</p>
            <ul>
                {resume_score.overall_score.suggestions?.map((suggestion, index) => (
                    <li key={index}>{suggestion}</li>
                ))}
            </ul>
        </div>
        <div className="card">
            <h1>Technical Skills</h1>
            <h2>{resume_score.technical_skills.score}/100</h2>
            <p><strong>Reason</strong></p>
            <p>{resume_score.technical_skills.reason}</p>
            <ul>
                {resume_score.technical_skills.suggestions?.map((suggestion, index) => (
                    <li key={index}>{suggestion}</li>
                ))}
            </ul>
        </div>
        <div className="card">
            <h1>Projects</h1>
            <ul>
                {resume_score.projects?.map((project,index)=>(
                    <li key ={index}>
                        <div>
                            <p><strong>{project.project_name}</strong></p>
                            <h2>{project.score}/100</h2>
                            <p>{project.reason}</p>
                            <ul>
                                {project.suggestions?.map((suggestion, index) => (
                                    <li key={index}>{suggestion}</li>
                                ))}
                            </ul>
                        </div>
                    </li>
                ))}
            </ul>
        </div>
        <div className="card">
            <h1>Experiance</h1>
            <h2>{resume_score.experience.score}/100</h2>
            <p><strong>Reason</strong></p>
            <p>{resume_score.experience.reason}</p>
            <ul>
                {resume_score.experience.suggestions?.map((suggestion, index) => (
                    <li key={index}>{suggestion}</li>
                ))}
            </ul>
        </div>
        <div className="card">
            <h1>Education</h1>
            <h2>{resume_score.education.score}/100</h2>
            <p><strong>Reason</strong></p>
            <p>{resume_score.education.reason}</p>
            <ul>
                {resume_score.education.suggestions?.map((suggestion, index) => (
                    <li key={index}>{suggestion}</li>
                ))}
            </ul>
        </div>
        <div className="card">
            <h1>Resume Quality</h1>
            <h2>{resume_score.resume_quality.score}/100</h2>
            <p><strong>Reason</strong></p>
            <p>{resume_score.resume_quality.reason}</p>
            <ul>
                {resume_score.resume_quality.suggestions?.map((suggestion, index) => (
                    <li key={index}>{suggestion}</li>
                ))}
            </ul>
        </div>
    
    </>);
}

export default ResumeScoreCard;