@echo off
echo ========================================
echo   Husqvarna Motorsag Chatbot
echo   Startar i bakgrunden...
echo ========================================
echo.

echo Kontrollerar att Docker ar installerat...
docker --version >nul 2>&1
if errorlevel 1 (
    echo FEL: Docker ar inte installerat!
    echo Ladda ner Docker Desktop fran: https://www.docker.com/products/docker-desktop
    pause
    exit /b 1
)

echo Docker hittades!
echo.

echo Stoppar eventuella gamla containers...
docker-compose down

echo.
echo Bygger och startar containers i bakgrunden...
echo Detta kan ta 5-10 minuter forsta gangen (laddar AI-modeller)
echo.

docker-compose up --build -d

echo.
echo Vantar pa att containers ska starta...
timeout /t 5 /nobreak >nul

echo.
echo Kontrollerar status...
docker-compose ps

echo.
echo ========================================
echo   Chatbot startad i bakgrunden!
echo ========================================
echo.
echo Backend API: http://localhost:8000
echo API Docs:    http://localhost:8000/docs
echo Frontend:    http://localhost:3000
echo.
echo För att se loggar, kör: docker-compose logs -f
echo För att stoppa, kör: stop.bat
echo.
pause
