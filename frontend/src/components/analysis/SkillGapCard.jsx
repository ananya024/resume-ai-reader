// SkillGapCard.jsx

import "../../styles/Card.css"

function SkillGapCard({ skill_gap }) {

    return (

        <div className="card">

            <h2>Skill Gap Analysis</h2>

            <h3>Current Strengths</h3>

            <ul>

                {skill_gap.current_strengths.map((item, index) => (

                    <li key={index}>{item}</li>

                ))}

            </ul>

            <h3>Missing Skills</h3>

            <ul>

                {skill_gap.missing_skills.map((item, index) => (

                    <li key={index}>{item}</li>

                ))}

            </ul>

        </div>

    );

}

export default SkillGapCard;