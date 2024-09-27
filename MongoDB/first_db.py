from pymongo import MongoClient as mc
import pymongo

#oconnect with mongo server
client=mc("mongodb://localhost:27017/")
#To create data base
db=client["Data"]
#To create Collections
collection=db['Student_data']
data=[{
    'name':'Arun',
    'age':25,
    'marks':90,
    'city':'Yadgir'},
    {
    'name':'Suresh',
    'age':60,
    'marks':91,
    'city':'Hubli',
},{
    'name':'Tanush',
    'age':22,
    'marks':93,
    'city':'Hubli',
}
    ]
# Inserting data into the collection
x=collection.insert_many(data)

client.close()
