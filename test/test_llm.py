from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

response = llm.invoke("Identifica-te")
print(response.content[0].get("text"))