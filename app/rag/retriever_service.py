from langchain_core.documents import Document

from app.rag.retriever import get_retriever


class RetrieverService:

    def retrieve(
        self,
        question: str,
        course_name: str | None = None,
        document_type: str | None = None,
    ) -> list[Document]:

        all_docs = []

        # --------------------------
        # Course Retrieval
        # --------------------------

        if course_name:

            retriever = get_retriever(course_name=course_name)

            course_docs = retriever.invoke(question)

            print(f"\nCourse Filter : {course_name}")
            print(f"Course Docs   : {len(course_docs)}")

            for doc in course_docs:
                print("   ", doc.metadata["source"])

            all_docs.extend(course_docs)

        # --------------------------
        # Policy Retrieval
        # --------------------------

        if document_type:

            retriever = get_retriever(document_type=document_type)

            policy_docs = retriever.invoke(question)

            print(f"\nPolicy Filter : {document_type}")
            print(f"Policy Docs   : {len(policy_docs)}")

            for doc in policy_docs:
                print("   ", doc.metadata["source"])

            all_docs.extend(policy_docs)

        docs = self.remove_duplicates(all_docs)

        print(f"\nFinal Docs : {len(docs)}")
        for doc in docs:
            print("   ", doc.metadata["source"])

        return docs

    def remove_duplicates(
        self,
        docs: list[Document],
    ) -> list[Document]:

        unique = {}

        for doc in docs:
            key = (
                doc.metadata.get("source"),
                doc.page_content,
            )
            unique[key] = doc

        return list(unique.values())
    