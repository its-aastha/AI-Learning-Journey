# Collections

Examples for the basic ChromaDB collection lifecycle.

## Scripts

- `createCollection.py` creates a persistent `Vehicle` collection and adds vehicle documents.
- `viewCollection.py` prints the documents in the existing `Vehicle` collection.
- `see_exisiting.py` reads the existing collection from `./chorma_db`.
- `query.py` creates an in-memory `Vehicles` collection and runs a semantic query.
- `updateCollection.py` replaces the document with ID `bus1` using `upsert`.
- `deleteCollection.py` deletes the document with ID `car1` from `./chorma_db`.

## Run

Activate the environment from the project root, then run scripts here:

```powershell
Set-Location collections
python createCollection.py
python viewCollection.py
python query.py
```

The scripts use both in-memory clients and relative persistent paths. Run them from this directory and create the expected collection before using a reader, updater, or deleter. The `chroma` and `chorma_db` folders contain generated local database files.
