import os
import streamlit as st

# --- Ponte de segredos: Streamlit Cloud usa st.secrets, não .env ---
# Isto faz com que o src/config.py (que lê os.getenv) continue a funcionar sem alterações
try:
    if "GEMINI_API_KEY" in st.secrets:
        os.environ["GEMINI_API_KEY"] = st.secrets["GEMINI_API_KEY"]
except Exception:
    pass  # sem secrets.toml (execução local) — o .env já trata disto via config.py

from src.agent.chain import ask

# --- Configuração da página ---
st.set_page_config(
    page_title="JurisAO — Legislação angolana",
    page_icon="⚖️",
    layout="centered",
)

# --- Identidade visual (paleta papel/dourado, tipografia serifada) ---
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<style>
    :root {
        --paper: #F6F1E7;
        --paper-raised: #FBF8F2;
        --ink: #241F1A;
        --ink-muted: #6B6255;
        --line: #D8CFB8;
        --gold: #A6752C;
        --gold-dark: #7A5620;
        --seal-red: #7A2E2E;
    }

    .stApp {
        background-color: var(--paper);
    }

    h1, h2, h3 {
        font-family: 'Source Serif 4', serif !important;
        color: var(--ink) !important;
    }

    .subtitle-box {
        text-align: center !important;
        color: var(--ink-muted);
        font-family: 'Inter', sans-serif;
        font-size: 15px;
        line-height: 1.6;
        width: 100%;
        max-width: 520px;
        margin: 0 auto 8px !important;
        display: block;
    }

    [data-testid="stChatMessage"] {
        font-family: 'Source Serif 4', serif;
        color: black;
        border-radius: 10px;
    }

    .footer-note {
        text-align: center;
        font-family: 'Inter', sans-serif;
        font-size: 11px;
        color: var(--ink-muted);
        margin-top: 32px;
        line-height: 1.6;
    }
    
    [data-testid="stChatMessage"] p,
    [data-testid="stChatMessage"] li,
    [data-testid="stChatMessage"] span,
    [data-testid="stChatMessage"] div {
        color: var(--ink) !important;
    }
    
    .stApp button:hover,
    .stApp button:focus,
    .stApp button:active {
        background-color: var(--ink) !important;
        color: var(--paper) !important;
        border-color: var(--ink) !important;
    }
    
    [data-testid="stChatInput"] {
        bottom: 42px !important;
    }
    
    h1 em{
        font-style: normal;
        color: var(--gold);
        border-bottom: 2px solid var(--gold);
    }
    
    div[data-testid="stPopover"] {
        margin-left: auto !important;
        margin-right: auto !important;
        width: fit-content !important;
        display: block !important;
    }
</style>
""", unsafe_allow_html=True)

# --- Logo (selo com balança) ---
st.markdown("""
<div style="text-align:center; margin-bottom: -10px;">
<svg width="52" height="52" viewBox="0 0 44 44" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="22" cy="22" r="20" stroke="#A6752C" stroke-width="1"/>
  <circle cx="22" cy="22" r="17" stroke="#A6752C" stroke-width="0.75"/>
  <line x1="22" y1="11" x2="22" y2="29" stroke="#A6752C" stroke-width="1.1" stroke-linecap="round"/>
  <circle cx="22" cy="10.5" r="1.2" fill="#A6752C"/>
  <line x1="11" y1="15" x2="33" y2="15" stroke="#A6752C" stroke-width="1.1" stroke-linecap="round"/>
  <line x1="11" y1="15" x2="11" y2="21" stroke="#A6752C" stroke-width="0.9" stroke-linecap="round"/>
  <line x1="33" y1="15" x2="33" y2="21" stroke="#A6752C" stroke-width="0.9" stroke-linecap="round"/>
  <ellipse cx="11" cy="22" rx="5.5" ry="2" stroke="#A6752C" stroke-width="0.9"/>
  <ellipse cx="33" cy="22" rx="5.5" ry="2" stroke="#A6752C" stroke-width="0.9"/>
  <line x1="22" y1="29" x2="22" y2="32" stroke="#A6752C" stroke-width="1.1" stroke-linecap="round"/>
  <line x1="16" y1="32" x2="28" y2="32" stroke="#A6752C" stroke-width="1.1" stroke-linecap="round"/>
</svg>
</div>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center; margin-bottom:0;'>A legislação angolana,<br>ao alcance de <em>todos</em>.</h1>", unsafe_allow_html=True)
st.markdown(
    "<p class='subtitle-box' >Pergunte sobre a legislação angolana disponível e receba respostas "
    "com a lei e o artigo exato de onde vêm.</p>",
    unsafe_allow_html=True,
)

with st.popover("Ver legislações disponíveis"):
    st.markdown("""
    **Fontes atualmente indexadas**
    - Constituição da República de Angola
    - Código Penal Angolano
    - Código do Processo Penal Angolano
    """)

@st.dialog("Sobre o JurisAO")
def show_about():
    st.markdown("""
**O que é o JurisAO?**

Um agente de Inteligência Artificial que responde a perguntas sobre legislação angolana, com base exclusivamente em documentos legais reais — nunca por adivinhação. Cada resposta inclui a lei e o artigo exato de onde a informação foi retirada.

**Como usar**

Escreve a tua pergunta em português corrente, como falarias com uma pessoa (ex: *"quais são os direitos da criança?"*). Não precisas de usar termos jurídicos — o agente entende linguagem natural.

**O que está disponível atualmente**
- Constituição da República de Angola
- Código Penal Angolano
- Código do Processo Penal Angolano

**Limitações importantes**
- É um assistente **informativo**, não substitui aconselhamento jurídico profissional
- Cada pergunta é processada de forma independente (ainda sem memória de conversa)
- A cobertura legal está a crescer — nem todas as leis angolanas estão disponíveis ainda
- Pode ocasionalmente não encontrar informação que existe nos documentos, devido a limitações técnicas de busca
    """)
    
if st.button("Sobre a plataforma"):
    show_about()

st.divider()

# --- Histórico de conversa (apenas visual; cada pergunta é processada de forma independente) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

question = st.chat_input("Ex: Quais são os direitos da criança?")

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("A consultar a legislação..."):
            try:
                result = ask(question, k=6)
                answer = result["answer"]
            except Exception:
                answer = (
                    "Não foi possível obter resposta neste momento "
                    "(limite de pedidos atingido ou instabilidade temporária). "
                    "Tente novamente dentro de instantes."
                )
        st.markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})

st.markdown(
    "<div class='footer-note' style='position:fixed; bottom:0; left:0; right:0; "
    "background:var(--paper); padding:6px 0 10px; z-index:999999; margin-top:0;'>"
    "JurisAO é um assistente informativo e não substitui aconselhamento jurídico profissional.<br>"
    "</div>",
    unsafe_allow_html=True,
)