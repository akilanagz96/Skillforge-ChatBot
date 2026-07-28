from app.rag.vector_store import get_vector_store


class CourseCatalog:

    def __init__(self):
        vector_store = get_vector_store()

        data = vector_store.get(include=["metadatas"])

        self.course_names = sorted(
            {
                metadata["course_name"]
                for metadata in data["metadatas"]
                if (
                    metadata.get("document_type") == "course"
                    and metadata.get("course_name")
                )
            }
        )

    def get_all_courses(self) -> list[str]:
        return self.course_names

    def search(self, query: str) -> list[str]:

        query_lower = query.lower()

        # Remove common catalog-question phrases
        stop_phrases = [
            "what",
            "which",
            "do you have",
            "any",
            "courses",
            "course",
            "do you offer",
            "are available",
            "available",
            "show me",
            "list",
        ]

        search_term = query_lower

        for phrase in stop_phrases:
            search_term = search_term.replace(phrase, " ")

        # Clean extra spaces and punctuation
        search_term = " ".join(
            search_term.replace("?", "").split()
        )

        if not search_term:
            return self.get_all_courses()

        # First: exact phrase matching
        exact_matches = [
            course
            for course in self.course_names
            if search_term in course.lower()
        ]

        if exact_matches:
            return exact_matches

        # Fallback: match all meaningful search words
        search_words = search_term.split()

        return [
                course
                for course in self.course_names
                if all(
                    word in course.lower()
                    for word in search_words
                )
            ]