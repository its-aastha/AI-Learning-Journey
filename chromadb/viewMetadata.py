import chromadb 

client = chromadb.PersistentClient('./chorma_db')

collection = client.get_collection("vehicle")

data = collection.get(include=["documents","metadatas"])

print("All documents with metadta:")
for i, doc, meta in zip(data["ids"], data["documents"], data["metadatas"]): #type: ignore
    print(f"{i} --> {doc} | Metadata: {meta}")