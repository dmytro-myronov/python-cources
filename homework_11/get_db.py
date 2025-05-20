from pymongo import MongoClient

def get_db():
    # Підключення до MongoDB
    client = MongoClient('mongodb://localhost:27017')
    db = client['online_store']
    return (db,client)
