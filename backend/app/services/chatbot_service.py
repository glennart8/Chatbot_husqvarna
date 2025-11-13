# -*- coding: utf-8 -*-
"""
Chatbot service - migrerad logik från chatbot.py
"""
import sys
import io
import logging
from typing import Optional

# Fixa encoding för svenska tecken
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from transformers import pipeline

from backend.app.core.config import settings

logger = logging.getLogger(__name__)

class ChatbotService:
    """
    Chatbot service som hanterar FAISS vektordatabas och AI-modell
    """

    def __init__(self):
        self.embeddings: Optional[HuggingFaceEmbeddings] = None
        self.vectorstore: Optional[FAISS] = None
        self.generator_pipeline = None
        self._model_loaded = False

    def initialize(self):
        """Initialisera modeller och vektordatabas"""
        try:
            logger.info("Initialiserar chatbot service...")

            # Ladda embeddings
            logger.info(f"Laddar embeddings: {settings.EMBEDDING_MODEL}")
            self.embeddings = HuggingFaceEmbeddings(
                model_name=settings.EMBEDDING_MODEL
            )

            # Ladda FAISS index
            logger.info(f"Laddar FAISS index från: {settings.FAISS_INDEX_PATH}")
            self.vectorstore = FAISS.load_local(
                settings.FAISS_INDEX_PATH,
                self.embeddings,
                allow_dangerous_deserialization=True
            )

            # Skapa text generation pipeline
            logger.info(f"Laddar AI-modell: {settings.MODEL_NAME}")
            self.generator_pipeline = pipeline(
                "text2text-generation",
                model=settings.MODEL_NAME,
                device=-1  # CPU
            )

            self._model_loaded = True
            logger.info("Chatbot service initialiserad!")

        except Exception as e:
            logger.error(f"Fel vid initialisering av chatbot: {e}")
            raise

    def is_ready(self) -> bool:
        """Kontrollera om modellen är redo"""
        return self._model_loaded

    def ask_question(self, query: str, k: int = 3) -> str:
        """
        Ställ en fråga till chatboten

        Args:
            query: Användarens fråga
            k: Antal dokument att hämta från FAISS

        Returns:
            Chatbotens svar
        """
        if not self.is_ready():
            raise RuntimeError("Chatbot är inte initialiserad. Kör initialize() först.")

        try:
            # Hämta relevanta dokument från FAISS
            docs = self.vectorstore.similarity_search(query, k=k)

            # Bygg context från dokument
            context = ""
            for doc in docs:
                if len(context) + len(doc.page_content) < settings.MAX_CONTEXT_LENGTH:
                    context += doc.page_content + "\n"
                else:
                    # Ta med en del av det sista dokumentet för att fylla ut
                    remaining_length = settings.MAX_CONTEXT_LENGTH - len(context)
                    if remaining_length > 0:
                        context += doc.page_content[:remaining_length]
                    break

            # Rensa context
            cleaned_context = context.replace('\n', ' ').strip()

            # Skapa prompt
            prompt = (
                f"Fråga: {query}\n\n"
                f"Kontext från manual: {cleaned_context}\n\n"
                f"Ge ett kort svar på svenska baserat på manualen:"
            )

            # Generera svar
            answer = self.generator_pipeline(
                prompt,
                max_new_tokens=100,
                do_sample=False,
                truncation=True
            )[0]['generated_text']

            return answer

        except Exception as e:
            logger.error(f"Fel vid frågehantering: {e}")
            raise

# Singleton instance
chatbot_service = ChatbotService()
