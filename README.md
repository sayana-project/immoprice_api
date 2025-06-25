# 🏡 Estimation du prix au m² - Lille & Bordeaux

Projet de Data Science visant à prédire le **prix au m²** de biens immobiliers (maisons/appartements) dans deux villes françaises : **Lille** et **Bordeaux**.

---

## 🚀 Phase 1 – Analyse et modélisation pour Lille

### Objectifs
- Prétraitement des données DVF (Demande de Valeurs Foncières) pour Lille.
- Création de modèles de régression pour prédire le prix au m² :
  - Appartements
  - Maisons
- Analyse des performances via des métriques (MSE, RMSE, R²) et visualisations.

### Modèles utilisés
- **Régression linéaire**
- **Random Forest Regressor**
- **Gradient Boosting**

### Variables sélectionnées
- `surface_bati`
- `surface_terrain`
- `nombre_pieces`
- `nombre_lots`
- `type_local`

### Résultats
- Visualisations des performances sur les jeux de test.
- Comparaison des modèles via courbes et barplots.

---

## 🏙️ Phase 2 – Réplication sur Bordeaux

### Objectifs
- Reprise du pipeline de Lille pour l’adapter aux données de Bordeaux.
- Réentraînement des modèles sur Bordeaux.
- Comparaison entre Lille et Bordeaux.

### Résultats obtenus
- Mêmes modèles, mêmes variables.
- Évaluation comparative via barplots :
  - MSE
  - RMSE
  - R²

---

## 🌐 Phase 3 – API REST FastAPI

### Objectif
Fournir un **service d’estimation automatisé** via une API REST basée sur les modèles de Lille et Bordeaux.

### Structure du projet

```
.
├── app/
│   ├── main.py            # Lancement de l’API
│   ├── models/            # Chargement des modèles et scalers
│   ├── routes/            # Définition des routes FastAPI
│   └── schemas/           # Schémas Pydantic pour validation des entrées
├── models/                # Fichiers .pkl des modèles
├── requirements.txt       # Dépendances
└── README.md              # Ce fichier
```

### 📌 Endpoints disponibles

#### 🔹 `/predict/lille` – Prédiction pour Lille
```json
{
  "surface_bati": 100,
  "nombre_pieces": 4,
  "type_local": "Appartement",
  "surface_terrain": 0,
  "nombre_lots": 1
}
```

#### 🔹 `/predict/bordeaux` – Prédiction pour Bordeaux
```json
{
  "surface_bati": 120,
  "nombre_pieces": 5,
  "type_local": "Maison",
  "surface_terrain": 200,
  "nombre_lots": 2
}
```

#### 🔹 `/predict` – Endpoint dynamique
```json
{
  "ville": "lille",
  "features": {
    "surface_bati": 90,
    "nombre_pieces": 3,
    "type_local": "Appartement",
    "surface_terrain": 0,
    "nombre_lots": 1
  }
}
```

### ✅ Exemple de réponse
```json
{
  "prix_m2_estime": 3820.75,
  "ville_modele": "Lille",
  "model": "RandomForestRegressor"
}
```

### ✅ Gestion des erreurs
- Vérification de la présence et du type des variables.
- Gestion des noms de ville incorrects.
- Messages explicites en cas d’erreur.

---

## 🧪 Tests
- Fonctionnement de l’API testé via Postman / Swagger UI.
- Requêtes de test fournies si nécessaire.

---

## 📦 Installation

1. Cloner le dépôt :
```bash
git clone https://github.com/sayana-project/immoprice_api.git
cd immoprice_api
```

2. Installer les dépendances :
```bash
pip install -r requirements.txt
```

3. Lancer l'API :
```bash
uvicorn app.main:app --reload
```

4. Accéder à la documentation interactive :
[http://localhost:8000/docs](http://localhost:8000/docs)

---

## ✍️ Auteurs
Projet réalisé dans le cadre de la formation développeur IA - Simplon, 2025.

---