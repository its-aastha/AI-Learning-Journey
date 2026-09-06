import chromadb

client = chromadb.PersistentClient(path="./chromadb")

collection = client.get_or_create_collection(name = "vehicles_embeddings")

print("collection is ready", collection.name)

# Add some text documents
collection.add (
    documents = [
        "Car runs on road",
        "Plane flies in the sky",
        "boat travels on water",
        "bus is public transport on road"],
    ids = [
        "cars1","plane1","boat1","bus1"
    ]
)
print("Documents added with embedding automatically generated !")