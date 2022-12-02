# Creating a new payment - CASH OUT

# To create a new cash out payment, you must run the code.
# If the it runs properly, a new payment cash out will be created.
# The return is the payments’s data.

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
# print(f'Id da fatura: {response.json()["txid"]}')
# txid = response.json()["txid"]

# # Verifica saldo na conta
# print('Saldo na conta:')
# response = requests.get(f'{URL}/api/account', headers=headers)
# print(response.text)

# # Verifica status da fatura a ser paga
# print('Status da fatura:')
# response = requests.get(f'{URL}/api/payment/{txid}', headers=headers)
# print(response.text)

# # Realiza o pagamento (está dando 404 page not found)
# print('Recebe pagamento:')
# response = requests.post(f'{URL}/api/payment/pay/{txid}', headers=headers)
# print(response.text)

# # Verifica status da fatura a ser paga (essa etapa é redundante quando
# # a fatura é paga pois o status deve aparecer automaticamente)

# print('Status da fatura:')
# response = requests.get(f'{URL}/api/payment/{txid}', headers=headers)
# print(response.text)

# # Verifica saldo na conta
# print('Saldo na conta:')
# response = requests.get(f'{URL}/api/account', headers=headers)
# print(response.text)
