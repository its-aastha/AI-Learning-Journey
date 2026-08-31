import chromadb 

client = chromadb.PersistentClient('./chorma_db')

collection  = client.list_collections()

print("All collections available:")
for c in collection:
    print("-",c.name)