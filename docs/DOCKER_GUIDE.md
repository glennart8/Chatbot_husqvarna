# 🐳 Docker Guide - Superenkelt!

## Förberedelser (En gång)

### Steg 1: Installera Docker Desktop

1. Ladda ner från: https://www.docker.com/products/docker-desktop
2. Installera och starta Docker Desktop
3. Vänta tills Docker Desktop är igång (grön ikon i systray)

**Verifiera:**
```bash
docker --version
docker-compose --version
```

## Starta Chatboten (Superenkelt!)

### Windows

Dubbelklicka på: **`start.bat`**

ELLER öppna terminal och kör:
```bash
start.bat
```

### Mac/Linux

Öppna terminal och kör:
```bash
./start.sh
```

## Vad händer?

1. **Första gången (5-10 minuter)**
   - Docker bygger containers
   - Laddar ner AI-modeller (~300 MB)
   - Installerar alla dependencies

2. **Nästa gånger (~30 sekunder)**
   - Startar direkt från cachade images
   - Mycket snabbare!

## Använd Chatboten

När du ser:
```
✓ Container husqvarna-chatbot-backend  Started
✓ Container husqvarna-chatbot-frontend Started
```

Öppna webbläsaren:
- **Frontend (Chat-UI):** http://localhost:3000
- **Backend API Docs:** http://localhost:8000/docs

## Stoppa Chatboten

### Alternativ 1: CTRL+C i terminalen

Tryck `CTRL+C` där start.bat/start.sh kör

### Alternativ 2: Stop-script

**Windows:**
```bash
stop.bat
```

**Mac/Linux:**
```bash
./stop.sh
```

### Alternativ 3: Manuellt
```bash
docker-compose down
```

## Felsökning

### "Docker är inte installerat"
**Lösning:** Installera Docker Desktop från länken ovan

### "Port 8000 already in use"
**Lösning:** Stoppa andra program på port 8000
```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Mac/Linux
lsof -ti:8000 | xargs kill
```

### Frontend visar felmeddelande
**Lösning:** Vänta 1-2 minuter - AI-modellen laddar fortfarande

### Kontrollera container status
```bash
docker-compose ps
docker-compose logs backend
docker-compose logs frontend
```

### Bygg om från scratch (vid problem)
```bash
docker-compose down --volumes --remove-orphans
docker-compose build --no-cache
docker-compose up -d
```

## Användbara Docker-kommandon

```bash
# Se alla containers
docker ps

# Se backend-logs live
docker-compose logs -f backend

# Se frontend-logs live
docker-compose logs -f frontend

# Stoppa allt
docker-compose down

# Starta utan att bygga om
docker-compose up -d

# Bygg om och starta
docker-compose up --build -d
```

## Fördelar med Docker

✅ Ingen manuell installation av dependencies
✅ Fungerar likadant på alla datorer
✅ Inget behov av två terminaler
✅ Lätt att starta och stoppa
✅ Perfekt för deployment senare

## Tips

- Första gången tar längst tid (laddar AI-modell)
- Låt Docker Desktop köra i bakgrunden
- Du kan fortsätta jobba medan containern kör
- Loggar visas direkt i terminalen

---

**Nu är det bara att köra `start.bat` och surfa till http://localhost:3000!** 🚀
