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
