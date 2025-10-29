import requests
import json
from urllib.parse import quote, unquote


def dictionary_to_string(dictionary):
    return json.dumps(dictionary)

def encode_string_into_url(string):
    return quote(string)

def print_response(response):
    print('-------- Response --------')
    print('Status code: {}'.format(response.status_code))
    print('-------- Content--------')
    print(response.text)
    print('------------------------')

# example data
dictionary = {}
dictionary['temperature'] = 20.0
dictionary['sensor_name'] = 'kitchen'

# ... your code ...
data = json.dumps(dictionary)

response = requests.post('http://10.22.114.76:8023//?data={}'.format(data))
print_response(response)