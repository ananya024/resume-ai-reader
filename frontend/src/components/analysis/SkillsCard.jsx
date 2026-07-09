import "../../styles/Card.css";

function SkillsCard({ skills }) {

    return (
        <div className="card">

            <h2>Skills</h2>

            <h3>Programming Languages</h3>
            <ul>
                {skills.programming_languages.map((skill, index) => (
                    <li key={index}>{skill}</li>
                ))}
            </ul>

            <h3>Frameworks</h3>
            <ul>
                {skills.frameworks.map((skill, index) => (
                    <li key={index}>{skill}</li>
                ))}
            </ul>

            <h3>Libraries</h3>
            <ul>
                {skills.libraries.map((skill, index) => (
                    <li key={index}>{skill}</li>
                ))}
            </ul>

            <h3>Databases</h3>
            <ul>
                {skills.databases.map((skill, index) => (
                    <li key={index}>{skill}</li>
                ))}
            </ul>

            <h3>Tools</h3>
            <ul>
                {skills.tools.map((skill, index) => (
                    <li key={index}>{skill}</li>
                ))}
            </ul>

            <h3>Cloud</h3>
            <ul>
                {skills.cloud.length > 0 ?
                    skills.cloud.map((skill, index) => (
                        <li key={index}>{skill}</li>
                    ))
                    :
                    <li>Not Available</li>
                }
            </ul>

            <h3>Other</h3>
            <ul>
                {skills.other.map((skill, index) => (
                    <li key={index}>{skill}</li>
                ))}
            </ul>

        </div>
    );
}

export default SkillsCard;