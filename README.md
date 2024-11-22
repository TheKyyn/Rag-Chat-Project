<div align="center">

[🇫🇷 Version Française](#version-française-1) | [🇬🇧 English Version](#english-version-1)

</div>

---

<h1 id="version-française-1">Version Française</h1>

# 🤖 RAG Chat Assistant

## 📝 Description
RAG Chat Assistant est une application de chat intelligente qui utilise la technique RAG (Retrieval-Augmented Generation) pour fournir des réponses contextuelles précises. L'application compare les réponses avec et sans RAG, permettant de voir l'impact de la connaissance contextuelle sur les réponses générées.

## ✨ Fonctionnalités
- 🔄 Comparaison en temps réel des réponses avec/sans RAG
- 🌡️ Ajustement de la température du modèle
- ☁️ Intégration avec Google Drive pour le stockage des documents
- 📊 Affichage des sources utilisées dans les réponses
- 🎯 Interface utilisateur intuitive avec Streamlit

## 🛠️ Technologies Utilisées
| Technologie | Version | Description |
|-------------|---------|-------------|
| Python | 3.11+ | Langage de programmation |
| Streamlit | 1.31.0 | Framework d'interface utilisateur |
| LangChain | 0.0.329 | Framework RAG |
| Ollama | Latest | Modèle de langage local |
| Google Drive API | v3 | Stockage cloud |
| ChromaDB | 0.4.15 | Base de données vectorielle |

## 📋 Prérequis
- [x] Python 3.11 ou supérieur
- [x] Ollama installé et configuré
- [x] Compte Google Cloud avec API Drive activée
- [x] Identifiants OAuth 2.0 de Google Cloud

## 🚀 Installation

### 1. Cloner le repository
```bash
git clone https://github.com/votre-username/rag-chat-assistant.git
cd rag-chat-assistant
```


### 2. Créer et activer l'environnement virtuel
<details>
<summary>Unix / macOS</summary>

```bash
python -m venv venv
source venv/bin/activate
```
</details>

<details>
<summary>Windows</summary>

```bash
python -m venv venv
.\venv\Scripts\activate
```
</details>

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configuration de l'environnement
Créer un fichier `.env` à la racine du projet :
```env
GOOGLE_DRIVE_FOLDER_ID="votre_id_de_dossier"
```


### 5. Configuration Google Drive
1. Placer `credentials.json` à la racine
2. Créer un dossier Google Drive pour les documents
3. Mettre l'ID du dossier dans `.env`

## 🎮 Utilisation

### Démarrage des services

1. **Lancer Ollama**
```bash
ollama serve
```


2. **Télécharger le modèle** (nouveau terminal)
```bash
ollama pull llama2
```


3. **Démarrer l'application** (nouveau terminal)
```bash
streamlit run src/streamlit_app.py
```


### Accès à l'interface
> Ouvrir un navigateur et accéder à [http://localhost:8501](http://localhost:8501)

## 📁 Structure du Projet

```markdown
rag_chat_project/
├── src/
│ ├── init.py
│ ├── streamlit_app.py # Interface utilisateur
│ ├── chat_service.py # Service de chat principal
│ ├── rag_service.py # Logique RAG
│ ├── document_loader.py # Chargement des documents
│ ├── google_drive_service.py # Intégration Google Drive
│ └── config.py # Configuration
├── tests/
│ └── test_drive_connection.py
├── .env # Variables d'environnement
├── requirements.txt # Dépendances
└── README.md
```


## 🔧 Configuration

### Google Drive
1. Créer un projet sur [Google Cloud Console](https://console.cloud.google.com)
2. Activer l'API Google Drive
3. Créer des identifiants OAuth 2.0
4. Télécharger `credentials.json`
5. Configurer l'ID du dossier dans `.env`

### Ollama
1. [Installer Ollama](https://ollama.ai)
2. Démarrer le serveur
3. Télécharger le modèle llama2

## 🤝 Contribution
1. Fork le projet
2. Créer une branche
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit les changements
   ```bash
   git commit -m 'feat: Ajout d'une fonctionnalité'
   ```
4. Push vers la branche
   ```bash
   git push origin feature/AmazingFeature
   ```
5. Ouvrir une Pull Request

## 📝 Conventions de Commit
| Type | Description |
|------|-------------|
| `feat` | Nouvelle fonctionnalité |
| `fix` | Correction de bug |
| `docs` | Documentation |
| `style` | Formatage |
| `refactor` | Refactorisation |
| `test` | Tests |
| `chore` | Maintenance |

## 🔒 Sécurité
> ⚠️ **Important**
- Ne jamais commiter `credentials.json`
- Ne pas partager les tokens d'accès
- Garder le fichier `.env` privé

## 📄 Licence
Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 👥 Auteurs
- [TheKyyn](https://github.com/TheKyyn)

---
<p align="center">
  Fait avec ❤️ par Maxime THEOPHILOS
</p>

---

<h1 id="english-version-1">English Version</h1>

# 🤖 RAG Chat Assistant

## 📝 Description
RAG Chat Assistant is an intelligent chat application that uses RAG (Retrieval-Augmented Generation) technique to provide precise contextual responses. The application compares responses with and without RAG, showing the impact of contextual knowledge on generated responses.

## ✨ Features
- 🔄 Real-time comparison of responses with/without RAG
- 🌡️ Model temperature adjustment
- ☁️ Google Drive integration for document storage
- 📊 Display of sources used in responses
- 🎯 Intuitive user interface with Streamlit

## 🛠️ Technologies Used
| Technology | Version | Description |
|-------------|---------|-------------|
| Python | 3.11+ | Programming language |
| Streamlit | 1.31.0 | UI Framework |
| LangChain | 0.0.329 | RAG Framework |
| Ollama | Latest | Local language model |
| Google Drive API | v3 | Cloud storage |
| ChromaDB | 0.4.15 | Vector database |

## 📋 Prerequisites
- [x] Python 3.11 or higher
- [x] Ollama installed and configured
- [x] Google Cloud account with Drive API enabled
- [x] Google Cloud OAuth 2.0 credentials

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/rag-chat-assistant.git
cd rag-chat-assistant
```


### 2. Create and activate virtual environment

<details>
<summary>Unix / macOS</summary>

```bash
python -m venv venv
source venv/bin/activate
```
</details>

<details>
<summary>Windows</summary>

```bash
python -m venv venv
.\venv\Scripts\activate
```
</details>

### 3. Install dependencies

```bash
pip install -r requirements.txt
```


### 4. Environment configuration
Create a `.env` file in the root directory:

```env
GOOGLE_DRIVE_FOLDER_ID="your_folder_id"
```


### 5. Google Drive Configuration
1. Place `credentials.json` in the root directory
2. Create a Google Drive folder for documents
3. Put the folder ID in `.env`

## 🎮 Usage

### Starting services

1. **Launch Ollama**

```bash
ollama serve
```


2. **Download the model** (new terminal)

```bash
ollama pull llama2
```


3. **Start the application** (new terminal)

```bash
streamlit run src/streamlit_app.py
```


### Accessing the interface
> Open a browser and go to [http://localhost:8501](http://localhost:8501)

## 📁 Project Structure

```markdown
rag_chat_project/
├── src/
│ ├── init.py
│ ├── streamlit_app.py # User interface
│ ├── chat_service.py # Main chat service
│ ├── rag_service.py # RAG logic
│ ├── document_loader.py # Document loading
│ ├── google_drive_service.py # Google Drive integration
│ └── config.py # Configuration
├── tests/
│ └── test_drive_connection.py
├── .env # Environment variables
├── requirements.txt # Dependencies
└── README.md
```


## 🔧 Configuration

### Google Drive
1. Create a project on [Google Cloud Console](https://console.cloud.google.com)
2. Enable Google Drive API
3. Create OAuth 2.0 credentials
4. Download `credentials.json`
5. Configure folder ID in `.env`

### Ollama
1. [Install Ollama](https://ollama.ai)
2. Start the server
3. Download the llama2 model

## 🤝 Contributing
1. Fork the project
2. Create a branch
   ```

   git checkout -b feature/AmazingFeature
   ```
3. Commit changes
   ```

   git commit -m 'feat: Add some AmazingFeature'
   ```
4. Push to the branch
   ```

   git push origin feature/AmazingFeature
   ```
5. Open a Pull Request

## 📝 Commit Conventions
| Type | Description |
|------|-------------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation |
| `style` | Formatting |
| `refactor` | Refactoring |
| `test` | Testing |
| `chore` | Maintenance |

## 🔒 Security
> ⚠️ **Important**
- Never commit `credentials.json`
- Don't share access tokens
- Keep `.env` file private

## 📄 License
This project is under MIT license. See [LICENSE](LICENSE) file for details.

## 👥 Authors
- [TheKyyn](https://github.com/TheKyyn)

---
<p align="center">
  Made with ❤️ by Maxime THEOPHILOS
</p>
