from app.rag.query_router import QueryRouter


router = QueryRouter()

questions = [
    "What Python courses do you offer?",
    "What courses are available?",
    "Do you have any data analytics courses?",
    "What is the duration of the Python Full Stack Development Course?",
    "How long is it?",
]


for question in questions:

    print("=" * 80)
    print("Question:", question)
    print("Catalog query:", router.is_catalog_query(question))