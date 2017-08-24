__author__ = 'root'

from Config import Config
from mongo_client import MongoClient

import sqlite3 as lite
from time import time

def insert_into_sqlite(sqlite_db_file, json_test_table, new_list):
    # Connecting to the database file
    conn = lite.connect(sqlite_db_file)
    c = conn.cursor()
    try:
        sql_table = """ CREATE TABLE IF NOT EXISTS json_test_table (
                                        id varchar,
                                        date varchar,
                                        output varchar,
                                        mongo_id varchar
                                    ); """
        c.execute(sql_table)

        query = """
            INSERT INTO
                {table}
            VALUES(?, ?, ?, ?)
        """.format(table=json_test_table)

        c.executemany(query, new_list)

    except Exception as e:
        print('ERROR: SQLite Error: ' + e.message)

    conn.commit()
    conn.close()


if __name__ == "__main__":

    try:
        ts = time()
        config = Config()
        uri = config.get_mongo_db_url()

        # print uri
        client = MongoClient(uri)
        db = client.json_db

        mongo_data = list(db.json_test_table.find())

        sqlite_db_file = config.get_mongo_sqlitedb_path()

        print 'exporting mongodb data to ' + sqlite_db_file

        json_test_table = 'json_test_table'

        new_list = list()

        for d in mongo_data:
            t = (d['id'],d['date'],d['output'],d['mongo_id'])
            new_list.append(t)


        # i = 1
        # for d in mongo_data:
        insert_into_sqlite(sqlite_db_file, json_test_table, new_list)
        #     print i
        #     i = i + 1

        print('Total record:{}'.format(len(new_list)))
        print('Took {}s'.format(time() - ts))

    except Exception as e:
        print('ERROR: MongoDB Error: ' + e.message)




