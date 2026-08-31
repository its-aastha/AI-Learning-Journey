import chromadb

client = chromadb.PersistentClient() # type: ignore
collection  = client.get_or_create_collection(name = "Vehicle")
print("collection created :- ", collection.name)

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
print("Added the Successfully !")

data = collection.get() 

#This is the code that is used to display the data 
for i, doc in zip(data["ids"], data["documents"]): #type: ignore
    print(f"{i} -> {doc}")