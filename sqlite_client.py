__author__ = 'root'

import sqlite3 as lite
from Config import Config


class SqliteClient:
    def __init__(self):
        self.db_path = Config.get_sqlite_path()


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




