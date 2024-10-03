
from pymongo import MongoClient
from datetime import datetime

client=MongoClient("mongodb://localhost:27017/")

db=client['Management']
collection=db['College']

Branch=input("Enter the Branch [EC,CS,B.Sc] : ")

# results=collection.aggregate([
#     {"$match":{"branch":Branch}},
#     {"$project":{"_id":0}}
# ])

data=[{"Name": "shruthi",
    "Age": 20,
    "Class":' 10',
    "Adress": "Sirsi",
    "DOB":datetime.strptime("2003-10-09", "%Y-%m-%d"),
    "Gender":"Male",
    "Father_Name":"Divakar",
    "Mother_Name":"Nagartna",
    "Mobile_No":8073300795,
    "branch":"CS",
    "Roll_No": 1
},
{"Name": "Sankar",
    "Age": 20,
    "Class":' 10',
    "Adress": "Honnavar",
    "DOB":datetime.strptime("2004-10-17", "%Y-%m-%d"),
    "Gender":"Female",
    "Father_Name":"Narayan",
    "Mother_Name":"Laxmi",
    "Mobile_No":8073300795,
    "branch":"B.Sc",
    "Roll_No": 2
},
{"Name": "Ramesh",
    "Age": 21,
    "Class":' 10',
    "Adress": "Hubli",
    "DOB":datetime.strptime("2003-01-01", "%Y-%m-%d"),
    "Gender":"Male",
    "Father_Name":"Suman",
    "Mother_Name":"Gayatri",
    "Mobile_No":8564241524, 
    "branch":"B.Sc",
    "Roll_No": 3
}]

collection.insert_many(data)

results=collection.aggregate([
    {"$match":{"branch":Branch}}
    
])
Find=collection.find({},{"$match":Branch})
print(Find)

print("the data type of the Find is :",type(Find))
# result=collection.find()


# for result in results:
#     print("*"*30,result,"*"*30,"\n")

client.close()