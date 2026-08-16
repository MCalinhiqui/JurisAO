import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from langchain_core.vectorstores import InMemoryVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
import time

inicio = time.time()
embed_model = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-multilingual-mpnet-base-v2",model_kwargs={"local_files_only":True})

vector_store = InMemoryVectorStore.load("data/processed/vector_store.json", embed_model)
print(f"Tempo a carregar: {time.time() - inicio:.2f} segundos")

responses = vector_store.similarity_search("Os jovens gozam de protecção especial para efectivação de quais direitos?", k=1)
for response in responses:
    print(f"{response.metadata} \n {response.page_content}")