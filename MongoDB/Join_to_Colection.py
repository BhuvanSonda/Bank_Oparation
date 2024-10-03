from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client['Management']
collection = db['School']
rollNo=int(input("enter the roll number : "))
# Perform the aggregation
results = collection.aggregate([
    {"$match": {"Roll_No":rollNo}},  
    {"$lookup": {
        "from": "Marks_Entry",
        "localField": "Roll_No",
        "foreignField": "Roll_No",
        "as": "Marks_Entry"
    }},
    {"$project": {
        "Name": 1,        
        "Marks_Entry": 1,
        "Subjects":1,
        "_id":0
    }}
])

# Print the results
for result in results:
    print(result)


client.close()
