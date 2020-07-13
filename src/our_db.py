from pymongo import MongoClient
from src.config import DBURL

client = MongoClient(DBURL)
print(f"Connected")
db = client.get_database()