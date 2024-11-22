from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import Ollama
from langchain.schema import Document
from typing import List, Optional
from src.document_loader import DocumentLoader
from src.config import Config
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
        self.document_loader = DocumentLoader()

    def initialize_vector_store(self) -> None:
        """Initialise le vector store avec les documents de Google Drive"""
        try:
            documents = self.document_loader.download_and_prepare_documents()
            
            if not documents:
                print("Aucun document trouvé dans Google Drive")
                return

            ids = [str(uuid.uuid4()) for _ in documents]
            
            texts = [doc.page_content for doc in documents]
            metadatas = [doc.metadata for doc in documents]

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
            
            print(f"Vector store initialisé avec {len(documents)} documents")
            
        except Exception as e:
            print(f"Erreur lors de l'initialisation du vector store: {str(e)}")
            self.vector_store = None
            self.qa_chain = None

    def get_response(self, query: str) -> dict:
        """Obtient une réponse en utilisant RAG"""
        if not self.qa_chain:
            return {
                "response": "Le service RAG n'est pas correctement initialisé.",
                "sources": []
            }
        
        try:
            result = self.qa_chain.invoke({"query": query})
            
            if self.vector_store:
                relevant_docs = self.vector_store.similarity_search(query, k=2)
                sources = [doc.metadata.get('source', 'Unknown') for doc in relevant_docs]
            else:
                sources = []
            
            return {
                "response": result["result"],
                "sources": sources
            }
        except Exception as e:
            print(f"Erreur lors de la génération de la réponse RAG: {str(e)}")
            return {
                "response": "Désolé, une erreur s'est produite.",
                "sources": []
            }

    def update_parameters(self, temperature: Optional[float] = None) -> None:
        """Met à jour les paramètres du LLM"""
        if temperature is not None:
            self.llm.temperature = temperature
