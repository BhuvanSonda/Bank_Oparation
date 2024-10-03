import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017/")

db=client['Management']
collection=db["Marks_Entry"]

marks=[
       {"Marks":[60,38,75,92,64,83],"Roll_No":1},
       {"Marks":[85,64,35,72,61,42],"Roll_No":2},
       {"Marks":[90,85,95,80,70,60],"Roll_No":3}
       ]

x=collection.insert_many(marks)

client.close()
print("inseted id :",x.inserted_ids,"\nAcknowledge :",x.acknowledged)