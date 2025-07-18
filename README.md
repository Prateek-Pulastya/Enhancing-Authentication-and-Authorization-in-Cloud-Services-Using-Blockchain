# Enhancing-Authentication-and-Authorization-in-Cloud-Services-Using-Blockchain
Master's Thesis
Here is a detailed summary of my MSc research thesis titled:

---

## **Title:**

**Blockchain-Based Identity and Authentication for Cloud Services**

---

## **Summary**

### **1. Objective**

The research investigates how blockchain technology, specifically **Self-Sovereign Identity (SSI)** frameworks, can enhance **authentication and identity management** in cloud computing environments. The goal is to overcome challenges like centralization, data breaches, and lack of user control in traditional cloud authentication systems.

---

### **2. Background and Motivation**

Traditional identity systems (like OAuth, SAML, OpenID) rely on centralized authorities, making them vulnerable to:

* Single points of failure
* Data leaks
* Identity theft

The COVID-19 pandemic and rise of remote work have further highlighted the need for **decentralized, secure, and privacy-preserving** identity solutions.

---

### **3. Proposed Solution**

The project proposes using a **blockchain-based SSI model** built on **Hyperledger Indy** and **Aries**. This allows users to:

* Control their own identity credentials
* Authenticate to cloud services securely without revealing excessive personal data
* Avoid dependence on third-party identity providers

---

### **4. Technologies Used**

* **Hyperledger Indy**: A blockchain for decentralized identity
* **Hyperledger Aries**: Middleware for issuing/verifying credentials
* **Trinsic**: API-based platform for SSI management
* **DIDComm**: Communication protocol between digital wallets
* **AnonCreds**: Privacy-preserving verifiable credentials
* **Python, Docker, Postman**: Tools used for implementation and testing

---

### **5. System Architecture**

The system involves three main actors:

* **Issuer** (e.g., university or company): Issues verifiable credentials
* **Holder** (user): Stores credentials in a digital wallet
* **Verifier** (cloud service): Requests proof for authentication

Workflow:

1. Issuer issues credentials via DID and Indy ledger
2. Holder stores credentials in Trinsic wallet
3. Verifier sends proof request → holder presents verifiable proof
4. Authentication completed based on cryptographic trust

---

### **6. Results and Evaluation**

* The prototype system was successfully implemented.
* Real-time issuance and verification of credentials worked.
* SSI showed improved user control, reduced identity theft risks, and removed the need for centralized authentication systems.

**Strengths Identified:**

* Better privacy and data minimization
* Reduced risk of phishing
* Transparent and auditable identity flows

---

### **7. Limitations**

* Performance testing was minimal.
* Integration with existing cloud platforms (like AWS, Azure) remains to be fully developed.
* Usability for non-technical users could be improved.

---

### **8. Conclusion**

The research demonstrates that SSI on blockchain is a **viable alternative to centralized identity** in the cloud. It improves security, privacy, and control while reducing reliance on intermediaries. It lays the groundwork for further exploration of scalable, interoperable identity systems using blockchain for real-world cloud ecosystems.

---

### **9. Future Work**

* Integration with mainstream cloud services (e.g., AWS IAM)
* Improved performance benchmarking
* Incorporation of Zero-Knowledge Proofs (ZKPs) for enhanced privacy
* Development of user-friendly digital wallet interfaces
* Study of regulatory and compliance implications (e.g., GDPR)
