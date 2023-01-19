# Javascript Codes

## Summary

* [Introduction](#introduction)
* [Getting an APIKEY and a merchant registration](#getting-an-apikey-and-a-merchant-registration)
* [Setting the URL](#setting-the-url)
* [Checking APIKEY](#checking-apikey)
* [Getting account data](#getting-account-data)
* [Customer section](#customer-section)
    * [Creating a new customer](#creating-a-new-customer)
    * [Getting customer data](#getting-customer-data)
* [Payments](#payments)
    * [Creating a new Payment - Cash In](#creating-a-new-payment---cash-in)
    * [Get Payment’s info](#get-payments-info)
    * [Creating a new Payment - Cash Out](#creating-a-new-payment---cash-out)
* [Webhooks](#webhooks)
    * [Webhook Example](#webhook-example)

# Introduction
The aim of this document is show how a developer can use the Nox gateway api in testnet. To use this system you must generate an API key and have an merchant registration. To access the main NoxPay API contact our team. This document is targeted towards Nox QA group.

# Getting an APIKEY and a merchant registration
To get an APIKEY and a merchant registration, you must get in contact with Nox, so we can provide them to you.

# Checking APIKEY
To check your APIKEY, you must run the checkAPIKEY() function in [index.js](index.js) file. If it runs properly, the return will be your data. This endpoint only works in the testnet.

```javascript
async function checkAPIKEY() {
    const response = await fetch('https://testnetapigateway.herokuapp.com/test-auth', {
        headers: {
            'api-key': signatureKey
        }
    });
    const data = await response.json();

    console.log(data);
}
```

Example of the output:
``` json
{"ID":1,"MerchantID":1,"Name":"NoxTrading","Hash":"-","CreatedAt":"2022-09-06T20:31:27Z"}
```

# Getting account data
To get your account’s data, you must run the getAccount function in the [index.js](index.js) file. If the function runs properly, the return will be the merchant’s name and balance. You must have your APIKEY to run this script.

```javascript
async function getAccount() {
    const response = await fetch('https://testnetapigateway.herokuapp.com/api/account', {
        headers: {
            'api-key': signatureKey
        }
    });
    const data = await response.json();

    console.log(data);
}
```

Example of the output:
``` json
{"name":"NoxTrading","balance":3152400.54}
```

# Customer section
## Creating a new customer

To create a new customer, you must run the createCustomer function in the[index.js](index.js) file. If the function runs properly, a new customer will be created. The function also returns the new customer’s data. To run this script, you must have your APIKEY.

```javascript
async function createCustomer() {
    console.log('Creating Customer Data')

    const options = {
        method: 'POST',
        headers: {
            'api-key': signatureKey,
            'content-type': 'application/json'
        },
        body: JSON.stringify(custdata)
    };
    const response = await fetch('https://testnetapigateway.herokuapp.com/api/customer', options
    );

    const data = await response.json();
    console.log(data);

}
```

Example of the output:
```json
{"name":"Usuario-f9940c6d-9830-4342-8954-4095b1ed8ade",
"email":"",
"code":"d4317b2d-1ce9-492d-b988-58f2de89beaa", "document":"f9940c6d-9830-4342-8954-4095b1ed8ade", "document_type":"CPF",
"pixkey":"",
"phone":"",
"birthday":"0001-01-01T00:00:00Z",
"metadata":"",
"createdat":"0001-01-01T00:00:00Z"}
```

## Getting customer data

To get the customer’s data, you should run the [getCostumer.py](getCustomer.py) file. If the .py runs properly, the return will be the customer’s data. To receive this data you must have the customer’s document and/or code, as well as your APIKEY.

``` python

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

```

Example of the output:
```json
Creating Customer
{"name":"Usuario-0cdca4d5-9eca-42b6-926d-272be2feb89d","email":"","code":"faecbcd3-3b66-4bcb-9e98-8cab0c6de756","document":"0cdca4d5-9eca-42b6-926d-272be2feb89d","document_type":"CPF","pixkey":"","phone":"","birthday":"0001-01-01T00:00:00Z","metadata":"","createdat":"0001-01-01T00:00:00Z"}

Get Customer
{"name":"Usuario-0cdca4d5-9eca-42b6-926d-272be2feb89d","email":"","code":"faecbcd3-3b66-4bcb-9e98-8cab0c6de756","document":"0cdca4d5-9eca-42b6-926d-272be2feb89d","document_type":"CPF","pixkey":"","phone":"","birthday":"0001-01-01T00:00:00Z","metadata":"","createdat":"2022-12-27T15:03:56.111208Z"}
```

# Payments
## Creating a new payment - CASH IN
To create a new payment, you must run the [cashIn.py](cashIn.py) file. If the .py runs properly, a new payment will be created. The .py also returns the payments’s data.

```python

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

print("Creating Customer")
response = requests.post(f'{URL}/api/customer',
                         headers=headers, json=data)

# print(response)
# print(response.headers)
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

```

Example of the output:
```json
Creating Customer
{"name":"Usuario-419b9c49-ce96-4c28-8aa5-fa328c68783d","email":"","code":"2d71e143-b1ba-40c0-a578-1fb9d54191e5","document":"419b9c49-ce96-4c28-8aa5-fa328c68783d","document_type":"CPF","pixkey":"","phone":"","birthday":"0001-01-01T00:00:00Z","metadata":"","createdat":"0001-01-01T00:00:00Z"}

Get Customer
{"name":"Usuario-419b9c49-ce96-4c28-8aa5-fa328c68783d","email":"","code":"2d71e143-b1ba-40c0-a578-1fb9d54191e5","document":"419b9c49-ce96-4c28-8aa5-fa328c68783d","document_type":"CPF","pixkey":"","phone":"","birthday":"0001-01-01T00:00:00Z","metadata":"","createdat":"2022-12-27T15:10:12.992656Z"}

Creating payment
{"method": "PIX", "code": "123333", "customer_doc": "419b9c49-ce96-4c28-8aa5-fa328c68783d", "items": [{"Description": "BTC", "Amount": 150000, "Quantity": 1.02, "Code": "cBTC", "Category": ""}, {"Description": "ADA", "Amount": 100, "Quantity": 10000.02, "Code": "cADA", "Category": ""}], "QRCode": https://noxbitcoin.com.br/logo-nox.svg, "txid": "62969bde144d4ed184b197bc8", "Status": "WAITING_PAYMENT"}
```

## Get Payment’s info
To get the payment’s data info you must use the ${URL}/api/payment/{txid}, where txid is returned from the payment creation.

To simulate a payment, you must use the URL/api/payment/pay/{txid}.
This feature only works in the testnet instance of the system.

```python 
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

```

Example of the expected output:
``` json
Creating customer
{"name":"Usuario-dd722fd9-5ed6-4fd0-9c10-ba14b3585b14",
 "email":"","code":"fc66a736-0bab-4028-81ed-111ddec007b7",
 "document":"dd722fd9-5ed6-4fd0-9c10-ba14b3585b14",
 "document_type":"UUID","phone":"",
 "birthday":"0001-01-01T00:00:00Z",
 "metadata":"","createdat":"0001-01-01T00:00:00Z"}

Get Customer
{"name":"Usuario-dd722fd9-5ed6-4fd0-9c10-ba14b3585b14",
 "email":"","code":"fc66a736-0bab-4028-81ed-111ddec007b7",
 "document":"dd722fd9-5ed6-4fd0-9c10-ba14b3585b14",
 "document_type":"UUID","phone":"",
 "birthday":"0001-01-01T00:00:00Z","metadata":"",
 "createdat":"2022-08-25T00:42:10.514883Z"}

Creating payment
Invoice Id: 789c7d41-1cab-4410-9699-79979e4ece91

Account balance:
{"name":"NoxTrading","balance":150100}

Invoice status:
{"Method":"PIX","Status":"WAITING_PAYMENT",
 "Code":"123333","TxID":"789c7d41-1cab-4410-9699-79979e4ece91",
 "Amount":150100}

Getting paid:
{"Method":"PIX","Status":"PAY",
 "Code":"123333","TxID":"789c7d41-1cab-4410-9699-79979e4ece91",
 "Amount":150100}

Invoice status:
{"Method":"PIX","Status":"PAY",
 "Code":"123333","TxID":"789c7d41-1cab-4410-9699-79979e4ece91",
 "Amount":150100}

Account balance:
{"name":"NoxTrading","balance":300200}
```
<!-- 
Example of the wrong output (problem with the payment):
```json
Creating Customer
{"name":"Usuario-5e13a651-8ea8-4177-ac77-8a3519130933","email":"","code":"9dd19d1d-63a9-429b-a9af-1ad05291ad0b","document":"5e13a651-8ea8-4177-ac77-8a3519130933","document_type":"CPF","pixkey":"","phone":"","birthday":"0001-01-01T00:00:00Z","metadata":"","createdat":"0001-01-01T00:00:00Z"}

Get Customer
{"name":"Usuario-5e13a651-8ea8-4177-ac77-8a3519130933","email":"","code":"9dd19d1d-63a9-429b-a9af-1ad05291ad0b","document":"5e13a651-8ea8-4177-ac77-8a3519130933","document_type":"CPF","pixkey":"","phone":"","birthday":"0001-01-01T00:00:00Z","metadata":"","createdat":"2022-12-27T15:19:53.76795Z"}

Creating Payment
Invoice Id: c254c1c0badc41829a4625e41

Account balance:
{"name":"NoxTrading","balance":3152400.54}

Invoice status:
{"Method":"PIX","Status":"WAITING_PAYMENT","Code":"123333","TxID":"c254c1c0badc41829a4625e41","Amount":150100}

Getting paid:
404 page not found


Invoice status:
{"Method":"PIX","Status":"WAITING_PAYMENT","Code":"123333","TxID":"c254c1c0badc41829a4625e41","Amount":150100}

Account balance:
{"name":"NoxTrading","balance":3152400.54}
``` -->

## Creating a new payment - CASH OUT
To create a new cash out payment, you must run the [cashOut.py](cashOut.py) code. If it runs properly, a new payment cash out will be created. The return is the payments’s data.

```python
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


```

Example of the output:
```json
========> Creating customer
{"name":"Usuario-ceb55928-0965-47a6-8a1c-258ead4a902c","email":"",
 "code":"2c84ea64-d692-4f71-9656-2f7eeab18f23","document":
 "ceb55928-0965-47a6-8a1c-258ead4a902c","document_type":"UUID",
 "phone":"","birthday":"0001-01-01T00:00:00Z","metadata":"",
 "createdat":"0001-01-01T00:00:00Z"}

Get Customer
{"name":"Usuario-ceb55928-0965-47a6-8a1c-258ead4a902c","email":"",
 "code":"2c84ea64-d692-4f71-9656-2f7eeab18f23",
 "document":"ceb55928-0965-47a6-8a1c-258ead4a902c","document_type":"UUID",
 "phone":"","birthday":"0001-01-01T00:00:00Z","metadata":"",
 "createdat":"2022-08-31T20:47:46.330245Z"}

========> Creating payment
Invoice Id: 36903be6-8711-4f90-8af1-8360539931ea

Account balance:
{"name":"NoxTrading","balance":0}

Invoice status:
{"Method":"PIX","Status":"WAITING_PAYMENT","Code":"123333",
 "TxID":"36903be6-8711-4f90-8af1-8360539931ea","Amount":300}

Getting paid:
{"Method":"PIX","Status":"PAY","Code":"123333",
 "TxID":"36903be6-8711-4f90-8af1-8360539931ea","Amount":300}

Invoice status:
{"Method":"PIX","Status":"PAY","Code":"123333",
 "TxID":"36903be6-8711-4f90-8af1-8360539931ea","Amount":300}

Account balance:
{"name":"NoxTrading","balance":300}

========> Creating payment out
Invoice Id: 2ed3f4d5-3365-47b6-bf24-83ee380a77c6

Account balance:
{"name":"NoxTrading","balance":300}

Invoice status:
{"Method":"PIXOUT","Status":"WAITING_PAYMENT","Code":"123",
 "TxID":"2ed3f4d5-3365-47b6-bf24-83ee380a77c6","Amount":250}

========> Paying
{"Method":"PIXOUT","Status":"PAY","Code":"123",
 "TxID":"2ed3f4d5-3365-47b6-bf24-83ee380a77c6","Amount":250}

Account balance:
{"name":"NoxTrading","balance":50}
```

# WebHooks
Your system can register two webhooks, one for the open PIX and one for the payment PIX.

- Each webhook must have a distinct URL.
- An open PIX does not have a pre-registered payment order in the NoxPay gateway. They are customarily used to allow the client to define the deposit value.
- The payment PIX has the payment order pre-registered in the NoxPay gateway.
- All webhooks requests are signed.

## How requests are signed
The NoxPay Gateway will provide you with a signature key. All requests must have 2 headers entries: 1) X-Signature, 2) noxpay-sign. These entries contain the same value, calculated using the sha256 hash of key signature concatenation with the message text.

See example below in Python:
```python
def simpleSign(plaintext, key):
    content = key + str(plaintext)
    encoded = content.encode()
    result = hashlib.sha256(encoded)
    return base64.b64encode(result.digest()).decode()
```

## The Requests Formats
The request will be something like this:

### Payment PIX example
```json
{"Method":"PIX",
 "Status":"PAY",
 "Code":"123333",
 "TxID":"789c7d41-1cab-4410-9699-79979e4ece91",
 "Amount":150100}
```

### Open PIX example
```json
{"end2end_id": "E31872495202212012125Yu7PIMArtyx", 
 "merchant": 27, 
 "value": 800.0, 
 "payer_document": "99999999999", 
 "payer_name": "John Doe", 
 "payer_account_type": "CONTA_CORRENTE", 
 "payer_account": "9999999", 
 "payer_account_digit": "9", 
 "payer_agency": "1", 
 "payer_bank_name": "Doe's Bank", 
 "payer_bank_code": "999", 
 "payer_bank_ispb": "99999999"}
 ```

## Webhook example
The Webhook folder is based on this code:
``` sh
    curl -X POST \
        -H 'X-Signature: fJ7Vy72eyUr5F4amcXHnFV5Cg5j+IF0hiM/h6ESAkjg=' \
        -H 'Content-Type: application/json' \
        --data "@webhook_example.json" \
        http://localhost:8080/webhook_endpoint
```

This code sends data via post request to the Nox API. The encrypted key is sent in the header, which will be compared with the NOX key. In the [webhook_example](webhook_example) we have two codes, one for the server and one for the client, as well as configuration files for environment variables and data, to simulate the complete operation.

<!-- Esse código envia dados via post request para a API da Nox. No cabeçalho é enviada a chave codificada, que será comparada com a chave da NOX. Na pasta [webhook_example](webhook_example) temos dois códigos, um do lado do servidor e outro do cliente, além de arquivos de configuração de variáveis de ambiente e dados, para simular a operação completa. -->

## Client Side
There are several ways to store your key securely. Here a JSON file is being used to store this information. A hash is created with the simpleSign function by combining the key with the data that will be sent.
Click to access the code: [webhook_client.py](webhook_example/webhook_client.py).

<!-- Existem várias formas de armazenar sua chave de forma segura. Aqui está sendo usado um arquivo json que guarda essa informação. Um hash é criado com a função simpleSign combinando a chave com os dados que serão enviados. 
Clique para acessar o código: [webhook_client.py](webhook_example/webhook_client.py). -->

```python
# IMPORTS
import requests
import json
import base64
import hashlib


# Creates the hash
def simpleSign(plaintext, key):
    content = key + str(plaintext)
    encoded = content.encode()
    result = hashlib.sha256(encoded)
    return base64.b64encode(result.digest()).decode()


# URL where data and hash will be sent
webhook_url = 'http://127.0.0.1:8080/webhook_endpoint'

# The first step is to load the signature_key as an environment variable.

# Opening JSON file that contains signature key
f = open('config.json')
# returns JSON object as a dictionary
data = json.load(f)
signature_key = data['SIGNATURE_KEY']


# Loading Data
with open('webhook_example.json') as f:
    data = f.read().replace('\n', '').replace('\r', '').encode()

# Creating Hash
signature = simpleSign(data.decode("utf-8"), signature_key)

# Headers
headers = {
    'X-Signature': signature,
    'Content-Type': 'application/json',
}

# Sending Webhook
response = requests.post(
    'http://localhost:8080/webhook_endpoint', headers=headers, data=data)

print(response)


```
Example of the output:
- Right request: <Response [200]>
- Wrong Request: <Response [403]>


## Server Side
Here, the address that will receive the webhook is made with Flask and the key was stored inside a .env file, which will be loaded with the load_dotenv method of the dotenv library. When the webhook is received, a hash is created with the data which is combined with the key stored on the server. This hash is compared with the one sent by the client.

Click to access the code: [webhook_server.py](webhook_example/webhook_server.py)

<!-- Aqui o endereço que receberá o webhook é feito com Flask e a chave foi armazenada dentro de um arquivo.env, que será carregado com o método load_dotenv da biblioteca dotenv. Quando o webhook é recebido, um hash é criado com os dados que são combinados com a chave armazenada no servidor. Esse hash é comparado com o enviado pelo cliente.

Clique para acessar o código: [webhook_server.py](webhook_example/webhook_server.py) -->

```python
import log
import base64
import hashlib
import os
from flask import Flask, json, request, Response
from waitress import serve
from dotenv import load_dotenv


api = Flask(__name__)
signature_key = ""


# Creates the hash
def simpleSign(plaintext, key):
    content = key + str(plaintext)
    encoded = content.encode()
    result = hashlib.sha256(encoded)
    return base64.b64encode(result.digest()).decode()


@api.route("/webhook_endpoint", methods=["POST"])
def webhook():
    print()
    log.info("Webhook received")
    """
    curl -X POST \
        -H 'X-Signature: fJ7Vy72eyUr5F4amcXHnFV5Cg5j+IF0hiM/h6ESAkjg=' \
        -H 'Content-Type: application/json' \
        --data "@webhook_example.json" \
        http://localhost:8080/webhook_endpoint
    """

    noxpay_sign = request.headers.get("X-Signature")
    signature = simpleSign(request.get_data().decode("utf-8"), signature_key)

    if signature != noxpay_sign:
        log.error("Invalid signature")
        return Response(
            json.dumps({"error": "Invalid signature"}),
            status=403,
            mimetype="application/json",
        )

    if request.is_json:
        log.info("Correct signature")

        data = request.get_json()

        print("end2end_id:", data["end2end_id"])
        print("merchant:", data["merchant"])
        print("value:", data["value"])
        print("payer_document:", data["payer_document"])
        print("payer_name:", data["payer_name"])
        print("payer_account_type:", data["payer_account_type"])
        print("payer_account:", data["payer_account"])
        print("payer_account_digit:", data["payer_account_digit"])
        print("payer_agency:", data["payer_agency"])
        print("payer_bank_name:", data["payer_bank_name"])
        print("payer_bank_code:", data["payer_bank_code"])
        print("payer_bank_ispb:", data["payer_bank_ispb"])

    return Response(
        json.dumps({"status": "ok"}),
        status=200,
        mimetype="application/json",
    )


if __name__ == "__main__":
    # Load environment variable
    load_dotenv()

    signature_key = os.environ['SIGNATURE_KEY']

    if signature_key is None:
        log.error("SIGNATURE_KEY is not set")
        exit(1)
    log.info("starting server on port 8080")
    serve(api, host="0.0.0.0", port=8080)

```

Example of the output in server side if key is correct:

```terminal
❯ python webhook_example/webhook_server.py
2022-12-27 19:11:47,697 - root - INFO --- starting server on port 8080
2022-12-27 19:11:47,702 - waitress - INFO --- Serving on http://0.0.0.0:8080

2022-12-27 19:14:34,089 - root - INFO --- Webhook received
2022-12-27 19:14:34,089 - root - INFO --- Correct signature
end2end_id: 0000000-1111-2222-3333-444444444444
merchant: 123
value: 0.01
payer_document: 11111111111
payer_name: Fulano de Tal
payer_account_type: CORRENTE
payer_account: 111111111
payer_account_digit: 1
payer_agency: 1111
payer_bank_name: Banco do Brasil
payer_bank_code: 001
payer_bank_ispb: 00000000

```

Example of the output in server side if key is incorrect:
```
2022-12-27 19:18:04,816 - root - INFO --- Webhook received
2022-12-27 19:18:04,816 - root - ERROR --- Invalid signature
```