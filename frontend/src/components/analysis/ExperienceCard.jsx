// ExperianceCard.jsx

// Experiance.jsx

import "../../styles/Card.css";

function ExperienceCard({ experience }) {

    return (
        <div className="card">

            <h2>Experience</h2>

            {experience.map((exp, index) => (

                <div key={index}>

                    <h3>{exp.position}</h3>

                    <p><strong>Company:</strong> {exp.company}</p>

                    <p><strong>Location:</strong> {exp.location || "Not Available"}</p>

                    <p><strong>Duration:</strong> {exp.start_date || "-"} - {exp.end_date || "-"}</p>

                    <ul>

                        {exp.description.length > 0 ?

                            exp.description.map((desc, i) => (
                                <li key={i}>{desc}</li>
                            ))

                            :

                            <li>No Description Available</li>

                        }

                    </ul>

                </div>

            ))}

        </div>
    );
}

export default ExperienceCard;