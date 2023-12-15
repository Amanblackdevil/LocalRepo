import requests
import pymongo
import json
import datetime

print("Welcome to pymongo")
client = pymongo.MongoClient("mongodb://localhost:27017/")
print(client)

base_url = 'https://randomuser.me/api'
data = requests.get(base_url).json()

db = client["ApiData"]
collection = db["data"]

# insert_deatails = collection.insert_one(data)
# details = {
#         "name" : "Aman",
#         "age" : 23,
#         "location" : "Raipur"
#     }

# details = [
#     {
#         "name" : "Ravi",
#         "age" : 50,
#         "location" : "Bilaspur"
#     },{
#         "name" : "Ajay",
#         "age" : 24,
#         "location" : "Devendranagar"
#     },{
#         "name" : "Rahul",
#         "age" : 23,
#         "location" : "Devendranagar"
#     },{
#         "name" : "asfsda",
#         "age" : 12,
#         "location" : "Devendranagar"
#     },{
#         "name" : "hljasdf",
#         "age" : 24,
#         "location" : "Devendranagar"
#     }
# ]
# collection.insert_one(details)
# collection.insert_many(details)
# writer_profile = [
#     {
#         "_id" : 1,
#         "user" : "Raj",
#         "title" : "Python",
#         "comment" : 5
#     },{
#         "_id" : 2,
#         "user" : "Asis",
#         "title" : "JavaScript",
#         "comment" : 10
#     },{
#         "_id" : 3,
#         "user" : "Satru",
#         "title" : "Java",
#         "comment" : 5
#     },{
#         "_id" : 4,
#         "user" : "Rajan",
#         "title" : "PHP",
#         "comment" : 15
#     },{
#         "_id" : 5,
#         "user" : "Monu",
#         "title" : "Web Development",
#         "comment" : 8
#     }
# ]

# collection.insert_many(writer_profile)
# agg_result = collection.aggregate(
#     [{
#         "$group" : {"_id" : "$user", "num_tutorial" : {"$sum" : 1}}
#     }]
# )

# for i in agg_result:
#     print(i)



dates = [
    {
        "_id" : 1,
        "name" : "Raj",
        "dob" : datetime.datetime(2000, 11, 23, 6, 0, 0)
    }

]

collection = db["Date"]
collection.insert_many(dates)

# alldates = collection.find(
#     {
#         "dob" : {
#             '$gte' : '2002-10-11T06:00:00.000+00:00',
#             '$lte' : '2010-12-15T06:00:00.000+00:00'
#         }
#     }
# )

# for item in alldates:
#     print(item)

# from_dt = datetime.datetime(2002, 10, 11, 6, 0, 0)
# to_dt = datetime.datetime(2002, 10, 11, 6, 0, 0)

# for post in collection.find({"dob" : {"$gte" : from_dt, "$lte" : to_dt}}):
#     print(post)


#Rough way to get the data from two connection (time consuming)

# allData = []
# data = collection.find({"name" : "Aman"})
# for item in data:
#     allData.append(item)


# collection = db['Date']
# data2 = collection.find({"name" : "Aman"})
# for item in data2:
#     allData.append(item)


# for i in allData:
#     print(i)

new_result = collection.aggregate([{
    '$lookup' : {
        "from" : "Date",
        "localField" : "_id",
        "foreignField" : "_id",
        "as" : "new collection"
    }
}])

for item in new_result:
    print(item.preety())