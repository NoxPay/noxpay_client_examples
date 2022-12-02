# Creating a new customer
# To create a new customer, you must run the createCustomer.sh file.
# If the .sh runs properly, a new customer will be created.
# The .sh also # # returns the new customer’s data.
# To run this script, you must have your APIKEY.

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

response = requests.post(f'{URL}/api/customer',
                         headers=headers, json=data)


# print(response)
# print(response.headers)
print(response.text)
