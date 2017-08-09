__author__ = 'root'

from pymongo import MongoClient
import ujson
import json


client = MongoClient('localhost:27017')
db = client.Articles


# Function to insert data into mongo db
def insert(d):
    try:

        db.Article.insert(d, check_keys=False)
    except Exception, e:
        print 'ERROR in MONGODB: ' + str(e)

