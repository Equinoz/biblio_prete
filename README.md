# Biblio prête  
Plateforme permettant de partager/échanger des livres entre différents utilisateurs  

## Installation et lancement du serveur  
Récupérer le contenu du repository avec la commande:  
``` bash
git clone https://github.com/Equinoz/biblio_prete.git
cd biblio_prete/
```
Puis renseigner les fichiers `env/postgres.env` et `env/server.env`  

Deux façons de lancer le serveur:  
### Via docker:  
`docker-compose up -d`  
Le projet est accessible à l'adresse `http://localhost:8000`  

### En installant le projet localement:  
``` bash
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
django-admin src/manage.py runserver 8000
```
Le projet est également accessible à l'adresse `http://localhost:8000`  