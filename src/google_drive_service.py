from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import os
import io
import pickle
from typing import List
from langchain.schema import Document

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

class GoogleDriveService:
    def __init__(self):
        self.creds = None
        self.FOLDER_ID = os.getenv('GOOGLE_DRIVE_FOLDER_ID')
        if not self.FOLDER_ID:
            raise ValueError("GOOGLE_DRIVE_FOLDER_ID n'est pas défini dans le fichier .env")
        self._authenticate()

    def _authenticate(self):
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                self.creds = pickle.load(token)

        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                self.creds = flow.run_local_server(port=0)
            
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.creds, token)

        self.service = build('drive', 'v3', credentials=self.creds)

    def list_files(self) -> List[dict]:
        try:
            print(f"Recherche de fichiers dans le dossier: {self.FOLDER_ID}")
            results = self.service.files().list(
                q=f"'{self.FOLDER_ID}' in parents and trashed=false",
                pageSize=10,
                fields="nextPageToken, files(id, name, mimeType)"
            ).execute()
            files = results.get('files', [])
            print(f"Nombre de fichiers trouvés: {len(files)}")
            return files
        except Exception as e:
            print(f"Erreur lors de la liste des fichiers: {str(e)}")
            raise

    def download_file(self, file_id: str) -> str:
        request = self.service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
        return fh.getvalue().decode('utf-8')

    def get_documents(self) -> List[Document]:
        documents = []
        files = self.list_files()
        
        for file in files:
            if file['mimeType'] == 'text/plain':
                content = self.download_file(file['id'])
                documents.append(
                    Document(
                        page_content=content,
                        metadata={"source": file['name']}
                    )
                )
        
        return documents 