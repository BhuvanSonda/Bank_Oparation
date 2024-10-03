import pymongo as pm

client=pm.MongoClient("mongodb://localhost:27017/")

db=client["Management"]
collection=db["College"]

# X=(collection.find())
# x = (collection.find_one(sort={"_id":-1}))

x = list(collection.find().sort({"_id":-1}))

# collection.find_one_and_delete({"Name":"Bhargav"},{"$set":{"Name":'Ramesh'}})
print(x[0])

# print(f"Name   : {x["Name"]}\nAge    : {x["Age"]}\nBranch : {x["branch"]}")
client.close()
