@echo off
echo Lancement du serveur FastAPI...
python -m uvicorn app.main:app --reload --port 8000
pause