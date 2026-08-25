import chromadb 

client = chromadb.PersistentClient(path = "./chorma_db")#type: ignore
collection = client.get_or_create_collection(name = "Vehicle") 

#delete one document
collection.delete(ids = ["car1"])
print("Data deleted successfully!")

data = collection.get()

print("\n Remaning data indide the 'vehicles'")
for i, doc in zip(data["ids"], data["documents"]):
    print(f"{i} -> {doc}")
