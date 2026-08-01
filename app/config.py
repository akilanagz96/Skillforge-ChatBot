from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:

    # ----------------------------
    # Models
    # ----------------------------

    LLM_MODEL: str = "google/gemma-4-31b-it:free"
    EMBEDDING_MODEL: str = "gemini-embedding-001"

    # ----------------------------
    # API Keys (.env)
    # ----------------------------

    GEMINI_API_KEY_ENV: str = "GEMINI_API_KEY"
    OPENROUTER_API_KEY_ENV: str = "OPENROUTER_API_KEY"

    # ----------------------------
    # Vector Database
    # ----------------------------

    COLLECTION_NAME: str = "education_courses"
    VECTOR_DB: str = "vectorstore"

    SUPABASE_URL_ENV: str = "SUPABASE_URL"
    SUPABASE_KEY_ENV: str = "SUPABASE_KEY"

    # ----------------------------
    # Retrieval
    # ----------------------------

    SEARCH_TYPE: str = "similarity"
    TOP_K: int = 5

    # ----------------------------
    # UI
    # ----------------------------

    LEAD_POPUP_AFTER: int = 5


settings = Settings()