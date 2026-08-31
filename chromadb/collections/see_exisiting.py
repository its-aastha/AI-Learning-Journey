import chromadb 

client  = chromadb.PersistentClient(path = "./chorma_db") # type: ignore
collection  = client.get_collection("Vehicle")
print(collection.get())