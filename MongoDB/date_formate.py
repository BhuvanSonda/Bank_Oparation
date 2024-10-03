
from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017/")

db=client["Management"]
collection=db["College"]

x=collection.aggregate([
   {"$match":{
                "branch":"EC"}
                },
                
            {"$project":{"DOB":{'$dateToString':{'format':"%d / %m / %Y","date":"$DOB"}},"Name":1,"_id":0}}
])
print(list(x))
client.close()