// Dashboard.jsx

import { useState } from "react";
import "../App.css";
import "../styles/Dashboard.css";
import NavBar from "./common/NavBar";
import ResumeParsed from "./ResumeParsed";
import AnalysisDashboard from "./AnalysisDashboard";

function Dashboard({ analysis }) {
    if (!analysis) return null;
    console.log("Analysis Data:", analysis);
    
    const [activeTab, setActiveTab] = useState("analysis"); // Default to the analysis tab

    // Build a safe structure for ResumeParsed to prevent crashes
    const parsedResumeMock = {
        contact_information: {
            name: "Not Available",
            email: "Not Available",
            phone: "Not Available",
            location: "Not Available",
            linkedin: "Not Available",
            github: "Not Available",
            portfolio: "Not Available"
        },

        professional_summary: "Not Available",

        skills: {
            programming_languages: analysis.skills?.extra?.filter(s =>
                ["Python", "Java", "JavaScript", "TypeScript", "C", "C++", "Go", "Rust", "SQL", "HTML", "CSS"].includes(s)
            ) || [],

            frameworks: analysis.skills?.extra?.filter(s =>
                ["React", "Node.js", "Express", "NestJS", "FastAPI", "Flask", "Django", "Spring Boot"].includes(s)
            ) || [],

            libraries: analysis.skills?.extra?.filter(s =>
                ["NumPy", "Pandas", "TensorFlow", "PyTorch", "Scikit-learn"].includes(s)
            ) || [],

            databases: analysis.skills?.extra?.filter(s =>
                ["PostgreSQL", "MySQL", "MongoDB", "SQLite", "Oracle", "Redis"].includes(s)
            ) || [],

            tools: analysis.skills?.extra?.filter(s =>
                ["Git", "GitHub", "Docker", "Postman", "VS Code", "Jira"].includes(s)
            ) || [],

            cloud: analysis.skills?.extra?.filter(s =>
                ["AWS", "Azure", "GCP"].includes(s)
            ) || [],

            other: analysis.skills?.extra?.filter(s =>
                ![
                    "Python", "Java", "JavaScript", "TypeScript", "C", "C++", "Go", "Rust",
                    "React", "Node.js", "Express", "NestJS", "FastAPI", "Flask", "Django",
                    "Spring Boot", "NumPy", "Pandas", "TensorFlow", "PyTorch", "Scikit-learn",
                    "PostgreSQL", "MySQL", "MongoDB", "SQLite", "Oracle", "Redis",
                    "Git", "GitHub", "Docker", "Postman", "VS Code", "Jira",
                    "AWS", "Azure", "GCP"
                ].includes(s)
            ) || []
        },

        education: [
            {
                institution: "Candidate Education",
                degree: analysis.education?.resume || "Not Available",
                field_of_study: "",
                start_date: "",
                end_date: "",
                cgpa: ""
            }
        ],

        experience: [
            {
                company: "Not Available",
                position: "Not Available",
                duration: `${analysis.experience?.resume_years ?? 0} years`,
                description: analysis.experience?.reason || "No experience information available."
            }
        ],

        projects: analysis.projects?.top_matches?.map(project => ({
            title: project.project,
            description: project.reason,
            technologies: [],
            github: "",
            live: ""
        })) || [],

        certifications: []
    };

    return (
        <div className="dashboard-page">

            <NavBar activeTab={activeTab} setActiveTab={setActiveTab} />
            <AnalysisDashboard analysis={analysis} />
            {/* {activeTab === "parsed" ? (
                <ResumeParsed parsedResume={parsedResumeMock} />
            ) : (
                <AnalysisDashboard analysis={analysis} />
            )} */}
        </div>
    );
}

export default Dashboard;