import chromadb
import numpy as np

client = chromadb.PersistentClient(path = "./chromadb")
collection = client.get_collection("vehicles_embeddings")

collection.update(
    ids = ["car1"]
,
documents= ["Car runs on electricity instead of petrol"])
print("The document is updated successfully !")

#Print the updated collection

update = collection.get(ids=["cars1"], include = ["documents","embeddings"])
print(f" Updated Text : {update['documents'][0]}") #type: ignore
print(f" Updated Embedding(First 10 values):{update['embeddings'][0][:10]}") #type: ignore 
