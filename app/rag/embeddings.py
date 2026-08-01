import os
import re
import time

from dotenv import load_dotenv
from google import genai
from google.genai import types
from google.genai.errors import ClientError

from app.config import settings

load_dotenv()

client = genai.Client(
    api_key=os.getenv(settings.GEMINI_API_KEY_ENV)
)


def _embed(contents):
    """
    Internal helper that automatically retries when the Gemini
    embedding API rate limit is reached.
    """

    while True:

        try:

            response = client.models.embed_content(
                model=settings.EMBEDDING_MODEL,
                contents=contents,
                config=types.EmbedContentConfig(
                    output_dimensionality=768
                ),
            )

            return response

        except ClientError as e:

            error_text = str(e)

            # Handle Gemini rate limits
            if "429" in error_text or "RESOURCE_EXHAUSTED" in error_text:

                match = re.search(r"Retry in ([0-9.]+)s", error_text)

                if match:
                    wait_time = int(float(match.group(1))) + 2
                else:
                    wait_time = 60

                print("\n" + "=" * 60)
                print("⚠ Gemini rate limit reached.")
                print(f"Waiting {wait_time} seconds...")
                print("=" * 60 + "\n")

                time.sleep(wait_time)
                continue

            # Any other error should still stop the program
            raise


def get_embedding(text: str) -> list[float]:
    """
    Generate a Gemini embedding for a single piece of text.
    """

    response = _embed(text)

    return response.embeddings[0].values


def get_embeddings(texts: list[str]) -> list[list[float]]:
    """
    Generate embeddings for multiple texts.
    """

    response = _embed(texts)

    return [embedding.values for embedding in response.embeddings]