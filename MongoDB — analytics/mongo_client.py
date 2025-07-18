"""MongoDB connection sample for storing logs"""
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client['video_platform']
logs_collection = db['logs']
