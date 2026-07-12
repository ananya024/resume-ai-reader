// ExperienceMatchCard.jsx

import "../../styles/Card.css";

function ExperienceMatchCard({ experience }) {
    if (!experience) return null;

    const { resume_years = 0, required_years = 0, matched = false, reason = "", score = 0 } = experience;

    return (
        <div className="card">
            <h2>Experience Matching</h2>
            
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

            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "15px", marginTop: "15px", borderBottom: "1px solid #edf2f7", paddingBottom: "15px" }}>
                <div style={{ textAlign: "center", backgroundColor: "#f7fafc", padding: "10px", borderRadius: "6px" }}>
                    <span style={{ fontSize: "0.8rem", color: "#718096", fontWeight: "bold" }}>Candidate Experience</span>
                    <span style={{ display: "block", fontSize: "1.8rem", fontWeight: "bold", color: "#2d3748", marginTop: "4px" }}>
                        {resume_years} {resume_years === 1 ? "Year" : "Years"}
                    </span>
                </div>
                <div style={{ textAlign: "center", backgroundColor: "#f7fafc", padding: "10px", borderRadius: "6px" }}>
                    <span style={{ fontSize: "0.8rem", color: "#718096", fontWeight: "bold" }}>Required Experience</span>
                    <span style={{ display: "block", fontSize: "1.8rem", fontWeight: "bold", color: "#2d3748", marginTop: "4px" }}>
                        {required_years} {required_years === 1 ? "Year" : "Years"}
                    </span>
                </div>
            </div>

            <div style={{ marginTop: "15px" }}>
                <span style={{ fontSize: "0.85rem", color: "#718096", fontWeight: "bold", display: "block" }}>
                    Evaluation Details:
                </span>
                <span style={{ fontSize: "0.95rem", color: "#4a5568", display: "block", marginTop: "4px", lineHeight: "1.5" }}>
                    {reason}
                </span>
            </div>
        </div>
    );
}

export default ExperienceMatchCard;
