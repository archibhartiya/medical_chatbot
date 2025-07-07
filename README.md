# 🤖 Medical RAG Chatbot with Local LLM (LLaMA3 + Ollama)

This is a lightweight **Medical Domain Chatbot** that uses **Retrieval-Augmented Generation (RAG)** with a **local open-source LLM** via [Ollama](https://ollama.com). It answers medical queries using scraped and indexed data, all running **offline** with a user-friendly **Streamlit UI**.

---

## 🚀 Features

- ✅ Medical question answering using RAG  
- ✅ LLaMA 3 model served locally with Ollama  
- ✅ FAISS-based semantic search on scraped articles  
- ✅ Streamlit frontend  
- ✅ Caching for fast reloads  
- ✅ Plug-and-play local deployment  
- ✅ Digital Twin static integration (mock)  

---

## 🧠 Architecture Overview

```
User ───▶ Streamlit UI
          │
          ▼
     RAG Chain (LangChain)
     ┌────────────┬────────────┐
     ▼                         ▼
Vector DB (FAISS)      Ollama LLaMA3
     ▼                         ▼
     └────▶ Final Answer + Sources
```

---

## 🗂️ Project Structure

```
medical_chatbot/
│
├── app/                  # Streamlit frontend
│   └── app.py
│
├── rag/                  # RAG setup and vector store
│   ├── rag_chat.py
│   └── vector_store.py
│
├── scraper/              # Scraping WHO/Medline articles
│   └── scrape_articles.py
│
├── faiss_medical/        # Saved FAISS vector DB
├── venv/                 # Python virtual environment
└── README.md
```

---

## 📦 Setup Instructions

### 1. Clone and set up environment

```bash
git clone https://github.com/yourusername/medical-chatbot-rag.git
cd medical-chatbot-rag
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run Ollama with LLaMA3 model

```bash
ollama run llama3
```

> ℹ️ Install Ollama from: https://ollama.com/download

### 3. Scrape and index knowledge base

```bash
python scraper/scrape_articles.py
python rag/vector_store.py
```

### 4. Launch Streamlit UI

```bash
streamlit run app/app.py
```

---

## 🧪 Technologies Used

| Component     | Tool                        |
|---------------|-----------------------------|
| LLM Backend   | LLaMA3 via Ollama           |
| Vector Store  | FAISS                       |
| Embeddings    | `sentence-transformers`     |
| UI            | Streamlit                   |
| RAG Logic     | LangChain                   |
| Scraping      | BeautifulSoup, requests     |

---

## 📘 Sample Query

> “What are the symptoms of dengue?”

→ Chatbot returns a natural language answer + references from your scraped articles.

---

## 💡 Future Enhancements

- 🔊 Voice input  
- 🧠 Smarter Digital Twin integration  
- 💾 Save user chat history in database  
- 🌐 Host on cloud/VPS  
