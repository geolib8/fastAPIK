from pymongo import MongoClient

client = MongoClient("mongodb+srv://a01376766:admin@cluster0.v86c5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.todo_db
collection_name = db["todo_collection"]