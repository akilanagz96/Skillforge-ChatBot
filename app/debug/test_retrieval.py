from app.rag.retriever import get_retriever

retriever = get_retriever()

docs = retriever.invoke(
    "What is the duration of the Python Full Stack Development course?"
)

for i, doc in enumerate(docs, start=1):

    print("=" * 80)
    print(f"Document {i}")
    print(doc.metadata["source"])
    print()
    print(doc.page_content)