import chromadb

client = chromadb.PersistentClient(path="./chromadb")

collection = client.get_or_create_collection(name = "vehicles_embeddings")

print("collection is ready", collection.name)

# Add some text documents
collection.add (
    documents = [
        "Car runs on petrol",
        "Bus carries Passengers",
        "Bicycle runs without fuel",
        "Boat travels on water",
        "Plane flies in the sky"],
    ids = [
        "cars1","bus1","bike1","boat1","plane1"
    ]
)
print("Documents added with embedding automatically generated !")