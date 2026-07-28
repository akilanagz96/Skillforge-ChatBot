from app.rag.course_resolver import CourseResolver


resolver = CourseResolver()

question = (
    "Which is better: Python Full Stack Development Course "
    "or AI-Integrated Python Full Stack Development Course?"
)

courses = resolver.resolve_all(question)

print("Resolved courses:")

for course in courses:
    print("-", course)