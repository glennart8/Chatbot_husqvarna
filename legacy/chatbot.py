# -*- coding: utf-8 -*-
import sys
import io

# Fixa encoding för svenska tecken
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from transformers import pipeline

# --- KONSTANTER ---
# Begränsa kontextlängden för att undvika att överskrida max tokens
MAX_CONTEXT_LENGTH = 600
# Använder mT5 för bättre flerspråkigt stöd (svenska + engelska)
MODEL_NAME = "google/mt5-small"

# --- Ladda FAISS-index ---
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-mpnet-base-v2")
vectorstore = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

# --- Skapa HuggingFace text generation pipeline ---
generator_pipeline = pipeline(
    "text2text-generation",
    model=MODEL_NAME,
    device=-1  # CPU
)

# --- Funktion för att ställa frågor ---
def ask_question(query, k=3): # Öka k för att få med relevanta chunks, men vi begränsar sedan texten
    # Hämta k närmaste dokument från FAISS
    docs = vectorstore.similarity_search(query, k=k)
    
    context = ""
    # Sammanfoga dokument, men sluta när MAX_CONTEXT_LENGTH uppnås
    for doc in docs:
        if len(context) + len(doc.page_content) < MAX_CONTEXT_LENGTH:
            context += doc.page_content + "\n"
        else:
            # Ta med en del av det sista dokumentet för att fylla ut
            remaining_length = MAX_CONTEXT_LENGTH - len(context)
            if remaining_length > 0:
                context += doc.page_content[:remaining_length]
            break
    
    # Ta bort onödiga radbrytningar och mellanslag från kontexten innan prompten skapas
    cleaned_context = context.replace('\n', ' ').strip()

    # Skapa prompt - mycket enklare för modellen
    # mT5 är bättre på direkta instruktioner
    prompt = (
        f"Fråga: {query}\n\n"
        f"Kontext från manual: {cleaned_context}\n\n"
        f"Ge ett kort svar på svenska baserat på manualen:"
    )

    # Generera svar - använd max_new_tokens istället för max_length
    answer = generator_pipeline(prompt, max_new_tokens=100, do_sample=False, truncation=True)[0]['generated_text']
    
    return answer

# --- Interaktiv loop ---
print("Chatbot redo — skriv fråga (skriv 'exit' för att avsluta).")
while True:
    query = input("\nFråga: ")
    if query.lower() in ["exit", "quit"]:
        break
    try:
        answer = ask_question(query)
        print("\nSvar:\n", answer)
    except Exception as e:
        print("Fel:", e)