# -*- coding: utf-8 -*-
"""
Health check API endpoint
"""
from fastapi import APIRouter
from backend.app.models.chat import HealthResponse
from backend.app.services.chatbot_service import chatbot_service
from backend.app.core.config import settings

router = APIRouter(prefix="/health", tags=["health"])

@router.get("/", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """
    Kontrollera om API:et är igång och redo

    Returnerar status, version och om AI-modellen är laddad
    """
    return HealthResponse(
        status="ok",
        version=settings.APP_VERSION,
        model_loaded=chatbot_service.is_ready()
    )
