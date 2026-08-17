import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.agent.chain import ask

resultado = ask("Se eu assassinar alguem sem querer qual será a pena?")
print(resultado["answer"])
print("\nFontes:")
for s in resultado["sources"]:
    print(" -", s.get("artigo"), "|", s.get("LEI"))