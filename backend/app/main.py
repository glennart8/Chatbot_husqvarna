# -*- coding: utf-8 -*-
"""
Husqvarna Motorsåg Chatbot - FastAPI Backend
"""
import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.core.config import settings
from backend.app.api import chat, health
from backend.app.services.chatbot_service import chatbot_service

# Konfigurera logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifecycle manager - körs vid start och shutdown
    """
    # Startup
    logger.info("Startar Husqvarna Chatbot API...")
    try:
        chatbot_service.initialize()
        logger.info("Chatbot initialiserad!")
    except Exception as e:
        logger.error(f"Kunde inte initiera chatbot: {e}")

    yield

    # Shutdown
    logger.info("Stänger ner Husqvarna Chatbot API...")

# Skapa FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="API för Husqvarna Motorsåg Chatbot - Få svar om motorsågsskötsel och användning",
    lifespan=lifespan
)

# Lägg till CORS middleware (tillåt frontend-anrop)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inkludera API routes
app.include_router(health.router, prefix=settings.API_V1_PREFIX)
app.include_router(chat.router, prefix=settings.API_V1_PREFIX)

@app.get("/")
async def root():
    """Root endpoint - välkomstmeddelande"""
    return {
        "message": "Välkommen till Husqvarna Motorsåg Chatbot API!",
        "version": settings.APP_VERSION,
        "docs": "/docs",
        "health": f"{settings.API_V1_PREFIX}/health"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "backend.app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
