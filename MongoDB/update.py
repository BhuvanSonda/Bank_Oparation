import pymongo
from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017/")

db=client['Data']
collection=db['Student_data']

update = {"$addToSet": {"Edu": {"$each": ["SSLC"],}}}

x=collection.update_one({'name':'Bhuvan'},update)

client.close()
print("Modified count is =",x.modified_count,"\ndid upserted id :",x.did_upsert)
print("Acknowledge is =",x.acknowledged,"\nupsertedd id : ",x.upserted_id)
