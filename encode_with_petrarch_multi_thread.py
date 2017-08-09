import logging
import os
from time import time

from Queue import Queue
from threading import Thread

logger = logging.getLogger(__name__)

from EventCoder import EventCoder
from encode_with_petrarch import code_articles
from mordecai import get_geo_location

class PETRARCHWorker(Thread):
   def __init__(self, queue, petrGlobals={}):
       Thread.__init__(self)
       self.queue = queue
       self.petrGlobal = petrGlobals

   def run(self):
       while True:
           # Get the work from the queue and expand the tuple
           article = self.queue.get()

           #encoding
           print code_articles(article, self.petrGlobal)
           self.queue.task_done()


if __name__ == "__main__":
    coder = EventCoder(petrGlobal={})

    articles = ['{ "type" : "story", "doc_id" : "nytasiapacific20160622.0002", "head_line" : "Lightning Ridge Journal: An Amateur Undertaking in Australian Mining Town With No Funeral Home", "date_line" : "Tue, 21 Jun 2016 03:52:15 GMT", "sentences" : [ { "sentence_id" : 1, "sentence" : "A Tunisian court has jailed a Nigerian student for two years for helping young militants join an armed Islamic group in Lebanon, his lawyer said Wednesday.", "parse_sentence" : "(ROOT (S (S (NP (DT A) (NNP Tunisian) (NN court)) (VP (VBZ has) (VP (VBN jailed) (NP (DT a) (NNP Nigerian) (NN student)) (PP (IN for) (NP (NP (CD two) (NNS years)) (PP (IN for) (S (VP (VBG helping) (S (NP (JJ young) (NNS militants)) (VP (VB join) (NP (DT an) (JJ armed) (JJ Islamic) (NN group)) (PP (IN in) (NP (NNP Lebanon))))))))))))) (, ,) (NP (PRP$ his) (NN lawyer)) (VP (VBD said) (NP (NNP Wednesday))) (. .)))" } ], "corref" : "" }',
                '{ "type" : "story", "doc_id" : "nytasiapacific20160622.0002", "head_line" : "Lightning Ridge Journal: An Amateur Undertaking in Australian Mining Town With No Funeral Home", "date_line" : "Tue, 21 Jun 2016 03:52:15 GMT", "sentences" : [ { "sentence_id" : 1, "sentence" : "A Tunisian court has jailed a Nigerian student for two years for helping young militants join an armed Islamic group in Lebanon, his lawyer said Wednesday.", "parse_sentence" : "(ROOT (S (S (NP (DT A) (NNP Tunisian) (NN court)) (VP (VBZ has) (VP (VBN jailed) (NP (DT a) (NNP Nigerian) (NN student)) (PP (IN for) (NP (NP (CD two) (NNS years)) (PP (IN for) (S (VP (VBG helping) (S (NP (JJ young) (NNS militants)) (VP (VB join) (NP (DT an) (JJ armed) (JJ Islamic) (NN group)) (PP (IN in) (NP (NNP Lebanon))))))))))))) (, ,) (NP (PRP$ his) (NN lawyer)) (VP (VBD said) (NP (NNP Wednesday))) (. .)))" } ], "corref" : "" }']

    num_of_thread = 20
    ts = time()

    # Create a queue to communicate with the worker threads
    queue = Queue()

    # Create worker threads
    for x in range(num_of_thread):
       worker = PETRARCHWorker(queue, coder.get_PETRGlobals())
       # Setting daemon to True will let the main thread exit even though the workers are blocking
       worker.daemon = True
       worker.start()

    # Put the tasks into the queue as a tuple
    for article in articles:
       logger.info('Queueing {}'.format(article))
       for i in range(1, 10000):
         queue.put(article)

    # Causes the main thread to wait for the queue to finish processing all the tasks
    queue.join()
    print('Took {}'.format(time() - ts))