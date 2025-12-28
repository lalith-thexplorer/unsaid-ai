# Unsaid
*A space for what you can’t say out loud.*

Unsaid is a **privacy-first, non-medical AI emotional support web app**.  
It helps users express difficult emotions through empathetic listening, gentle coping suggestions, and short-term emotional reflection — **without login, tracking, or diagnosis**.

Built for moments when talking feels hard, but staying silent feels heavier.

---

## 🧠 Problem Statement

Many people struggle with stress, anxiety, or emotional overload but hesitate to talk about it due to:
- Fear of judgment  
- Difficulty expressing feelings  
- Privacy concerns  
- Stigma around mental health  

Existing solutions often feel **clinical, intrusive, or overwhelming**.

**Unsaid lowers the barrier to expression** by offering a calm, anonymous, and supportive space — focused on **listening, not fixing**.

---

## ✨ Key Features

- 😊 **Mood Badge Check-In**  
  Express how you feel using simple emoji-based moods  

- 💬 **Empathetic AI Chat**  
  Active listening without diagnosis or advice overload  

- 🧘 **Gentle Coping Suggestions**  
  Optional, short grounding actions  

- 🚨 **Crisis-Aware Safety Support**  
  Transparent guidance toward real-world help  

- 📊 **Short-Term Mood Insights**  
  Visual reflection, not heavy analytics  

- 📄 **Reflection Export**  
  Shareable summary for personal or professional use  

---

## 🛠️ Tech Stack

- **Frontend & App Framework:** Streamlit (Python)  
- **AI Engine:** Gemini 1.5 Flash API  
- **Data Visualization:** Plotly  
- **Export:** FPDF / HTML  
- **Storage:** Local session state (privacy-first)  

---

## 🚀 Getting Started (Local Setup)

### Prerequisites
- Python 3.9+
- Git

### Run the App
```bat
git clone https://github.com/<your-username>/unsaid-ai.git
cd unsaid-ai
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
