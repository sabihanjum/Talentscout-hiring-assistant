

# 🤖 TalentScout – AI Hiring Assistant Chatbot

TalentScout is an intelligent AI-powered hiring assistant built using **Streamlit** and **Gemini Pro (Google Generative AI)**. It collects candidate details and generates technical interview questions based on the provided tech stack.

---

## 🚀 Features

- Conversational chatbot interface
- Collects candidate info (name, experience, tech stack, etc.)
- Generates 3–5 technical questions per tech stack
- Graceful fallback and context-aware flow
- Built using Gemini API instead of OpenAI

---

## 📦 Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python + Gemini API (`google-generativeai`)
- **Env Handling**: Python-dotenv
- **Deployment**: Local (optional: Streamlit Cloud)

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/hiring-assistant-gemini.git
cd hiring-assistant-gemini
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Gemini API Key

- Get your API key from [Google MakerSuite](https://makersuite.google.com/app/apikey)
- Create a `.env` file in the root directory:

```
GOOGLE_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📁 Folder Structure

```
.
├── app.py             # Main Streamlit app
├── prompts.py         # Prompt templates
├── utils.py           # Gemini API handler
├── .env               # API key (excluded in Git)
├── requirements.txt   # Dependencies
└── README.md          # Project readme
```

---

## ✨ Prompt Design

Prompts are written to guide the Gemini model to:

- Greet the user and explain the chatbot’s purpose
- Collect structured candidate data
- Generate technical questions for each tech skill
- Respond clearly to unknown or invalid inputs
- End the conversation professionally

---

