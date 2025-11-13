@echo off
echo ========================================
echo   Husqvarna Motorsag Chatbot
echo   Startar med Docker...
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
echo Bygger och startar containers...
echo Detta kan ta 5-10 minuter forsta gangen (laddar AI-modeller)
echo.

docker-compose up --build

echo.
echo ========================================
echo   Chatbot stangd!
echo ========================================
echo.
pause
