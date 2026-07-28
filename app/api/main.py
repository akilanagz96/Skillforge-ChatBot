from fastapi import FastAPI

from app.models.request import ChatRequest
from app.models.response import ChatResponse
from app.rag.service import RAGService


app = FastAPI(
    title="Education Chatbot API",
    version="1.0"
)

chatbot = RAGService()


@app.get("/")
def home():
    return {
        "message": "Education Chatbot API"
    }


@app.post(
    "/chat",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    return chatbot.ask(
        session_id=request.session_id,
        question=request.question
    )