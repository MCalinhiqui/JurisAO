from .loader import load_all_docs
from .chunker import create_chunks

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from src.util.doc_standardization import find_header

def join_pages(path: str) -> list:
    documents = load_all_docs(path)
    all_chunks = []
    for document_pages in documents.values():
        chunks = create_chunks(document_pages)   # uma chamada por documento
        all_chunks.extend(chunks)                # so' aqui e' que juntas
    return all_chunks  

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
def create_index(all_articles: list):
    embed_model = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2", model_kwargs={"local_files_only":True})
    vector_store = InMemoryVectorStore.from_documents(all_articles,embed_model)
    return vector_store

if __name__ == "__main__":
    articles = join_pages("data/raw")
    vector_store = create_index(articles)
    vector_store.dump("data/processed/vector_store.json")