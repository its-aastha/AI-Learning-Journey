#this file is only creating for the view the data only 
import chromadb 


client = chromadb.PersistentClient(path = "./chorma_db") #type: ignore 

#Fetching the vehicles form the chroma_db directory 
collection = client.get_collection("Vehicle")

data = collection.get()

#To display the data in the proper formate
for i,doc in zip(data["ids"],data["documents"]): #type: ignore
    print(f"{i} -> {doc}")