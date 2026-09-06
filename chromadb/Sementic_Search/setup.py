import chromadb

#So HERE IS THE DATABASE WHERE THE VALUES ARE STORED
DB_PATH = r"C:\AI\AI-Learning-Journey\chromadb\chroma_db"

client = chromadb.PersistentClient(path=DB_PATH)

# Create fresh collection
collection = client.get_or_create_collection(
    name="vehicles_semantic"
)

# Add data
collection.add(
    documents=[
        "Cars run on petrol.",
        "Bus carries passengers on road.",
        "Bicycle runs without fuel.",
        "Boat travels on water.",
        "Plane flies in the sky."
    ],
    ids=[
        "cars1",
        "bus1",
        "bike1",
        "boat1",
        "plane1"
    ]
)
print()
print("Sample data added!")

# Semantic search
results = collection.query(
    query_texts=[
        "vehicles that don't need fuel"
    ],
    n_results=2
)

print("Semantic Search:")

for doc, dist in zip(results["documents"][0], results["distances"][0]): #type: ignore
    print(f"{doc} (distance : {dist:.4f})")