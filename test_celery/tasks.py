from __future__ import absolute_import
from test_celery.celery import app
import time,requests
from pymongo import MongoClient

from test_celery.EventCoder import EventCoder
from test_celery.encode_with_petrarch import code_articles, code_articles_
from test_celery.sqlite_client import SqliteClient
from test_celery.Config import Config

config = Config()
uri = config.get_mongo_db_url()
client = MongoClient(uri)


db = client.Articles
post = db.Article

@app.task #(bind=True,default_retry_delay=10) # set a retry delay, 10 equal to 10s
def longtime_add(i):
    print 'long time task begins'
    try:
        r = requests.get(i)
        post.insert({'status':r.status_code,"creat_time":time.time()}) 
        print 'long time task finished'
    except Exception as exc:
        print 'error'
    return r.status_code



@app.task
def process_new(x, y):
    z = x + y

    sql = 'select * from json_test_table limit {}, {}'.format(z, y)
    sqlite_c = SqliteClient()
    data = sqlite_c.read_data(sql)
    #for d in data:
    #    process.delay(d)
    coder = EventCoder(petrGlobal={})

    result = list()
    for d in data:
        #result.append(code_articles_(d, coder.get_PETRGlobals()))

        db_value = {}

        db_value['petrarch'] = code_articles_(d, coder.get_PETRGlobals())
        try:
            post.insert(db_value)
            print 'long time task finished'
        except Exception as exc:
            print 'error'
  

    return result
                             
