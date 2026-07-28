# 🎓 SkillForge AI ChatBot

An intelligent Retrieval-Augmented Generation (RAG) chatbot built for an EdTech platform that answers student queries about courses, admissions, placements, scholarships, policies, refunds, certifications, and more.

Instead of relying solely on an LLM's knowledge, the chatbot retrieves information from a curated knowledge base and generates accurate, context-aware responses using Google's Gemini model.

---

## ✨ Features

- 🤖 AI-powered conversational chatbot
- 📚 Retrieval-Augmented Generation (RAG)
- 🎯 Metadata-aware document retrieval
- 🔍 Course-specific filtering
- 🧠 Conversation memory
- 🔄 Question rewriting for follow-up conversations
- 🎓 Intelligent course resolution
- ⚠️ Ambiguity detection
- 📄 Answers grounded in company documents
- ⚡ FastAPI REST API
- 🗂️ Chroma Vector Database
- ☁️ Ready for cloud deployment

---

## 🏗️ System Architecture

```
                 User
                   │
                   ▼
             FastAPI Backend
                   │
        ┌──────────┴──────────┐
        │                     │
Conversation Memory     Query Router
        │                     │
        └──────────┬──────────┘
                   ▼
         Question Rewriter
                   │
                   ▼
          Course Resolver
                   │
                   ▼
         Chroma Vector Store
                   │
      HuggingFace Embeddings
                   │
         Relevant Documents
                   │
                   ▼
           Gemini 2.0 Flash Lite
                   │
                   ▼
               Final Answer
```

---

## ⚙️ Tech Stack

### Backend

- Python
- FastAPI
- LangChain

### LLM

- Google Gemini 2.0 Flash Lite

### Embeddings

- BAAI/bge-small-en-v1.5

### Vector Database

- ChromaDB

### Document Processing

- RecursiveCharacterTextSplitter

### Data Storage

- DOCX
- PDF

---

## 📂 Project Structure

```text
app/
├── api/
├── rag/
├── memory/
├── models/
├── config.py
├── build_vector_db.py

data/
    Company policies
    Course documents
    FAQs
    Student handbook

vectorstore/

requirements.txt
README.md
```

---

## 🚀 Getting Started

### Clone

```bash
git clone https://github.com/akilanagz96/Skillforge-ChatBot.git
cd Skillforge-ChatBot
```

### Install

```bash
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file.

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

### Build Vector Database

```bash
python app/build_vector_db.py
```

### Run

```bash
python -m uvicorn app.api.main:app --reload
```

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## 🧠 RAG Pipeline

1. User submits a question.
2. Conversation history is analysed.
3. Follow-up questions are rewritten.
4. Course names are detected.
5. Metadata filters narrow the search.
6. Relevant document chunks are retrieved from ChromaDB.
7. Retrieved context is passed to Gemini.
8. Gemini generates a grounded response.

---

## 📚 Knowledge Base

The chatbot is trained on:

- Company policies
- Admissions policy
- Placement policy
- Refund policy
- Scholarship policy
- Privacy policy
- Terms & Conditions
- Student handbook
- FAQs
- 12 SkillForge course brochures

---

## 💬 Example Questions

- What is the fee for the Data Science course?
- Do you offer placement assistance?
- Can I get a scholarship?
- What is the refund policy?
- Which course is suitable for beginners?
- What certifications are provided?

---

## 📸 Screenshots

Coming soon

- Swagger UI
- Chat interface
- Retrieval logs
- API responses

---

## 🚀 Future Improvements

- Next.js frontend
- Authentication
- Admin dashboard
- WhatsApp integration
- Voice support
- Analytics dashboard
- Docker support
- Kubernetes deployment

---

## 👨‍💻 Author

**Akila Nagarajan**

GitHub:
https://github.com/akilanagz96

LinkedIn:
https://www.linkedin.com/in/akila-nagarajan-485104244/
