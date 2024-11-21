import os
from typing import List
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from .cloud_storage import get_storage_client
from .config import Config

class DocumentLoader:
    def __init__(self):
        self.storage_client = get_storage_client()
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=Config.CHUNK_SIZE,
            chunk_overlap=Config.CHUNK_OVERLAP
        )

    def download_and_prepare_documents(self, cloud_prefix: str = "") -> List[Document]:
        os.makedirs("data/documents", exist_ok=True)
        
        cloud_files = self.storage_client.list_files(prefix=cloud_prefix)
        documents = []
        
        for cloud_path in cloud_files:
            local_path = f"data/documents/{os.path.basename(cloud_path)}"
            if self.storage_client.download_file(cloud_path, local_path):
                with open(local_path, 'r', encoding='utf-8') as f:
                    text = f.read()
                    doc = Document(
                        page_content=text,
                        metadata={"source": cloud_path}
                    )
                    documents.append(doc)

        if documents:
            return self.text_splitter.split_documents(documents)
        return [] 