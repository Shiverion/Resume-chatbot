import os
import pandas as pd
import hashlib
from pathlib import Path
from openai import OpenAI
import chromadb
from chromadb.config import Settings
from typing import List, Dict
from functools import lru_cache
import gradio as gr
from dotenv import load_dotenv

load_dotenv(override=True)
# === EMBEDDING CACHE ===
embedding_cache = {}

# === INIT OPENAI CLIENT ===
openai_client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# === INIT ChromaDB ===
chroma_client = chromadb.PersistentClient(
    path="vector_db",
    settings=Settings(anonymized_telemetry=False)
)
collection = chroma_client.get_or_create_collection(
    name="dpr_agenda",
    metadata={"hnsw:space": "cosine"}
)

# === OPTIONAL METADATA CLASS ===
class Me:
    def __init__(self):
        self.name = "Chatbot DPR"

# === EMBEDDING HANDLING ===
@lru_cache(maxsize=1000)
def get_embeddings_cached(text: str) -> List[float]:
    try:
        text_hash = hashlib.md5(text.encode()).hexdigest()
        if text_hash in embedding_cache:
            return embedding_cache[text_hash]

        response = openai_client.embeddings.create(
            model="text-embedding-3-small",
            input=[text]
        )
        embedding = response.data[0].embedding
        embedding_cache[text_hash] = embedding
        return embedding
    except Exception as e:
        print(f"❌ Embedding error: {e}")
        return [0.0] * 1536  # Dummy fallback

def get_embeddings(texts: List[str]) -> List[List[float]]:
    return [get_embeddings_cached(t) for t in texts]

# === LOAD AGENDA DATASET ===
def load_agenda():
    file_path = Path("me/agenda_clean.csv")
    if not file_path.exists():
        print("❌ agenda_clean.csv not found in /me")
        return

    df = pd.read_csv(file_path)
    docs = {}
    for i, row in df.iterrows():
        content = f"""
Tanggal: {row.get('date', 'tidak diketahui')}
Judul: {row.get('title', '')}
Deskripsi: {row.get('description', '')}
Tempat: {row.get('tempat', '')}
AKD: {row.get('id_akd', '')}
Jenis Agenda: {row.get('id_jenis_agenda', '')}
ID Rapat: {row.get('id', '')}
Status Rapat: {row.get('status', '')}
        """
        docs[f"agenda_{i}"] = content.strip()

    if collection.count() == 0:
        print("🧠 Memproses dan menyimpan agenda ke vector DB...")
        embeddings = get_embeddings(list(docs.values()))
        collection.add(
            documents=list(docs.values()),
            metadatas=[{"source": k} for k in docs.keys()],
            ids=list(docs.keys()),
            embeddings=embeddings
        )
        print(f"✅ {len(docs)} agenda berhasil ditambahkan ke vector DB.")
    else:
        print("🟡 Vector DB sudah berisi data. Lewati pemrosesan ulang.")


# === CONTEXT RETRIEVAL ===
def retrieve_context(query: str, top_k: int = 5) -> str:
    query_emb = get_embeddings_cached(query)
    results = collection.query(query_embeddings=[query_emb], n_results=top_k)
    docs = results.get("documents", [[]])[0]
    return "\n---\n".join(docs)

# === SYSTEM PROMPT ===
def make_prompt(context="") -> str:
    return f"""
Kamu adalah asisten jadwal DPR RI. Tugasmu adalah membantu pengawal anggota dewan untuk mengetahui agenda rapat, jadwal kegiatan, tempat, dan deskripsi kegiatan DPR.

Jika tidak ditemukan, katakan dengan sopan bahwa kamu tidak tahu. Jangan mengarang informasi.

Gunakan konteks di bawah ini sebagai referensi utama:
{context}
    """.strip()

# === MAIN CHAT FUNCTION ===
def chat_fn(message, history):
    context = retrieve_context(message)
    system_msg = {"role": "system", "content": make_prompt(context)}
    messages = [system_msg] + history + [{"role": "user", "content": message}]

    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        temperature=0.3,
        max_tokens=1024,
    )
    return response.choices[0].message.content

# === RUN CHATBOT ===
if __name__ == "__main__":
    load_agenda()
    gr.ChatInterface(chat_fn, type="messages").launch()
