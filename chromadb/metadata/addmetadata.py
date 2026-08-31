import chromadb 

client = chromadb.PersistentClient(path = './chorma_db') #type: ignore

#resuse the existing thing 
collection = client.get_or_create_collection("vehicle")

#add data to the collection then how i add with meta data

collection.add(
documents=[
    "Bus carries passengers on road",
    "Plane flies across countries",
    "boat travels on water",
    "Bicycle runs without fuel"
    ],
ids = ["bus1","plane1","boat1","bike1"],
metadatas = [
    {"type":"public_transport", "fuel":"diesel"},
    {"type":"air_transport", "fuel":"jet"},
    {"type":"water_transport", "fuel":"diesel"},
    {"type":"personal_transport", "fuel":"manual"},

    ]
) # type: ignore

print("Data with metadta is Successfully !")