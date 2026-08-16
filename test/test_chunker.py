import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.ingestion.loader import load_all_docs, load_doc
from src.ingestion.chunker import create_chunks

pages = load_all_docs("data/raw")
chunks = []
for name, page in pages.items():
    chunks_ = create_chunks(page)
    print(f"{name} tem {len(page)} páginas e {len(chunks_)} artigos")
    chunks.extend(chunks_)

# print(len(chunks))

# for name, page in pages.items():
#     if name == "codigo_penal":
#         chunks_ = create_chunks(page)
#         chunks_ordenados = sorted(
#             chunks_,
#             key=lambda doc: len(doc.page_content)
#         )
        
#         for a in chunks_ordenados:
#             print(a.page_content.split("\n")[0])
#             print()
    