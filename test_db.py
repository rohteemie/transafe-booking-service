from db import Database
from os import getenv
from dotenv import load_dotenv


load_dotenv()

host = getenv('TRNSF_HOST')
port = int(getenv('TRNSF_PORT'))
db = getenv('TRNSF_DB')

# The code below this line is to Test the class above
data: dict = {
    'name': 'Rotimi Transafe',
    'seat': 4,
    'destination': 'Lagos'
}

db_table = 'user_bookings'

database: Database = Database(host, port, db)
query = database.get_all(db_table)

# # Update data in the collection
# query = {'name': 'Rotimi'}
# new_data = {'destination': 'Abuja'}
# database.update_one(db_table, query, new_data)

# # Delete data from the collection
# query = {'name': 'Rotimi'}
# database.delete_one(db_table, query)

print(query)
