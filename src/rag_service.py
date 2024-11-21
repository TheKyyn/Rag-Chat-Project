from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import Ollama
from typing import List, Optional
from .config import Config
from .document_loader import DocumentLoader

class RAGService:
    def __init__(self, temperature: float = 0.7):
        self.embeddings = OllamaEmbeddings(
            model=Config.MODEL_NAME,
            base_url=Config.OLLAMA_BASE_URL
        )
        self.llm = Ollama(
            model=Config.MODEL_NAME,
            base_url=Config.OLLAMA_BASE_URL,
            temperature=temperature
        )
        self.vector_store = None
        self.qa_chain = None

    def initialize_vector_store(self, documents: List = None) -> None:
        """Initialise ou met à jour le vector store avec les documents"""
        if documents is None:
            loader = DocumentLoader()
            documents = loader.download_and_prepare_documents()

        self.vector_store = Chroma.from_documents(
            documents=documents,
            embedding=self.embeddings,
            persist_directory=Config.VECTOR_STORE_PATH
        )
        
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vector_store.as_retriever(
                search_kwargs={"k": 3}
            )
        )

    def get_response(self, query: str) -> str:
        """Obtient une réponse en utilisant RAG"""
        if not self.qa_chain:
            return "Erreur: Le service RAG n'est pas initialisé. Appelez initialize_vector_store d'abord."
        
        try:
            result = self.qa_chain.invoke({"query": query})
            return result["result"]
        except Exception as e:
            print(f"Erreur lors de la génération de la réponse RAG: {str(e)}")
            return "Désolé, une erreur s'est produite lors de la génération de la réponse."

    def update_parameters(self, temperature: Optional[float] = None) -> None:
        """Met à jour les paramètres du LLM"""
        if temperature is not None:
            self.llm.temperature = temperature
