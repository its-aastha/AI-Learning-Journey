import chromadb

#client = chromadb.Client() # type: ignore
client = chromadb.PersistentClient(path = "./chorma_db") # type: ignore

collection = client.create_collection("Vehicle")

collection.add(
    documents = ["Car runs on the road"],
    ids = ["cars1"]
)
print("data added and saved a permanenatly ")