
import chromadb 
client = chromadb.Client()  # type: ignore

collection = client.create_collection(name = "Vehicles")
print("collection Created:-",collection.name)

#Add the data to the collection (adding the documents)
collection.add(
    #Documents == Your data 
    documents = [
        "cars runs on the land",
        "Plane flies in the sky",
        "boat travels on the water",
        "bus is public transport on the road"
    ],
    ids = [
        "car1","plane1","boat1","bus1"
    ]
)

#Query the collection 
results = collection.query(
    #Query to run eg :
    #1. vehicles that on the roads
query_texts = ["i have to cath the fish , what should i use "],
n_results = 2
)
print(results)
