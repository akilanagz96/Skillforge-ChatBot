from app.rag.course_catalog_data import COURSES
from app.rag.course_display_names import (
    COURSE_DISPLAY_NAMES,
    COURSE_ALIASES,
)


class CourseResolver:

    def __init__(self):

        self.course_names = sorted(
            COURSES,
            key=len,
            reverse=True,
        )

        self.search_terms = {}

        for course_name in self.course_names:

            terms = {course_name}

            display_name = COURSE_DISPLAY_NAMES.get(course_name)

            if display_name:
                terms.add(display_name)

                short_name = display_name.replace(
                    " Professional Program",
                    ""
                )
                terms.add(short_name)

            for alias in COURSE_ALIASES.get(course_name, []):
                terms.add(alias)

            self.search_terms[course_name] = sorted(
                terms,
                key=len,
                reverse=True,
            )

    def resolve(self, question: str):
        """
        Return the first matching course, or None.
        """
        question = question.lower()

        for course_name, terms in self.search_terms.items():
            for term in terms:
                if term.lower() in question:
                    return course_name

        return None

    def resolve_all(self, question: str):
        """
        Return all matching courses.
        """
        question = question.lower()

        matches = []

        for course_name, terms in self.search_terms.items():
            if any(term.lower() in question for term in terms):
                matches.append(course_name)

        return matches

    def find_partial_matches(self, question: str):
        """
        Return courses whose search terms partially match the query.
        """
        question = question.lower()

        matches = []

        for course_name, terms in self.search_terms.items():
            for term in terms:
                words = term.lower().split()

                if any(word in question for word in words):
                    matches.append(course_name)
                    break

        return matches