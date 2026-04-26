# 🤖 RAG-Based Customer Support Assistant (LangGraph + HITL + Memory)

A production-style **Retrieval-Augmented Generation (RAG)** system that answers customer queries from a PDF knowledge base using **LangGraph workflows**, supports **Human-in-the-Loop (HITL) escalation**, and maintains **conversation memory** for context-aware responses.

---

## 🚀 Features

* 📄 PDF-based knowledge ingestion
* 🔍 Semantic search using embeddings (ChromaDB)
* 🧠 Context-aware answers using Groq LLM
* 🔀 Graph-based workflow (LangGraph)
* ⚠️ Human-in-the-Loop (HITL) escalation
* 🧾 Conversation memory (handles follow-ups like *“Yes”*)
* 💻 CLI-based interactive chatbot (stable for demo)
* ⚡ Supports HuggingFace embeddings (GitHub-friendly)

---

## 🧠 What is RAG?

Retrieval-Augmented Generation (RAG) combines:

* **Retrieval** → fetch relevant chunks from documents
* **Generation** → LLM generates grounded answers

This reduces hallucination and ensures answers come from real data.

---

## 🏗️ System Architecture

```id="arch1"
User Query
   ↓
Retriever (ChromaDB)
   ↓
Relevant Context
   ↓
LLM (Groq)
   ↓
Decision (Answer / Escalate)
   ↓
LangGraph Workflow
   ↓
Human-in-the-Loop (if needed)
```

---

## 📁 Project Structure

```id="struct1"
Customer_Support_Assistant/
│
├── app/
│   ├── document_ingestion.py   # PDF → chunks → vector DB
│   ├── retriever.py            # Embeddings + retrieval
│   ├── graph.py                # LangGraph workflow (RAG + HITL)
│
├── data/
│   └── samsung_care_policy.pdf # Knowledge base
│
├── main.py                     # CLI chatbot runner
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Installation

### 1. Clone repository

```bash id="cmd1"
git clone https://github.com/your-username/rag-customer-support.git
cd rag-customer-support
```

---

### 2. Create virtual environment

```bash id="cmd2"
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash id="cmd3"
pip install -r requirements.txt
```

---

### 4. Add environment variables

Create `.env` file:

```env id="env1"
GROQ_API_KEY=your_api_key_here
```

---

### 5. Load and Process the PDF (IMPORTANT)

Run this once to:

* Load the PDF
* Split it into chunks
* Generate embeddings
* Store them in ChromaDB

```bash
python -m app.document_ingestion
```

> ⚠️ Make sure your PDF file path is correct inside `app/document_ingestion.py` before running this command.

## 6. Running the Project

```bash id="cmd5"
python main.py
```

---

## 💬 Example Interaction

```id="ex1"
User: What is covered under Samsung Care+?
🤖 Answer: Covers accidental damage and extended warranty.

User: Does it cover theft?
🤖 Answer: No, theft is excluded.

User: Can I buy water bottle?
⚠️ Escalation triggered
👨 Human Agent: This is not related
🤖 Answer: Human Expert: This is not related

User: ok tell me about refund policy
⚠️ Escalation triggered
👨 Human Agent: Do you mean refund policy?
🤖 Answer: Human Expert: Do you mean refund policy?

User: Yes
🤖 Answer: (Uses memory and continues correctly)
```

---

## 🔀 Workflow (LangGraph)

### Nodes

* **Retrieve** → Fetch relevant chunks
* **Process** → Generate answer
* **Human** → Handle escalation

### Routing Logic

* If answer found → return
* If not → escalate

---

## ⚠️ Human-in-the-Loop (HITL)

Escalation triggers when:

* No relevant context found
* Query outside knowledge base
* LLM uncertainty

---

## 🧾 Memory System

* Stores conversation history
* Injected into LLM prompt
* Enables follow-up understanding

Example:

```id="mem1"
User: Do you mean refund policy?
User: Yes → System understands context
```

---

## ⚙️ Tech Stack

* **LangChain**
* **LangGraph**
* **ChromaDB**
* **Groq LLM (LLaMA 3)**
* **HuggingFace Embeddings**
* **PyPDFLoader (PDF loader)**

---

## 📊 Design Decisions

* Chunk size: 800 (balance context vs performance)
* Overlap: 200 (avoid information loss)
* Memory: lightweight in-state history

---

## ⚠️ Challenges Faced

* PDF extraction quality
* Retrieval accuracy tuning
* Handling ambiguous queries
* Managing HITL flow

---

## 🚀 Future Enhancements

* Streamlit / Web UI
* Multi-document support
* Persistent memory
* FastAPI deployment
* Feedback learning loop

---

## 🏆 Key Learnings

* RAG system design
* Graph-based orchestration
* Decision routing
* Memory integration
* Human-AI collaboration

---
