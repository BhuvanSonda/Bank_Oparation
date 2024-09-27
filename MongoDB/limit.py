import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017/")

db=client["time"]
collection=db["data"]
print("\nAll documents are : \n")
total=collection.find()
for i in total:
    print(i,'\n')
print("limited documents are  : \n")
limited=collection.find().limit(2)
for i in limited:
    print(i,"\n")
client.close()