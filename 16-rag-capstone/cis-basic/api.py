from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from assistants.policy_agent_enhanced import build_assistant

# Initialize FastAPI
app = FastAPI(
    title="CIS Policy Intelligence API",
    version="1.0.0"
)

# Build the assistant once at startup
assistant = build_assistant()


class QueryRequest(BaseModel):
    query: str


class QueryResponse(BaseModel):
    answer: str


@app.post("/ask", response_model=QueryResponse)
def ask(request: QueryRequest):
    try:
        result = assistant(request.query)

        # Expected structure:
        # {
        #   "query": "...",
        #   "answer": "...",
        #   "source_docs": ...,
        #   "type": ...
        # }

        answer = result.get("answer")

        if answer is None:
            raise HTTPException(
                status_code=500,
                detail="Assistant did not return an answer."
            )

        return {"answer": answer}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
