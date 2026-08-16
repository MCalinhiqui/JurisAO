from langchain_community.document_loaders import PyPDFLoader

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from src.util.constants import STATE_MAP, STANDARD_ARTICLE
from src.util.doc_standardization import find_header, find_page_noise, reset_level

def load_doc(path: str) -> list:
    """
    Load a document from a given path.
    
    param 
        path: The path to the document to be loaded.
    """
    
    
    loader = PyPDFLoader(path)
    pages = [page for page in loader.lazy_load()]
    
    return pages

from pathlib import Path
def load_all_docs(raw_path: str) -> dict :
    """
    Load all documents from a given raw path.
    
    param 
        raw_path: The path to the directory containing the documents to be loaded.
    """
    
    
    paths = Path(raw_path).glob("*.pdf")
    docs = {}
    
    for path in paths:
        try:
            doc = load_doc(path)
            docs[path.stem] = doc
        except Exception as e:
            print(f"Erro: {e.__str__()}")
            continue
        
    return docs
