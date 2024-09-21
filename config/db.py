from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

class MongoDBConfig:
    def __init__(self):
        self.mongo_url = os.getenv("MONGO_URL")
        self.database_name = os.getenv("DATABASE_NAME")
        self.collection_name = os.getenv("COLLECTION_NAME")
        self.prompt_collection = os.getenv("PROMPT_COLLECTION")
        self.client = MongoClient(self.mongo_url)
        self.db = self.client[self.database_name]
        self.collection = self.db[self.collection_name]
        self.prompt = self.db[self.prompt_collection]

    def get_collection(self):
        return self.collection
    def get_prompt(self):
        return self.prompt