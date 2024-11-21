import os
from typing import List
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from src.cloud_storage import get_storage_client
from src.config import Config

class DocumentLoader:
    def __init__(self):
        self.storage_client = get_storage_client()
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=Config.CHUNK_SIZE,
            chunk_overlap=Config.CHUNK_OVERLAP
        )

    def download_and_prepare_documents(self, cloud_prefix: str = "") -> List[Document]:
        return [
            Document(
                page_content="Python est un langage de programmation interprété, multi-paradigme et multiplateformes.",
                metadata={"source": "python_info.txt"}
            ),
            Document(
                page_content="JavaScript est un langage de programmation de scripts principalement employé dans les pages web.",
                metadata={"source": "javascript_info.txt"}
            )
        ] 