// FileUpload.jsx

import { useState } from "react";
import { analyseResume } from "../../services/api";
import NavBar from "../common/NavBar";
import Dashboard from "../Dashboard";
import "../../App.css";

function FileUpload() {
    const [selectedFile, setSelectedFile] = useState(null);
    const [selectedJDFile, setSelectedJDFile] = useState(null);
    const [resumeAnalysis, setResumeAnalysis] = useState(null);
    const [isLoading, setIsLoading] = useState(false);

    const handleFileChange = (event) => {
        const file = event.target.files[0];
        if (file) {
            setSelectedFile(file);
        }
    };

    const handleJDFileChange = (event) => {
        const file = event.target.files[0];
        if (file) {
            setSelectedJDFile(file);
        }
    };

    const handleUpload = async () => {
        if (!selectedFile || !selectedJDFile) {
            alert("Please upload both Resume and Job Description PDFs.");
            return;
        }

        setIsLoading(true);
        try {
            const result = await analyseResume(selectedFile, selectedJDFile);
            setResumeAnalysis(result);
        } catch (e) {
            console.error(e);
            alert("An error occurred during analysis. Please try again.");
        } finally {
            setIsLoading(false);
        }
    };


    if (isLoading) {
        return (
            <div className="loading-container">
                <div className="loader"></div>
                <h2>Analyzing Resume against JD...</h2>
                <p>Please wait while our NLP models evaluate your profile alignment.</p>
            </div>
        );
    }

    return (
        <>
            {!resumeAnalysis ? (
                <div className="upload-box">
                    <p style={{ fontWeight: "600", fontSize: "1.1rem" }}>
                        Upload your Resume & Job Description to see the match metrics.
                    </p>
                                      
                    <div style={{ margin: "20px 0", textAlign: "left" }}>
                        <label style={{ display: "block", marginBottom: "8px", fontWeight: "bold" }}>
                            Resume PDF:
                        </label>
                        <input type="file" accept=".pdf" onChange={handleFileChange} />
                        {selectedFile && (
                            <p className="file-name" style={{ marginTop: "4px" }}>
                                Selected: {selectedFile.name}
                            </p>
                        )}
                    </div>

                    <div style={{ margin: "20px 0", textAlign: "left" }}>
                        <label style={{ display: "block", marginBottom: "8px", fontWeight: "bold" }}>
                            Job Description (JD) PDF:
                        </label>
                        <input type="file" accept=".pdf" onChange={handleJDFileChange} />
                        {selectedJDFile && (
                            <p className="file-name" style={{ marginTop: "4px" }}>
                                Selected: {selectedJDFile.name}
                            </p>
                        )}
                    </div>

                    <button 
                        disabled={!selectedFile || !selectedJDFile} 
                        onClick={handleUpload}
                        style={{ marginTop: "10px", width: "100%", padding: "12px" }}
                    > 
                        Upload & Analyze  
                    </button>
                </div>
            ) : (
                <div className="analysis-box">
                    {resumeAnalysis && <Dashboard analysis={resumeAnalysis} />}
                </div>
            )}
        </>
    );
}

export default FileUpload;