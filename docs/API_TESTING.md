# 🧪 Testa Backend API

Detta dokument visar hur du testar backend API:et utan att starta frontend.

## Alternativ 1: Swagger UI (Rekommenderat)

FastAPI har inbyggd interaktiv API-dokumentation!

1. Starta backend:
```bash
python -m uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
```

2. Öppna webbläsaren: **http://localhost:8000/docs**

3. Du ser nu alla endpoints med "Try it out"-knappar!

### Testa Health Check
1. Klicka på `GET /api/v1/health/`
2. Klicka på "Try it out"
3. Klicka på "Execute"
4. Se svaret nedan!

### Testa Chat Endpoint
1. Klicka på `POST /api/v1/chat/`
2. Klicka på "Try it out"
3. Ändra request body:
```json
{
  "question": "Hur byter man kedjan?",
  "session_id": "test-123"
}
```
4. Klicka på "Execute"
5. Vänta 5-10 sekunder (AI-modellen tänker)
6. Se svaret!

## Alternativ 2: cURL (Kommandorad)

### Health Check
```bash
curl http://localhost:8000/api/v1/health/
```

### Chat Request
```bash
curl -X POST http://localhost:8000/api/v1/chat/ \
  -H "Content-Type: application/json" \
  -d '{
    "question": "Hur byter man kedjan?",
    "session_id": "curl-test"
  }'
```

## Alternativ 3: PowerShell (Windows)

### Health Check
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/api/v1/health/" -Method Get
```

### Chat Request
```powershell
$body = @{
    question = "Hur byter man kedjan?"
    session_id = "powershell-test"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/api/v1/chat/" `
  -Method Post `
  -ContentType "application/json" `
  -Body $body
```

## Alternativ 4: Python Requests

Skapa en fil `test_api.py`:

```python
import requests
import json

BASE_URL = "http://localhost:8000/api/v1"

# Test health check
print("Testing health check...")
response = requests.get(f"{BASE_URL}/health/")
print(f"Status: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2)}\n")

# Test chat
print("Testing chat...")
chat_data = {
    "question": "Hur byter man kedjan?",
    "session_id": "python-test"
}
response = requests.post(f"{BASE_URL}/chat/", json=chat_data)
print(f"Status: {response.status_code}")
print(f"Response: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
```

Kör:
```bash
python test_api.py
```

## Förväntat svar från Health Check

```json
{
  "status": "ok",
  "version": "1.0.0",
  "model_loaded": true
}
```

## Förväntat svar från Chat

```json
{
  "answer": "För att byta kedjan på Husqvarna 365 motorsågen...",
  "question": "Hur byter man kedjan?",
  "session_id": "test-123",
  "timestamp": "2025-01-13T11:30:00.123456"
}
```

## Felsökning

### Error 503: Service Unavailable
- AI-modellen har inte laddat klart än
- Vänta 1-2 minuter och försök igen
- Kontrollera backend logs

### Error 500: Internal Server Error
- Kontrollera att FAISS-index finns i `faiss_index/`
- Kolla backend logs för detaljerat felmeddelande
- Verifiera att alla dependencies är installerade

### Timeout
- Chat-svaret kan ta 5-10 sekunder (normal)
- Om det tar >30 sekunder, kontrollera att modellen laddades korrekt
- Testa att minska MAX_CONTEXT_LENGTH i config

## Tips

- Använd Swagger UI för snabb utveckling och testning
- Använd cURL/Python för automatiska tester
- Lägg till fler testfrågor för att verifiera kvaliteten
- Testa olika session_id för att se om sessions fungerar

Happy testing! 🧪
