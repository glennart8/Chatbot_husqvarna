# -*- coding: utf-8 -*-
"""
Chat API endpoints
"""
from fastapi import APIRouter, HTTPException, status
import logging

from backend.app.models.chat import ChatRequest, ChatResponse
from backend.app.services.chatbot_service import chatbot_service

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/chat", tags=["chat"])

@router.post("/", response_model=ChatResponse, status_code=status.HTTP_200_OK)
async def chat(request: ChatRequest) -> ChatResponse:
    """
    Skicka en fråga till chatboten och få svar

    - **question**: Din fråga om Husqvarna motorsågar
    - **session_id**: (Valfri) Session ID för att spåra konversation
    """
    try:
        if not chatbot_service.is_ready():
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Chatbot är inte redo. Försök igen senare."
            )

        # Få svar från chatbot
        answer = chatbot_service.ask_question(request.question)

        # Skapa response
        response = ChatResponse(
            answer=answer,
            question=request.question,
            session_id=request.session_id
        )

        logger.info(f"Svar skapat för fråga: '{request.question[:50]}...'")
        return response

    except Exception as e:
        logger.error(f"Fel i chat endpoint: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ett fel uppstod: {str(e)}"
        )
