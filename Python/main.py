# import sys
from fastapi import FastAPI
from pymongo import MongoClient
app = FastAPI()



client = MongoClient("mongodb+srv://Joben:Anne060123@joben.a1aoz0g.mongodb.net/?retryWrites=true&w=majority")
db = client["Users"] 

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/data")
def read_root():
    return {"message": "Hello"}

@app.post("/data/1")
def read_root():
    return {"message": "part1"}

@app.post("/add_data/")
async def add_data(data: dict):
    collection = db.get_collection("Users")
    # result = collection.insert_one(data)
    return data

@app.post("/get_data/")
async def get_data():
    # Get the collection (assuming "Users" is your collection name)
    collection = db["Users"]

    # Query the collection and convert ObjectId to string
    data = list(collection.find({}))
    for item in data:
        item["_id"] = str(item["_id"])  # Convert ObjectId to string

    return data

# a = 10
# b = 11

# if (a > b):
#     print('log1')
# else :
#     print('log2')
# def greet(name):
#     return f"Hello, {name}!"

# if __name__ == "__main__":
    # name = sys.argv[1]
    # greeting = greet(name)
# print('Hello Worla')