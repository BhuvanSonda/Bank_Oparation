# import datetime as dt

# def age_finder(year,month,day):
#     now=dt.date.today()
#     birth=dt.date(year=year,month=month,day=day)
#     print(f'you born on "{birth.strftime("%A")}"')
#     print(f"your current age is {(now.year-birth.year)-1} year - {now.month+(12-birth.month)} months \n")

# def alram(day=0,hrs=0,min=0,sec=0):
#     current=dt.datetime.now()
#     t=current.time()
#     set=dt.time(hour=hrs,minute=min,second=sec)
#     D_set=current+dt.timedelta(days=day)
#     print(f"your alram is set for {D_set.strftime('%A')}, {set} ")
#     print(f"remaining time is {D_set.day-current.day} days , {t.hour-set.hour}:{t.minute-set.minute}:{t.second-set.second} \n")



# age_finder(2005,10,17)
# alram(1,1,1,0)

import pymongo

# Connect to the MongoDB server
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Access the database and collection
db = client['Management']
collection = db['school']

# Define the update for the validator
update = {
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["Subjects", "Roll_No"],
            "properties": {
                "Roll_No": {
                    "bsonType": "int",
                    "description": "Roll number should be integer and it is required"
                },
                "Subjects": {
                    "bsonType": "array",
                    "items": {
                        "bsonType": "string",
                        "description": "Subjects should be string and it is required"
                    }
                }
            }
        }
    }
}

# Apply the validation to the collection
db.command("collMod", "school", validator=update["validator"], validationLevel="moderate")

# Close the client
client.close()

print("Validation keys updated successfully")

