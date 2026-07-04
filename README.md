# Sample FastAPI + SQLAlchemy + SQLite

Projet de démonstration d'une API REST avec FastAPI, SQLAlchemy et SQLite, organisé en architecture DAL (Data Access Layer).

## Architecture

```
├── api/
│   ├── controllers/         # Logique métier et gestion des erreurs
│   ├── routes/              # Endpoints FastAPI (routeurs)
│   ├── schemas/             # Schémas Pydantic (validation entrée/sortie)
│   └── app.py               # Point d'entrée de l'application
├── dal/
│   ├── repositories/        # Accès aux données (pattern Repository)
│   ├── models/              # Modèles SQLAlchemy (tables)
│   └── database.py          # Connexion et session SQLAlchemy
├── .env                     # Variables d'environnement
├── .gitignore
└── requirements.txt
```

### Flux d'une requête

```
Route → Controller → Repository → Modèle SQLAlchemy → SQLite
```

| Couche        | Rôle                                                      |
|---------------|-----------------------------------------------------------|
| `routes`      | Déclare les endpoints, délègue au controller              |
| `controllers` | Logique métier, lève les `HTTPException`                  |
| `repositories`| Requêtes SQL via SQLAlchemy, abstrait la base de données  |
| `models`      | Définition des tables (ORM)                               |
| `schemas`     | Validation des données entrantes/sortantes (Pydantic)     |

## Prérequis

- Python 3.11 ou supérieur
- pip

## Installation

### 1. Cloner ou télécharger le projet

```bash
git clone <url-du-repo>
cd sample-sqlalchemy-fastapi-sqlite
```

### 2. Créer un environnement virtuel

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python -m venv .venv
source .venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configurer les variables d'environnement

Le fichier `.env` est déjà présent avec la configuration par défaut :

```env
DATABASE_URL=sqlite:///./app.db
```

La base de données SQLite `app.db` sera créée automatiquement au premier lancement.

## Lancer l'application

```bash
uvicorn api.app:app --reload
```

Le serveur démarre sur `http://127.0.0.1:8000`.

| URL                           | Description                              |
|-------------------------------|------------------------------------------|
| `http://127.0.0.1:8000/`      | Message de bienvenue                     |
| `http://127.0.0.1:8000/docs`  | Swagger UI (documentation interactive)   |
| `http://127.0.0.1:8000/redoc` | ReDoc (documentation alternative)        |

## Endpoints disponibles

### Users

| Méthode  | URL                    | Description                               |
|----------|------------------------|-------------------------------------------|
| `GET`    | `/api/v1/users/`       | Lister tous les utilisateurs              |
| `GET`    | `/api/v1/users/{id}`   | Récupérer un utilisateur (+ ses exemples) |
| `POST`   | `/api/v1/users/`       | Créer un utilisateur                      |
| `PATCH`  | `/api/v1/users/{id}`   | Modifier un utilisateur                   |
| `DELETE` | `/api/v1/users/{id}`   | Supprimer un utilisateur                  |

### Exemples

| Méthode  | URL                       | Description                     |
|----------|---------------------------|---------------------------------|
| `GET`    | `/api/v1/exemples/`       | Lister tous les exemples        |
| `GET`    | `/api/v1/exemples/{id}`   | Récupérer un exemple            |
| `POST`   | `/api/v1/exemples/`       | Créer un exemple                |
| `PATCH`  | `/api/v1/exemples/{id}`   | Modifier un exemple             |
| `DELETE` | `/api/v1/exemples/{id}`   | Supprimer un exemple            |

## Exemple d'utilisation rapide

```bash
# Créer un utilisateur
curl -X POST http://127.0.0.1:8000/api/v1/users/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice", "email": "alice@example.com"}'

# Créer un exemple lié à cet utilisateur (owner_id: 1)
curl -X POST http://127.0.0.1:8000/api/v1/exemples/ \
  -H "Content-Type: application/json" \
  -d '{"titre": "Mon premier exemple", "description": "Description optionnelle", "owner_id": 1}'

# Lister les utilisateurs
curl http://127.0.0.1:8000/api/v1/users/

# Voir un utilisateur avec ses exemples
curl http://127.0.0.1:8000/api/v1/users/1
```
