import pymongo
from pymongo import MongoClient
import datetime
import pprint   #provide the capability to preety-print arbitary python data structure in the form
                #which can be used as input to the interpreter
from bson.objectid import ObjectId

client = MongoClient("mongodb://localhost:27017/")
print(client)

#getting a database
'''db = client.test_database
print(db)'''

db = client['test-database']
print(db)


#getting a collection
collection = db.test_collection
print(collection)


#Document
post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.now(tz=datetime.timezone.utc),
}

#Inserting a Document
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print("The Id of the inserted document is :", post_id)

#after inserting the first document 
print(db.list_collection_names())

#getting a single document with find_one()
pprint.pprint(posts.find_one())

#we can also find post by it's id
# print(post_id)
pprint.pprint(posts.find({"_id" : post_id}))

def get(post_id):
    #Convert from string to ObjectId
    document = client.db.collection.find_one({'_id' : ObjectId(post_id)})

#insert many or Bulk insertion
new_posts = [
    {
        "author" : "Ravi",
        "text" : "This is all about Actor",
        "tags" : ["SK", "SRK", "HRX"],
        "date" : datetime.datetime(2009, 11, 12, 11, 14)    
    },{
        "author" : "Developer",
        "text" : "This is all about developing",
        "tags" : ["Python", "Java", "HTML"],
        "date" : datetime.datetime(2009, 11, 10, 10, 45) 
    }
]
result = posts.insert_many(new_posts)
result.inserted_ids

#Querying more than one document
for post in posts.find():
    pprint.pprint(post)

#To get the limited result

for post in posts.find({"author": "Ravi"}):
    pprint.pprint(post)


#Counting
print(posts.count_documents({}))

#indexing
result = db.profiles.create_index([("user_id", pymongo.ASCENDING)], unique=True)
sorted(list(db.profiles.index_information()))
user_profiles = [{"user_id": 211, "name": "Luke"}, {"user_id": 212, "name": "Ziltoid"}]
result = db.profiles.insert_many(user_profiles)