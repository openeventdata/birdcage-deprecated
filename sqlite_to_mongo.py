__author__ = 'root'


from sqlite_client import SqliteClient
from Config import Config
from mongo_client import MongoClient


if __name__ == "__main__":
    sqlite_c = SqliteClient()

    sqlite_data = sqlite_c.read_data('select * from json_test_table')

    try:
        config = Config()
        uri = config.get_mongo_db_url()
        # print uri
        client = MongoClient(uri)
        db = client.json_db

        for d in sqlite_data:
            db.json_test_table.insert(d, check_keys=False)

        print 'Successfully loaded data to MongoDB'

    except Exception, e:
        print 'ERROR in MONGODB: ' + str(e)

