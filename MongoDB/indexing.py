import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017/")

db=client['time']
collection=db['data']

# collection.create_index({"city":"text"})

find=(collection.find({
    "$text":{
        "$search":"Sirsi"
    }}
)
)

# for i in find:
#     print(i)


index=("indexs are :",collection.index_information())

for i in index:
    print(i,'\n')
client.close()

