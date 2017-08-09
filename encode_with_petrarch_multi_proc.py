import logging
import os
from time import time
from functools import partial
from multiprocessing.pool import Pool

logger = logging.getLogger(__name__)

from EventCoder import EventCoder
from encode_with_petrarch import code_articles


def do_encoding_multi_proc(articleText, petrGlobals={}):
    print code_articles(articleText, petrGlobals)

if __name__ == "__main__":
    coder = EventCoder(petrGlobal={})

    articles = ['{ "type" : "story", "doc_id" : "nytasiapacific20160622.0002", "head_line" : "Lightning Ridge Journal: An Amateur Undertaking in Australian Mining Town With No Funeral Home", "date_line" : "Tue, 21 Jun 2016 03:52:15 GMT", "sentences" : [ { "sentence_id" : 1, "sentence" : "A Tunisian court has jailed a Nigerian student for two years for helping young militants join an armed Islamic group in Lebanon, his lawyer said Wednesday.", "parse_sentence" : "(ROOT (S (S (NP (DT A) (NNP Tunisian) (NN court)) (VP (VBZ has) (VP (VBN jailed) (NP (DT a) (NNP Nigerian) (NN student)) (PP (IN for) (NP (NP (CD two) (NNS years)) (PP (IN for) (S (VP (VBG helping) (S (NP (JJ young) (NNS militants)) (VP (VB join) (NP (DT an) (JJ armed) (JJ Islamic) (NN group)) (PP (IN in) (NP (NNP Lebanon))))))))))))) (, ,) (NP (PRP$ his) (NN lawyer)) (VP (VBD said) (NP (NNP Wednesday))) (. .)))" } ], "corref" : "" }',
                '{ "type" : "story", "doc_id" : "nytasiapacific20160622.0002", "head_line" : "Lightning Ridge Journal: An Amateur Undertaking in Australian Mining Town With No Funeral Home", "date_line" : "Tue, 21 Jun 2016 03:52:15 GMT", "sentences" : [ { "sentence_id" : 1, "sentence" : "A Tunisian court has jailed a Nigerian student for two years for helping young militants join an armed Islamic group in Lebanon, his lawyer said Wednesday.", "parse_sentence" : "(ROOT (S (S (NP (DT A) (NNP Tunisian) (NN court)) (VP (VBZ has) (VP (VBN jailed) (NP (DT a) (NNP Nigerian) (NN student)) (PP (IN for) (NP (NP (CD two) (NNS years)) (PP (IN for) (S (VP (VBG helping) (S (NP (JJ young) (NNS militants)) (VP (VB join) (NP (DT an) (JJ armed) (JJ Islamic) (NN group)) (PP (IN in) (NP (NNP Lebanon))))))))))))) (, ,) (NP (PRP$ his) (NN lawyer)) (VP (VBD said) (NP (NNP Wednesday))) (. .)))" } ], "corref" : "" }']

    num_of_processes = 8
    ts = time()

    total_articles = []
    for article in articles:
       for i in range(1, 10000):
         total_articles.append(article)

    encoding = partial(do_encoding_multi_proc, petrGlobals=coder.get_PETRGlobals())

    from contextlib import closing

    with closing(Pool(processes=num_of_processes)) as pool:
        pool.map(encoding, total_articles)

    print('Took {}s'.format(time() - ts))