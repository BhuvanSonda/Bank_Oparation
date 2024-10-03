import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017/")

db=client['Management']

validate={
    "$jsonSchema":{
        "bsonType":"object",
        "title":"Marks Entry",
        "required":["Roll_No","Marks"],
        "properties":{
            "Roll_No":{"bsonType":"int","description":"Roll number should be an innteger and it is required"},
            "Subjects":{"bsonType":"array","items":{"bsonType":"int","description":"Subjects should integer amd it is required"}}
        }
    }
}

db.create_collection(
    "Marks_Entry",validator=validate,validationAction="error"#"warn"
)
client.close()

print("marks entry collection successfully created")