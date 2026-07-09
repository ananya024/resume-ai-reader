// ResumeImprovementsCard.jsx

import "../../styles/Card.css"

function ResumeImprovementsCard({ improvements }) {

    return (
        <div className="card">

            <h2>Resume Improvements</h2>

            {improvements.map((item, index) => (

                <div key={index} className="improvement">

                    <h3>
                        {item.priority} Priority • {item.issue}
                    </h3>

                    <p>
                        <strong>Impact</strong>
                    </p>

                    <p>{item.impact}</p>

                    <p>
                        <strong>Recommendation</strong>
                    </p>

                    <p>{item.suggestion}</p>

                </div>

            ))}

        </div>
    );

}

export default ResumeImprovementsCard;