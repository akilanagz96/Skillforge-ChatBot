from app.rag.vector_store import get_vector_store
from app.rag.course_display_names import (
    COURSE_DISPLAY_NAMES,
    COURSE_ALIASES,
)


class CourseResolver:

    def __init__(self):

        vector_store = get_vector_store()

        data = vector_store.get(include=["metadatas"])

        self.course_names = sorted(
            {
                metadata["course_name"]
                for metadata in data["metadatas"]
                if metadata.get("course_name")
            },
            key=len,
            reverse=True,
        )

        # Build searchable terms for each course
        self.search_terms = {}

        for course_name in self.course_names:

            terms = set()

            # Internal name
            terms.add(course_name)

            # Display name
            display_name = COURSE_DISPLAY_NAMES.get(course_name)

            if display_name:

                terms.add(display_name)

                # Short version without "Professional Program"
                short_name = display_name.replace(
                    " Professional Program",
                    ""
                )
                terms.add(short_name)

            # Aliases
            for alias in COURSE_ALIASES.get(course_name, []):
                terms.add(alias)

            self.search_terms[course_name] = sorted(
                terms,
                key=len,
                reverse=True,
            )

        print(self.search_terms)

    def resolve(self, question: str) -> str | None:
        """
        Return the first course mentioned in the question.
        """
        matches = self.resolve_all(question)

        return matches[0] if matches else None

    def resolve_all(self, question: str) -> list[str]:
        """
        Return all courses mentioned in the question.
        """

        question_lower = question.lower()

        matches = []

        for course_name, terms in self.search_terms.items():

            for term in terms:

                if term.lower() in question_lower:

                    matches.append(course_name)
                    break

        return matches

    def find_partial_matches(self, question: str) -> list[str]:
        """
        Find likely course matches from partial names.
        """

        stop_words = {
            "tell",
            "me",
            "about",
            "the",
            "a",
            "an",
            "course",
            "courses",
            "what",
            "is",
            "do",
            "you",
            "have",
            "for",
            "professional",
            "program",
            "please",
            "give",
            "show",
        }

        question_words = {
            word.lower().strip("?!.,")
            for word in question.split()
            if word.lower().strip("?!.,") not in stop_words
        }

        if not question_words:
            return []

        matches = []

        for course_name, terms in self.search_terms.items():

            searchable = " ".join(terms).lower()

            if all(word in searchable for word in question_words):
                matches.append(course_name)

        return matches