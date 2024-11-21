from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from typing import Dict, Optional
from .config import Config

class LLMService:
    def __init__(self, temperature: float = 0.7):
        self.llm = Ollama(
            model=Config.MODEL_NAME,
            base_url=Config.OLLAMA_BASE_URL,
            temperature=temperature,
            callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
        )

    def get_response(self, prompt: str) -> str:
        try:
            return self.llm.invoke(prompt)
        except Exception as e:
            print(f"Erreur lors de l'appel au LLM: {str(e)}")
            return "Désolé, une erreur s'est produite lors de la génération de la réponse."

    def update_parameters(self, parameters: Dict[str, any]) -> None:
        """Mise à jour des paramètres du LLM (température, etc.)"""
        if 'temperature' in parameters:
            self.llm.temperature = parameters['temperature']
