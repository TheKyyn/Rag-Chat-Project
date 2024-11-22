from google_drive_service import GoogleDriveService
from dotenv import load_dotenv
import os

def test_drive_connection():
    load_dotenv()
    
    folder_id = os.getenv('GOOGLE_DRIVE_FOLDER_ID')
    if not folder_id:
        print("❌ GOOGLE_DRIVE_FOLDER_ID n'est pas défini dans le fichier .env")
        return False
    
    print(f"📁 Utilisation du dossier Google Drive: {folder_id}")
    
    try:
        drive_service = GoogleDriveService()
        files = drive_service.list_files()
        
        if not files:
            print("\n⚠️ Aucun fichier trouvé dans le dossier")
            return False
            
        print("\n📄 Fichiers trouvés dans le dossier Google Drive :")
        print("--------------------------------------------")
        for file in files:
            print(f"📌 Nom: {file['name']}")
            print(f"🔑 ID: {file['id']}")
            print(f"📎 Type: {file['mimeType']}")
            print("--------------------------------------------")
        
        text_files = [f for f in files if f['mimeType'] == 'text/plain']
        if text_files:
            content = drive_service.download_file(text_files[0]['id'])
            print("\n📝 Contenu du premier fichier texte :")
            print("--------------------------------------------")
            print(content[:500] + "..." if len(content) > 500 else content)
        
        return True
    except Exception as e:
        print(f"\n❌ Erreur lors de la connexion à Google Drive : {str(e)}")
        return False

if __name__ == "__main__":
    print("🔄 Test de connexion à Google Drive...")
    success = test_drive_connection()
    if success:
        print("\n✅ Connexion et lecture des fichiers réussies !")
    else:
        print("\n❌ Échec de la connexion ou de la lecture des fichiers.") 