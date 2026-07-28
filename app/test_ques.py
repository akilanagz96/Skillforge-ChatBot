from app.rag.question_rewriter import QuestionRewriter

rewriter = QuestionRewriter()

history = [

    {
        "role": "user",
        "content": "Tell me about the Python Full Stack Development course."
    },

    {
        "role": "assistant",
        "content": "It is a full stack course using Python and Django."
    }

]

question = "How long is it?"

new_question = rewriter.rewrite(
    history,
    question
)

print(new_question)