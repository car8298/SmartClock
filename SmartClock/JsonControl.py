import json
import requests
from urllib.request import urlopen

'''
def get_json(url):
    with urlopen(url) as json_file:
        json_data = json.loads(json_file.read())
    return json_data
'''

def get_json(url):
    response = requests.get(url)
    return json.loads(response.content.decode('utf-8'))
