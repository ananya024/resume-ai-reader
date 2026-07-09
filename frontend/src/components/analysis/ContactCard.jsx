// ContactCard.jsx

import "../../styles/Card.css";

function ContactCard({ parsedResume }) {

    return (
        <div className="card">

            <h2>Contact Information</h2>

            <p><strong>Name:</strong> {parsedResume.name || "Not Available"}</p>

            <p><strong>Email:</strong> {parsedResume.email || "Not Available"}</p>

            <p><strong>Phone:</strong> {parsedResume.phone || "Not Available"}</p>

            <p><strong>Location:</strong> {parsedResume.location || "Not Available"}</p>

            <p><strong>LinkedIn:</strong> {parsedResume.linkedin || "Not Available"}</p>

            <p><strong>GitHub:</strong> {parsedResume.github || "Not Available"}</p>

            <p><strong>Portfolio:</strong> {parsedResume.portfolio || "Not Available"}</p>

            <p><strong>Professional Summary:</strong></p>

            <p>{parsedResume.professional_summary || "Not Available"}</p>

        </div>
    );
}

export default ContactCard;