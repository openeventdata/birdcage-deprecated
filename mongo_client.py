__author__ = 'root'

from pymongo import MongoClient
from Config import Config

uri = Config.get_mongo_db_url()
client = MongoClient(uri)


db = client.Articles


# Function to insert data into mongo db
def insert(d):
    try:

        db.Article.insert(d, check_keys=False)
    except Exception, e:
        print 'ERROR in MONGODB: ' + str(e)

