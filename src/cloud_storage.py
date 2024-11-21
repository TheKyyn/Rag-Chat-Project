from abc import ABC, abstractmethod
import boto3
from typing import List, BinaryIO
from .config import Config

class CloudStorageInterface(ABC):
    @abstractmethod
    def upload_file(self, file_path: str, destination_path: str) -> bool:
        pass
    
    @abstractmethod
    def download_file(self, cloud_path: str, local_path: str) -> bool:
        pass
    
    @abstractmethod
    def list_files(self, prefix: str = "") -> List[str]:
        pass

class S3Storage(CloudStorageInterface):
    def __init__(self):
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=Config.AWS_ACCESS_KEY,
            aws_secret_access_key=Config.AWS_SECRET_KEY
        )
        self.bucket_name = Config.AWS_BUCKET_NAME

    def upload_file(self, file_path: str, destination_path: str) -> bool:
        try:
            self.s3_client.upload_file(file_path, self.bucket_name, destination_path)
            return True
        except Exception as e:
            print(f"Erreur lors de l'upload: {str(e)}")
            return False

    def download_file(self, cloud_path: str, local_path: str) -> bool:
        try:
            self.s3_client.download_file(self.bucket_name, cloud_path, local_path)
            return True
        except Exception as e:
            print(f"Erreur lors du téléchargement: {str(e)}")
            return False

    def list_files(self, prefix: str = "") -> List[str]:
        try:
            response = self.s3_client.list_objects_v2(
                Bucket=self.bucket_name,
                Prefix=prefix
            )
            return [obj['Key'] for obj in response.get('Contents', [])]
        except Exception as e:
            print(f"Erreur lors de la liste des fichiers: {str(e)}")
            return []

def get_storage_client(provider: str = "s3") -> CloudStorageInterface:
    if provider.lower() == "s3":
        return S3Storage()
    raise ValueError(f"Provider de stockage non supporté: {provider}")
