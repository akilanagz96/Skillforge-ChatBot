import os
from threading import Lock

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


MODELS = [
    "google/gemma-4-31b-it:free",
    "google/gemma-4-26b-a4b-it:free",
    "openai/gpt-oss-20b:free",
]

API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = "https://openrouter.ai/api/v1"

_current_model = 0
_llm = None
_lock = Lock()


def _create_llm(model: str) -> ChatOpenAI:

    return ChatOpenAI(
        model=model,
        api_key=API_KEY,
        base_url=BASE_URL,
        temperature=0,
    )


def get_llm() -> ChatOpenAI:

    global _llm

    with _lock:

        if _llm is None:

            _llm = _create_llm(
                MODELS[_current_model]
            )

            print(
                f"✅ Using OpenRouter model: {MODELS[_current_model]}"
            )

    return _llm


def switch_model() -> str:

    global _current_model
    global _llm

    with _lock:

        _current_model = (
            (_current_model + 1)
            % len(MODELS)
        )

        _llm = _create_llm(
            MODELS[_current_model]
        )

        print(
            f"🔄 Switched to: {MODELS[_current_model]}"
        )

        return MODELS[_current_model]


def get_model_count() -> int:

    return len(MODELS)


def get_current_model() -> str:

    return MODELS[_current_model]