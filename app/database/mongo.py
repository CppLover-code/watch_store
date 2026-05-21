from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

mongo_db = client["watch_store"]

reviews_collection = mongo_db["reviews"]
