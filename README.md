# 🪚 Husqvarna Motorsåg Chatbot

En intelligent chatbot för Husqvarna 365 motorsåg, byggd med FastAPI, React och AI. Ställ frågor om motorsågsskötsel, underhåll och användning baserat på den officiella manualen.

## 🏗️ Projektstruktur

```
Chatbot_for_Opel_vectra/
├── backend/                    # FastAPI Backend
│   ├── app/
│   │   ├── api/               # API endpoints
│   │   ├── core/              # Konfiguration
│   │   ├── models/            # Pydantic models
│   │   ├── services/          # Business logic
│   │   └── main.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/                   # React Frontend
│   ├── src/
│   │   ├── components/        # React komponenter
│   │   ├── services/          # API kommunikation
│   │   ├── types/             # TypeScript typer
│   │   └── ...
│   ├── package.json
│   └── Dockerfile
├── data/                       # PDF-manualer
├── docs/                       # Dokumentation
│   ├── QUICKSTART.md
│   ├── DOCKER_GUIDE.md
│   ├── API_TESTING.md
│   └── README_FIRST.md
├── faiss_index/               # Vektordatabas
├── scripts/                    # Utility scripts
│   ├── chat_setup.py          # Skapa FAISS index
│   ├── diagnose.bat
│   └── check-status.bat
├── chatbot.py                 # Original CLI chatbot
├── docker-compose.yml
├── start.bat / start.sh       # Starta med Docker
├── stop.bat / stop.sh         # Stoppa Docker
└── README.md

```

## 🚀 Snabbstart

### 🐳 Rekommenderat: Docker (Superenkelt!)

**Kräver endast:** Docker Desktop installerat

#### Windows
Dubbelklicka på: **`start.bat`**

#### Mac/Linux
```bash
./start.sh
```

**Det är allt!** Öppna sedan: **http://localhost:3000**

📖 Läs mer: [docs/DOCKER_GUIDE.md](docs/DOCKER_GUIDE.md)

---

### 🔧 Alternativ: Lokal utveckling (För lärande & debugging)

Använd detta om du vill köra utan Docker och lära dig mer om hur backend och frontend fungerar.

📖 Se fullständig guide: [docs/QUICKSTART.md](docs/QUICKSTART.md)

**Snabb sammanfattning:**

#### Backend (Terminal 1)
```bash
python -m uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Frontend (Terminal 2)
```bash
cd frontend
npm install
npm run dev
```

Öppna: http://localhost:5173

## 📚 API Dokumentation

### Endpoints

#### `GET /api/v1/health/`
Kontrollera om API:et är igång och AI-modellen är laddad.

**Response:**
```json
{
  "status": "ok",
  "version": "1.0.0",
  "model_loaded": true
}
```

#### `POST /api/v1/chat/`
Skicka en fråga till chatboten.

**Request:**
```json
{
  "question": "Hur byter man kedjan?",
  "session_id": "user-123"
}
```

**Response:**
```json
{
  "answer": "För att byta kedjan på Husqvarna 365...",
  "question": "Hur byter man kedjan?",
  "session_id": "user-123",
  "timestamp": "2025-01-13T10:30:00"
}
```

## 🛠️ Teknisk Stack

### Backend
- **FastAPI** - Modernt Python web framework
- **LangChain** - RAG (Retrieval Augmented Generation) framework
- **FAISS** - Vektordatabas för semantic search
- **mT5** - Multilingual AI-modell för svenska svar
- **Sentence Transformers** - Text embeddings

### Frontend
- **React 18** - UI library
- **TypeScript** - Type-safe JavaScript
- **Vite** - Snabb build tool
- **Tailwind CSS** - Utility-first CSS
- **Axios** - HTTP client

### DevOps
- **Docker & Docker Compose** - Containerization
- **Nginx** - Reverse proxy för frontend

## 🎯 Funktioner

✅ Semantic search i Husqvarna 365 manual
✅ Svenska svar från multilingual AI-modell
✅ Modern React-baserad chat-UI
✅ RESTful API med FastAPI
✅ Containerized med Docker
✅ Health checks och error handling
✅ Session-baserad konversation

## 📖 Utvecklingsguide

### Lägg till fler PDF-manualer

1. Lägg PDF-filer i `data/` mappen
2. Uppdatera `scripts/chat_setup.py` för att inkludera nya filer
3. Kör setup-scriptet för att generera nytt FAISS index:

```bash
python scripts/chat_setup.py
```

### Anpassa AI-modellen

Redigera `backend/app/core/config.py`:
```python
MODEL_NAME: str = "google/mt5-base"  # Byt till annan modell
MAX_CONTEXT_LENGTH: int = 800        # Justera context-storlek
```

### Frontend-anpassningar

- **Färgschema:** Redigera `frontend/tailwind.config.js`
- **API URL:** Ändra i `frontend/.env`
- **Komponenter:** Hitta i `frontend/src/components/`

## 🐛 Troubleshooting

### Backend startar inte
- Kontrollera att FAISS-index finns: `ls faiss_index/`
- Kör `python scripts/chat_setup.py` om index saknas
- Verifiera Python version: Python 3.9+

### Frontend kan inte ansluta till backend
- Kontrollera att backend körs på port 8000
- Verifiera CORS-settings i `backend/app/core/config.py`
- Kontrollera `.env` fil i frontend

### AI-modellen är långsam
- mT5 körs på CPU - förvänta 5-10 sekunder per svar
- För snabbare svar: Använd mindre modell eller GPU
- Reducera `MAX_CONTEXT_LENGTH` i config

## 🎓 Lärandemål

Detta projekt lär dig:
1. **Backend API development** med FastAPI
2. **Frontend development** med React + TypeScript
3. **AI/ML integration** med LangChain och Transformers
4. **Vector databases** med FAISS
5. **Full-stack arkitektur** (separation of concerns)
6. **Docker containerization**
7. **REST API design**
8. **TypeScript** och type-safe development

## 📝 Licens

Detta projekt är skapat för lärandesyften.

## 🤝 Bidra

Detta är ett lärandeprojekt. Förslag och förbättringar är välkomna!

---

**Skapad av:** Henri
**Datum:** 2025-01-13
