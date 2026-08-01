from app.memory.memory import ConversationMemory
from app.models.response import ChatResponse
import logging

from app.rag.llm import (
    get_llm,
    switch_model,
    get_model_count,
)

from app.rag.prompt import get_prompt
from app.rag.question_rewriter import QuestionRewriter
from app.rag.course_resolver import CourseResolver
from app.rag.course_catalog import CourseCatalog
from app.rag.query_router import QueryRouter
from app.rag.ambiguity_detector import AmbiguityDetector
from app.rag.course_display_names import COURSE_DISPLAY_NAMES
from app.rag.document_display_names import DOCUMENT_DISPLAY_NAMES
from app.rag.retriever_service import RetrieverService


logger = logging.getLogger(__name__)

class RAGService:

    def __init__(self):

        self.memory = ConversationMemory()
        self.rewriter = QuestionRewriter()
        self.course_resolver = CourseResolver()
        self.course_catalog = CourseCatalog()
        self.query_router = QueryRouter()
        self.ambiguity_detector = AmbiguityDetector()

        self.retriever_service = RetrieverService()

        self.llm = get_llm()
        self.prompt = get_prompt()

    def build_context(self, docs):

        contexts = []

        for doc in docs:

            source = doc.metadata["source"]

            file_name = source.replace("data\\", "").replace(".docx", "")

            display_name = COURSE_DISPLAY_NAMES.get(
                file_name,
                DOCUMENT_DISPLAY_NAMES.get(
                    file_name,
                    file_name
                )
            )

            contexts.append(
                f"Course: {display_name}\n\n{doc.page_content}"
            )

        return "\n\n".join(contexts)

    def ask(self, session_id: str, question: str) -> ChatResponse:

        history = self.memory.get_history(session_id)

        # --------------------------------------------------
        # 1. CATALOG DISCOVERY PATH
        # --------------------------------------------------

        if self.query_router.is_catalog_query(question):

            courses = self.course_catalog.search(question)

            if not courses:
                courses = self.course_catalog.get_all_courses()

            answer = "Available courses:\n\n" + "\n".join(
                f"- {course}"
                for course in courses
            )

            self.memory.add_user_message(
                session_id,
                question
            )

            self.memory.add_ai_message(
                session_id,
                answer
            )

            show_lead_popup = self.memory.should_show_lead_popup(
                session_id
            )

            return ChatResponse(
                answer=answer,
                show_lead_popup=show_lead_popup
            )

        # --------------------------------------------------
        # 2. RESOLVE EXPLICIT COURSE
        # --------------------------------------------------

        resolved_course = self.course_resolver.resolve(question)

        # --------------------------------------------------
        # 3. AMBIGUITY CHECK
        # --------------------------------------------------

        if self.ambiguity_detector.is_ambiguous(
            question=question,
            has_history=bool(history),
            resolved_course=resolved_course,
        ):

            answer = "Which course are you referring to?"

            self.memory.add_user_message(
                session_id,
                question
            )

            self.memory.add_ai_message(
                session_id,
                answer
            )

            show_lead_popup = self.memory.should_show_lead_popup(
                session_id
            )

            return ChatResponse(
                answer=answer,
                show_lead_popup=show_lead_popup
            )
                    


        # --------------------------------------------------
        # 4. PARTIAL COURSE DISAMBIGUATION
        # --------------------------------------------------

        if not resolved_course and not history:

            partial_matches = self.course_resolver.find_partial_matches(
                question
            )

            if len(partial_matches) > 1:

                answer = (
                    "I found multiple matching courses. "
                    "Which one are you interested in?\n\n"
                    + "\n".join(
                        f"- {course}"
                        for course in partial_matches
                    )
                )

                self.memory.add_user_message(
                    session_id,
                    question
                )

                self.memory.add_ai_message(
                    session_id,
                    answer
                )

                show_lead_popup = self.memory.should_show_lead_popup(
                    session_id
                )

                return ChatResponse(
                    answer=answer,
                    show_lead_popup=show_lead_popup
                )

            elif len(partial_matches) == 1:

                resolved_course = partial_matches[0]

        # --------------------------------------------------
        # 5. QUESTION REWRITING
        # --------------------------------------------------

        is_course_selection = (
            resolved_course is not None
            and question.strip().lower()
            == resolved_course.strip().lower()
        )

        if history and (
            not resolved_course
            or is_course_selection
        ):
            try:
                standalone_question = self.rewriter.rewrite(
                    history,
                    question
                )

            except Exception  as e:
                logger.exception("Question rewriting failed: %s", e)

                # Fall back to the original question
                standalone_question = question

        else:
            standalone_question = question

        # --------------------------------------------------
        # 6. RESOLVE ALL COURSES
        # --------------------------------------------------

        print("Original Question:", question)
        print("Standalone Question:", standalone_question)

        course_names = self.course_resolver.resolve_all(
            standalone_question
        )

        if not course_names:
            course_names = self.course_resolver.find_partial_matches(
                standalone_question
            )

        if not course_names and resolved_course:
            course_names = [resolved_course]

        logger.info("Resolved Courses: %s", course_names)
        print("Resolved Courses:", course_names)

        # --------------------------------------------------
        # 7. RETRIEVAL
        # --------------------------------------------------

        route = self.query_router.route(
            standalone_question
        )

        logger.info("=" * 60)
        logger.info("Question: %s", standalone_question)
        logger.info("Resolved Courses: %s", course_names)
        logger.info("Route: %s", route)
        logger.info("=" * 60)

        print("Route:", route)


        docs = []

        # ----------------------------------------
        # Multi-course retrieval
        # ----------------------------------------

        if len(course_names) > 1:

            for course_name in course_names:

                docs.extend(
                    self.retriever_service.retrieve(
                        question=standalone_question,
                        course_name=course_name,
                        document_type=route,
                    )
                )

        # ----------------------------------------
        # Single-course / General retrieval
        # ----------------------------------------

        else:

            docs = self.retriever_service.retrieve(
                question=standalone_question,
                course_name=course_names[0] if course_names else None,
                document_type=route,
            )

        # --------------------------------------------------
        # 8. DEBUG RETRIEVED DOCUMENTS
        # --------------------------------------------------

        logger.info("Retrieved %d document(s)", len(docs))

        for i, doc in enumerate(docs, start=1):

            logger.info(
                "Document %d | Source: %s",
                i,
                doc.metadata["source"],
            )

        # --------------------------------------------------
        # 9. BUILD CONTEXT
        # --------------------------------------------------

        context = self.build_context(docs)

        logger.info(
            "Context prepared with %d document(s)",
            len(docs),
        )

        

        # --------------------------------------------------
        # 10. GENERATE ANSWER
        # --------------------------------------------------

        messages = self.prompt.invoke(
            {
                "context": context,
                "question": standalone_question,
            }
        )

        last_error = None

        # Try each available model at most once
        for attempt in range(get_model_count()):

            try:

                response = self.llm.invoke(messages)

                answer = response.content.strip()

                break

            except Exception as e:

                logger.exception("LLM Error: %s", e)

                last_error = e

                print(f"\nModel attempt {attempt + 1} failed.")

                # No more models left
                if attempt == get_model_count() - 1:

                    return ChatResponse(
                        answer=(
                            "I'm sorry, our AI service is temporarily unavailable. "
                            "Please try again later."
                        ),
                        show_lead_popup=False,
                    )

                print("Switching to next OpenRouter model...\n")

                switch_model()

                self.llm = get_llm()

        else:

            raise RuntimeError(
                "LLM generation failed after trying all models."
            ) from last_error

        
        # --------------------------------------------------
        # 11. HANDLE FALLBACK / LOG SOURCES
        # --------------------------------------------------

        fallback_answer = (
            "I couldn't find that information "
            "in the available course documents."
        )

        refusal_phrases = [
            "i couldn't find that information",
            "i cannot provide information",
            "not mentioned in the provided context",
            "not available in the course documents",
        ]

        answer_lower = answer.lower()

        if any(
            phrase in answer_lower
            for phrase in refusal_phrases
        ):
            answer = fallback_answer

        else:

            sources = sorted(
                {
                    doc.metadata["source"]
                    for doc in docs
                }
            )

            logger.info("Sources Used: %s", sources)

            print("Sources Used:", sources)
                

        # --------------------------------------------------
        # 12. SAVE CONVERSATION MEMORY
        # --------------------------------------------------

        self.memory.add_user_message(
            session_id,
            question
        )

        self.memory.add_ai_message(
            session_id,
            answer
        )


        history = self.memory.get_history(session_id)
        
        print("\n========== HISTORY ==========")
        for msg in history:
                    print(msg["role"], ":", msg["content"])
        print("=============================\n")



        
        # --------------------------------------------------
        # 13. RETURN RESPONSE
        # --------------------------------------------------

        show_lead_popup = self.memory.should_show_lead_popup(
            session_id
        )

        return ChatResponse(
            answer=answer,
            show_lead_popup=show_lead_popup
        )


        