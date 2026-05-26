# SAP S/4HANA T-Code Assistant

A React + FastAPI application that helps users find SAP S/4HANA transaction codes using natural language.

## Examples

- check material → MM03
- create material → MM01
- change material → MM02
- create purchase order → ME21N
- create production order → CO01
- stock overview → MMBE

## Tech Stack

- Frontend: React, Vite, Tailwind CSS
- Backend: FastAPI, Python
- Search: RapidFuzz
- LLM: OpenRouter API
- Data: SAP S/4HANA T-Code JSON knowledge base

## Project Structure

```text
sap-tcode-assistant/
├── backend/
│   ├── app/
│   ├── data/
│   ├── scripts/
│   ├── .env.example
│   └── requirements.txt
├── frontend/
│   ├── src/
│   └── package.json
├── .gitignore
└── README.md