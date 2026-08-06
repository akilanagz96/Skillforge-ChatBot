from fastapi import FastAPI

from app.models.request import ChatRequest
from app.models.response import ChatResponse
from app.rag.service import RAGService
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Education Chatbot API",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://skillforge-frontend-swart.vercel.app",
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

chatbot = RAGService()


@app.get("/")
def home():
    return {
        "message": "Education Chatbot API",
        "cors_test": "2026-08-06"
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