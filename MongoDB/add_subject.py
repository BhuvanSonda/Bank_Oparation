import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")


db = client['Management']
collection = db["School"]


sub = [
    {"Subjects": ["Kannada", "English", "Hindi", "Social", "Science", "Maths"], "Roll_No": 1},
    {"Subjects": ["Kannada", "English", "Hindi", "Social", "Science", "Maths"], "Roll_No": 2},
    {"Subjects": ["Kannada", "English", "Hindi", "Social", "Science", "Maths"], "Roll_No": 3}
]


for entry in sub:
    result = collection.update_one(
        {"Roll_No": entry["Roll_No"]},  
        {"$set": {"Subjects": entry["Subjects"]}}, 
        upsert=True
    )


client.close()
