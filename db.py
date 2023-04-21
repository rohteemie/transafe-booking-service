from pymongo import MongoClient
from typing import List, Dict, Any


class Database:
    def __init__(self, host: str, port: int, database_name: str):
        self.host = host
        self.port: int = port
        self.database_name: str = database_name
        self.client: MongoClient = MongoClient(self.host, self.port, maxPoolSize=100)

    def connect(self) -> MongoClient:
        """
        Returns a MongoDB database object to perform database operations
        """
        return self.client[self.database_name]

    def insert_one(self, collection_name: str, data: dict) -> None:
        """
        Inserts a single document into the specified collection
        """
        collection = self.connect()[collection_name]
        collection.insert_one(data)

    def insert_many(self, collection_name: str, data: List[dict]) -> None:
        """
        Inserts multiple documents into the specified collection
        """
        collection = self.connect()[collection_name]
        collection.insert_many(data)

    def get_all(self, collection_name: str) -> List[Dict[str, Any]]:
        """
        Retrieves all documents from the specified collection
        """
        collection = self.connect()[collection_name]
        return list(collection.find())

    def get_one(self, collection_name: str, query: dict) -> Dict[str, Any]:
        """
        Retrieves a single document from the specified collection based on the query
        """
        collection = self.connect()[collection_name]
        return collection.find_one(query)

    def update_one(self, collection_name: str, query: dict, data: dict) -> None:
        """
        Updates a single document in the specified collection based on the query
        """
        collection = self.connect()[collection_name]
        collection.update_one(query, {'$set': data}, upsert=True)

    def update_many(self, collection_name: str, query: dict, data: dict) -> None:
        """
        Updates multiple documents in the specified collection based on the query
        """
        collection = self.connect()[collection_name]
        collection.update_many(query, {'$set': data})

    def delete_one(self, collection_name: str, query: dict) -> None:
        """
        Deletes a single document from the specified collection based on the query
        """
        collection = self.connect()[collection_name]
        collection.delete_one(query)

    def delete_many(self, collection_name: str, query: dict) -> None:
        """
        Deletes multiple documents from the specified collection based on the query
        """
        collection
