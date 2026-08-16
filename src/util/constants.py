import re

LEVELS_STANDARD = re.compile(r'^(LIVRO|PARTE|T[IÍ]TULO|CAP[IÍ]TULO|SUBSEC[CÇ][AÃ]O|SEC[CÇ][AÃ]O)\s+([IVXLCDM]+|ÚNICO)$')

STANDARD_ARTICLE = re.compile(r'^ARTIGO\s+(\d+)\.?[º°]?')

REFERENCE_CODE_PATTERN = re.compile(r'^\(\d+-\d+-[A-Z]+-[A-Z]+\)$')

ANEXO_PATTERN = re.compile(r'^ANEXO\s+([IVXLCDM]+)$')

HYPHENATION_PATTERN = re.compile(r'([a-zà-úçãõâêôA-ZÀ-Ú])\s+-\s+([a-zà-úçãõ])')

LEVELS_MAP = {
    "LIVRO": "livro",
    "PARTE": "parte",
    "TÍTULO": "titulo",
    "CAPÍTULO": "capitulo",
    "SECÇÃO": "seccao",
    "SUBSECÇÃO": "subseccao"
}

LEVELS_EQ = {
    "TITULO":"TÍTULO",
    "CAPITULO": "CAPÍTULO",
    "SECCAO":"SECÇÃO",
    "SUBSECCAO":"SUBSECÇÃO",
}

LEVELS_ORDER = ["lei","parte","livro", "titulo", "capitulo", "seccao", "subseccao"]

STATE_MAP = {
    "LEI": None,
    "PARTE": None,
    "LIVRO": None,
    "TÍTULO": None,
    "CAPÍTULO": None,
    "SECÇÃO": None,
    "SUBSECÇÃO": None
}

PAGE_NOISE = [
    "DIÁRIO DA REPÚBLICA",
    "SUMÁRIO",
    "ASSEMBLEIA NACIONAL",
    "ASSINATURA",
    "ÓRGÃO OFICIAL DA REPÚBLICA DE ANGOLA",
    "ÓRGÃO  OFICIAL DA REPÚBLICA DE ANGOLA",  # repara nos 2 espaços, como aparece no texto real
    "LEGISLADORES CONSTITUINTES",
]

STANDARD_PAGE_NUMBER = re.compile(r'^\d+$')