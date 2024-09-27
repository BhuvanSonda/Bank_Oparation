import pymongo
from pymongo import MongoClient

db=MongoClient("mongodb://localhost:27017/")

print(db.list_database_names())
collection=db['time']
collection.drop_collection('FileNmae')
print(collection.list_collection_names())

