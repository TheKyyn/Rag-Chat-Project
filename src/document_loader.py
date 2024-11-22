from typing import List
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from src.google_drive_service import GoogleDriveService
from src.config import Config

class DocumentLoader:
    def __init__(self):
        self.drive_service = GoogleDriveService()
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=Config.CHUNK_SIZE,
            chunk_overlap=Config.CHUNK_OVERLAP
        )

    def download_and_prepare_documents(self) -> List[Document]:
        try:
            documents = self.drive_service.get_documents()
            
            split_documents = []
            for doc in documents:
                splits = self.text_splitter.split_text(doc.page_content)
                split_documents.extend([
                    Document(
                        page_content=split,
                        metadata=doc.metadata
                    ) for split in splits
                ])
            
            return split_documents
        except Exception as e:
            print(f"Erreur lors du chargement des documents: {str(e)}")
            return [] 