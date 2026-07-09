import "../../styles/Card.css";

function EducationCard({ education }) {

    return (
        <div className="card">

            <h2>Education</h2>

            {education.map((edu, index) => (

                <div key={index}>

                    <h3>{edu.institution}</h3>

                    <p><strong>Degree:</strong> {edu.degree}</p>

                    <p><strong>Field:</strong> {edu.field_of_study}</p>

                    <p><strong>Duration:</strong> {edu.start_date} - {edu.end_date}</p>

                    <p><strong>CGPA:</strong> {edu.cgpa}</p>

                </div>

            ))}

        </div>
    );
}

export default EducationCard;