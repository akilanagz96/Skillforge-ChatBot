from langchain_core.documents import Document

from app.config import settings
from app.rag.document_map import DOCUMENT_MAP
from app.rag.embeddings import get_embedding
from app.rag.supabase_store import match_documents


def get_relevant_documents(
    query: str,
    course_name: str | None = None,
    document_type: str | None = None,
) -> list[Document]:

    embedding = get_embedding(query)

    source = None

    if document_type:
        sources = DOCUMENT_MAP.get(document_type)

        if sources:
            source = sources[0]

    response = match_documents(
        embedding=embedding,
        match_count=settings.TOP_K,
        course_name=course_name,
        source=source,
    )

    docs = []

    for row in response.data:

        docs.append(
            Document(
                page_content=row["content"],
                metadata=row["metadata"],
            )
        )

    return docs