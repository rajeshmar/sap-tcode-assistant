from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.data_loader import load_tcodes
from app.llm_client import LLMClientError, generate_tcode_explanation
from app.schemas import SearchRequest, SearchResponse
from app.search import search_tcodes


app = FastAPI(title="SAP T-Code Assistant API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

TCODE_RECORDS = load_tcodes()


@app.get("/health")
def health_check() -> dict:
    return {
        "status": "ok",
        "records": len(TCODE_RECORDS),
    }


@app.get("/modules")
def get_modules() -> list[dict]:
    modules = {}

    for row in TCODE_RECORDS:
        modules[row["module"]] = row["module_name"]

    return [
        {"code": code, "name": name}
        for code, name in sorted(modules.items())
    ]


@app.post("/search", response_model=SearchResponse)
async def search(request: SearchRequest) -> SearchResponse:
    results = search_tcodes(
        query=request.query,
        records=TCODE_RECORDS,
        module=request.module,
        top_k=request.top_k,
    )

    if not results:
        return SearchResponse(
            query=request.query,
            results=[],
            explanation="No matching SAP T-Code found. Try a more specific business process.",
        )

    try:
        explanation = await generate_tcode_explanation(request.query, results)
    except LLMClientError as error:
        raise HTTPException(status_code=500, detail=str(error)) from error

    return SearchResponse(
        query=request.query,
        results=results,
        explanation=explanation,
    )