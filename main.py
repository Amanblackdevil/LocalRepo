import pymongo

if __name__ == "__main__":
    print("Welcome to pymongo")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client['Aman']
    collection = db['mySampleCollectionFromAman']
    # dictionary = {'name' : 'Aman Yadav', 'marks' : 45}
    # collection.insert_one(dictionary)
    # insert_these = [
    #     {
    #         '_id' : 1,
    #         'name' : 'Ravi Aman Yadav',
    #         'location' : 'Raipur',
    #     },{
    #         '_id' : 2,
    #         'name' : 'Rahul',
    #         'location' : 'Korba'
    #     },{
    #         '_id' : 3,
    #         'name' : 'Ajay',
    #         'location' : 'Bilaspur'
    #     }
    # ]
    # collection.insert_many(insert_these)

    #find 
    one = collection.find_one({'name' : 'Aman Yadav'})
    print(one)

    allDocument = collection.find({'_id' : 1})
    for item in allDocument:
        print(item)
    

#    # Show all the database
#     allDataBase = client.list_database_names()
#     print("ALl the data base present in Mongo DB")
#     print(allDataBase)

#     allCOllection = client['Aman']
#     print('All the collection we have in database Aman')
#     print(allCOllection.list_collection_names())

#     #Update database
#     print("Performing Updation")
#     prev = {"name" : "Ajay"}
#     nextt = {"$set" : {"location" : "Devendranagar"}}
#     collection.update_one(prev, nextt)

#     prev = {"name" : "Ravi Aman Yadav"}
#     nextt = {"$set" : {"location" : "Hyderabad"}}
#     collection.update_many(prev, nextt)


#    # delete
#     print("Performing deletion")
#     rec = {"name" : "Aman Yadav"}
#     collection.delete_one(rec)

#     #Update many
#     rec = {"name" : "Ajay"}
#     collection.delete_many(rec)

collection.create_index([("email", 1)],unique=True)

developer = {
    "name" : "Aman",
    "email" : "Dhiraj@nxgsolutions"
}

collection.insert_one(developer)

