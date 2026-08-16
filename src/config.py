from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
chave = os.getenv("GEMINI_API_KEY")

if not chave:
    raise ValueError("A chave não foi encontrada!!")

