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

            <h3>Strengths</h3>

            <ul>
                {candidate_summary.key_strengths.map((strength, index) => (
                    <li key={index}>{strength}</li>
                ))}
            </ul>

            <h3>Weaknesses</h3>

            <ul>
                {candidate_summary.key_weaknesses.map((weakness, index) => (
                    <li key={index}>{weakness}</li>
                ))}
            </ul>

        </div>
    );
}

export default CandidateSummaryCard;