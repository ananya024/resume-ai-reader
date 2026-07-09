// CertificatesCard.jsx

import "../../styles/Card.css";

function CertificationsCard({ certifications }) {

    return (
        <div className="card">

            <h2>Certifications</h2>

            <ul>

                {certifications.map((certification, index) => (

                    <li key={index}>

                        <strong>{certification.name}</strong>

                        <br />

                        Issuer: {certification.issuer || "Not Available"}

                        <br />

                        Date: {certification.date || "Not Available"}

                    </li>

                ))}

            </ul>

        </div>
    );
}

export default CertificationsCard;