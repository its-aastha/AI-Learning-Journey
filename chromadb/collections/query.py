
import chromadb 
client = chromadb.Client()  # type: ignore

collection = client.create_collection(name = "Vehicles")
print("collection Created:-",collection.name)

#Add the data to the collection (adding the documents)
collection.add(
    #Documents == Your data 
    documents = [
           "Cars runs on petrol",
           "Bus carries passangers on road",
           "Bicycle runs without flue",
           "boat travels on water",
           "Plane flies in the sky"],
   
       ids = ["cars1","bus1","bike1","boat1","plane1"]
)

#Query the collection 
results = collection.query(
    #Query to run eg :
    #1. vehicles that on the roads
query_texts = ["i have to cath the fish , what should i use "],
n_results = 2
)
print(results)
