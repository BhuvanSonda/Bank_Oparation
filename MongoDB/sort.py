import pymongo as pm

client=pm.MongoClient("mongodb://localhost:27017/")
db=client['time']
collection=db['data']

doc=collection.find().sort("likes")
for x in doc:
    print(x)
    print("*"*30,"\n")