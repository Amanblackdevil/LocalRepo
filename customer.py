import requests
import pymongo


print("Welcome to pymongo")
client = pymongo.MongoClient("mongodb://localhost:27017/")
print(client)

base_url = 'https://randomuser.me/api'
data = requests.get(base_url).json()

db = client["Cust"]
collection = db["Cutomer"]

# collection = db["Order"]

# details2 = [
#     {
#         "c_id" : 1,
#         "food" : "Mara Peetha"
#     },{
#         "c_id" : 2,
#         "food" : "Fara"
#     },{
#         "c_id" : 3,
#         "food" : "Noodel"
#     },{
#         "c_id" : 4,
#         "food" : "Chocolate"
#     },{
#         "c_id" : 5,
#         "food" : "Maggi"
#     }
# ]


# collection.insert_many(details2)


data = collection.aggregate([{
    "$lookup" : {
        "from" : "Order",
        "localField" : "_id",
        "foreignField" : "c_id",
        "as" : "OrderDetails"
    }
}])

for item in data:
    print(item)