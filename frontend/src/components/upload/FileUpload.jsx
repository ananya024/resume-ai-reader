// FileUpload.jsx

import { useState } from "react";
import {analyseResume} from "../../services/api"
import NavBar from "../common/NavBar"
import Dashboard from "../Dashboard";
import "../../App.css"

function FileUpload(){
    const [selectedFile, setSelectedFile] = useState(null);
    const [resumeAnalysis, setResumeAnalysis] = useState(null);
    const [isLoading, setIsLoading] = useState(false);

    const handleFileChange = (event)=> {
        const file = event.target.files[0];
        if(file){
            setSelectedFile(file);
        }
    };
    const handleUpload = async () => {
        setIsLoading(true);
        try {
            const result = await analyseResume(selectedFile);
            setResumeAnalysis(result);
        } catch (e) {
            console.error(e);
        } finally {
            setIsLoading(false);
        }
    };
    if (isLoading) {
        return (
            <div className="loading-container">

                <div className="loader"></div>

                <h2>Analyzing Resume...</h2>

                <p>Please wait while our AI evaluates your resume.</p>

            </div>
        );
    }
    return (<>
        {!resumeAnalysis 
        ?
            <div className="upload-box">
                <p>Upload a resume and receive AI-powered analysis.</p>
                <input type="file" accept=".pdf" onChange={handleFileChange}/>
                {selectedFile && (<p className="file-name">Selected File: {selectedFile.name}</p>)}
                <button disabled={!selectedFile} onClick={handleUpload}> Upload Resume </button>
            </div>
        :
            <div className="analysis-box">
                {resumeAnalysis && (<Dashboard  analysis={resumeAnalysis}/>)}
            </div>
        }
    </>)
}
export default FileUpload;