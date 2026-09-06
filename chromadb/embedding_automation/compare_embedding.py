import chromadb
import numpy as np


# Cosine Similarity Function
def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (
        np.linalg.norm(vec1) * np.linalg.norm(vec2)
    )

# Connect to ChromaDB
client = chromadb.PersistentClient(path="./chromadb")

# Get the existing collection
collection = client.get_collection("vehicles_embeddings")


# Get documents and embeddings
data = collection.get(
    include=["documents", "embeddings"]
)


# Store embeddings
emb_car = data["embeddings"][0] #type: ignore
emb_bus = data["embeddings"][1] #type: ignore
emb_bike = data["embeddings"][2] #type: ignore


#compare simillarity
sim_car_bus = cosine_similarity(emb_car,emb_bus)
sim_car_bike = cosine_similarity(emb_car,emb_bike)

print("Cosine Similarity")
print(f"Car vs Bus: {sim_car_bus:.4f}")
print(f"Car vs Bike: {sim_car_bike:.4f}")
