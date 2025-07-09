from pymongo import MongoClient

class Conectar:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client["project"]
        self.collection = self.db["users"]

    def get_collection(self):
        return self.collection