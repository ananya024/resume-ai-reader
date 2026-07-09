// LearningRoadmapCard.jsx

import "../../styles/Card.css"

function LearningRoadmapCard({ roadmap }) {

    return (

        <div className="card">

            <h2>Learning Roadmap</h2>

            {roadmap.map((step) => (

                <div key={step.step}>

                    <h3>

                        Step {step.step}

                    </h3>

                    <p>

                        <strong>{step.topic}</strong>

                    </p>

                    <p>{step.reason}</p>

                </div>

            ))}

        </div>

    );

}

export default LearningRoadmapCard;