
from datetime import datetime
from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017/")

db=client['Management']
collection=db['College']

data=[{
    "Name": "Bhuvan",
    "Age": 20,
    "Class":' 10',
    "Adress": "Sirsi",
    "DOB":datetime.strptime("09-10-2003", "%d-%m-%Y"),
    "Gender":"Male",
    "Father_Name":"Divakar",
    "Mother_Name":"Nagartna",
    "Mobile_No":8073300795,
    "branch":"EC",
    "Roll_No": 1
},
{"Name": "Santoshi",
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
{"Name": "Rakshit",
    "Age": 21,
    "Class":' 10',
    "Adress": "Hubli",
    "DOB":datetime.strptime("2003-01-01", "%Y-%m-%d"),
    "Gender":"Male",
    "Father_Name":"Suman",
    "Mother_Name":"Gayatri",
    "Mobile_No":8564241524, 
    "branch":"CS",
    "Roll_No": 3
}]

x=collection.insert_many(data)

client.close()
print("inseted id :",x.inserted_ids,"\nAcknowledge :",x.acknowledged)
