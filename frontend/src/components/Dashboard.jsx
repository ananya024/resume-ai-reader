// Dashboard.jsx

import "../App.css";
import "../styles/Dashboard.css";
import NavBar from "./common/NavBar";
import ResumeParsed from "./ResumeParsed";
import AnalysisDashboard from "./AnalysisDashboard";
import { useState } from "react";

function Dashboard({analysis}){
    if(!analysis)
        return null;
    console.log(analysis);
    const [activeTab, setActiveTab] = useState("parsed");
    return (
        <div className="dashboard-page">
            <NavBar activeTab={activeTab} setActiveTab={setActiveTab}/>
            {activeTab === "parsed"
                ?<ResumeParsed parsedResume={analysis.parsed_resume}/>
                :<AnalysisDashboard analysis={analysis.analysis}/>
            }
        </div>
    )
}

export default Dashboard;