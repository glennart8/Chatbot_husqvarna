from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from pypdf import PdfReader
from dotenv import load_dotenv
import os

load_dotenv()

# --- Läs PDF och rensa text ---
pdf_file = "data/husqvarna365.pdf"  # byt till din fil
reader = PdfReader(pdf_file)

text = ""
print(f"Läser in text från PDF: {pdf_file}")

# DEFINIERA SIDINTERVALL (indexbaserat: Sida 2 till Sida 41)
START_INDEX = 1   # Index för Sida 2
END_INDEX = 41    # Index FÖRBI Sida 41 (Standard Python slicing: index upp till, men exklusive, detta nummer)

# Ändra loopen för att iterera över sidor i intervallet [START_INDEX, END_INDEX)
for i in range(START_INDEX, END_INDEX):
    if i < len(reader.pages):
        page = reader.pages[i]
        page_text = page.extract_text()
        
        if page_text:
            # Ta bort onödiga radbrytningar
            page_text = page_text.replace("\n", " ").strip()
            text += page_text + "\n"
        else:
            # Kan vara bra att se om någon sida är tom p.g.a. OCR-problem
            print(f"Varning: Sida {i+1} gav ingen text vid extraktion.")
    else:
        # Detta bör inte hända om filen har minst 41 sidor
        print(f"Varning: Försökte läsa sida {i+1}, men PDF:en slutade.")
        break

# --- Skapa Document-objekt ---
docs = [Document(page_content=text)]

# --- Dela upp i chunks ---
text_splitter = RecursiveCharacterTextSplitter(chunk_size=650, chunk_overlap=150)
docs_split = text_splitter.split_documents(docs)
print(f"Antal chunks: {len(docs_split)}")

# --- Skapa embeddings (lokalt HuggingFace, gratis) ---
print("Skapar embeddings med HuggingFace...")
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-mpnet-base-v2")

# --- Skapa FAISS-index ---
vectorstore = FAISS.from_documents(docs_split, embeddings)

# --- Spara index lokalt ---
vectorstore.save_local("faiss_index")
print("FAISS-index sparat som 'faiss_index'")
