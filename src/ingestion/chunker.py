import sys
from pathlib import Path

from src.util.doc_standardization import find_header, find_page_noise, reset_level
sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from src.util.constants import STANDARD_ARTICLE, STATE_MAP, HYPHENATION_PATTERN
from langchain_core.documents import Document

def create_chunks(pages: list):
    
    state = STATE_MAP.copy()
    uppercase_buffer = []   # <- nova variável, vive fora do loop, tal como 'state'
    current_article_lines = [] # <— vai acumulando o texto do artigo que está a ser construído neste momento
    current_article_header = None
    lines = []
    chunks = []
    
    for page in pages:
        lines.extend(page.page_content.split("\n"))
    
    for i, line in enumerate(lines):
        line_strip = line.strip()

        if find_page_noise(line_strip):
            continue   # ignora esta linha por completo, nem mexe no buffer

        header_match = find_header(line_strip)
        article_match = STANDARD_ARTICLE.match(line_strip)

        if header_match or article_match:
            if uppercase_buffer:                          # esvazia o buffer, se tiver algo
                texto_lei = " ".join(uppercase_buffer)
                state = reset_level(state, {"lei": texto_lei})
                uppercase_buffer.clear()
            if header_match:
                state = reset_level(state, header_match)
            if article_match:
                if current_article_lines:
                    full_content = " ".join(current_article_lines)
                    full_content = HYPHENATION_PATTERN.sub(r'\1\2', full_content)
                    document_ = Document(page_content=full_content, metadata={**state, "ARTIGO": current_article_header})
                    chunks.append(document_)
                    
                current_article_lines = [line_strip]
                current_article_header = line_strip

        elif line_strip.isupper():
            uppercase_buffer.append(line_strip)           # acumula, nao decide nada ainda

        else:
            if uppercase_buffer:                           # linha normal: esvazia o buffer tambem
                texto_lei = " ".join(uppercase_buffer)
                state = reset_level(state, {"lei": texto_lei})
                uppercase_buffer.clear()
            if current_article_lines:
                current_article_lines.append(line_strip)
                
    if current_article_lines:
        full_content = " ".join(current_article_lines)
        full_content = HYPHENATION_PATTERN.sub(r'\1\2', full_content)
        document_ = Document(page_content=full_content, metadata={**state, "ARTIGO": current_article_header})
        chunks.append(document_)
        
    return chunks