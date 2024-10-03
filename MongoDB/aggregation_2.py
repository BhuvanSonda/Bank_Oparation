import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017/")

db=client['Data']
collection=db['Student_data']

collection.aggregate([
    {
        "$addFeilds":{
            "ertyui":["SSLC","PUCII"]
        }
    }
])
client.close()

print("Data Updated Successfully")