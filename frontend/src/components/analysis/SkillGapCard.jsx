// SkillGapCard.jsx

import "../../styles/Card.css";

function SkillGapCard({ skills }) {
    if (!skills) return null;

    const { matched = [], missing = [], extra = [], category_matches = {}, score = 0 } = skills;

    return (
        <div className="card">
            <h2>Skills Gap Analysis</h2>
            
            <div className="score" style={{ fontSize: "2rem", margin: "10px 0", color: "#3182ce" }}>
                {score}% Match
            </div>

            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "20px", marginTop: "15px" }}>
                <div>
                    <h3 style={{ color: "#2f855a", borderBottom: "2px solid #c6f6d5", paddingBottom: "4px" }}>
                        Matched Skills ({matched.length})
                    </h3>
                    {matched.length > 0 ? (
                        <ul className="strength-list" style={{ paddingLeft: "20px" }}>
                            {matched.map((item, index) => (
                                <li key={index} style={{ margin: "4px 0" }}>{item}</li>
                            ))}
                        </ul>
                    ) : (
                        <p style={{ fontStyle: "italic" }}>None</p>
                    )}
                </div>

                <div>
                    <h3 style={{ color: "#c53030", borderBottom: "2px solid #fed7d7", paddingBottom: "4px" }}>
                        Missing Skills ({missing.length})
                    </h3>
                    {missing.length > 0 ? (
                        <ul style={{ paddingLeft: "20px" }}>
                            {missing.map((item, index) => (
                                <li key={index} style={{ margin: "4px 0", color: "#e53e3e" }}>{item}</li>
                            ))}
                        </ul>
                    ) : (
                        <p style={{ fontStyle: "italic", color: "#38a169" }}>No missing skills!</p>
                    )}
                </div>
            </div>

            <div style={{ marginTop: "20px" }}>
                <h3 style={{ borderBottom: "1px solid #e2e8f0", paddingBottom: "4px" }}>
                    Hierarchical Category Alignment
                </h3>
                <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(200px, 1fr))", gap: "10px", marginTop: "10px" }}>
                    {Object.entries(category_matches).map(([category, isMatched], idx) => (
                        <div 
                            key={idx} 
                            style={{ 
                                display: "flex", 
                                alignItems: "center", 
                                padding: "8px 12px", 
                                borderRadius: "6px",
                                border: isMatched ? "1px solid #c6f6d5" : "1px solid #edf2f7",
                                backgroundColor: isMatched ? "#f0fff4" : "#f7fafc"
                            }}
                        >
                            <span style={{ 
                                marginRight: "8px", 
                                color: isMatched ? "#38a169" : "#a0aec0",
                                fontWeight: "bold"
                            }}>
                                {isMatched ? "✓" : "✗"}
                            </span>
                            <span style={{ fontSize: "0.9rem", color: isMatched ? "#22543d" : "#4a5568" }}>
                                {category}
                            </span>
                        </div>
                    ))}
                </div>
            </div>

            {extra.length > 0 && (
                <div style={{ marginTop: "20px" }}>
                    <h3 style={{ color: "#4a5568", borderBottom: "1px solid #e2e8f0", paddingBottom: "4px" }}>
                        Additional Candidate Skills ({extra.length})
                    </h3>
                    <div style={{ display: "flex", flexWrap: "wrap", gap: "8px", marginTop: "10px" }}>
                        {extra.map((item, index) => (
                            <span 
                                key={index} 
                                style={{ 
                                    padding: "4px 10px", 
                                    backgroundColor: "#edf2f7", 
                                    borderRadius: "15px", 
                                    fontSize: "0.85rem",
                                    color: "#4a5568"
                                }}
                            >
                                {item}
                            </span>
                        ))}
                    </div>
                </div>
            )}
        </div>
    );
}

export default SkillGapCard;