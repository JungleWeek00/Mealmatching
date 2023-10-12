from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient("mongodb+srv://daeun:daeun0101@cluster0.sdxyqrk.mongodb.net/?retryWrites=true&w=majority")

db = client.hobby

doc = {'name':'ㅎㅎ','age':21}
db.test.insert_one(doc)


try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)