# 🚀 Snabbstart - Kom igång på 5 minuter!

## Steg 1: Installera Node.js (om du inte har det)

Ladda ner och installera Node.js från: https://nodejs.org/ (LTS version)

Verifiera installation:
```bash
node --version
npm --version
```

## Steg 2: Starta Backend

Öppna en terminal och navigera till projektmappen:

```bash
# Windows (Git Bash eller PowerShell)
cd "c:\Users\henri\source\repos\Python\Egna projekt\Chatbot_for_Opel_vectra"

# Aktivera virtual environment (om du redan har ett)
.\venv\Scripts\activate

# Eller skapa nytt venv
python -m venv venv
.\venv\Scripts\activate

# Installera backend dependencies
cd backend
pip install -r requirements.txt

# Gå tillbaka till projektrot
cd ..

# Starta backend (från projektrot!)
python -m uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000
```

**Vänta tills du ser:**
```
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

✅ Backend är igång! Testa: http://localhost:8000/docs

## Steg 3: Starta Frontend (Ny terminal!)

Öppna en **NY terminal** (låt backend köra i den första):

```bash
# Navigera till frontend-mappen
cd "c:\Users\henri\source\repos\Python\Egna projekt\Chatbot_for_Opel_vectra\frontend"

# Installera dependencies (tar några minuter första gången)
npm install

# Skapa .env fil
copy .env.example .env

# Starta development server
npm run dev
```

**Vänta tills du ser:**
```
  VITE v5.x.x  ready in XXX ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
```

✅ Frontend är igång!

## Steg 4: Öppna Chatboten!

Öppna din webbläsare och gå till: **http://localhost:5173**

Du bör nu se Husqvarna Motorsåg Chatbot-gränssnittet!

## Testa Chatboten

Ställ några frågor:
- "Hur byter man kedjan?"
- "Hur spänner man kedjan?"
- "Var hittar jag oljenivån?"

## Troubleshooting

### Backend-fel: "No module named 'backend'"
**Lösning:** Kör uvicorn från projektrot, inte från backend-mappen.

### Backend-fel: "FAISS index not found"
**Lösning:** Kontrollera att `faiss_index/` mappen finns i projektroten.

### Frontend-fel: "npm: command not found"
**Lösning:** Installera Node.js från https://nodejs.org/

### Frontend kan inte ansluta till backend
**Lösning:**
1. Kontrollera att backend körs på port 8000
2. Öppna http://localhost:8000/api/v1/health/ - ska visa "ok"
3. Kolla att CORS är aktiverat i `backend/app/core/config.py`

### AI-modellen laddar långsamt första gången
**Detta är normalt!** Första gången backend startar laddar den ner mT5-modellen (ca 300 MB).
Vänta 1-2 minuter. Nästa gång går det mycket snabbare.

## Nästa steg

När allt fungerar:
1. Läs [README.md](README.md) för fullständig dokumentation
2. Utforska koden i `backend/app/` och `frontend/src/`
3. Testa att ändra UI-färger i `frontend/src/components/ChatContainer.tsx`
4. Lägg till fler PDF-manualer (se README.md)

## Behöver du hjälp?

Kontrollera:
1. Att båda terminalerna kör (backend OCH frontend)
2. Att inga felmeddelanden visas i terminalerna
3. Browser console (F12) för frontend-fel

Ha kul med att lära dig! 🎉
