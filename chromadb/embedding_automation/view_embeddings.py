import chromadb 

client = chromadb.PersistentClient(path="./chromadb")

collection = client.get_collection(name = "vehicles_embeddings")

data = collection.get(include=["documents","embeddings"])

for doc_id,text,emed in zip(data["documents"],data["embeddings"],data["ids"]): #type: ignore
    print(f"\n {doc_id}:{text}")
    print(f"Embedding (First 10 values): {emed[:10]}") #show first few numbers only