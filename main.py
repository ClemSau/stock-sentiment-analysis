from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

@app.get('/')
async def index():
    return{'hello': 'world'} 

client = MongoClient()
db = client[]