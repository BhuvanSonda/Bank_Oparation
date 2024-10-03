import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['Management']
collection_name = 'School'  # Use the name of the collection as a string

# Define the validation schema
update = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["Subjects", "Roll_No"],
        "properties": {
            "Roll_No": {
                "bsonType": "int",
                "description": "Roll number should be integer and it is required"
            },
            "Subjects": {
                "bsonType": "array",
                "items": {
                    "bsonType": "string",
                    "description": "Subjects should be strings and it is required"
                },
                "description": "Must be an array of strings"
            }
        }
    }
}

# Apply the validation schema to the collection

db.command("collMod", collection_name, validator=update)

client.close()
print("Validation keys updated successfully.")