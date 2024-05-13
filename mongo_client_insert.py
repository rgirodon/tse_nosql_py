from pymongo import MongoClient
from random import randint

client = MongoClient('localhost:27017')

db = client.test

names = ['Kitchen','Animal','State', 'Tastey', 'Big','City','Fish', 'Pizza','Goat', 'Salty','Sandwich','Lazy','Fun']

company_type = ['LLC','Inc','Company','Corporation']

company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian', 'Mexican', 'American', 'Sushi Bar', 'Vegetarian']

for x in range(1, 501):

    business = {
        'name' : names[randint(0, (len(names)-1))] + ' ' + names[randint(0, (len(names)-1))]  + ' ' + company_type[randint(0, (len(company_type)-1))],
        'rating' : randint(1, 5),
        'cuisine' : company_cuisine[randint(0, (len(company_cuisine)-1))] 
    }

    result=db.reviews.insert_one(business)

    print('Created {0} of 500 as {1}'.format(x,result.inserted_id))

print('finished creating 500 business reviews')
