// CandidateSummaryCard.jsx

import "../../styles/Card.css"

function CandidateSummaryCard({ candidate_summary }) {

    return (
        <div className="card">

            <h2>Candidate Summary</h2>

            <p>
                <strong>Professional Level:</strong>{" "}
                {candidate_summary.professional_level}
            </p>

            <p>
                <strong>Career Domain:</strong>{" "}
                {candidate_summary.career_domain}
            </p>

            <p>{candidate_summary.overall_summary}</p>

            <h3 className="strength-heading">Strengths</h3>
            <ul className="strength-list">
                {candidate_summary.key_strengths.map((strength, index) => (
                    <li key={index}>{strength}</li>
                ))}
            </ul>

            <h3 className="weakness-heading">Weaknesses</h3>
            <ul className="weakness-list">
                {candidate_summary.key_weaknesses.map((weakness, index) => (
                    <li key={index}>{weakness}</li>
                ))}
            </ul>

        </div>
    );
}

export default CandidateSummaryCard;