import json
import requests

# Opening JSON file
f = open('python_examples/config.json')

# returns JSON object as a dictionary
data = json.load(f)
URL = data['URL']

# Closing file
f.close()

headers = {
    'api-key': '12345678',
}

# Get info
response = requests.get(f'{URL}/test-auth', headers=headers)
# print(response)
# print(response.headers)
print(response.text)
