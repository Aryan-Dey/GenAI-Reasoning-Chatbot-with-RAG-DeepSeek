# ⚖️ AI Lawyer – RAG-Based Legal Reasoning Chatbot

This project is an **AI-powered legal chatbot** built using **Retrieval-Augmented Generation (RAG)** that can read, understand, and reason over complex legal or constitutional documents. Users can upload PDFs, and the chatbot retrieves relevant sections and provides **context-grounded, reasoning-based answers** using advanced LLMs.

---

## 📘 Project Objectives

* Build an intelligent **RAG pipeline** that connects document retrieval with reasoning-based LLMs.
* Enable **contextual Q&A** over uploaded legal PDFs such as Acts or Human Rights documents.
* Ensure **explainable and traceable responses** through document-aware reasoning.
* Provide an easy-to-use **Streamlit interface** for legal research and AI-driven analysis.

---

## 🧬 Key Components & Workflow

| Step                                 | Description                                                                                            |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| **1️⃣ PDF Upload & Text Extraction** | Users upload PDFs; text is extracted using `PDFPlumberLoader`.                                         |
| **2️⃣ Chunking & Embeddings**        | Text is divided into 1000-character overlapping chunks (200 overlap) for efficient context mapping.    |
| **3️⃣ Vector Database (FAISS)**      | All embeddings are stored in FAISS for high-speed semantic search.                                     |
| **4️⃣ Reasoning LLM Setup**          | Uses **DeepSeek-R1 (7B)** via Ollama or **Llama-3.3-70B-Versatile** via Groq Cloud for deep reasoning. |
| **5️⃣ Retrieval & Generation**       | Relevant chunks are retrieved and passed to the LLM for logical, factual answers.                      |
| **6️⃣ Streamlit Frontend**           | Interactive web interface allowing file uploads, questions, and real-time AI responses.                |

---

## 🧠 Tech Stack

| Category           | Tools / Libraries                                                                           |
| ------------------ | ------------------------------------------------------------------------------------------- |
| **Language**       | Python 3.12                                                                                 |
| **Frameworks**     | LangChain, Streamlit                                                                        |
| **Databases**      | FAISS Vector Store                                                                          |
| **Models (LLMs)**  | DeepSeek-R1 (Ollama), Llama-3.3 (Groq)                                                      |
| **Libraries Used** | `langchain`, `langchain_community`, `langchain_ollama`, `pdfplumber`, `dotenv`, `faiss-cpu` |

---

## ⚙️ Setup Instructions

### 📟 1. Create Virtual Environment

```bash
py -3.12 -m venv venv
venv\Scripts\activate
```

### 📆 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔑 3. Add Environment Variables

Create a `.env` file in the project root:

```bash
GROQ_API_KEY=your_groq_api_key_here
```

### ▶️ 4. Run the Application

```bash
streamlit run frontend.py
```

---

## 💡 Example Query

> **Question:** If a government restricts citizens from forming labor unions, which Articles of the Universal Declaration of Human Rights are violated and why?

**AI Lawyer Answer (Example):**
It identifies **Article 20** (freedom of peaceful assembly) and **Article 23** (right to form unions) as violated, explaining the reasoning based on retrieved document content.

---

## 🔍 Features

* 🧠 **Legal Reasoning via RAG + LLMs**
* ⚡ **FAISS Vector Search for Fast Retrieval**
* 📚 **Multi-Page PDF Parsing**
* 💬 **Natural Language Q&A**
* 🌐 **Streamlit-Based UI for Interactive Use**
* ** Support for **multiple PDF uploads**

---

## 🔮 Future Enhancements

* **Voice-enabled Q&A** via Whisper API
* Integration with **PostgreSQL for long-term vector storage**
* Option to switch between **multiple reasoning models dynamically**

---

