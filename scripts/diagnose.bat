@echo off
echo ========================================
echo   DIAGNOS - Husqvarna Chatbot
echo ========================================
echo.

echo 1. Kontrollerar Docker...
docker --version
if errorlevel 1 (
    echo [FAIL] Docker ar inte installerat!
    pause
    exit /b 1
)
echo [OK] Docker ar installerat
echo.

echo 2. Kontrollerar Docker Desktop...
docker info >nul 2>&1
if errorlevel 1 (
    echo [FAIL] Docker Desktop ar inte igång!
    echo Starta Docker Desktop och försök igen.
    pause
    exit /b 1
)
echo [OK] Docker Desktop ar igång
echo.

echo 3. Kontrollerar projektfiler...
if not exist "docker-compose.yml" (
    echo [FAIL] docker-compose.yml saknas!
    pause
    exit /b 1
)
echo [OK] docker-compose.yml finns

if not exist "backend\Dockerfile" (
    echo [FAIL] backend\Dockerfile saknas!
    pause
    exit /b 1
)
echo [OK] backend\Dockerfile finns

if not exist "frontend\Dockerfile" (
    echo [FAIL] frontend\Dockerfile saknas!
    pause
    exit /b 1
)
echo [OK] frontend\Dockerfile finns

if not exist "faiss_index" (
    echo [VARNING] faiss_index mappen saknas!
    echo Detta kommer orsaka fel. Kör: python chat_setup.py
    echo.
) else (
    echo [OK] faiss_index finns
)

if not exist "data" (
    echo [VARNING] data mappen saknas!
    echo.
) else (
    echo [OK] data finns
)
echo.

echo 4. Kontrollerar om portar ar lediga...
netstat -ano | findstr :8000 >nul
if not errorlevel 1 (
    echo [VARNING] Port 8000 ar upptagen!
    netstat -ano | findstr :8000
    echo.
) else (
    echo [OK] Port 8000 ar ledig
)

netstat -ano | findstr :3000 >nul
if not errorlevel 1 (
    echo [VARNING] Port 3000 ar upptagen!
    netstat -ano | findstr :3000
    echo.
) else (
    echo [OK] Port 3000 ar ledig
)

echo.
echo ========================================
echo   DIAGNOS KLAR
echo ========================================
echo.
echo Om allt ar OK, kör: docker-compose up --build
echo.
pause
