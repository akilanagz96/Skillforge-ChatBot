class AmbiguityDetector:

    AMBIGUOUS_PHRASES = [
        "the course",
        "this course",
        "it",
        "its",
    ]

    def is_ambiguous(
        self,
        question: str,
        has_history: bool,
        resolved_course: str | None,
    ) -> bool:

        # Exact course already identified
        if resolved_course:
            return False

        # Conversation history may provide the missing reference
        if has_history:
            return False

        question_lower = question.lower()

        return any(
            phrase in question_lower
            for phrase in self.AMBIGUOUS_PHRASES
        )