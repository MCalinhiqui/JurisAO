import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.ingestion.indexer import create_index, join_pages, load_vectorstore

# Abre o ficheiro em modo de escrita ('w') com codificação UTF-8 para evitar erros de acentos
# with open("verificacao_documentos.txt", "w", encoding="utf-8") as f:
#     for i, doc in enumerate(articles, start=1):
#         # Escreve o cabeçalho do documento atual
#         f.write(f"==================================================\n")
#         f.write(f" DOCUMENTO #{i}\n")
#         f.write(f"==================================================\n")
        
#         # Escreve os Metadados formatados de forma legível
#         f.write("METADADOS:\n")
#         for chave, valor in doc.metadata.items():
#             f.write(f"  - {chave}: {valor}\n")
        
#         f.write("\n--------------------------------------------------\n")
        
#         # Escreve o Conteúdo do Documento
#         f.write("CONTEÚDO:\n")
#         f.write(doc.page_content)
#         f.write("\n\n")  # Dá espaço para o próximo documento

# print("Ficheiro 'verificacao_documentos.txt' gerado com sucesso!")

# responses = vector_store.similarity_search("Os jovens gozam de protecção especial para efectivação de quais direitos?",k=2)
# for response in responses:
#     print(f"{response.metadata} \n {response.page_content[:500]}")

# articles = join_pages("data/raw")
# vector_store = create_index(articles)
# vector_store.dump("data/processed/vector_store.json")
