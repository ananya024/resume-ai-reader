// OverallExplanationCard.jsx

import "../../styles/Card.css";

function OverallExplanationCard({ overall_score, overall_explanation }) {
    if (!overall_explanation) return null;

    const { 
        weighted_calculation = "", 
        final_explanation = "", 
        strongest_areas = [], 
        weakest_areas = [], 
        contributions = {} 
    } = overall_explanation;

    return (
        <div className="card" style={{ gridColumn: "1 / -1", backgroundColor: "#f8fafc", border: "1px solid #e2e8f0" }}>
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", borderBottom: "2px solid #cbd5e1", paddingBottom: "15px", flexWrap: "wrap", gap: "20px" }}>
                <div>
                    <h1 style={{ fontSize: "2.2rem", margin: "0", color: "#1e293b" }}>Overall Compatibility</h1>
                    <p style={{ margin: "5px 0 0 0", color: "#64748b", fontStyle: "italic" }}>
                        Calculation Formula: {weighted_calculation}
                    </p>
                </div>
                <div style={{ 
                    display: "flex", 
                    flexDirection: "column", 
                    alignItems: "center", 
                    backgroundColor: "#1e3a8a", 
                    color: "#ffffff", 
                    padding: "15px 30px", 
                    borderRadius: "12px", 
                    boxShadow: "0 4px 6px -1px rgba(0, 0, 0, 0.1)" 
                }}>
                    <span style={{ fontSize: "2.8rem", fontWeight: "bold" }}>{overall_score}</span>
                    <span style={{ fontSize: "0.85rem", textTransform: "uppercase", letterSpacing: "1px", opacity: "0.9" }}>Match Score</span>
                </div>
            </div>

            <div style={{ margin: "20px 0" }}>
                <h3 style={{ margin: "0 0 10px 0", color: "#334155" }}>Executive Summary</h3>
                <p style={{ lineHeight: "1.7", fontSize: "1.05rem", color: "#475569", whiteSpace: "pre-line" }}>
                    {final_explanation}
                </p>
            </div>

            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "20px", margin: "20px 0" }}>
                <div style={{ backgroundColor: "#f0fff4", border: "1px solid #c6f6d5", padding: "15px", borderRadius: "8px" }}>
                    <h4 style={{ margin: "0 0 10px 0", color: "#22543d", display: "flex", alignItems: "center" }}>
                        <span style={{ marginRight: "6px" }}>▲</span> Strongest Areas
                    </h4>
                    <div style={{ display: "flex", flexWrap: "wrap", gap: "8px" }}>
                        {strongest_areas.map((area, idx) => (
                            <span key={idx} style={{ padding: "4px 10px", backgroundColor: "#c6f6d5", color: "#22543d", borderRadius: "15px", fontSize: "0.85rem", fontWeight: "bold" }}>
                                {area}
                            </span>
                        ))}
                    </div>
                </div>

                <div style={{ backgroundColor: "#fff5f5", border: "1px solid #fed7d7", padding: "15px", borderRadius: "8px" }}>
                    <h4 style={{ margin: "0 0 10px 0", color: "#742a2a", display: "flex", alignItems: "center" }}>
                        <span style={{ marginRight: "6px" }}>▼</span> Weakest Areas
                    </h4>
                    <div style={{ display: "flex", flexWrap: "wrap", gap: "8px" }}>
                        {weakest_areas.length > 0 ? (
                            weakest_areas.map((area, idx) => (
                                <span key={idx} style={{ padding: "4px 10px", backgroundColor: "#fed7d7", color: "#742a2a", borderRadius: "15px", fontSize: "0.85rem", fontWeight: "bold" }}>
                                    {area}
                                </span>
                            ))
                        ) : (
                            <span style={{ padding: "4px 10px", backgroundColor: "#c6f6d5", color: "#22543d", borderRadius: "15px", fontSize: "0.85rem", fontWeight: "bold" }}>
                                None (Well-rounded profile)
                            </span>
                        )}
                    </div>
                </div>
            </div>

            <div style={{ marginTop: "25px" }}>
                <h3 style={{ margin: "0 0 15px 0", color: "#334155" }}>Weighted Score Breakdown</h3>
                <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))", gap: "15px" }}>
                    <div style={{ border: "1px solid #e2e8f0", padding: "15px", borderRadius: "8px", backgroundColor: "#ffffff" }}>
                        <div style={{ fontSize: "0.9rem", color: "#64748b", fontWeight: "bold" }}>Technical Skills (45%)</div>
                        <div style={{ fontSize: "1.8rem", fontWeight: "bold", color: "#0f172a", marginTop: "5px" }}>
                            {contributions.skills} <span style={{ fontSize: "0.9rem", color: "#64748b" }}>/ 45.00</span>
                        </div>
                    </div>
                    <div style={{ border: "1px solid #e2e8f0", padding: "15px", borderRadius: "8px", backgroundColor: "#ffffff" }}>
                        <div style={{ fontSize: "0.9rem", color: "#64748b", fontWeight: "bold" }}>Experience (25%)</div>
                        <div style={{ fontSize: "1.8rem", fontWeight: "bold", color: "#0f172a", marginTop: "5px" }}>
                            {contributions.experience} <span style={{ fontSize: "0.9rem", color: "#64748b" }}>/ 25.00</span>
                        </div>
                    </div>
                    <div style={{ border: "1px solid #e2e8f0", padding: "15px", borderRadius: "8px", backgroundColor: "#ffffff" }}>
                        <div style={{ fontSize: "0.9rem", color: "#64748b", fontWeight: "bold" }}>Project Alignment (20%)</div>
                        <div style={{ fontSize: "1.8rem", fontWeight: "bold", color: "#0f172a", marginTop: "5px" }}>
                            {contributions.projects} <span style={{ fontSize: "0.9rem", color: "#64748b" }}>/ 20.00</span>
                        </div>
                    </div>
                    <div style={{ border: "1px solid #e2e8f0", padding: "15px", borderRadius: "8px", backgroundColor: "#ffffff" }}>
                        <div style={{ fontSize: "0.9rem", color: "#64748b", fontWeight: "bold" }}>Education (10%)</div>
                        <div style={{ fontSize: "1.8rem", fontWeight: "bold", color: "#0f172a", marginTop: "5px" }}>
                            {contributions.education} <span style={{ fontSize: "0.9rem", color: "#64748b" }}>/ 10.00</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default OverallExplanationCard;
