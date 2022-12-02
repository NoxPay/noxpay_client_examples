# Get Payment Info

# To get the payment’s data info you must use the ${URL}/api/payment/{txid},
# where txid is returned from the payment creation.

# To simulate a payment, you must use the URL/api/payment/pay/{txid}.
# This feature only works in the testnet instance of the system.

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

print("\nGet Customer")
headers = {
    'api-key': '12345678',
}
response = requests.get(f'{URL}/api/customer/{custid}', headers=headers)
print(response.text)

print("\nCreating Payment")
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

# print(response.text)
print(f'Invoice Id: {response.json()["txid"]}')
txid = response.json()["txid"]

# Check account balance
print('\nAccount balance:')
response = requests.get(f'{URL}/api/account', headers=headers)
print(response.text)

# Checks the status of the invoice to be paid
print('\nInvoice status:')
response = requests.get(f'{URL}/api/payment/{txid}', headers=headers)
print(response.text)

# Make the payment
print('\nGetting paid:')
response = requests.post(f'{URL}/api/payment/pay/{txid}', headers=headers)
print(response.text)

# Check the status of the invoice to be paid
print('\nInvoice status:')
response = requests.get(f'{URL}/api/payment/{txid}', headers=headers)
print(response.text)

# Check account balance
print('\nAccount balance:')
response = requests.get(f'{URL}/api/account', headers=headers)
print(response.text)
