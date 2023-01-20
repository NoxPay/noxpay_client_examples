# Creating a new payment - CASH OUT

# To create a new cash out payment, you must run the code.
# If the it runs properly, a new payment cash out will be created.
# The return is the payments’s data.

import json
import requests
import uuid

# Opening JSON file
f = open('config.json')

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

print("========> Creating Customer")
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

# ============= CASH IN ============= #

print("\n========> Creating Payment")
payment = {
    'method': 'PIX',
    'code': '123333',
    'customer_doc': custid,
    'items': [
        {
            'description': 'BTC',
            'amount': 100.0,
            'quantity': 1.02,
            'code': 'cBTC'
        },
        {
            'description': 'ADA',
            'amount': 200.0,
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

# ============= CASH OUT ============= #

print('\n========> Creating payment out')

paymentout = {
    'method': 'PIXOUT',
    'code': '123',
    'customer_doc': '${custid}',
    'items': [
        {
            'description': 'Reward',
            'amount': 250.0,
            'quantity': 1,
            'code': 'RWD1'
        }
    ]
}

response = requests.post(f'{URL}/api/payment',
                         headers=headers, json=paymentout)

print(response.text)
print(f'Invoice Id: {response.json()["txid"]}')
txoutid = response.json()["txid"]
# txoutid = "2ed3f4d5-3365-47b6-bf24-83ee380a77c6"

# Check account balance
print('\nAccount balance:')
response = requests.get(f'{URL}/api/account', headers=headers)
print(response.text)

# Check the status of the invoice to be paid
print('\nInvoice status:')
response = requests.get(f'{URL}/api/payment/{txoutid}', headers=headers)
print(response.text)

# # Realiza o pagamento (está dando 404 page not found)
# Make the payment
print('\n========> Paying')
response = requests.post(f'{URL}/api/payment/pay/{txoutid}', headers=headers)
print(response.text)

# Check account balance
print('\nAccount balance:')
response = requests.get(f'{URL}/api/account', headers=headers)
print(response.text)
