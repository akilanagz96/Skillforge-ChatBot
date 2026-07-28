import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from app.config import settings

load_dotenv()


def get_llm():
    return ChatGoogleGenerativeAI(
        model=settings.LLM_MODEL,
        google_api_key=os.getenv(settings.GEMINI_API_KEY_ENV),
        temperature=0,
        max_retries=5,
    )