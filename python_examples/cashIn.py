# Creating a new payment - CASH IN

# To create a new payment, you must run the createPayment.sh file. If the .
# sh runs properly, a new payment will be created.
# The .sh also returns the payments’s data.

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

print(response)
print(response.headers)
print(response.text)

print("Get Customer")
headers = {
    'api-key': '12345678',
}
response = requests.get(f'{URL}/api/customer/{custid}', headers=headers)
print(response.text)

print("Creating payment")

payment = {
    'method': 'PIX',
    'code': '123333',
    'customer_doc': custid,
    'items': [
        {
            'description': 'BTC',
            'amount': 150000.0,
            'quantity': 1.02,
            'code': 'cBTC'
        },
        {
            'description': 'ADA',
            'amount': 100.0,
            'quantity': 10000.02,
            'code': 'cADA'
        }
    ]
}

response = requests.post(f'{URL}/api/payment', headers=headers, json=payment)
print(response.json())
