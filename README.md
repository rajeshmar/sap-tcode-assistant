Absolutely. Replace your current root `README.md` with this polished GitHub version.

Copy everything below and paste it into:

```text
SAP-TCODE-ASSISTANT/README.md
```

````md
# 🚀 SAP S/4HANA T-Code Assistant

A modern **AI-powered SAP Transaction Code Assistant** that helps users find the right SAP S/4HANA T-Code from simple natural-language business needs.

Instead of remembering hundreds of SAP transaction codes, users can simply ask:

> “check material”  
> “create purchase order”  
> “display sales order”  
> “create production order”  
> “stock overview”

And the app returns the best matching SAP T-Code with usage instructions. ✨

---

## 📌 Project Overview

SAP has thousands of transaction codes across modules like MM, FI, SD, PP, QM, PM, WM, and more. Remembering the right T-Code can be difficult, especially for beginners, consultants, support teams, and business users.

This project solves that problem by combining:

- 🔎 Fast local search
- 🧠 AI-generated usage guidance
- 📚 SAP S/4HANA T-Code knowledge base
- 🎨 Clean React + Tailwind UI
- ⚡ FastAPI backend
- 🤖 OpenRouter LLM integration

---

## 🎯 Key Features

✅ Search SAP T-Codes using plain English  
✅ Get recommended T-Code instantly  
✅ See module name, description, and match score  
✅ View related alternative T-Codes  
✅ Copy T-Code with one click  
✅ AI-generated usage instructions  
✅ Clean dark UI with modern dashboard design  
✅ Backend API with FastAPI  
✅ Frontend built with React, Vite, and Tailwind CSS  
✅ Uses structured SAP T-Code JSON data  
✅ OpenRouter model support  

---

## 🧠 Example Searches

| User Search | Recommended T-Code | Purpose |
|---|---:|---|
| check material | MM03 | Display Material |
| create material | MM01 | Create Material |
| change material | MM02 | Change Material |
| create purchase order | ME21N | Create Purchase Order |
| display purchase order | ME23N | Display Purchase Order |
| create production order | CO01 | Production Order Create |
| display production order | CO03 | Production Order Display |
| stock overview | MMBE | Stock Overview |
| display sales order | VA03 | Display Sales Order |
| post incoming payment | F-28 | Post Incoming Payments |

---

## 🖼️ Application Flow

```text
User Query
   ↓
React Frontend
   ↓
FastAPI Backend
   ↓
SAP T-Code Search Engine
   ↓
Top Matching T-Codes
   ↓
OpenRouter LLM
   ↓
Usage Instructions + Related Codes
````

---

## 🏗️ Architecture

```text
sap-tcode-assistant/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── data_loader.py
│   │   ├── search.py
│   │   ├── schemas.py
│   │   └── llm_client.py
│   │
│   ├── data/
│   │   ├── SAP_S4_HANA_T_Code.md
│   │   └── sap_tcodes.json
│   │
│   ├── scripts/
│   │   └── convert_md_to_json.py
│   │
│   ├── .env.example
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   │   └── client.js
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   │
│   ├── package.json
│   ├── tailwind.config.js
│   └── vite.config.js
│
├── .gitignore
└── README.md
```

---

## 🧰 Tech Stack

### Frontend 🎨

* React
* Vite
* Tailwind CSS
* Axios
* Lucide React Icons

### Backend ⚙️

* Python
* FastAPI
* Uvicorn
* Pydantic
* RapidFuzz
* HTTPX
* Python Dotenv

### AI / LLM 🤖

* OpenRouter API
* Free model routing via `openrouter/free`
* Prompt-controlled SAP usage explanation

### Data 📚

* SAP S/4HANA T-Code Markdown source
* Converted structured JSON knowledge base
* 3,750 SAP transaction records

---

## 📂 Data Source

The original SAP S/4HANA T-Code document was converted into structured JSON format.

Each record contains:

```json
{
  "tcode": "MM03",
  "description": "Display Material",
  "module": "MM",
  "module_name": "Materials Management"
}
```

This makes the data easy to search, rank, and pass into the LLM for explanation.

---

## ⚙️ Backend Setup

Go to the backend folder:

```bash
cd backend
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate virtual environment:

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Create your environment file:

```bash
cp .env.example .env
```

Update `backend/.env`:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
OPENROUTER_MODEL=openrouter/free
```

Run backend:

```bash
python -m uvicorn app.main:app --reload
```

Backend will run at:

```text
http://127.0.0.1:8000
```

Health check:

```text
http://127.0.0.1:8000/health
```

Expected response:

```json
{
  "status": "ok",
  "records": 3750
}
```

---

## 🎨 Frontend Setup

Go to the frontend folder:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run frontend:

```bash
npm run dev
```

Frontend will run at:

```text
http://localhost:5173
```

---

## 🚀 Running the Full App

You need two terminals.

### Terminal 1: Backend

```bash
cd backend
source .venv/bin/activate
python -m uvicorn app.main:app --reload
```

### Terminal 2: Frontend

```bash
cd frontend
npm run dev
```

Then open:

```text
http://localhost:5173
```

---

## 🔎 API Endpoints

### Health Check

```http
GET /health
```

Returns backend status and total SAP T-Code records.

### Get Modules

```http
GET /modules
```

Returns available SAP modules.

### Search T-Codes

```http
POST /search
```

Request:

```json
{
  "query": "check material",
  "module": null,
  "top_k": 5
}
```

Response:

```json
{
  "query": "check material",
  "results": [
    {
      "tcode": "MM03",
      "description": "Display Material",
      "module": "MM",
      "module_name": "Materials Management",
      "score": 100
    }
  ],
  "explanation": "Recommended T-Code: MM03..."
}
```

---

## 🧪 Sample Test Queries

Try these in the UI:

```text
check material
create material
change material
create purchase order
display purchase order
create production order
display production order
mrp run
display bom
stock overview
display sales order
post incoming payment
```

---

## 🔐 Security Notes

Never commit real API keys.

This project uses:

```text
backend/.env
```

for local secrets.

The real `.env` file is ignored by Git.

Only this safe file should be committed:

```text
backend/.env.example
```

Example:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
OPENROUTER_MODEL=openrouter/free
```

---

## 🧠 Why Search First, LLM Second?

This app does **not** blindly ask an LLM to guess SAP T-Codes.

Instead, it follows a safer architecture:

```text
User query → Local SAP T-Code search → Top candidates → LLM explanation
```

This reduces hallucination and keeps answers grounded in the actual SAP T-Code dataset.

---

## 🛣️ Future Improvements

Planned enhancements:

* ⭐ Favorite T-Codes
* 🕘 Recent searches
* 📊 Module dashboard
* 🔍 Semantic search with embeddings
* 🧪 Automated test suite
* 📁 Export search result as PDF
* 🧠 Better SAP process synonyms
* 👤 User login
* 🌐 Cloud deployment
* 🔗 ERP integration possibilities

---

## 📚 Learning Outcomes

This project demonstrates:

* Building a real AI application
* Converting unstructured SAP data into structured JSON
* Creating a FastAPI backend
* Building a React + Tailwind frontend
* Implementing fuzzy search with RapidFuzz
* Integrating an LLM through OpenRouter
* Protecting API keys with `.env`
* Preparing a full-stack app for GitHub

---

## 👨‍💻 Author

Built by **Rajesh Kumar Sugumaran** 🚀

A practical AI/ML engineering project focused on SAP, ERP, automation, and intelligent business process assistance.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

Happy building! 🚀

```
```
