from app.rag.course_catalog import CourseCatalog


catalog = CourseCatalog()

print("ALL COURSES")
print("=" * 80)

for course in catalog.get_all_courses():
    print("-", course)


print("\nPYTHON SEARCH")
print("=" * 80)

results = catalog.search(
    "What Python courses do you offer?"
)

for course in results:
    print("-", course)