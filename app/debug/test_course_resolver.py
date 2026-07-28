from app.rag.course_resolver import CourseResolver


resolver = CourseResolver()

questions = [
    "Does the Python Full Stack Development Course include AI integration?",
    "What is the duration of the AI-Integrated Python Full Stack Development Course?",
    "What Python courses do you offer?",
]


for question in questions:
    course = resolver.resolve(question)

    print("=" * 80)
    print("Question:", question)
    print("Resolved course:", course)