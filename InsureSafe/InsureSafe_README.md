# InsureSafe — AI-Powered Policy Recommendation & Customer Service Portal

> An intelligent insurance platform that automates policy recommendation, identity verification, and claims processing using AI/ML.

---

## 📌 Overview

The insurance industry today struggles with slow verification, lack of personalized recommendations, and rising fraud. **InsureSafe** solves this by combining a policy recommendation engine, facial verification, document (OCR) verification, and AI-assisted claims processing into a single platform — with separate dashboards for customers and admins.

---

## ❗ Problem This Solves

- Manual, paperwork-heavy verification causing delays in claims and policy approval
- No personalized policy recommendations — users pick blind
- Weak fraud detection in existing systems
- Ineffective chatbot support and poor user experience on legacy insurance platforms
- Outdated, siloed systems that slow down access to customer data

## 🎯 Objectives

- Recommend suitable insurance policies based on user demographics (age, income, lifestyle)
- Verify identity securely using facial recognition (live selfie vs. stored photo)
- Extract and validate identity documents (e.g., Aadhaar) using OCR
- Detect vehicle damage and flag/approve/reject claims automatically using computer vision
- Provide separate, purpose-built dashboards for customers and administrators

---

## 🧠 AI/ML Models Used

**DeepFace** — Facial verification; matches a live selfie against the stored user photo for identity validation.

**OCR (Optical Character Recognition)** — Extracts and validates details from uploaded identity documents (e.g., Aadhaar).

**YOLO11** — Detects vehicle damage from uploaded claim images and assists in fraud analysis and cost estimation.

**Performance metrics** :

```
DeepFace verification accuracy:       98 %  (tested on ___ sample pairs)
OCR extraction accuracy:              76 %  (tested on ___ documents)
YOLO11 damage detection mAP/accuracy: 90 %  (tested on ___ images)
Average claim processing time:        9-10 seconds 
False positive/fraud-flag rate:       98 %
```

---

## 🛠️ Technology Stack

**Frontend:**
- HTML5, CSS3, JavaScript
- Bootstrap 5.3.7

**Backend:**
- Python 3.13.1
- Flask 3.1.2
- MongoDB 1.46.11

**AI/ML:**
- DeepFace (facial verification)
- OCR (document verification)
- YOLO11 (damage detection)

---

## ⚙️ How It Works

1. **Policy Selection** — User provides basic details (age, income, lifestyle); the recommendation engine suggests the most relevant policies.
2. **Identity Verification** — User takes a live selfie, which DeepFace compares against their stored photo/ID to confirm identity.
3. **Document Verification** — Uploaded identity documents (e.g., Aadhaar) are processed through OCR to extract and validate details automatically.
4. **Policy Issuance** — Once identity and documents are verified, the policy is issued digitally.
5. **Claims Processing** — When a claim is filed, uploaded images (e.g., of vehicle damage) are analyzed using YOLO11 to detect and assess damage; the system automatically approves, rejects, or flags the claim for manual review.
6. **Dashboards** — Customers track their policies/claims from their dashboard; admins manage and review flagged cases from theirs.

---

## 🏗️ System Architecture

![alt text](image-7.png)


---

## 📸 Screenshots

<!-- Paste each screenshot below its heading -->
![alt text](image.png)
### Landing Page

![alt text](image-1.png)
### Face Verification

![alt text](image-2.png)
### Policies Page

![alt text](image-3.png)
### Application for Policies

![alt text](image-4.png)
### AI Claims Processing

![alt text](image-5.png)
### Admin Panel

![alt text](image-6.png)
### Profile Page


---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/elfeyaoo/My-Projects.git
cd My-Projects/InsureSafe

# Create a virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables (MongoDB URI, model paths, etc.)
cp .env.example .env

# Run the application
flask run
```

## 🌍 Impact

InsureSafe aligns with **UN SDG 9: Industry, Innovation, and Infrastructure** — by applying AI (facial verification, document intelligence, and automated claims analysis) to modernize insurance infrastructure, making it faster, safer, and more accessible.

---

## 🔮 Future Scope

- Extend fraud detection to additional claim types beyond vehicle damage
- Add multilingual support for the chatbot/customer service layer
- Integrate real-time analytics dashboards for admins
- Deploy models via a scalable inference service (e.g., containerized microservices)

---

## 📄 License

*(Add a license if you intend for others to reuse this code — MIT is a common choice for student/portfolio projects.)*
