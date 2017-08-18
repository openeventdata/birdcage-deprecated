__author__ = 'root'

import json
import requests
from Config import Config
def get_geo_location(articleText):
    data = dict()
    data['text'] = articleText
    data = json.dumps(data)
    url = Config().get_mordecai_url()

    headers = {'Content-Type': 'application/json'}

    try:
        return requests.post(url, data=data, headers=headers).text
    except Exception as e:
        print(e.message)

    return "[]"


print get_geo_location("I live in Bangladesh")