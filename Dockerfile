FROM python:3.11-slim

# evite que python génère des pycache
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# définit le répertoire de travail
WORKDIR /app

# Copie du dossier source qui contient requirement.txt et le pickle 
COPY src/ src/ 

# bdd qui contient les dataset
COPY bdd/ bdd/ 

# Installe les dépendances présentes dans le requirements.txt
RUN pip install -r src/requirements.txt

# Copie les autres fichiers
COPY app.py /app/


# Commande pour démarrer l'application
CMD ["python", "app.py"]
