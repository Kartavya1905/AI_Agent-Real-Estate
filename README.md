# 🏢 Real Estate AI Agent

An AI-powered conversational assistant for commercial real estate, built using:
- 🧠 Groq LLM (LLaMA 3, Mistral, etc.)
- 🚀 FastAPI for the backend
- 💬 HTML/JavaScript frontend chat interface
- 🗂️ Lightweight CRM module (optional)

---

## 📦 Features

- Conversational chat powered by Groq's blazing fast inference
- Retrieval-ready structure for future document ingestion (RAG)
- API endpoint for LLM (`/chat`) and CRM integration
- Frontend interface to chat in real time

---

## 🚀 Quick Start

### 1. Clone the repo and move inside
```bash
git clone <your-repo-url>
cd AI_Real_Estate
```

### 2. Create a virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set your environment variables
Create a `.env` file in the root with:
```env
GROQ_API_KEY=your-groq-api-key
```

> Get a free Groq API key here: https://console.groq.com/keys

---

### 5. Run the backend server
```bash
uvicorn main:app --reload
```
Then open: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### 6. Launch the frontend
Use a local web server to open the chat UI:

```bash
# In the project folder
python -m http.server 5500
```

Then go to:  
[http://localhost:5500/chat.html](http://localhost:5500/chat.html)

---

## 🧪 API Endpoints

| Method | Endpoint            | Description              |
|--------|---------------------|--------------------------|
| POST   | `/chat`             | Get response from AI     |
| POST   | `/crm/create_user`  | (Optional) Add user info |

---

## 📁 Project Structure

```
AI_Real_Estate/
├── main.py                  # FastAPI app setup
├── .env                     # API keys
├── run.sh                   # Bash script for setup
├── requirements.txt         # Python packages
├── chat.html                # Frontend UI
├── app/
│   ├── api/routes.py        # Routes for /chat, /crm
│   ├── llm/agent.py         # Groq LLM logic
│   ├── crm/models.py        # CRM schema
│   ├── crm/database.py      # CRM logic
│   └── utils/helpers.py     # (Optional) Utilities
```

---

## 🤖 Supported LLMs

You can change the model in `agent.py`:
```python
model="llama3-8b-8192"  # ✅ Fast + capable
```

Other options:
- `"gemma-7b-it"`

Check: [Groq Model Docs](https://console.groq.com/docs/models)

---

## 🙌 Credits

- Built with 💡 using FastAPI + Groq
- Inspired by real-world real estate automation needs

---

## 📬 Contact
Kartavya Mandora
Have questions or feature requests? Open an issue or reach out via email.
kartavyamandora648@gmail.com