from pymongo import MongoClient
from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.host: str = getenv('TRNSF_HOST')
        self.port: int = int(getenv('TRNSF_PORT'))
        self.database_name: str = getenv('TRNSF_DB')
        self.client: MongoClient = MongoClient(self.host, self.port)

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

    def close(self) -> None:
        """
        Closes the MongoDB client connection
        """
        self.client.close()


# The code below this line is to Test the class above
data: dict = {
    'name': 'Rotimi Transafe',
    'seat': 4,
    'destination': 'Lagos'
}

db_table: str = 'user_bookings'

database: Database = Database()
database.insert_one(db_table, data)
database.close()
