// EducationMatchCard.jsx

import "../../styles/Card.css";

function EducationMatchCard({ education }) {
    if (!education) return null;

    const { resume = "", required = "", matched = false, reason = "", score = 0 } = education;

    return (
        <div className="card">
            <h2>Education Qualification Matching</h2>
            
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", margin: "10px 0" }}>
                <div className="score" style={{ fontSize: "2rem", color: "#3182ce" }}>
                    {score}% Score
                </div>
                <div style={{ 
                    fontSize: "0.85rem", 
                    fontWeight: "bold",
                    padding: "4px 12px", 
                    borderRadius: "15px",
                    backgroundColor: matched ? "#c6f6d5" : "#fee2e2",
                    color: matched ? "#22543d" : "#991b1b"
                }}>
                    {matched ? "✓ Met Requirements" : "✗ Requirements Not Met"}
                </div>
            </div>

            <div style={{ display: "flex", flexDirection: "column", gap: "12px", marginTop: "15px" }}>
                <div style={{ borderBottom: "1px solid #edf2f7", paddingBottom: "10px" }}>
                    <span style={{ fontSize: "0.85rem", color: "#718096", fontWeight: "bold", display: "block" }}>
                        Extracted Candidate Education:
                    </span>
                    <span style={{ fontSize: "0.95rem", color: "#2d3748", whiteSpace: "pre-line", display: "block", marginTop: "4px" }}>
                        {resume}
                    </span>
                </div>

                <div style={{ borderBottom: "1px solid #edf2f7", paddingBottom: "10px" }}>
                    <span style={{ fontSize: "0.85rem", color: "#718096", fontWeight: "bold", display: "block" }}>
                        Job Description Requirements:
                    </span>
                    <span style={{ fontSize: "0.95rem", color: "#2d3748", display: "block", marginTop: "4px" }}>
                        {required}
                    </span>
                </div>

                <div>
                    <span style={{ fontSize: "0.85rem", color: "#718096", fontWeight: "bold", display: "block" }}>
                        Evaluation Details:
                    </span>
                    <span style={{ fontSize: "0.95rem", color: "#4a5568", display: "block", marginTop: "4px", lineHeight: "1.5" }}>
                        {reason}
                    </span>
                </div>
            </div>
        </div>
    );
}

export default EducationMatchCard;
