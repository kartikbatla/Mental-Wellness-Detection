**🧠 MindFlow – AI Powered Mental Wellness Journal**
MindFlow is an AI-powered mental wellness monitoring system that analyzes user journal entries and emotional check-ins to assess mental well-being. The system combines Natural Language Processing, questionnaire analysis, and emotional trend tracking to generate wellness scores, detect stress patterns, and provide personalized recommendations.

This project demonstrates the integration of Machine Learning, Full-Stack Development, and Data Analysis to create a digital mental wellness assistant.

**🚀 Features**
- **📝 AI Journal Analysis** - Users can write daily journal entries describing their thoughts and emotions. The system analyzes the text using emotion detection models.
- **📊 Emotional Check-in Questionnaire**
Users answer a short psychological questionnaire that evaluates:
1. Stress 
2. Emotional stability 
3. Mental exhaustion 
4. Emotional support 
5. Anxiety levels

**🧠 Mental Wellness Scoring**
The system calculates a combined wellness score using: 
-Emotion detection from journal 
-Psychological questionnaire results

**⚠️ Early Stress Detection**
The application identifies early signs of stress patterns using emotional trend analysis.

**📈 Weekly Emotional Dashboard**

Users can visualize their emotional trends through:

-Emotion distribution charts
-Wellness score trends 
-Stress pattern detection 
-Weekly insights

**💡 Personalized Recommendations**
Based on the analysis, the system generates mental wellness recommendations such as:

-relaxation techniques 
-mindfulness practices 
-behavioral improvements

**✨ Motivational Quotes**

The home page displays motivational quotes based on the user’s emotional condition.

🏗 System Architecture User 
       │ 
       ▼ 
React Frontend (Vite) 
       │ 
       ▼ 
FastAPI Backend 
│ 
├── Emotion Prediction Model 
├── Questionnaire Analysis 
├── Wellness Score Engine 
├── Weekly Analytics Engine 
        │ 
        ▼ 
SQLite Database

⚙️ Tech Stack Frontend - React (Vite), JavaScript, React Router, Chart.js / Recharts

Backend - FastAPI, Python, Machine Learning, Scikit-learn, NLTK, Pandas, NumPy

Database - SQLite

📂 Project Structure

<img width="421" height="684" alt="image" src="https://github.com/user-attachments/assets/5a91b786-c8b6-40b3-8152-c1149a8197f0" />

📊 Machine Learning Workflow 
1️⃣ Emotion Prediction - The journal text is analyzed using an emotion classification model to detect emotions such as:

joy
sadness
anger
fear
surprise
love

2️⃣ Emotional Trend Analysis

The system tracks emotional changes over time to compute:

emotional stability index
stress probability
emotional patterns

3️⃣ Questionnaire Analysis

The questionnaire responses are scored and normalized to produce a mental wellness score.

4️⃣ Combined Wellness Score Final Wellness Score = Emotion Score + Questionnaire Score

This score determines the user’s mental wellness status.

📈 Weekly Analysis

The system performs weekly analytics including:

emotion distribution
average wellness score
stress trend
emotional stability index
This information is displayed on the dashboard using interactive charts.

