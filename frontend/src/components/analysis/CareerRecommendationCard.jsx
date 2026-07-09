// CareerRecommendationCard.jsx

import "../../styles/Card.css"

function CareerRecommendationCard({ recommendation }) {

    return (

        <div className="card">

            <h2>Career Recommendation</h2>

            <p>

                <strong>Confidence:</strong>{" "}
                {recommendation.confidence}

            </p>

            <p>{recommendation.reason}</p>

            <h3>Best Fit Roles</h3>

            <ul>

                {recommendation.best_fit_roles.map((role, index) => (

                    <li key={index}>{role}</li>

                ))}

            </ul>

            <h3>Alternative Roles</h3>

            <ul>

                {recommendation.alternative_roles.map((role, index) => (

                    <li key={index}>{role}</li>

                ))}

            </ul>

        </div>

    );

}

export default CareerRecommendationCard;