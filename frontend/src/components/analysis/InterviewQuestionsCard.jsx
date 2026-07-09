// InterviewQuestionsCard.jsx

import "../../styles/Card.css"

function InterviewQuestionsCard({ questions }) {

    return (

        <div className="card">

            <h2>Technical Interview Questions</h2>

            {questions.technical.map((question, index) => (

                <div key={index}>

                    <h3>

                        {question.topic}

                    </h3>

                    <p>

                        {question.question}

                    </p>

                    <hr />

                </div>

            ))}

        </div>

    );

}

export default InterviewQuestionsCard;