import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017/")

db=client['time']
#to get the collection list
collections=(db.list_collection_names())

#to get the speciic query
fnd={'likes':{"$eq":35}}
#to get the collection data
for data in collections:
    obj=db[data].find()
    for x in obj:
        print(x)
    print("-*-"*20)




for collection in collections:
    print("-*-"*30,"\n")
    print(f"Searching in collection: {collection}")
    finder = db[collection].find(fnd)  # Use the query to find documents
    print()
    for result in finder:
        print(result,"\n")  # Print each document found

        
    
    
#to close the client
client.close()