from app.rag.course_resolver import CourseResolver


resolver = CourseResolver()

questions = [
    "Tell me about the full stack course.",
    "Tell me about the Python full stack course.",
    "Tell me about the Flutter course.",
]


for question in questions:

    matches = resolver.find_partial_matches(question)

    print("=" * 80)
    print("Question:", question)
    print("Matches:")

    for match in matches:
        print("-", match)