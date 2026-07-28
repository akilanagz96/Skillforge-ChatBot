from app.rag.llm import get_llm
from app.rag.course_resolver import CourseResolver
from app.rag.course_display_names import COURSE_DISPLAY_NAMES


class QuestionRewriter:

    def __init__(self):
        self.llm = get_llm()
        self.course_resolver = CourseResolver()

    def rewrite(self, history, question: str) -> str:

        recent_history = history[-6:]

        history_text = "\n".join(
            f"{m['role']}: {m['content']}"
            for m in recent_history
        )

        history_course_names = self.course_resolver.resolve_all(
            history_text
        )

        # Convert internal names to display names
        display_names = [
            COURSE_DISPLAY_NAMES.get(course, course)
            for course in history_course_names
        ]

        course_context = "\n".join(
            f"- {course}"
            for course in display_names
        )

        prompt = f"""
You rewrite follow-up questions into standalone questions.

Conversation:
{history_text}

Courses mentioned:
{course_context if course_context else "None"}

Latest user question:
{question}

Rules:

1. NEVER answer the question.

2. If the latest question already contains a complete course name,
leave it unchanged.

3. If the latest question contains pronouns such as:
- it
- this
- that
- this course
- the course
- the first one
- the second one
replace them with the correct course name from the conversation.

4. Preserve the user's exact intent.

5. Return ONLY the rewritten standalone question.

Standalone question:
"""

        response = self.llm.invoke(prompt)

        return response.content.strip()