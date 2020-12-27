from fastapi import Request, Depends, FastAPI, HTTPException
from pymongo import MongoClient

app = FastAPI()

@app.get('/')
async def index():
    return{'hello': 'world'} 

client = MongoClient()
db = client['cluster0-shard-00-02.q52vq.mongodb.net:27017']