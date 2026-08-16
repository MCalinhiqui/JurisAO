import sys
from .constants import ANEXO_PATTERN, REFERENCE_CODE_PATTERN, LEVELS_EQ, LEVELS_MAP, LEVELS_ORDER, LEVELS_STANDARD, PAGE_NOISE, STANDARD_PAGE_NUMBER

def get_normalized_key(key: str) -> str:
    new_key_complete = key.upper()
    new_key = new_key_complete.split(" ")
    
    key = LEVELS_EQ.get(new_key[0], new_key[0])
    if len(new_key) > 1:
        new_key_complete = key+" "+new_key_complete.split(" ")[1]
    else:
        new_key_complete = key 
    return new_key_complete

def find_header(linha: str):
    linha = linha.strip();
    match_ = bool(LEVELS_STANDARD.match(linha))
    if match_ :
        linha = get_normalized_key(linha)
        key = linha.split(" ")[0]
        value = LEVELS_MAP.get(key)
        return {value:linha}
    else:
        return None

def reset_level(estado: dict, match_: dict):
    match_key, match_value = list(match_.items())[0]
    key = get_normalized_key(match_key)
    
    estado[key] = match_value
    
    index = LEVELS_ORDER.index(match_key)
    levels = LEVELS_ORDER[index+1:]
        
    for level in levels:
        if level in LEVELS_MAP.values():
            key = get_normalized_key(level)
            estado[key] = None
    
    return estado
    
def find_page_noise(linha: str) -> bool:
    is_noise = PAGE_NOISE.__contains__(linha)
    is_annex = bool(ANEXO_PATTERN.match(linha))
    is_page_number = bool(STANDARD_PAGE_NUMBER.match(linha))
    is_reference_code = bool(REFERENCE_CODE_PATTERN.match(linha))
    if is_noise or is_page_number or is_reference_code or is_annex:
        return True
    else:
        return False
        
