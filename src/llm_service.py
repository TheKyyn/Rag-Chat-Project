from langchain.llms import Ollama
from src.config import Config

class LLMService:
    def __init__(self, temperature: float = 0.7):
        self.llm = Ollama(
            model=Config.MODEL_NAME,
            base_url=Config.OLLAMA_BASE_URL,
            temperature=temperature
        )

    def get_response(self, query: str) -> str:
        try:
            return self.llm.invoke(query)
        except Exception as e:
            print(f"Erreur lors de la génération de la réponse: {str(e)}")
            return "Désolé, une erreur s'est produite lors de la génération de la réponse."

    def update_parameters(self, params: dict) -> None:
        if "temperature" in params:
            self.llm.temperature = params["temperature"]
