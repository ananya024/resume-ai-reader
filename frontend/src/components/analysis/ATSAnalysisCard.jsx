// ATSAnalysisCard.jsx

import "../../styles/Card.css"

function ATSAnalysisCard({ ats_analysis }) {

    return (
        <div className="card">

            <h2>ATS Analysis</h2>

            <div className="score">
                {ats_analysis.ats_score}/100
            </div>

            <p>
                <strong>Keyword Coverage</strong>
            </p>

            <p>
                {ats_analysis.keyword_coverage.assessment}
            </p>

            <h3>Missing Keywords</h3>

            <ul>
                {ats_analysis.keyword_coverage.missing_keywords.map(
                    (keyword, index) => (
                        <li key={index}>
                            {keyword}
                        </li>
                    )
                )}
            </ul>

        </div>
    );
}

export default ATSAnalysisCard;