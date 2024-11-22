FROM python:3.11-slim

WORKDIR /app

# Installation des dépendances système
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Copie des fichiers du projet
COPY requirements.txt .
COPY src/ ./src/
COPY .env .

# Installation des dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Exposition du port Streamlit
EXPOSE 8501

# Commande de démarrage
CMD ["streamlit", "run", "src/streamlit_app.py"] 