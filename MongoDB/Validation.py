import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017/")
db= client["Management"]

validation_schema = {
            "$jsonSchema":{
                "bsonType":"object",
                "title":"School Management",
                "required":['Name','Age','DOB','Gender','Class','Father_Name','Mother_Name','Adress'],
                "properties":{
                    "Name":{"bsonType":"string",'description':"Name Should be in string and Required"},
                    "Age":{"bsonType":"int",'description':"Age Should be in Integer and Required"},
                    "Father_Name":{"bsonType":"string",'description':"Father Name Should be in string and Required"},
                    "Mother_Name":{"bsonType":"string",'description':"Mother Name Should be in string and Required"},
                    "DOB":{"bsonType":"date",'description':"Date of Birth Should be in Date and required"},
                    "Adress":{"bsonType":"string",'description':"Address Should be in string and Required"},
                    "Class":{"bsonType":"string",'description':"Class Should be in string and Required"},
                    "Gender":{"bsonType":"string",'description':"Gender Should be in string and Required"},
                            }
                        }
                    }
db.create_collection(
        'School',
        validator=validation_schema,
        validationAction="error"
    )
client.close()
print("Collection 'School' created successfully.")
