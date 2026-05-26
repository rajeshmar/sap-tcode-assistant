from pydantic import BaseModel, Field


class TCodeResult(BaseModel):
    tcode: str
    description: str
    module: str
    module_name: str
    score: float = Field(ge=0, le=100)


class SearchRequest(BaseModel):
    query: str = Field(min_length=1)
    module: str | None = None
    top_k: int = Field(default=5, ge=1, le=10)


class SearchResponse(BaseModel):
    query: str
    results: list[TCodeResult]
    explanation: str