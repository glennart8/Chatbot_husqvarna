from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from transformers import pipeline

# --- KONSTANTER ---
# Begränsa kontextlängden för att undvika att överskrida max tokens
MAX_CONTEXT_LENGTH = 1024 
# Valt en större modell för bättre svar (OBS: Blir långsammare på CPU)
MODEL_NAME = "google/flan-t5-base" 

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
def ask_question(query, k=5): # Öka k för att få med relevanta chunks, men vi begränsar sedan texten
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
            
    # Skapa prompt med kontext + fråga
    # Förbättra instruktionen till modellen (prompt-engineering)
    prompt = f"Du är en expert på motorsågar som svarar baserat på manualens text. Manualens text:\n{context}\n\nFråga: {query}\nSvar:"
    
    # Generera svar
    # max_length i pipeline motsvarar max_new_tokens när man använder T5-modeller för att generera *nya* tokens.
    answer = generator_pipeline(prompt, max_length=256, truncation=True)[0]['generated_text']
    
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