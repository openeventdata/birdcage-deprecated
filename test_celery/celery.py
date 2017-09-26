from __future__ import absolute_import
from celery import Celery
from test_celery.Config import Config

config = Config()
uri = config.get_rabbit_mq_celeru_url()

app = Celery('test_celery',broker=uri, backend='rpc://',include=['test_celery.tasks'])
