from app.rag.vector_store import get_vector_store

db = get_vector_store()

print("Number of chunks in ChromaDB:")
print(db._collection.count())