from typing import Dict, Tuple
from .llm_service import LLMService
from .rag_service import RAGService

class ChatService:
    def __init__(self):
        self.llm_service = LLMService()
        self.rag_service = RAGService()
        self.rag_service.initialize_vector_store()

    def get_comparison(self, query: str) -> Dict[str, str]:
        """Compare les réponses avec et sans RAG"""
        standard_response = self.llm_service.get_response(query)
        rag_response = self.rag_service.get_response(query)
        
        return {
            "standard": standard_response,
            "rag": rag_response
        }

    def update_temperature(self, temperature: float) -> None:
        """Met à jour la température pour les deux services"""
        self.llm_service.update_parameters({"temperature": temperature})
        self.rag_service.update_parameters(temperature=temperature) 