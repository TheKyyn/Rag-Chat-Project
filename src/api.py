from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Optional

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "RAG Chat API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

class QueryRequest(BaseModel):
    query: str
    temperature: Optional[float] = 0.7

@app.post("/chat")
async def chat(request: QueryRequest):
    try:
        return {"response": f"Vous avez demandé: {request.query}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 