#Newly added by Sayeed Salam sxs149331@utdallas.edu
import json
from StringIO import StringIO
from dateutil import parser
from petrarch2 import utilities
from datetime import datetime
from mordecai import get_geo_location
import sys



def read_json(jsonString):
    holding = {}
    sentence_limit = 7
    article = None
    try:
        article = json.load(StringIO(jsonString), encoding='utf-8')
    except:
        print("Error while PARSING \n"+jsonString)

    dateObject = None
    if len(article['date_line']) == 0:
        dateObject = datetime.now()
    else:    
        dateObject = parser.parse(article['date_line']) 

    
    try:
        entry_id = str(article['doc_id'])
        sent_dict = {}
        article_date = datetime.strftime(dateObject, '%Y%m%d')
        meta_content = {'date': article_date, 'headline': article['head_line']}
        counter = 0
    
        for sentence in article['sentences']:
            sent_id = str(sentence['sentence_id'])
            counter = counter + 1
            if counter == sentence_limit:
                break #read only the first 7 sentences of a article
            parsed_text = utilities._format_parsed_str(sentence['parse_sentence'])
            sent_dict[sent_id] = {'content': sentence['sentence'], 'parsed':
                                        parsed_text, 'geo-location': json.load(StringIO(get_geo_location(sentence['sentence'])), encoding='utf-8')}
        content_dict = {'sents': sent_dict, 'meta': meta_content}
        holding[entry_id] = content_dict
        return holding
    except:
        print('Invalid JSON Format')
        print(sys.exc_info()[0])
        
        return {}


def read_json_(article_main):
    holding = {}
    sentence_limit = 7
    article = None

    dateObject = None
    if ('date' not in article_main) or (len(article_main['date']) == 0):
        dateObject = datetime.now()
    else:
        dateObject = str(article_main['date'])[:-3]

    article = json.load(StringIO(article_main['output']), encoding='utf-8')

    try:
        entry_id = str(article['doc_id'])
        sent_dict = {}
        article_date = datetime.fromtimestamp(long(dateObject)).strftime('%Y%m%d')

        #datetime.strftime(dateObject, '%Y%m%d')
        meta_content = {'date': article_date}
        counter = 0

        for sentence in article['sentences']:
            counter = counter + 1
            sent_id = str(counter)

            if counter == sentence_limit:
                break #read only the first 7 sentences of a article
            parsed_text = utilities._format_parsed_str(sentence['parse_sentence'])
            sent_dict[sent_id] = {'content': sentence['sentence'], 'parsed':
                                        parsed_text, 'geo-location': json.load(StringIO(get_geo_location(sentence['sentence'])), encoding='utf-8')}
        content_dict = {'sents': sent_dict, 'meta': meta_content}
        holding[entry_id] = content_dict
        return holding
    except Exception as e:
        print(e.message)
        print(sys.exc_info()[0])

        return {}
