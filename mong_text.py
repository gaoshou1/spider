from pymongo import MongoClient

client = MongoClient(host="127.0.0.1", port=27017)
collection = client["text"]["t251"]


collection.insert({"name": "xiaowang", "age": 10})

