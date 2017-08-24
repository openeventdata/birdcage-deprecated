__author__ = 'root'

from pymongo import MongoClient
from Config import Config

# Function to insert data into mongo db
def insert(d):
    try:
        config = Config()
        uri = config.get_mongo_db_url()
        # print uri
        client = MongoClient(uri)
        db = client.Articles
        db.Article.insert(d, check_keys=False)
    except Exception, e:
        print 'ERROR in MONGODB: ' + str(e)

