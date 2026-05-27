Here is the updated `README.md` content. Copy and replace your current `README.md` with this version.

````md
# 🚀 SAP S/4HANA T-Code Assistant

A modern **SAP Transaction Code Assistant** that helps users find the right SAP S/4HANA T-Code from simple natural-language business needs.

Instead of remembering hundreds or thousands of SAP transaction codes, users can simply ask:

> “check material”  
> “create purchase order”  
> “display sales order”  
> “create production order”  
> “stock overview”

And the app returns the best matching SAP T-Code with clear usage instructions, related alternatives, module details, and a confidence score. ✨

---

## 📌 Project Overview

SAP has thousands of transaction codes across modules like **MM, FI, SD, PP, QM, PM, WM, IM, CO, PS, HR**, and more.

For beginners, consultants, support teams, and business users, remembering the correct transaction code can be difficult. This project solves that problem by converting a structured SAP S/4HANA T-Code knowledge base into a searchable assistant.

The system can work in two modes:

1. **Fast Local RAG Mode** ⚡  
   Uses the local `sap_tcodes.json` knowledge base and a deterministic RAG-style response generator.

2. **Optional OpenRouter LLM Mode** 🤖  
   Can be connected to OpenRouter when richer AI-generated explanations are needed.

This makes the project flexible:

- Use **Local RAG** for speed, zero cost, and reliability.
- Use **OpenRouter** when you want more natural, conversational explanations.

---

## 🧠 What This Project Does

The assistant takes a user’s business need and maps it to the best SAP transaction code.

Example:

```text
User: I want to check material details
````

Output:

```text
Recommended T-Code: MM03
Module: Materials Management
Purpose: Display Material

How to use in SAP:
1. Open SAP Easy Access.
2. Enter MM03 in the command field.
3. Press Enter.
4. Enter the material number.
5. Select the required views.
6. Review the material master data.
```

---

## 🎯 Key Features

✅ Search SAP T-Codes using plain English
✅ Get recommended T-Code instantly
✅ See module name, description, and match score
✅ View related alternative T-Codes
✅ Copy T-Code with one click
✅ Local RAG-style explanation generation
✅ Optional OpenRouter LLM support
✅ No mandatory paid API dependency
✅ Clean dark UI with modern dashboard design
✅ Backend API with FastAPI
✅ Frontend built with React, Vite, and Tailwind CSS
✅ Uses structured SAP T-Code JSON data
✅ Works well for SAP beginners, consultants, and support teams

---

## 🧩 RAG Concept Used in This Project

This project uses a simple and practical version of **RAG**, which stands for:

```text
Retrieval-Augmented Generation
```

In simple terms:

> First, the app searches the SAP T-Code knowledge base.
> Then, it generates an answer using only the retrieved matching records.

This avoids random guessing and keeps the result grounded in the local SAP data.

---

## 🔎 Local RAG Flow

```text
User Query
   ↓
React Frontend
   ↓
FastAPI Backend
   ↓
SAP T-Code Search Engine
   ↓
Retrieve Top Matching T-Codes from sap_tcodes.json
   ↓
Local RAG Answer Generator
   ↓
Usage Instructions + Related Codes
```

Example:

```text
User Query: create production order
```

The backend searches `sap_tcodes.json`, retrieves the best matches, and returns:

```text
CO01 - Production Order Create
```

Then the local RAG generator creates beginner-friendly usage instructions.

---

## 🤖 Optional OpenRouter Flow

OpenRouter can be used when you want richer natural-language explanations.

```text
User Query
   ↓
React Frontend
   ↓
FastAPI Backend
   ↓
SAP T-Code Search Engine
   ↓
Retrieve Top Matching T-Codes
   ↓
OpenRouter LLM
   ↓
Polished AI Explanation
```

OpenRouter is optional. The app can run without it.

Use OpenRouter when you want:

* More human-like explanations
* Better phrasing
* More flexible usage guidance
* Advanced reasoning over retrieved T-Code candidates

Use Local RAG when you want:

* Faster responses
* Zero API cost
* No internet dependency
* Predictable output
* Better control over answers

---

## ⚖️ Local RAG vs OpenRouter

| Mode       | Best For                              |             Cost |     Speed | Internet Required |
| ---------- | ------------------------------------- | ---------------: | --------: | ----------------: |
| Local RAG  | Fast T-Code lookup and usage guidance |             Free | Very fast |                No |
| OpenRouter | Richer AI-generated explanations      | Depends on model |    Slower |               Yes |

Recommended approach:

```text
Default: Local RAG
Optional: OpenRouter
```

For the current MVP, **Local RAG is the best choice** because the SAP T-Code data already exists in structured JSON format.

---

## 🧠 Example Searches

| User Search              | Recommended T-Code | Purpose                  |
| ------------------------ | -----------------: | ------------------------ |
| check material           |               MM03 | Display Material         |
| create material          |               MM01 | Create Material          |
| change material          |               MM02 | Change Material          |
| create purchase order    |              ME21N | Create Purchase Order    |
| display purchase order   |              ME23N | Display Purchase Order   |
| create production order  |               CO01 | Production Order Create  |
| display production order |               CO03 | Production Order Display |
| stock overview           |               MMBE | Stock Overview           |
| display sales order      |               VA03 | Display Sales Order      |
| post incoming payment    |               F-28 | Post Incoming Payments   |

---

## 🖼️ Application Flow

### Default Local RAG Flow

```text
User Query
   ↓
React Frontend
   ↓
FastAPI Backend
   ↓
search.py
   ↓
sap_tcodes.json
   ↓
Top Matching SAP T-Codes
   ↓
llm_client.py Local RAG Generator
   ↓
Final Usage Instructions
```

### Optional OpenRouter Flow

```text
User Query
   ↓
React Frontend
   ↓
FastAPI Backend
   ↓
search.py
   ↓
sap_tcodes.json
   ↓
Top Matching SAP T-Codes
   ↓
OpenRouter Model
   ↓
AI-generated Usage Instructions
```

---

## 🏗️ Tech Stack

### Frontend

* React
* Vite
* Tailwind CSS
* Axios
* Lucide React Icons

### Backend

* Python
* FastAPI
* Uvicorn
* RapidFuzz
* Pydantic

### Data Layer

* Markdown source file
* Converted JSON knowledge base
* `sap_tcodes.json`

### Optional AI Layer

* OpenRouter API
* Free or paid OpenRouter models

---

## 📁 Project Structure

```text
sap-tcode-assistant/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── data_loader.py
│   │   ├── search.py
│   │   ├── llm_client.py
│   │   └── schemas.py
│   │
│   ├── data/
│   │   ├── SAP_S4_HANA_T_Code.md
│   │   └── sap_tcodes.json
│   │
│   ├── scripts/
│   │   └── convert_md_to_json.py
│   │
│   ├── requirements.txt
│   └── .env
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
│   ├── postcss.config.js
│   └── vite.config.js
│
└── README.md
```

---

## ⚙️ Backend Setup

Go to the backend folder:

```bash
cd backend
```

Create and activate virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run backend server:

```bash
python -m uvicorn app.main:app --reload
```

Backend runs at:

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

Frontend runs at:

```text
http://localhost:5173
```

---

## 🔐 Optional OpenRouter Setup

OpenRouter is optional. Use it only if you want AI-generated explanations instead of local RAG-style explanations.

Create or update:

```text
backend/.env
```

Add:

```env
OPENROUTER_API_KEY=your_openrouter_api_key_here
OPENROUTER_MODEL=deepseek/deepseek-chat-v3-0324:free
```

Important:

```text
Do not commit your .env file to GitHub.
```

Recommended `.gitignore`:

```gitignore
.env
.venv/
node_modules/
__pycache__/
dist/
```

---

## 🧪 API Endpoints

### Health Check

```http
GET /health
```

Returns backend status and number of loaded records.

### Get Modules

```http
GET /modules
```

Returns available SAP modules.

### Search T-Code

```http
POST /search
```

Example request:

```json
{
  "query": "check material",
  "module": null,
  "top_k": 5
}
```

Example response:

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

## 🧭 How the Search Works

The search engine uses:

* Fuzzy matching
* Business-intent boosts
* Module-aware ranking
* Action-aware ranking
* SAP-specific correction rules

Example:

```text
create production order
```

The system prioritizes:

```text
CO01 - Production Order Create
```

instead of less relevant codes from other modules.

---

## 🧠 Why Local RAG Works Well Here

This project does not need to train a model from scratch.

The SAP T-Code knowledge already exists in a structured format:

```text
T-Code
Description
Module
Module Name
```

So the best design is:

```text
Retrieve the best matching records first.
Then generate an explanation from those retrieved records.
```

This makes the app:

* Faster
* Cheaper
* Easier to debug
* Less likely to hallucinate
* More suitable for SAP lookup use cases

---

## 🚧 Future Enhancements

Planned improvements:

* ⭐ Save favorite T-Codes
* 🕘 Recent search history
* 📦 Module dashboard
* 🔍 Semantic search with embeddings
* 🧠 Optional vector database support
* 🤖 Optional OpenRouter toggle in UI
* 📄 Export usage instructions as PDF
* 🧪 Automated backend tests
* 🛡️ Better authorization and role-based recommendations
* 🌐 Deployment to cloud

---

## 🧪 Suggested Test Queries

Use these to validate the app:

```text
check material
create material
change material
stock overview
create purchase order
display purchase order
create production order
display production order
mrp run
display bom
display sales order
create sales order
display inspection lot
create maintenance order
display equipment
```

---

## 👨‍💻 Author

Built as a practical AI + SAP learning project.

This project demonstrates:

* SAP process knowledge
* Python backend development
* React frontend development
* Local RAG-style architecture
* Optional LLM integration
* Practical AI assistant design

---

## ✅ Current Status

```text
MVP completed
Frontend working
Backend working
SAP JSON data loaded
Local RAG enabled
OpenRouter optional
```

---

## 🌟 Summary

The **SAP S/4HANA T-Code Assistant** helps users quickly find the correct SAP transaction code using simple business language.

It combines:

```text
SAP knowledge base + local search + RAG-style explanation + modern UI
```

This makes SAP navigation easier, faster, and more beginner-friendly. 🚀

```
```
