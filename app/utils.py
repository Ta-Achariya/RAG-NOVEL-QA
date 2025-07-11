from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import chromadb
import subprocess

model = SentenceTransformer("all-MiniLM-L6-v2")

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    return "\n".join([page.extract_text() for page in reader.pages])

""" 
check = extract_text_from_pdf("data/sword-come-ch1.pdf")
print(check)"""

def chunk_text(text, size=500,overlap=50):
    return [text[i:i+size] for i in range(0,len(text), size - overlap)]


def embed_chunks(chunks):
    return model.encode(chunks).tolist()


def get_chroma_collection():
    client = chromadb.PersistentClient(path="./chroma_db")
    return client.get_or_create_collection("novel_chapters")


def call_ollama(prompt):
    result = subprocess.run(
        ["ollama", "run", "llama3.2", prompt],
        capture_output=True,
        text=True
    )
    return result.stdout