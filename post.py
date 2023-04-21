import http.client
import json

connection = http.client.HTTPSConnection("www.httpbin.org")

headers = {'Content-type': 'application/json'}

foo = {'text': 'Hello HTTP #1 **cool**, and #1!'}
json_data = json.dumps(foo)

connection.request('POST', '/post', json_data, headers)

response = connection.getresponse()
print(response.read().decode())