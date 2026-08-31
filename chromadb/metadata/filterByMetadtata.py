import chromadb 

client = chromadb.PersistentClient('./chorma_db')

collection  = client.get_collection("vehicle")


pub_transport = collection.get(where = {"type": "public_transport"})
print("Public Transport")
print(pub_transport)

print(" ")
diesel = collection.get(where = {"fuel": "diesel"})
print("diesel vehicles:")
print(diesel)