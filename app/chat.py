from app.rag.service import RAGService

chatbot = RAGService()

SESSION_ID = "demo-user"

print("=" * 60)
print("Education AI Chatbot")
print("Type 'exit' to quit.")
print("=" * 60)

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    result = chatbot.ask(
        SESSION_ID,
        question
    )

    print("\nBot:")
    print(result.answer)

    print("\nSources:")

    for source in result.sources:
        print("-", source)