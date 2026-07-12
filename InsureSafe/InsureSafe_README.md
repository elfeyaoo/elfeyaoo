# InsureSafe — AI-Powered Policy Recommendation & Customer Service Portal

InsureSafe is an intelligent insurance platform that automates policy recommendation, identity verification, document validation, and claims processing using AI and computer vision — replacing slow, manual, fraud-prone insurance workflows with a faster, secure, and personalized digital experience.

> Final-year major project | A. P. Shah Institute of Technology, Mumbai University
> Team: Avadhoot Virkar, Chinmay Pawaskar, Atharva Nimkar | Guide: Ms. Poonam Pangarkar

---

## 🧩 Problem

The insurance industry today still struggles with:
- Lack of **personalized policy recommendations** for customers
- **Manual identity and document verification**, prone to human error and delay
- Rising **fraudulent claims**, with no automated way to flag them
- Outdated, siloed systems that make customer data hard to access
- Ineffective chatbots and non-user-friendly insurance portals

InsureSafe was built to solve these problems with a single AI-driven platform.

---

## ✨ Key Features

- **Policy Recommendation Engine** — Suggests suitable insurance plans based on user data such as age, income, and lifestyle.
- **Facial Verification Module** — Uses **DeepFace** to match a live selfie against stored user data for secure identity validation during policy issuance.
- **Document Verification Module** — Uses **OCR** to extract and validate Aadhaar/identity document details for compliance and fraud detection.
- **AI-Assisted Claims Processing** — Uses **YOLO11** for vehicle damage detection from uploaded images, enabling automatic claim approval, rejection, or flagging for review.
- **Separate Dashboards** — Dedicated views for customers and administrators for easy policy and claims management.

---

## 🛠 Tech Stack

**Frontend**
- HTML5, CSS3, JavaScript
- Bootstrap 5.3.7

**Backend**
- Python 3.13.1
- Flask 3.1.2
- MongoDB 1.46.11

**AI / ML Models**
- **DeepFace** — facial verification
- **OCR (Optical Character Recognition)** — document data extraction & validation
- **YOLO11** — vehicle damage detection & fraud analysis

---

## ⚙️ How It Works

1. **Policy Selection** — User provides basic details (age, income, lifestyle); the recommendation engine suggests the most relevant policies.
2. **Identity Verification** — User takes a live selfie, which DeepFace compares against their stored photo/ID to confirm identity.
3. **Document Verification** — Uploaded identity documents (e.g., Aadhaar) are processed through OCR to extract and validate details automatically.
4. **Policy Issuance** — Once identity and documents are verified, the policy is issued digitally.
5. **Claims Processing** — When a claim is filed, uploaded images (e.g., of vehicle damage) are analyzed using YOLO11 to detect and assess damage; the system automatically approves, rejects, or flags the claim for manual review based on the analysis.
6. **Dashboards** — Customers track their policies/claims from their dashboard; admins manage and review flagged cases from theirs.

*(Add your system architecture / module diagram image here — e.g. `![Architecture](assets/architecture.png)`)*

---

## 📸 Screenshots

> Add screenshots from your prototype demo here for each module, e.g.:

| Module | Preview |
|---|---|
| Landing Page | `![Landing Page](assets/landing.png)` |
| Face Verification | `![Face Verification](assets/face-verification.png)` |
| Policies Page | `![Policies](assets/policies.png)` |
| Claim Application | `![Claim Application](assets/claim-application.png)` |
| AI Claims Processing | `![AI Claims](assets/ai-claims.png)` |
| Admin Panel | `![Admin Panel](assets/admin-panel.png)` |
| Profile Page | `![Profile Page](assets/profile.png)` |

*(Export the relevant slides/images from your PPT as PNGs and drop them in an `assets/` folder, then swap in the paths above.)*

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
*(Adjust these commands to match your actual project structure, and add a `requirements.txt` if you haven't already — this makes the repo runnable for anyone who clones it, including recruiters.)*

---

## 🌍 Impact

InsureSafe aligns with **UN SDG 9: Industry, Innovation, and Infrastructure** — by applying AI (facial verification, document intelligence, and automated claims analysis) to modernize insurance infrastructure, making it faster, safer, and more accessible.

---

## 🔮 Future Scope

- Extend fraud detection to additional claim types beyond vehicle damage
- Add multilingual support for the chatbot/customer service layer
- Integrate real-time analytics dashboards for admins
- Deploy models via a scalable inference service (e.g., containerized microservices)

---

## 👥 Team

- **Avadhoot Virkar** — [GitHub](https://github.com/elfeyaoo)
- **Chinmay Pawaskar**
- **Atharva Nimkar**

*Project Guide: Ms. Poonam Pangarkar*

---

## 📄 License

*(Add a license if you intend for others to reuse this code — MIT is a common choice for student/portfolio projects.)*
