__author__ = 'root'

import json

class Config:

    data = None
    def __init__(self):
        with open('config.json') as json_data_file:
            self.data = json.load(json_data_file)

    def get_mongo_db_url(self):
        host = ''
        username = ''
        password = ''
        db = ''
        admin_db = ''
        port = ''

        if self.data is None:
            raise Exception('Configuration file is missing')

        if 'mongodb' in self.data:
            host = self.data['mongodb']['host']
            username = self.data['mongodb']['user']
            password = self.data['mongodb']['password']
            admin_db = self.data['mongodb']['admin-db']
            port = self.data['mongodb']['port']
        if port == "":
            port = '27017'


        if username == "":
            return 'mongodb://{}:{}/{}'.format(host, port, admin_db)

        if password == "":
            return 'mongodb://{}@{}:{}/{}'.format(username, host, port, admin_db)

        return 'mongodb://{}:{}@{}:{}/{}'.format(username, password,host, port, admin_db)

    def get_rabbit_mq_celeru_url(self):
        host = ''
        username = ''
        password = ''
        db = ''
        admin_db = ''
        port = ''

        if self.data is None:
            raise Exception('Configuration file is missing')

        # broker='pyamqp://boomer:burritos_for_breakfast@localhost//
        if 'rabbit-mq' in self.data:
            host = self.data['rabbit-mq']['host']
            username = self.data['rabbit-mq']['user']
            password = self.data['rabbit-mq']['password']
            port = self.data['rabbit-mq']['port']


        if port != "":
            host = '{}:{}'.format(host, port)

        if password != "":
           username = '{}:{}'.format(username, password)

        return 'pyamqp://{}@{}//'.format(username, host,)

    def get_mordecai_url(self):
        url = ''

        if self.data is None:
            raise Exception('Configuration file is missing')

        # broker='pyamqp://boomer:burritos_for_breakfast@localhost//
        if 'mordecai' in self.data:
            url = self.data['mordecai']['url']


        return url

    def get_sqlite_path(self):
        db_path = ''

        if self.data is None:
            raise Exception('Configuration file is missing')

        # broker='pyamqp://boomer:burritos_for_breakfast@localhost//
        if 'sqlite' in self.data:
            db_path = self.data['sqlite']['db-path']


        return db_path


c = Config()
print c.get_sqlite_path()

