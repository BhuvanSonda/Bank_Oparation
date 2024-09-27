import pymongo

from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017/")

db=client["Data"]
collection=db["Student_data"]

value=(
    collection.aggregate(
        [
            {"$sort":{
                 "marks":1
                 }
            },
            {"$project":{
                    # "name":1,
                    # 'age':1,
                    # 'city':1,
                    "_id":0
                        }
            },
            
            {"$limit":5}
        ]
    )
)
print("-*-"*30)
for info in value:
    print(info)
print("-*-"*30)