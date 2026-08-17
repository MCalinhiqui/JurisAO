from pydantic import BaseModel

class QuestionRequest(BaseModel):
    question: str
    k: int = 4

class AnswerResponse(BaseModel):
    answer: str
    sources: list[dict]