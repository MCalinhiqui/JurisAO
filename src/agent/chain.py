from langchain_google_genai import ChatGoogleGenerativeAI
from src.agent.retriever import load_vector_store, retrieve_articles
from src.agent.prompts import SYSTEM_PROMPT, QUERY_REWRITE_PROMPT, build_context
from dotenv import load_dotenv

load_dotenv()

_vector_store = None
_llm = None

def rewrite_query(question: str) -> str:
    try:
        llm = get_llm()
        prompt = QUERY_REWRITE_PROMPT.format(question=question)
        response = llm.invoke(prompt)
        return extract_text(response.content).strip()
    except Exception:
        return question

def get_vector_store():
    global _vector_store
    if _vector_store is None:
        _vector_store = load_vector_store()
    return _vector_store

def get_llm():
    global _llm
    if _llm is None:
        _llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
    return _llm

def extract_text(content) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "".join(bloco.get("text", "") for bloco in content if isinstance(bloco, dict))
    return str(content)

def ask(question: str, k: int = 4) -> dict:
    vector_store = get_vector_store()
    search_query = rewrite_query(question)

    articles_rewritten = retrieve_articles(vector_store, search_query, k=k)
    articles_original = retrieve_articles(vector_store, question, k=k)

    seen = set()
    articles = []
    for a in articles_rewritten + articles_original:
        chave = (a.metadata.get("LEI"), a.metadata.get("artigo"))
        if chave not in seen:
            seen.add(chave)
            articles.append(a)
    articles = articles[:k]

    context = build_context(articles)
    prompt = SYSTEM_PROMPT.format(context=context, question=question)

    try:
        llm = get_llm()
        response = llm.invoke(prompt)
        answer = extract_text(response.content)
    except Exception:
        answer = (
            "De momento não foi possível gerar uma resposta, provavelmente devido a "
            "limite de pedidos ao modelo de linguagem. Por favor, tente novamente "
            "dentro de alguns instantes."
        )

    return {
        "answer": answer,
        "sources": [a.metadata for a in articles],
        "search_query_used": search_query,
    }
    

