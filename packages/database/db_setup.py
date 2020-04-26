from pymongo import MongoClient

# DATABASE SETUP
client = MongoClient('mongodb://localhost:27017')
db = client.pymongo_test