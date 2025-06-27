from joblib import load
from pathlib import Path

# Point d'accès racine du projet
root_path = Path(__file__).resolve().parents[1]

# Chargement des modèles et scalers
model_appt = load(root_path / "models" / "model_regression_apartement.pkl")
scaler_X_appt = load(root_path / "models" / "scaler_X_apartement.pkl")

model_house = load(root_path / "models" / "model_regression_house.pkl")
scaler_X_house = load(root_path / "models" / "scaler_X_house.pkl")
