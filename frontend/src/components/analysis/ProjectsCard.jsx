// ProjectsCard.jsx

import "../../styles/Card.css";

function ProjectsCard({ projects }) {

    return (
        <div className="card">

            <h2>Projects</h2>

            {projects.map((project, index) => (

                <div key={index}>

                    <h3>{project.title}</h3>

                    <p>

                        <strong>Technologies:</strong>{" "}

                        {project.technologies.join(", ")}

                    </p>

                    <ul>

                        {project.description.map((desc, i) => (

                            <li key={i}>{desc}</li>

                        ))}

                    </ul>

                </div>

            ))}

        </div>
    );
}

export default ProjectsCard;