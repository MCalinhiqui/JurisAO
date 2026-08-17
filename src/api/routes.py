from fastapi import APIRouter
from src.api.schemas import QuestionRequest, AnswerResponse
from src.agent.chain import ask

router = APIRouter()

@router.post("/ask", response_model=AnswerResponse)
def ask_question(request: QuestionRequest):
    result = ask(request.question, k=request.k)
    return AnswerResponse(answer=result["answer"], sources=result["sources"])

@router.get("/health")
def health_check():
    return {"status": "ok"}