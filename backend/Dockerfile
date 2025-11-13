# Backend Dockerfile
FROM python:3.11-slim

WORKDIR /code

# Installera system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Kopiera requirements och installera Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiera hela backend-mappen
COPY . /code/backend/

# Exponera port
EXPOSE 8000

# Kör applikationen
CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
