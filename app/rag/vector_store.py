import os
import shutil

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from app.config import settings


# --------------------------------------------------------------------
# Singleton instances
# --------------------------------------------------------------------

_embeddings = None
_vector_store = None


def get_embeddings() -> HuggingFaceEmbeddings:
    """
    Load the embedding model only once and reuse it
    for the lifetime of the application.
    """

    global _embeddings

    if _embeddings is None:
        print("Loading embedding model...")

        _embeddings = HuggingFaceEmbeddings(
            model_name=settings.EMBEDDING_MODEL,
            model_kwargs={
                "device": "cpu"
            },
            encode_kwargs={
                "normalize_embeddings": True
            },
        )

    return _embeddings


def get_vector_store() -> Chroma:
    """
    Load the Chroma vector store only once.
    """

    global _vector_store

    if _vector_store is None:
        print("Loading vector store...")

        _vector_store = Chroma(
            collection_name=settings.COLLECTION_NAME,
            embedding_function=get_embeddings(),
            persist_directory=settings.VECTOR_DB,
        )

    return _vector_store


def build_vector_store(chunks):
    """
    Rebuild the vector database from scratch.
    """

    global _vector_store

    if os.path.exists(settings.VECTOR_DB):
        shutil.rmtree(settings.VECTOR_DB)

    # Create a brand-new Chroma instance
    vector_store = Chroma(
        collection_name=settings.COLLECTION_NAME,
        embedding_function=get_embeddings(),
        persist_directory=settings.VECTOR_DB,
    )

    batch_size = 50
    total = len(chunks)

    for i in range(0, total, batch_size):

        batch = chunks[i:i + batch_size]

        print(
            f"Embedding batch {i // batch_size + 1} "
            f"({i + 1}-{min(i + batch_size, total)}/{total})"
        )

        vector_store.add_documents(batch)

    # Cache the newly built vector store
    _vector_store = vector_store

    return vector_store