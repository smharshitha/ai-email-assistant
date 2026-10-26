"""Email drafting API with a safe deterministic baseline."""
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="AI Email Assistant", version="0.1.0")

class DraftRequest(BaseModel):
    purpose: str = Field(min_length=3, max_length=500)
    recipient_context: str = Field(default="", max_length=1000)
    key_points: list[str] = Field(default_factory=list, max_length=12)
    tone: str = Field(default="professional", pattern="^(professional|friendly|formal|concise)$")

class DraftResponse(BaseModel):
    subject: str
    body: str
    provider: str

def deterministic_draft(req: DraftRequest) -> DraftResponse:
    points = "\n".join(f"- {p}" for p in req.key_points) or "- [Add the key details]"
    greeting = "Hello,"
    closing = "Best regards,"
    body = (f"{greeting}\n\n{req.purpose.strip()}\n\n"
            f"Key details:\n{points}\n\n{closing}\n[Your name]")
    return DraftResponse(subject="Draft: " + req.purpose[:70], body=body, provider="template")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/draft", response_model=DraftResponse)
def draft_email(req: DraftRequest):
    # Replace this adapter with a hosted/local LLM, preserving user review.
    return deterministic_draft(req)
