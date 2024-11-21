from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Optional
from .chat_service import ChatService

app = FastAPI(title="RAG Chat API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

chat_service = ChatService()

class QueryRequest(BaseModel):
    query: str
    temperature: Optional[float] = 0.7

class TemperatureUpdate(BaseModel):
    temperature: float

@app.post("/chat/compare")
async def compare_responses(request: QueryRequest) -> Dict[str, str]:
    """Compare les réponses avec et sans RAG"""
    try:
        if request.temperature != chat_service.llm_service.llm.temperature:
            chat_service.update_temperature(request.temperature)
        
        responses = chat_service.get_comparison(request.query)
        return responses
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/update-temperature")
async def update_temperature(request: TemperatureUpdate):
    """Met à jour la température des modèles"""
    try:
        chat_service.update_temperature(request.temperature)
        return {"message": "Température mise à jour avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    """Vérifie l'état de l'API"""
    return {"status": "healthy"} 