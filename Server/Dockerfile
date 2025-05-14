# Utiliser l'image Python 3.12
FROM python:3.12-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers du projet
COPY . .

# Installer Poetry
RUN pip install poetry

# Installer les dépendances du projet
RUN poetry install

# Exposer le port de Django
EXPOSE 8000

