# 🤖 Agentic PRD Generator: 10k Review Analyzer

An Agentic AI pipeline that scrapes 10,000+ Play Store reviews, distills them using NLP sentiment analysis, and utilizes a **CrewAI Senior Product Manager Agent** to generate professional Product Requirements Documents (PRDs).

## 🚀 The Agentic Workflow
Unlike simple wrappers, this project uses a multi-stage pipeline:
1.  **Harvester:** Scrapes raw data from Google Play.
2.  **Processor:** Uses `TextBlob` and `Pandas` to perform sentiment analysis, filtering 10,000+ reviews down to the "Crux" (Top 50 Positive/Negative extremes).
3.  **Agent:** A **Gemini 2.0 Flash** powered agent (via CrewAI) acts as a Senior PM to transform pain points into technical features, user stories, and KPIs.

## 🛠️ Tech Stack
- **Framework:** [CrewAI](https://www.crewai.com/)
- **LLM:** Google Gemini 2.0 Flash
- **Analysis:** Pandas, TextBlob (NLP)
- **Data:** Google Play Scraper

## 📦 Installation

1. **Clone the repo:**
   ```bash
   git clone [https://github.com/your-username/playstore-prd-agent.git](https://github.com/your-username/playstore-prd-agent.git)
   cd playstore-prd-agent

## 🛠️ Setup & Installation

### 2. Set up Virtual Environment
Isolate your project dependencies to avoid conflicts.
```powershell
# Create the environment
python -m venv venv

# Activate it (Windows)
.\venv\Scripts\activate

# Activate it (Mac/Linux)
source venv/bin/activate
**
### 📦 3. Install Dependencies**
Install the core AI framework (CrewAI), the Google GenAI SDK, and the NLP tools required for sentiment processing.
```bash
# Install all required libraries
pip install -r requirements.txt

# Download the NLP data for TextBlob sentiment analysis
python -m textblob.download_corpora lite

## ⚙️ 4. Configuration
This project uses a `.env` file to manage sensitive credentials. This ensures your **Paid Gemini API Key** is never hardcoded or uploaded to GitHub.

1. Create a file named `.env` in the root folder.
2. Add your key exactly like this:
```env
GOOGLE_API_KEY=your_actual_gemini_api_key_here

---

## 🤖 Example Agent Output (The PRD)

When the **Senior PM Agent** processes the "Crux" data, it generates a structured Product Requirements Document. Below is a sample of the intelligence the agent provides:

> ### **I. Executive Summary**
> Based on the analysis of 10,000+ reviews, the primary mission is to restore **Transaction Trust**. While the UI/UX is rated 5-stars, the "Financial Loop" (refunds and stuck payments) is currently a 1-star experience for 15% of power users.
>
> ### **II. Critical Pain Points (The "Crux")**
> * **Stuck Transactions:** Users reporting high-value payments (₹40,000+) pending for 5-7 days.
> * **Support Friction:** Automated AI bots are preventing users from reaching human agents for critical financial failures.
> * **Ecommerce Reliability:** One-month shipping delays on the CRED Store without proactive status updates.
>
> ### **III. Feature Requirements**
> * **"Human-in-the-Loop" Escalation:** An automated trigger to connect a user to a live agent if a transaction >₹5,000 stays in "Processing" for >2 hours.
> * **Merchant Escrow System:** Release funds to Store vendors only upon verified delivery to reduce refund "Black Holes."
>
> ### **IV. Success Metrics (KPIs)**
> * **Refund TTR (Time to Resolve):** Aiming for < 24 hours.
> * **User Retention:** Target 15% reduction in "App Uninstalled" mentions related to stuck payments.
