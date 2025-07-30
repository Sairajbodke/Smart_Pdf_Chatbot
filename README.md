# 🤖 Smart PDF Chatbot (RAG + Together AI)

A Streamlit-based web app that allows users to upload a PDF and ask natural language questions. The chatbot understands context using sentence embeddings, FAISS for semantic search, and Together AI for generating intelligent answers.

---

## 📦 Features

- 📄 Upload any PDF file
- 💬 Ask natural questions from the PDF
- 🧠 RAG-based architecture using:
  - Sentence Transformers (`MiniLM`)
  - FAISS semantic search
  - Together AI (`Mixtral-8x7B-Instruct`) LLM
- 🔥 Fast and lightweight interface
- 🖼️ Custom homepage with chatbot logo and description
- 🗂️ Modular code structure for clarity

---

## 🚀 How to Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/your-username/pdf-chatbot.git
cd pdf-chatbot
