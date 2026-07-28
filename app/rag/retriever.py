from app.config import settings
from app.rag.vector_store import get_vector_store
from app.rag.document_map import DOCUMENT_MAP


def get_retriever(
    course_name: str | None = None,
    document_type: str | None = None,
):

    vector_store = get_vector_store()

    search_kwargs = {
        "k": settings.TOP_K
    }

    # --------------------------------------------------
    # Course-specific retrieval
    # --------------------------------------------------

    if course_name:

        search_kwargs["filter"] = {
            "course_name": course_name
        }

    # --------------------------------------------------
    # Policy / document retrieval
    # --------------------------------------------------

    elif document_type:

        sources = DOCUMENT_MAP.get(document_type)

        if sources:

            search_kwargs["filter"] = {
                "source": sources[0]
            }

    # --------------------------------------------------
    # Return Retriever
    # --------------------------------------------------

    return vector_store.as_retriever(
        search_type=settings.SEARCH_TYPE,
        search_kwargs=search_kwargs,
    )