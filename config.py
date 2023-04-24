import os

DEBUG = True

#This is for testing purposes
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/bookingdb')
