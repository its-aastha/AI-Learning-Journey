# ChromaDB Learning Journey

Small, runnable examples for learning the main ChromaDB workflows in Python:

- creating and managing collections;
- storing documents and querying by semantic similarity;
- letting ChromaDB generate embeddings automatically;
- inspecting embeddings and comparing them with cosine similarity; and
- attaching and filtering documents by metadata.

## Project Layout

| Directory | Topic |
| --- | --- |
| [`collections`](collections/README.md) | Create, view, query, update, and delete collection data |
| [`embedding_automation`](embedding_automation/README.md) | Automatic embeddings and similarity comparison |
| [`metadata`](metadata/README.md) | Metadata creation, inspection, listing, and filtering |
| [`chroma`](chroma/README.md) | Persistent ChromaDB data created by an example run |
| [`chorma_db`](chorma_db/README.md) | Persistent ChromaDB data created by an example run |

The `chroma.sqlite3` files and UUID-named folders are generated database files. They are not source code and should be treated as local learning data.

## Setup

From this directory, create and activate a virtual environment, then install the dependencies:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install chromadb numpy
```

On macOS or Linux:

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install chromadb numpy
```

## Running Examples

Run a script from its own directory so its relative database path is predictable:

```powershell
Set-Location collections
python createCollection.py
python viewCollection.py
python query.py
```

The examples use local `PersistentClient` stores. Run creation scripts before view, update, delete, or filter scripts that expect an existing collection. Some scripts intentionally use different relative paths (`chroma`, `chroma_db`, or `chorma_db`); the directory READMEs call out those details.

## What ChromaDB Provides

ChromaDB stores documents, IDs, embeddings, and optional metadata. Its similarity queries compare vector meaning rather than exact keywords, making it useful for semantic search and retrieval-augmented generation (RAG). It complements rather than replaces a relational database when the application needs joins and strongly structured transactions.

## Notes

- `chorma_db` is the spelling currently used by several examples; it is kept to match the existing files.
- Re-running a script that calls `add` with the same IDs can produce duplicate-ID errors. Use new IDs or clear the learning store when experimenting.
- The examples are educational scripts rather than a packaged application, so their relative paths depend on the current working directory.
