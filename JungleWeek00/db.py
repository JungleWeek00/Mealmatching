from pymongo.mongo_client import MongoClient
from flask import Flask
app = Flask(__name__)

#https://scribblinganything.tistory.com/178

uri = "mongodb+srv://daeun:daeun0101@cluster0.sdxyqrk.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)

db = client.team1week00


try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

locations = db.locations

data_to_insert = [
    {
        "number": "1",
        "location_name": "경술랭",
        "location": "제1복지관 지하1층",
        "count": "0"
    },
    {
        "number": "2",
        "location_name": "E-스퀘어",
        "location": "제2복지관 1층",
        "count": "0"
    },
    {
        "number": "3",
        "location_name": "감성코어",
        "location": "제3복지관 ",
        "count": "0"
    },
    {
        "number": "4",
        "location_name": "경기드림타워",
        "location": "경기드림타워 1층",
        "count": "0"
    },
    {
        "number": "5",
        "location_name": "오아시스",
        "location": "홍보관",
        "count": "0"
    }
]


for data in data_to_insert:
    locations.insert_one(data)

client.close()

