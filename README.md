<div align="center">

# 🎓 SkillForge AI ChatBot

### Intelligent RAG Chatbot for an EdTech Platform

An AI-powered chatbot that provides accurate, context-aware answers about courses, admissions, placements, scholarships, policies, certifications, and student support using **Retrieval-Augmented Generation (RAG)**.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116-green?logo=fastapi)
![LangChain](https://img.shields.io/badge/LangChain-RAG-success)
![Gemini](https://img.shields.io/badge/Google-Gemini%202.0%20Flash-orange)
![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-purple)
![License](https://img.shields.io/badge/License-MIT-blue)

</div>

---

# 📖 Overview

SkillForge AI ChatBot is a Retrieval-Augmented Generation (RAG) chatbot developed for an EdTech platform. Instead of relying solely on a Large Language Model (LLM), it retrieves information from an internal knowledge base and generates responses grounded in official SkillForge documents.

The chatbot is designed to answer questions related to:

- 📚 Courses
- 🎓 Admissions
- 💼 Placements
- 💰 Scholarships
- 💳 Payments & Refunds
- 📜 Company Policies
- 📞 Student Support
- ❓ Frequently Asked Questions

By combining semantic search with Google's Gemini model, the chatbot produces responses that are more accurate, relevant, and less prone to hallucination.

---

# ✨ Features

- 🤖 AI-powered conversational chatbot
- 📚 Retrieval-Augmented Generation (RAG)
- 🧠 Google Gemini 2.0 Flash Lite integration
- 🔍 Semantic document search using ChromaDB
- 🎯 Metadata-based retrieval filtering
- 📖 Course-aware document retrieval
- 💬 Multi-turn conversation memory
- 🔄 Automatic follow-up question rewriting
- ⚠️ Ambiguity detection for vague queries
- 🚀 FastAPI REST API
- 📄 Swagger API documentation
- ⚡ Optimised embedding and vector database loading
- ☁️ Cloud deployment ready

---

# 🏗️ System Architecture

```text
                        User
                          │
                          ▼
                 FastAPI REST API
                          │
                          ▼
                  Conversation Memory
                          │
                          ▼
                  Question Rewriter
                          │
                          ▼
                   Query Router
                          │
                          ▼
                 Course Resolver
                          │
                          ▼
              Metadata-based Retrieval
                          │
                          ▼
                Chroma Vector Database
                          │
            HuggingFace Embeddings
                          │
                          ▼
               Relevant Document Chunks
                          │
                          ▼
             Google Gemini 2.0 Flash Lite
                          │
                          ▼
                   Final Response
```

---

# 🧠 RAG Pipeline

```text
User Question
      │
      ▼
Conversation History
      │
      ▼
Question Rewriting
      │
      ▼
Course Detection
      │
      ▼
Metadata Filtering
      │
      ▼
Semantic Search
      │
      ▼
Relevant Chunks
      │
      ▼
Gemini LLM
      │
      ▼
Grounded Response
```

---

# ⚙️ Tech Stack

## Backend

- Python 3.11
- FastAPI
- Uvicorn

## AI Framework

- LangChain

## Large Language Model

- Google Gemini 2.0 Flash Lite

## Embedding Model

- BAAI/bge-small-en-v1.5

## Vector Database

- ChromaDB

## Document Processing

- RecursiveCharacterTextSplitter

## Data Sources

- DOCX
- PDF

---

# 📂 Project Structure

```text
SF_ChatBot
│
├── app
│   ├── api
│   ├── debug
│   ├── memory
│   ├── models
│   ├── rag
│   ├── build_vector_db.py
│   └── config.py
│
├── data
│   ├── Company Bible
│   ├── Student Handbook
│   ├── Policies
│   ├── FAQs
│   └── Course Documents
│
├── vectorstore
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 📚 Knowledge Base

The chatbot retrieves information from curated internal documents including:

- Company Bible
- Student Handbook
- Admissions Policy
- Placement Policy
- Refund Policy
- Scholarship Policy
- Privacy Policy
- Terms & Conditions
- Contact & Support
- Frequently Asked Questions

### Course Brochures

- Data Analytics
- Data Science
- Artificial Intelligence & Machine Learning
- Generative AI
- Python Programming
- SQL
- Power BI
- Excel for Business
- Cloud Computing
- UI/UX Design
- Digital Marketing
- Cybersecurity

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/akilanagz96/Skillforge-ChatBot.git

cd Skillforge-ChatBot
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file.

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

---

## Build Vector Database

```bash
python app/build_vector_db.py
```

---

## Run the Application

```bash
python -m uvicorn app.api.main:app --reload
```

---

## Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# 💬 Example Questions

- What courses do you offer?
- Tell me about the Data Science course.
- What is the duration of the AI & Machine Learning course?
- Do you provide placement assistance?
- What scholarships are available?
- What is your refund policy?
- Which course is suitable for beginners?
- How can I contact student support?

---

# 🔍 API Endpoint

## POST `/chat`

### Request

```json
{
    "question": "Tell me about the Data Science course",
    "session_id": "123"
}
```

### Response

```json
{
    "answer": "...",
    "show_lead_popup": false
}
```

---

# 📸 Screenshots

> Screenshots will be added after deployment.

Suggested screenshots:

- Home Page
- Chat Interface
- Swagger UI
- API Response
- Retrieval Logs

---

# 🚀 Future Enhancements

- Next.js Frontend
- User Authentication
- Admin Dashboard
- WhatsApp Integration
- Voice Assistant
- Analytics Dashboard
- Docker Support
- Kubernetes Deployment
- CI/CD Pipeline
- Multi-language Support

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

Feel free to fork the repository and submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

## Akila Nagarajan

**GitHub**

https://github.com/akilanagz96

**LinkedIn**

https://www.linkedin.com/in/akila-nagarajan-485104244/

---

<div align="center">

### ⭐ If you found this project interesting, please consider giving it a star!

</div>
