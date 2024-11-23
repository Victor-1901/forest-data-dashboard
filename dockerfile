FROM python:3.9-slim

WORKDIR /app

# Copier les fichiers nécessaires dans l'image
COPY ./assets /app/assets
COPY requirements.txt .
COPY new_dashboard_forest_utf8.py .
COPY ./db /app/db

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port par défaut de Streamlit
EXPOSE 8501

# Commande pour démarrer Streamlit
CMD ["streamlit", "run", "new_dashboard_forest_utf8.py", "--server.port=8501", "--server.address=0.0.0.0"]
