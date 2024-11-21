import unittest
from src.document_loader import DocumentLoader
from src.cloud_storage import S3Storage, get_storage_client

class TestStorage(unittest.TestCase):
    def setUp(self):
        self.loader = DocumentLoader()
        
    def test_document_loading(self):
        documents = self.loader.download_and_prepare_documents()
        self.assertIsNotNone(documents)
        if documents:
            self.assertTrue(len(documents) > 0)
            
    def test_storage_client_creation(self):
        client = get_storage_client()
        self.assertIsInstance(client, S3Storage)

if __name__ == '__main__':
    unittest.main() 