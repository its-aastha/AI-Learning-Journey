import chromadb

client = chromadb.PersistentClient(path = "./chroma_db") #type: ignore
collection = client.get_or_create_collection(name = "Vehicle")

#update the documents
#so here the python 3.14 + versions write the **upsert** not the update 
collection.upsert(
    ids=["bus1"],
    documents=["Bus carries more than 40 Passaengers and runs on roads"]
)
print("Updated record for bus1")


data = collection.get() 

#This is the code that is used to display the data 
for i, doc in zip(data["ids"], data["documents"]): #type: ignore
    print(f"{i} -> {doc}")

