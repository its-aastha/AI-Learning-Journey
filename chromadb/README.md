# ChromaDB Notes & Quickstart

**ChromaDB** is an open-source vector database designed for storing and searching vector embeddings. It is widely used in AI/ML workflows such as semantic search, Retrieval-Augmented Generation (RAG), and document-based question-answering systems.

> **Note:** ChromaDB is a Python library and vector store—it is not intended for standard structured relational data.

---

## 📌 What I Learned

ChromaDB enables you to:
- Store text documents alongside their dense vector embeddings.
- Perform semantic similarity searches rather than exact keyword matches.
- Retrieve contextual information for LLMs.
- Power the retrieval layer in RAG pipelines.

### ChromaDB vs. SQL

| Feature | ChromaDB | SQL Databases |
| :--- | :--- | :--- |
| **Primary Use** | Semantic / vector similarity search | Relational data storage & querying |
| **Search Mechanism**| Mathematical distance between vectors (meaning) | Exact conditions, joins, filtering (exact match) |
| **Data Type** | Unstructured text, embeddings, metadata | Structured tables (rows and columns) |

---

## ⚙️ Installation & Setup

### Step 1: Create a Project Directory
```bash
mkdir chromadb-project
cd chromadb-project
```

### Step 2: Set Up a Virtual Environment
```bash
# Create the virtual environment
python -m venv venv

# Activate on Windows:
venv\Scripts\activate

# Activate on macOS/Linux:
source venv/bin/activate
```

### Step 3:Install ChromaDB
```bash
# Check if already installed
pip show chromadb

# Install ChromaDB
pip install chromadb

# Verify installation
pip show chromadb
```
