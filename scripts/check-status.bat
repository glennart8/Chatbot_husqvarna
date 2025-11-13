@echo off
echo ========================================
echo   Kontrollerar Docker status...
echo ========================================
echo.

echo 1. Kontrollerar om Docker ar igång...
docker --version
if errorlevel 1 (
    echo FEL: Docker ar inte installerat eller inte igång!
    pause
    exit /b 1
)
echo    [OK] Docker ar installerat
echo.

echo 2. Kontrollerar containers...
docker ps -a --filter "name=husqvarna"
echo.

echo 3. Senaste loggarna från backend:
echo ========================================
docker logs husqvarna-chatbot-backend --tail 50
echo.

echo 4. Senaste loggarna från frontend:
echo ========================================
docker logs husqvarna-chatbot-frontend --tail 20
echo.

echo ========================================
echo.
pause
