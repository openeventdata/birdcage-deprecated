from celery import Celery
from EventCoder import EventCoder
from encode_with_petrarch import code_articles, code_articles_
from sqlite_client import SqliteClient
from mongo_client import insert
from Config import Config

config = Config()
celery_uri = config.get_rabbit_mq_celeru_url()

app = Celery('tasks', broker=celery_uri)


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
        insert(db_value)

    return result