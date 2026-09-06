# Automatic Embeddings

These examples show how ChromaDB creates embeddings automatically when documents are added without explicitly supplied vectors.

## Scripts

- `create_embeddings.py` creates the `vehicles_embeddings` collection in `./chromadb` and adds four documents.
- `view_embeddings.py` prints each document and the first ten values of its generated embedding.
- `compare_embedding.py` calculates cosine similarity between the car/bus and car/bike embeddings with NumPy.

## Run

```powershell
Set-Location embedding_automation
python create_embeddings.py
python view_embeddings.py
python compare_embedding.py
```

Run `create_embeddings.py` first. The `chromadb` subdirectory is a generated persistent store, not a Python package.
