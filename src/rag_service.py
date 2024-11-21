from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import Ollama
from langchain.schema import Document
from typing import List, Optional
from .config import Config
import uuid

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

    def initialize_vector_store(self, documents: List[Document] = None) -> None:
        """Initialise ou met à jour le vector store avec les documents"""
        if documents is None:
            documents = [
                Document(
                    page_content="Python est un langage de programmation interprété, multi-paradigme et multiplateformes. Il favorise la programmation impérative structurée, fonctionnelle et orientée objet.",
                    metadata={"source": "python_info.txt", "id": str(uuid.uuid4())}
                ),
                Document(
                    page_content="JavaScript est un langage de programmation de scripts principalement employé dans les pages web interactives. C'est un langage orienté objet à prototype.",
                    metadata={"source": "javascript_info.txt", "id": str(uuid.uuid4())}
                )
            ]

        try:
            texts = [doc.page_content for doc in documents]
            metadatas = [doc.metadata for doc in documents]
            ids = [str(uuid.uuid4()) for _ in documents]

            self.vector_store = Chroma.from_texts(
                texts=texts,
                embedding=self.embeddings,
                persist_directory=Config.VECTOR_STORE_PATH,
                metadatas=metadatas,
                ids=ids
            )
            
            self.qa_chain = RetrievalQA.from_chain_type(
                llm=self.llm,
                chain_type="stuff",
                retriever=self.vector_store.as_retriever(
                    search_kwargs={"k": 3}
                )
            )
        except Exception as e:
            print(f"Erreur lors de l'initialisation du vector store: {str(e)}")
            self.vector_store = None
            self.qa_chain = None

    def get_response(self, query: str) -> str:
        """Obtient une réponse en utilisant RAG"""
        if not self.qa_chain:
            return "Le service RAG n'est pas correctement initialisé. Utilisation du LLM standard."
        
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
