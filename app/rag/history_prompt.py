from langchain_core.prompts import ChatPromptTemplate


def get_history_prompt():

    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
You rewrite user questions.

Use the conversation history to rewrite the latest question into a
complete standalone question.

Rules:

- Do NOT answer the question.
- Only rewrite it.
- If the question is already complete, return it unchanged.
                """
            ),

            (
                "human",
                """
Conversation History:

{history}

Current Question:

{question}

Standalone Question:
                """
            )
        ]
    )