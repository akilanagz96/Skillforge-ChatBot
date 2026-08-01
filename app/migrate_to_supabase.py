from app.rag.loader import load_documents
from app.rag.splitter import split_documents
from app.rag.embeddings import get_embeddings
from app.rag.supabase_store import supabase

BATCH_SIZE = 50


def build_metadata(chunk, index):
    metadata = dict(chunk.metadata)

    return {
        "course_name": metadata.get("course_name"),
        "document_type": metadata.get("document_type"),
        "source": metadata.get("source"),
        "chunk_index": index,
        "metadata": metadata,
    }


def get_uploaded_count():
    """
    Returns the number of documents already uploaded to Supabase.
    """

    response = (
        supabase.table("documents")
        .select("id", count="exact")
        .limit(1)
        .execute()
    )

    return response.count or 0


def migrate():

    print("Loading documents...")
    documents = load_documents()

    print("Splitting documents...")
    chunks = split_documents(documents)

    total_chunks = len(chunks)

    print(f"Total chunks: {total_chunks}")

    uploaded = get_uploaded_count()

    print(f"Already uploaded: {uploaded}")

    if uploaded >= total_chunks:
        print("All documents have already been migrated.")
        return

    print(f"Resuming from chunk {uploaded}...")

    for start in range(uploaded, total_chunks, BATCH_SIZE):

        batch = chunks[start:start + BATCH_SIZE]

        texts = [chunk.page_content for chunk in batch]

        embeddings = get_embeddings(texts)

        rows = []

        for i, (chunk, embedding) in enumerate(zip(batch, embeddings), start=start):

            meta = build_metadata(chunk, i)

            rows.append(
                {
                    "content": chunk.page_content,
                    "embedding": embedding,
                    "course_name": meta["course_name"],
                    "document_type": meta["document_type"],
                    "source": meta["source"],
                    "chunk_index": meta["chunk_index"],
                    "metadata": meta["metadata"],
                }
            )

        supabase.table("documents").insert(rows).execute()

        print(
            f"Uploaded {min(start + BATCH_SIZE, total_chunks)}/{total_chunks}"
        )

    print("\nMigration complete!")
    print(f"Total documents uploaded: {total_chunks}")


if __name__ == "__main__":
    migrate()