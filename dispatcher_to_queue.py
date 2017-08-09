__author__ = 'root'

import logging
import os
from time import time

from Queue import Queue
from threading import Thread
from sqlite_client import SqliteClient


logger = logging.getLogger(__name__)


class DispatcherWorker(Thread):
   def __init__(self, queue):
       Thread.__init__(self)
       self.queue = queue

   def run(self):
       while True:
           # Get the work from the queue and expand the tuple
           start_index, number_of_record = self.queue.get()

           #encoding
           print('\nindex {}, number of record {}'.format(start_index, num_of_record))
           self.queue.task_done()


if __name__ == "__main__":

    num_of_thread = 3
    ts = time()

    sqlite_c = SqliteClient()

    total_record = int(sqlite_c.read_data('select count(*) as count from json_test_table')[0]['count'])

    num_of_record = total_record/num_of_thread

    # Create a queue to communicate with the worker threads
    queue = Queue()

    # Create worker threads
    for x in range(num_of_thread):
       worker = DispatcherWorker(queue)
       # Setting daemon to True will let the main thread exit even though the workers are blocking
       worker.daemon = True
       worker.start()

    # Put the tasks into the queue as a tuple

    index = 0
    for i in range(0, num_of_thread):
        queue.put((index, num_of_record))
        index = index + num_of_record

    # Causes the main thread to wait for the queue to finish processing all the tasks
    queue.join()
    print('Took {}'.format(time() - ts))