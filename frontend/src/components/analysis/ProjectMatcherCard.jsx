// ProjectMatcherCard.jsx

import "../../styles/Card.css";

function ProjectMatcherCard({ projects }) {
    if (!projects) return null;

    const { 
        matched_topics = [], 
        missing_topics = [], 
        top_matches = [], 
        similarity = 0, 
        reason = "", 
        score = 0 
    } = projects;

    return (
        <div className="card">
            <h2>Project Alignment Analysis</h2>
            
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", margin: "10px 0" }}>
                <div className="score" style={{ fontSize: "2rem", color: "#3182ce" }}>
                    {score}% Match
                </div>
                <div style={{ fontSize: "0.9rem", color: "#718096", border: "1px solid #e2e8f0", padding: "4px 10px", borderRadius: "15px" }}>
                    Max Similarity: {similarity}%
                </div>
            </div>

            <p style={{ lineHeight: "1.6", color: "#4a5568", backgroundColor: "#f7fafc", padding: "10px 15px", borderRadius: "6px", borderLeft: "4px solid #3182ce" }}>
                <strong>Assessment:</strong> {reason}
            </p>

            <div style={{ marginTop: "20px" }}>
                <h3 style={{ borderBottom: "1px solid #e2e8f0", paddingBottom: "6px" }}>Itemized Project Evaluations</h3>
                {top_matches.length > 0 ? (
                    <div style={{ display: "flex", flexDirection: "column", gap: "15px", marginTop: "10px" }}>
                        {top_matches.map((item, index) => (
                            <div 
                                key={index} 
                                style={{ 
                                    border: "1px solid #edf2f7", 
                                    padding: "12px 15px", 
                                    borderRadius: "8px", 
                                    backgroundColor: item.matched ? "#fff" : "#fff" 
                                }}
                            >
                                <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start" }}>
                                    <h4 style={{ margin: "0", color: "#2d3748", fontSize: "1.05rem" }}>{item.project}</h4>
                                    <span style={{ 
                                        fontSize: "0.8rem", 
                                        fontWeight: "bold",
                                        padding: "2px 8px", 
                                        borderRadius: "10px",
                                        backgroundColor: item.matched ? "#c6f6d5" : "#fee2e2",
                                        color: item.matched ? "#22543d" : "#991b1b"
                                    }}>
                                        {item.similarity}% Sim
                                    </span>
                                </div>
                                <p style={{ margin: "8px 0 0 0", fontSize: "0.9rem", color: "#4a5568" }}>
                                    <strong>Matched Responsibility:</strong> {item.matched_responsibility}
                                </p>
                                <p style={{ margin: "4px 0 0 0", fontSize: "0.85rem", color: "#718096", fontStyle: "italic" }}>
                                    {item.reason}
                                </p>
                            </div>
                        ))}
                    </div>
                ) : (
                    <p style={{ fontStyle: "italic" }}>No projects extracted from the resume.</p>
                )}
            </div>

            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "20px", marginTop: "25px" }}>
                <div>
                    <h3 style={{ color: "#2f855a", borderBottom: "2px solid #c6f6d5", paddingBottom: "4px" }}>
                        Matched Responsibilities ({matched_topics.length})
                    </h3>
                    {matched_topics.length > 0 ? (
                        <ul style={{ paddingLeft: "20px" }}>
                            {matched_topics.map((topic, index) => (
                                <li key={index} style={{ margin: "6px 0", fontSize: "0.9rem", color: "#276749" }}>
                                    {topic}
                                </li>
                            ))}
                        </ul>
                    ) : (
                        <p style={{ fontStyle: "italic" }}>None</p>
                    )}
                </div>

                <div>
                    <h3 style={{ color: "#c53030", borderBottom: "2px solid #fed7d7", paddingBottom: "4px" }}>
                        Uncovered Responsibilities ({missing_topics.length})
                    </h3>
                    {missing_topics.length > 0 ? (
                        <ul style={{ paddingLeft: "20px" }}>
                            {missing_topics.map((topic, index) => (
                                <li key={index} style={{ margin: "6px 0", fontSize: "0.9rem", color: "#9b2c2c" }}>
                                    {topic}
                                </li>
                            ))}
                        </ul>
                    ) : (
                        <p style={{ fontStyle: "italic", color: "#38a169" }}>All responsibilities matched by projects!</p>
                    )}
                </div>
            </div>
        </div>
    );
}

export default ProjectMatcherCard;
