from app.predict import Predict
import pytest

pytestmark = pytest.mark.asyncio
predict=Predict()

class TestPredictPrice:

    async def test_predict_valid_appartement_lille(self):
        data = {
            "surface_bati": 45,
            "nombre_pieces": 2,
            "nombre_lots": 10,
            "type_local": "appartement"
        }
        city = "lille"
        prediction, type_local, model,data = await predict.predict_price(data, city)
        assert isinstance(prediction, float)
        assert type_local == "appartement"
        assert model == "XGBRegressor"

    def test_invalid_city(self):
        data = {
            "surface_bati": 45,
            "nombre_pieces": 2,
            "nombre_lots": 10,
            "type_local": "appartement"
        }
        try:
            predict.predict_price(data, "paris")
        except ValueError as e:
            assert "Ville inconnue" in str(e)

    def test_invalid_type_local(self):
        data = {
            "surface_bati": 45,
            "nombre_pieces": 2,
            "nombre_lots": 10,
            "type_local": "chateau"
        }
        try:
            predict.predict_price(data, "lille")
        except ValueError as e:
            assert "Erreur interne" in str(e)

    def test_missing_field(self):
        data = {
            "surface_bati": 45,
            "type_local": "appartement"
            # manque nombre_pieces et nombre_lots
        }
        try:
            predict.predict_price(data, "lille")
        except ValueError as e:
            assert "Champ(s) manquant(s)" in str(e)