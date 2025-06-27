from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict_valid_lille():
    data = {
        "surface_bati": 60,
        "nombre_pieces": 3,
        "nombre_lots": 12,
        "type_local": "appartement"
    }
    response = client.post("/predict/lille/", json=data)
    assert response.status_code == 200
    json = response.json()
    assert json["ville"].lower() == "Lille".lower()
    assert json["type_local"] == "appartement"
    assert isinstance(json["prediction m²"], float)

def test_predict_invalid_city():
    data = {
        "surface_bati": 50,
        "nombre_pieces": 2,
        "nombre_lots": 6,
        "type_local": "appartement"
    }
    response = client.post("/predict/?city=paris", json=data)
    assert response.status_code == 400
    assert "Ville inconnue" in response.json()["detail"]

def test_predict_missing_field():
    data = {
        "surface_bati": 50,
        "type_local": "maison"
    }
    response = client.post("/predict/lille/", json=data)
    assert response.status_code == 422
    details = response.json()["detail"]
    
    # Vérifie que le champ "nombre_pieces" est bien signalé comme manquant
    assert any(
        d["loc"][-1] == "nombre_pieces" and d["msg"] == "Field required"
        for d in details
    )
    
    # Vérifie aussi "nombre_lots"
    assert any(
        d["loc"][-1] == "nombre_lots" and d["msg"] == "Field required"
        for d in details
    )