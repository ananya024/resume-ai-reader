// NavBar.jsx

import "../../App.css";
import "../../styles/NavBar.css";

function NavBar({activeTab, setActiveTab}){
    return (
        <div className="navbar">
            {/* <button
                className={activeTab === "parsed" ? "active" : ""}
                onClick={() => setActiveTab("parsed")}
            >
                Parsed Resume
            </button> */}
            <button
                className={activeTab === "analysis" ? "active" : ""}
                onClick={() => setActiveTab("analysis")}
            >
                AI Analysis
            </button>
        </div>
    )
}
export default NavBar;