import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.util.constants import HYPHENATION_PATTERN, LEVELS_STANDARD, STATE_MAP, REFERENCE_CODE_PATTERN
from src.util.doc_standardization import find_header, reset_level

# exemplo_linhas = [
#     "a seguinte:",
#     "LEI QUE APROVA",
#     "O CÓDIGO PENAL ANGOLANO",
#     "ARTIGO 1.º",
#     "(Aprovação)",
# ]
# print(find_law_title(exemplo_linhas, 3))  # esperado: "LEI QUE APROVA O CÓDIGO PENAL ANGOLANO"

# exemplo_linhas2 = [
#     "3. Alguma frase normal do artigo anterior.",
#     "",
#     "ARTIGO 82.º",
#     "(Terceira idade)",
# ]
# print(find_law_title(exemplo_linhas2, 2))  # esperado: None

# exemplo = ["TÍTULO I", "CAPÍTULO III", "SECÇÃO II", "TÍTULO II", "texto qualquer","TITULO V"]

# for e in exemplo:
#     match_ = find_header(e)
#     if match_:
#         dic = reset_level(STATE_MAP,match_)
#         print(dic)
        
# print("--- CASOS VÁLIDOS (Deverm retornar True) ---")
# print("LIVRO III : " + str(bool(LEVELS_STANDARD.match("LIVRO III"))))
# print("LIVRO IV : " + str(bool(LEVELS_STANDARD.match("LIVRO IV"))))
# print("LIVRO ÚNICO : " + str(bool(LEVELS_STANDARD.match("LIVRO ÚNICO"))))
# print("TITULO V : " + str(bool(LEVELS_STANDARD.match("TITULO V"))))
# print("TÍTULO X : " + str(bool(LEVELS_STANDARD.match("TÍTULO X"))))
# print("CAPITULO L : " + str(bool(LEVELS_STANDARD.match("CAPITULO L"))))
# print("CAPÍTULO C : " + str(bool(LEVELS_STANDARD.match("CAPÍTULO C"))))
# print("CAPÍTULO ÚNICO : " + str(bool(LEVELS_STANDARD.match("CAPÍTULO ÚNICO"))))
# print("CAPÍTULO III : " + str(bool(LEVELS_STANDARD.match("CAPÍTULO III"))))
# print("SECCAO M : " + str(bool(LEVELS_STANDARD.match("SECCAO M"))))
# print("SECÇÃO MMXXVI : " + str(bool(LEVELS_STANDARD.match("SECÇÃO MMXXVI"))))
# print("SUBSECCAO II : " + str(bool(LEVELS_STANDARD.match("SUBSECCAO II"))))
# print("SUBSECÇÃO IX : " + str(bool(LEVELS_STANDARD.match("SUBSECÇÃO IX"))))
# print("SUBSECÇÃO ÚNICO : " + str(bool(LEVELS_STANDARD.match("SUBSECÇÃO ÚNICO"))))
# print("CAPÍTULO VI: " + str(bool(LEVELS_STANDARD.match("CAPÍTULO VI"))))

# print("\n--- ESPAÇOS EM BRANCO EXTRAS (Devem retornar True) ---")
# print("LIVRO   I : " + str(bool(LEVELS_STANDARD.match("LIVRO   I"))))
# print("SECÇÃO \t IV : " + str(bool(LEVELS_STANDARD.match("SECÇÃO \t IV"))))

# print("\n--- CASOS INVÁLIDOS (Devem retornar False) ---")
# print("livro I (Minúsculo) : " + str(bool(LEVELS_STANDARD.match("livro I"))))
# print("LIVRO 1 (Número Arábico) : " + str(bool(LEVELS_STANDARD.match("LIVRO 1"))))
# print("LIVRO UNICO (Sem acento) : " + str(bool(LEVELS_STANDARD.match("LIVRO UNICO"))))
# print("LIVRO I  (Espaço no fim) : " + str(bool(LEVELS_STANDARD.match("LIVRO I "))))
# print(" LIVRO I (Espaço no início) : " + str(bool(LEVELS_STANDARD.match(" LIVRO I"))))
# print("ARTIGO 1.º (Palavra fora da lista) : " + str(bool(LEVELS_STANDARD.match("ARTIGO 1.º"))))
# print("LIVRO ABC (Letras normais) : " + str(bool(LEVELS_STANDARD.match("LIVRO ABC"))))
# print("LIVRO (Faltando o número) : " + str(bool(LEVELS_STANDARD.match("LIVRO"))))
# print("LIVRO I PARTE A (Texto extra) : " + str(bool(LEVELS_STANDARD.match("LIVRO I PARTE A"))))

print(bool(REFERENCE_CODE_PATTERN.match("(21-6725-A-PR)")))  # esperado: True
print(bool(REFERENCE_CODE_PATTERN.match("21-6725-A-PR")))    # esperado: False (sem parenteses)
print(bool(REFERENCE_CODE_PATTERN.match("(texto qualquer)")))  # esperado: False

print(HYPHENATION_PATTERN.sub(r'\1\2', "efecti - vação dos seus direitos"))
# esperado: "efectivação dos seus direitos"

print(HYPHENATION_PATTERN.sub(r'\1\2', "político-partidária"))
# esperado: SEM alteração (não tem espaços à volta do hífen, não deve mexer)