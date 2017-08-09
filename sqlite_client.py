__author__ = 'root'

import sqlite3 as lite
import sys


class SqliteClient:
    def __init__(self):
        self.db_path = 'data/test_solaimani_new.db'


    def read_data(self, query):

        result = []
        try:
            con = lite.connect(self.db_path)
            cur = con.cursor()
            cur.execute(query)

            result = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]



        except lite.Error, e:

            print "Error %s:" % e.args[0]

        finally:

            if con:
                con.close()

        return result




sqlite_c = SqliteClient()
#print sqlite_c.read_data('select count(*) as count from json_test_table')[0]['count']
print sqlite_c.read_data('select * from json_test_table limit 2')

#i = 1230
#print sqlite_c.read_data('select mongo_id from json_test_table limit 1228, 10')
#print sqlite_c.read_data('select mongo_id from json_test_table limit 1228, 3')
#print sqlite_c.read_data('select mongo_id from json_test_table limit 1231, 3')
#print sqlite_c.read_data('select mongo_id from json_test_table limit 1234, 3')
