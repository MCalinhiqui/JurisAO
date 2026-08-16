import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.util.constants import STATE_MAP
from src.ingestion.loader import load_all_docs


# documents = load_all_docs("data/raw")
# for name, pages in documents.items():
#     print(f"{name}: {len(pages)} páginas carregadas")
#     print(pages[0].page_content[:300])
    

