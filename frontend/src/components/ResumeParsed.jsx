// ResumeParsed.jsx

import "../App.css";
import "../styles/Dashboard.css";
import "../styles/Card.css";

import ContactCard from "./analysis/ContactCard";
import SkillsCard from "./analysis/SkillsCard";
import EducationCard from "./analysis/EducationCard";
import ExperienceCard from "./analysis/ExperienceCard";
import ProjectsCard from "./analysis/ProjectsCard";
import CertificationsCard from "./analysis/CertificationsCard";

function ResumeParsed({ parsedResume }) {
    console.log(parsedResume);
    if (!parsedResume)
        return null;

    return (
        <>
            <div>
                <p className="file-name">Parsed Resume</p>
            </div>

            <div className="dashboard">

                <ContactCard
                    parsedResume={parsedResume}
                />

                <SkillsCard
                    skills={parsedResume.skills}
                />

                <EducationCard
                    education={parsedResume.education}
                />

                <ExperienceCard
                    experience={parsedResume.experience}
                />

                <ProjectsCard
                    projects={parsedResume.projects}
                />

                <CertificationsCard
                    certifications={parsedResume.certifications}
                />

            </div>
        </>
    );
}

export default ResumeParsed;