from app.rag.ambiguity_detector import AmbiguityDetector


detector = AmbiguityDetector()

tests = [
    ("How long is the course?", False, None),
    ("What technologies does it use?", False, None),
    ("How long is the Python Full Stack Development Course?", False,
     "Python Full Stack Development Course"),
    ("How long is it?", True, None),
]


for question, has_history, resolved_course in tests:

    result = detector.is_ambiguous(
        question=question,
        has_history=has_history,
        resolved_course=resolved_course,
    )

    print("=" * 80)
    print("Question:", question)
    print("Ambiguous:", result)