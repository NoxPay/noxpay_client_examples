# Getting customer data

# To get the customer’s data, you must run the getCostumer.sh file.
# If the .sh runs properly, the return will be the customer’s data.
# To receive this data you must have the customer’s document and/or code,
# as well as your APIKEY.

import json
import requests
import uuid

# Opening JSON file
f = open('python_examples/config.json')

# returns JSON object as a dictionary
data = json.load(f)
URL = data['URL']

# Closing file
f.close()

# Generating Id
custid = str(uuid.uuid4())

# APIKEY here
headers = {
    'api-key': '12345678',
    'content-type': 'application/x-www-form-urlencoded',
}

# User data
data = {
    'name': 'Usuario-'+custid,
    'document': custid,
    'document_type': 'CPF'
}

print("Creating Customer")
response = requests.post(f'{URL}/api/customer',
                         headers=headers, json=data)

# print(response)
# print(response.headers)
print(response.text)

print("\n\nGet Customer")
headers = {
    'api-key': '12345678',
}
response = requests.get(f'{URL}/api/customer/{custid}', headers=headers)
print(response.text)
