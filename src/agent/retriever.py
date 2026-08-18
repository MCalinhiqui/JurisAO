from langchain_core.vectorstores import InMemoryVectorStore
from langchain_huggingface import HuggingFaceEmbeddings

VECTOR_STORE_PATH = "data/processed/vector_store.json"
EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"

def load_vector_store():
    embed_model = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    return InMemoryVectorStore.load(VECTOR_STORE_PATH, embed_model)

def retrieve_articles(vector_store, question: str, k: int = 40):
    return vector_store.similarity_search(question, k=k)