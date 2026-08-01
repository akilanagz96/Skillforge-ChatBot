from app.rag.supabase_store import supabase


class CourseCatalog:

    _course_names = None

    def __init__(self):

        if CourseCatalog._course_names is None:

            response = (
                supabase.table("documents")
                .select("course_name")
                .eq("document_type", "course")
                .execute()
            )

            CourseCatalog._course_names = sorted(
                {
                    row["course_name"]
                    for row in response.data
                    if row["course_name"]
                }
            )

        self.course_names = CourseCatalog._course_names

    def get_all_courses(self):
        return self.course_names

    def search(self, query: str):
        """
        Return matching course names.
        If no matches are found, return an empty list.
        """
        query = query.lower()

        return [
            course
            for course in self.course_names
            if query in course.lower()
            or course.lower() in query
        ]