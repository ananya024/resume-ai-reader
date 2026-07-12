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
        skills: {
            programming_languages: analysis.skills?.matched?.filter(s => 
                ["JavaScript", "TypeScript", "Python", "C++", "C", "Go", "Rust", "Java", "SQL", "HTML", "CSS"].includes(s)
            ) || [],
            frameworks: analysis.skills?.matched?.filter(s => 
                ["React", "Express", "Node.js", "NestJS", "FastAPI", "Django", "Flask", "Spring Boot"].includes(s)
            ) || [],
            libraries: [],
            databases: analysis.skills?.matched?.filter(s => 
                ["PostgreSQL", "MySQL", "MongoDB", "Redis", "SQLite"].includes(s)
            ) || [],
            tools: analysis.skills?.matched?.filter(s => 
                ["Git", "Docker", "Kubernetes", "VS Code", "Postman", "Jira"].includes(s)
            ) || [],
            cloud: analysis.skills?.matched?.filter(s => 
                ["AWS", "Azure", "GCP"].includes(s)
            ) || [],
            other: analysis.skills?.extra || []
        },
        education: [
            {
                institution: "Candidate Education Info",
                degree: analysis.education?.resume || "Not Extracted",
                field_of_study: "",
                start_date: "",
                end_date: "",
                cgpa: ""
            }
        ]
    };

    return (
        <div className="dashboard-page">

            <NavBar activeTab={activeTab} setActiveTab={setActiveTab} />
            
            {activeTab === "parsed" ? (
                <ResumeParsed parsedResume={parsedResumeMock} />
            ) : (
                <AnalysisDashboard analysis={analysis} />
            )}
        </div>
    );
}

export default Dashboard;