from pymongo import MongoClient
from random import randint

client = MongoClient('localhost:27017')

db = client.tse

fivestar = db.reviews.find_one({'rating': 5})

print(fivestar)