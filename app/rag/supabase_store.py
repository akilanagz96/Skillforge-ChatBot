import os

from dotenv import load_dotenv
from supabase import create_client

from app.config import settings

load_dotenv()

supabase = create_client(
    os.getenv(settings.SUPABASE_URL_ENV),
    os.getenv(settings.SUPABASE_KEY_ENV),
)


def insert_document(
    content: str,
    embedding: list[float],
    metadata: dict,
):
    return (
        supabase.table("documents")
        .insert(
            {
                "content": content,
                "embedding": embedding,
                "course_name": metadata.get("course_name"),
                "document_type": metadata.get("document_type"),
                "source": metadata.get("source"),
                "chunk_index": metadata.get("chunk_index"),
                "metadata": metadata,
            }
        )
        .execute()
    )


def match_documents(
    embedding: list[float],
    match_count: int,
    course_name: str | None = None,
    source: str | None = None,
):
    return (
        supabase.rpc(
            "match_documents",
            {
                "query_embedding": embedding,
                "match_count": match_count,
                "filter_course": course_name,
                "filter_source": source,
            },
        )
        .execute()
    )