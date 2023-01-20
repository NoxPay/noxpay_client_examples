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

To create a new customer, you must run the createCustomer function in the [index.js](index.js) file. If the function runs properly, a new customer will be created. The function also returns the new customer’s data. To run this script, you must have your APIKEY.

```javascript
async function createCustomer() {
    console.log('Creating Customer')

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
Creating Customer Data
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

To get the customer’s data, you should run the getCustomer function in [index.js](index.js) file. If the function runs properly, the return will be the customer’s data. To receive this data you must have the customer’s document and/or code, as well as your APIKEY.

``` javascript

async function getCustomer() {


    console.log('Getting Customer')

    const response = await fetch(`https://testnetapigateway.herokuapp.com/api/customer/${custid}`, {
        method: 'GET',
        headers: {
            'api-key': signatureKey,
            'content-type': 'application/json'
        }
    });

    const data = await response.json();
    console.log(data)

}

```

Example of the output:
```json
Creating Customer
{"name":"Usuario-0cdca4d5-9eca-42b6-926d-272be2feb89d","email":"","code":"faecbcd3-3b66-4bcb-9e98-8cab0c6de756","document":"0cdca4d5-9eca-42b6-926d-272be2feb89d","document_type":"CPF","pixkey":"","phone":"","birthday":"0001-01-01T00:00:00Z","metadata":"","createdat":"0001-01-01T00:00:00Z"}

Getting Customer
{"name":"Usuario-0cdca4d5-9eca-42b6-926d-272be2feb89d","email":"","code":"faecbcd3-3b66-4bcb-9e98-8cab0c6de756","document":"0cdca4d5-9eca-42b6-926d-272be2feb89d","document_type":"CPF","pixkey":"","phone":"","birthday":"0001-01-01T00:00:00Z","metadata":"","createdat":"2022-12-27T15:03:56.111208Z"}
```
## Updating customer data

The only field that can be updated is the customer’s name. To update the customer’s pix key.

``` javascript

async function updateCustomer() {
    console.log('Updating Customer Name')

    const newdata = {
        "name": "Tyler"
    }

    const options = {
        method: 'PUT',
        headers: {
            'api-key': signatureKey,
            'content-type': 'application/json'
        },
        body: JSON.stringify(newdata)
    };
    const response = await fetch(`https://testnetapigateway.herokuapp.com/api/customer/${custid}`, options
    );

    // console.log(response)
    const data = await response.json();
    console.log(data);

}

```

# Payments
## Creating a new payment - CASH IN
To create a new payment, you must run the createPaymentIn function in [index.js](index.js) file. If the function runs properly, a new payment will be created. The function also returns the payments’s data.

```javascript

async function createPaymentIn() {
    const payment =
    {
        "method": "PIX",
        "code": "123333",
        "customer_doc": `${custid}`,
        "items": [
            {
                "description": "BTC",
                "amount": 150000.0,
                "quantity": 1.02,
                "code": "cBTC"
            },
            {
                "description": "ADA",
                "amount": 100.0,
                "quantity": 10000.02,
                "code": "cADA"
            }
        ]
    }

    console.log('Creating Payment')

    const response = await fetch('https://testnetapigateway.herokuapp.com/api/payment', {
        method: 'POST',
        headers: {
            'api-key': signatureKey,
            'content-type': 'application/json'
        },
        body: JSON.stringify(payment)
    });

    const data = await response.json();
    console.log(data);

    const txid = data.txid;
    console.log(`TXID: ${txid}`);

    return txid;
}

```

Example of the output:
```json

Creating payment
{"method": "PIX", "code": "123333", "customer_doc": "419b9c49-ce96-4c28-8aa5-fa328c68783d", "items": [{"Description": "BTC", "Amount": 150000, "Quantity": 1.02, "Code": "cBTC", "Category": ""}, {"Description": "ADA", "Amount": 100, "Quantity": 10000.02, "Code": "cADA", "Category": ""}], "QRCode": https://noxbitcoin.com.br/logo-nox.svg, "txid": "62969bde144d4ed184b197bc8", "Status": "WAITING_PAYMENT"}
```

## Get Payment’s info
To get the payment’s data info you must use the ${URL}/api/payment/{txid}, where txid is returned from the payment creation.

To simulate a payment, you must use the URL/api/payment/pay/{txid}.
This feature only works in the testnet instance of the system.

```javascript 
async function getPaymentInfo(txid) {
    console.log('Get Payment Info')
    console.log(`https://testnetapigateway.herokuapp.com/api/payment/${txid}`)

    const response = await fetch(`https://testnetapigateway.herokuapp.com/api/payment/${txid}`, {
        method: 'GET',
        headers: {
            'api-key': signatureKey,
            'content-type': 'application/json'
        },

    });

    const data = await response.json();
    console.log(data)

}
```

Example of the expected output:
``` json

TXID: fd85d8263c0d4dd2855452845
Get Payment Info
https://testnetapigateway.herokuapp.com/api/payment/fd85d8263c0d4dd2855452845

{"Method":"PIX","Status":"WAITING_PAYMENT",
 "Code":"123333","TxID":"789c7d41-1cab-4410-9699-79979e4ece91",
 "Amount":150100}

```
## Cash In

``` javascript
async function cashIn(txid) {
    try {
        const response = await fetch(`https://testnetapigateway.herokuapp.com/api/payment/pay/${txid}`, {
            method: 'POST',
            headers: {
                'api-key': signatureKey
            }
        });

        // const data = await response.json();
        console.log(response.json())
    } catch (err) {
        console.log(`SOMETHING WENT WRONG: ${err}`)
    }
}
```
Example of the expected output:
```json
{"Method":"PIX","Status":"PAY",
 "Code":"123333","TxID":"789c7d41-1cab-4410-9699-79979e4ece91",
 "Amount":150100}
```
## Creating pix out
To create a pix out, you need to create payment with method PIXOUT. You can use a existing customer or create a new one.

```javascript

async function createPaymentOut() {
    const paymentOut = {
        'method': 'PIXOUT',
        'code': '123',
        'customer_doc': `${custid}`,
        'items': [
            {
                'description': 'Reward',
                'amount': 250.0,
                'quantity': 1,
                'code': 'RWD1'
            }
        ]
    }

    const response = await fetch('https://testnetapigateway.herokuapp.com/api/payment', {
        method: 'POST',
        headers: {
            'api-key': signatureKey,
            'content-type': 'application/json'
        },
        body: JSON.stringify(paymentOut)
    });

    const data = await response.json();
    console.log(data);

    const txoutid = data.txid;
    console.log(`TXOUTID: ${txoutid}`);

    return txoutid;

}

```

Example of the output:
```json

{"Method":"PIXOUT","Status":"WAITING_PAYMENT","Code":"123",
 "TxID":"2ed3f4d5-3365-47b6-bf24-83ee380a77c6","Amount":250}

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
```javascript
function simpleSign(text, key) {
    const hash = createHmac('sha256', key)
        .update(text)
        .digest('hex');
    // console.log(hash);
    return hash;
}

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
The Webhook code is based on this example:
``` sh
    curl -X POST \
        -H 'X-Signature: fJ7Vy72eyUr5F4amcXHnFV5Cg5j+IF0hiM/h6ESAkjg=' \
        -H 'Content-Type: application/json' \
        --data "@webhook_example.json" \
        http://localhost:8080/webhook_endpoint
```

This code sends data via post request to the Nox API. The encrypted key is sent in the header, which will be compared with the NOX key. In this example we have two codes, one for the server and one for the client, as well as configuration files for environment variables and data, to simulate the complete operation.

<!-- Esse código envia dados via post request para a API da Nox. No cabeçalho é enviada a chave codificada, que será comparada com a chave da NOX. Na pasta [webhook_example](webhook_example) temos dois códigos, um do lado do servidor e outro do cliente, além de arquivos de configuração de variáveis de ambiente e dados, para simular a operação completa. -->

## Client Side
There are several ways to store your key securely. Here a JSON file is being used to store this information. A hash is created with the simpleSign function by combining the key with the data that will be sent.
Click to access the code: [webhook_client.js](webhook_client.js).

<!-- Existem várias formas de armazenar sua chave de forma segura. Aqui está sendo usado um arquivo json que guarda essa informação. Um hash é criado com a função simpleSign combinando a chave com os dados que serão enviados. 
Clique para acessar o código: [webhook_client.py](webhook_example/webhook_client.py). -->

```javascript
const { createHmac } = await import('node:crypto');
import * as dotenv from 'dotenv'
dotenv.config()

const signatureKey = process.env.API_KEY_CLIENT
// console.log(signatureKey)

function simpleSign(text, key) {
    const hash = createHmac('sha256', key)
        .update(text)
        .digest('hex');
    // console.log(hash);
    return hash;
}

import file from './webhook_example.json' assert { type: 'json' };
console.log(file);
// console.log(JSON.stringify(file))

const hash = simpleSign(JSON.stringify(file), signatureKey)
// console.log(hash)

async function send_data(file, signature) {
    const now = new Date();
    console.log('Sending data - ' + now);
    
    const url = 'http://localhost:8080/webhook_endpoint'
    const options = {
        method: 'POST',
        headers: {
            'X-Signature': signature,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(file)
    }
    const response = await fetch(url, options)
    const data = await response.json();
    console.log(data)
}

send_data(file, hash);
```

Example of the output:
``` terminal
Sending data - Fri Jan 20 2023 18:20:13 GMT-0300 (Horário Padrão de Brasília)
{ status: "success", name: "Fulano de Tal" }
```

```terminal
Sending data - Fri Jan 20 2023 18:22:27 GMT-0300 (Horário Padrão de Brasília)
{ status: "fail" }
```


## Server Side
Here, the address that will receive the webhook is made with Flask and the key was stored inside a .env file, which will be loaded with the load_dotenv method of the dotenv library. When the webhook is received, a hash is created with the data which is combined with the key stored on the server. This hash is compared with the one sent by the client.

Click to access the code: [webhook_server.js](webhook_server.js)

<!-- Aqui o endereço que receberá o webhook é feito com Flask e a chave foi armazenada dentro de um arquivo.env, que será carregado com o método load_dotenv da biblioteca dotenv. Quando o webhook é recebido, um hash é criado com os dados que são combinados com a chave armazenada no servidor. Esse hash é comparado com o enviado pelo cliente.

Clique para acessar o código: [webhook_server.py](webhook_example/webhook_server.py) -->

```javascript
import * as dotenv from 'dotenv'
dotenv.config()
// console.log(process.env);

import express from 'express';
const app = express();
app.listen(8080, () => console.log('listening at 8080'));
app.use(express.json({ limit: '1mb' }))

const { createHmac } = await import('node:crypto');

function simpleSign(text, key) {
    const hash = createHmac('sha256', key)
        .update(text)
        .digest('hex');
    // console.log(hash);
    return hash;
}

const server_signature = process.env.API_KEY_SERVER

app.post('/webhook_endpoint', (request, response) => {
    const now = new Date();
    // convert date to a string in UTC timezone format:
    // console.log(now.toUTCString());
    
    console.log('I got a request! - ' + now);
    const data = request.body

    const server_hash = simpleSign(JSON.stringify(data), server_signature)

    const client_hash = request.headers['x-signature']

    if (server_hash === client_hash) {
        console.log('API KEY CORRECT')
        console.log('Data received!')
        console.log(data);
        // console.log(request.headers['x-signature'])


        response.json({
            status: 'success',
            name: data.payer_name
        });
    } else {
        console.log('WRONG API KEY')
        response.json({
        status: 'fail'
        });
    }
});


```

Example of the output in server side if key is correct:

```terminal
listening at 8080
I got a request! - Fri Jan 20 2023 18:20:13 GMT-0300 (Horário Padrão de Brasília)
API KEY CORRECT
Data received!
{
  end2end_id: "0000000-1111-2222-3333-444444444444",
  merchant: 123,
  value: 0.01,
  payer_document: "11111111111",
  payer_name: "Fulano de Tal",
  payer_account_type: "CORRENTE",
  payer_account: "111111111",
  payer_account_digit: "1",
  payer_agency: "1111",
  payer_bank_name: "Banco do Brasil",
  payer_bank_code: "001",
  payer_bank_ispb: "00000000"
}

```

Example of the output in server side if key is incorrect:
```
I got a request! - Fri Jan 20 2023 18:22:27 GMT-0300 (Horário Padrão de Brasília)
WRONG API KEY
```