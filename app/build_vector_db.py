from app.rag.loader import load_documents
from app.rag.splitter import split_documents
from app.rag.vector_store import build_vector_store


def main():

    print("Loading documents...")
    documents = load_documents()

    print(f"Loaded {len(documents)} documents")

    print("Splitting documents...")
    chunks = split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    print("Building vector database...")
    build_vector_store(chunks)

    print("✅ Done!")


if __name__ == "__main__":
    main()