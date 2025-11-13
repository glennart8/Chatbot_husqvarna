#!/bin/bash

echo "========================================"
echo "  Husqvarna Motorsåg Chatbot"
echo "  Startar med Docker..."
echo "========================================"
echo ""

# Kontrollera Docker
if ! command -v docker &> /dev/null; then
    echo "FEL: Docker är inte installerat!"
    echo "Ladda ner Docker Desktop från: https://www.docker.com/products/docker-desktop"
    exit 1
fi

echo "Docker hittades!"
echo ""

echo "Stoppar eventuella gamla containers..."
docker-compose down

echo ""
echo "Bygger och startar containers..."
echo "Detta kan ta 5-10 minuter första gången (laddar AI-modeller)"
echo ""

docker-compose up --build -d

echo ""
echo "========================================"
echo "  Chatbot startad!"
echo "========================================"
echo ""
echo "Backend API: http://localhost:8000"
echo "API Docs:    http://localhost:8000/docs"
echo "Frontend:    http://localhost:3000"
echo ""
echo "Tryck CTRL+C för att avsluta"
echo ""

# Visa logs
docker-compose logs -f
