import pymongo as pm

client=pm.MongoClient("mongodb://localhost:27017/")
db=client["Management"]

validate={"$jsonSchema":{
    "bsonType":"object",
    "title":"College Management",
    "required":["Name","Age","branch",'DOB','Gender','Father_Name','Mother_Name','Adress'],
    "properties":{
        "Name":{"bsonType":"string","description":"Name should be string and Required"},
        "Age":{"bsonType":"int","description":"Age should be integer and Required"},
        "branch":{"bsonType":"string","description":"branch should be string and Required"},
        "DOB":{"bsonType":"date","description":"Date of Birth should be date and Required"},
        "Gender":{"bsonType":"string","description":"Gender should be string and Required"},
        "Father_Name":{"bsonType":"string","description":"Father Name should be string and Required"},
        "Mother_Name":{"bsonType":"string","description":"Mother Name should be string and Required"},
        "Adress":{"bsonType":"string","description":"Address should be string and Required"}
                }                   
            }
        }

db.create_collection(
    "College",
    validator=validate,
    validationAction="error"
)

client.close()

print("College collection created successfully")
