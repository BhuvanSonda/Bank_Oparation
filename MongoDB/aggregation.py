from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017/")

db=client["Management"]
collection=db["College"]

value=(
    collection.aggregate(
        [
            # {"$sort":{
            #      "Age":1
            #      }
            # },
            # {"$match":{
                   
            #         "Roll_No":{"$lte":2}
            #             }
            # },          
            # {"$limit":10},
            # {"$match":{
            #     "branch":"EC"}
            #     },
                
            # {"$project":{"DOB":{'$dateToString':{'format':"%d / %m / %Y","date":"$DOB"}},"Name":1,"Roll_No":1,"_id":0}},
            # {"$sort":{"DOB":1}},
            {"$addFields":{"grade":"A+"}}
            
        ]
    )
)
print("^-*-"*30)
for info in value:
    print(info,"\n")
print("^-*-"*30)