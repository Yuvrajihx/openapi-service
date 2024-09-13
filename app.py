import json
import openai
from fastapi import FastAPI
from openai import OpenAI
from worker.extract import TextExtractor
from pydantic import BaseModel
from worker.prompt import keys_extraction
from config.db import MongoDBConfig
from dotenv import load_dotenv
import os

print("ggggggggggggggggggggggggggggggggg")
print("cur dir:", os.getcwd())
load_dotenv()

API_KEY=os.getenv("API_KEY")
client = OpenAI(
    # This is the default and can be omitted
    api_key=API_KEY,
)

app = FastAPI()
# Initialize MongoDB configuration
db_config = MongoDBConfig()

class Item(BaseModel):
    data:str
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
    
    
@app.get("/home")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.post("/openapi/extract")
def read_item(request:Item):
    extracter=TextExtractor(request.data, client)
    extracted_data=extracter.extract_fields_with_open_ai(keys_extraction)
    try:
        data = json.loads(extracted_data)
        print("Manually Parsed JSON:", data)
        db_config.get_collection().insert_one(data)
        return {"isDataExtracted": True}
    except json.JSONDecodeError:
        print("Failed to decode JSON from the response content.")
        return {"isDataExtracted": False}