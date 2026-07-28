from app.rag.loader import load_documents
from app.rag.splitter import split_documents

documents = load_documents()
chunks = split_documents(documents)

print(f"Total chunks created: {len(chunks)}")

for chunk in chunks:
    if "Course Duration" in chunk.page_content:
        print("=" * 80)
        print(chunk.metadata["source"])
        print(chunk.page_content)