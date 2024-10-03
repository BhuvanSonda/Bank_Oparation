
import pymongo as pm

client = pm.MongoClient("mongodb://localhost:27017/")
db = client["Management"]
collection = db["College"]


find_update = list(collection.find({"branch": "CS"}).limit(10))
print("before updating the branch:", find_update)
# new_data = []
# for x_data in find_update:
#     x_data['branch'] = 'EC'
#     new_data.append(x_data)

# print("********************************************************************")

# print("UPDATE DATa:------------", new_data)

    # if x_data['branch'] == 'CS':
        # test_update = collection.update_many({"branch":"EC"})

result = collection.update_many(
        {"branch":"EC"}, 
         {"$set":{"test":True}  },upsert=True
    )
# Branch = []
# for doc in find_update:
#     Branch.append(doc["branch"])
    
# print(Branch)
# if Branch:  
#     result = collection.update_many(
#         {"branch": {"$in": Branch}}, 
#         {"$set": {"branch": "B.Ed"}}  
#     )
#     print(f'Modified {result.modified_count} documents with branch "B.Sc" to "Ec".')
# else:
#     print("No documents found with branch 'B.Sc'.")


client.close()
