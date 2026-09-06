import chromadb

client = chromadb.PersistentClient() # type: ignore
collection  = client.get_or_create_collection(name = "Vehicle")
print("collection created :- ", collection.name)

collection.add (
    documents = [
               "Cars runs on petrol",
               "Bus carries passangers on road",
               "Bicycle runs without fule",
               "boat travels on water",
               "Plane flies in the sky"],
       
           ids = ["cars1","bus1","bike1","boat1","plane1"]
)
print("Added the Successfully !")

data = collection.get() 

#This is the code that is used to display the data 
for i, doc in zip(data["ids"], data["documents"]): #type: ignore
    print(f"{i} -> {doc}")