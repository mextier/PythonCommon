#http://api.mongodb.com/python/current/
import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.mdbtest1

if db.users.count_documents({})==0:
    db.users.insert_one({"name":"Dmitriy", "age":38})
    db.users.insert_one({"name":"Vasya", "age":49})
    db.users.insert_one({"name":"Lena", "age":30})

for item in db.users.find({"age":{"$lt":40}}):
    #print(list(item.keys()))
    print(item)


#db.users.remove({})
