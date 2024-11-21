from typing import Dict
from src.llm_service import LLMService
from src.rag_service import RAGService

class ChatService:
    def __init__(self):
        self.llm_service = LLMService()
        self.rag_service = RAGService()
        try:
            self.rag_service.initialize_vector_store()
        except Exception as e:
            print(f"Erreur lors de l'initialisation du RAG: {str(e)}")

    def get_comparison(self, query: str) -> Dict[str, str]:
        """Compare les réponses avec et sans RAG"""
        try:
            standard_response = self.llm_service.get_response(query)
        except Exception as e:
            standard_response = f"Erreur avec le LLM standard: {str(e)}"

        try:
            rag_response = self.rag_service.get_response(query)
        except Exception as e:
            rag_response = f"Erreur avec le RAG: {str(e)}"
        
        return {
            "standard": standard_response,
            "rag": rag_response
        }

    def update_temperature(self, temperature: float) -> None:
        """Met à jour la température pour les deux services"""
        self.llm_service.update_parameters({"temperature": temperature})
        self.rag_service.update_parameters(temperature=temperature) 