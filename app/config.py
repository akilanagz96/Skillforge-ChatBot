from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    # Gemini Models
    LLM_MODEL: str = "gemini-2.0-flash-lite"
    EMBEDDING_MODEL: str = "BAAI/bge-small-en-v1.5"

    # API Key (loaded from .env)
    GEMINI_API_KEY_ENV: str = "GEMINI_API_KEY"

    # Vector Database
    COLLECTION_NAME: str = "education_courses"
    VECTOR_DB: str = "vectorstore"

    # Retrieval
    SEARCH_TYPE: str = "similarity"
    TOP_K: int = 5

    # UI
    LEAD_POPUP_AFTER: int = 5


settings = Settings()