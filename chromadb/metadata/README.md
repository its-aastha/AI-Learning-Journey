# Metadata

Examples for adding and querying metadata alongside ChromaDB documents.

## Scripts

- `addmetadata.py` creates or reuses the `vehicle` collection and adds transport documents with `type` and `fuel` metadata.
- `viewMetadata.py` prints document IDs, text, and metadata.
- `filterdata.py` uses `where` filters for public transport, diesel vehicles, and personal transport.
- `list_collections.py` lists collections in the persistent client.

## Run

```powershell
Set-Location metadata
python addmetadata.py
python viewMetadata.py
python filterdata.py
python list_collections.py
```

These scripts use the relative `./chorma_db` store, so run them from this directory. The nested database folder contains generated SQLite and index files.
