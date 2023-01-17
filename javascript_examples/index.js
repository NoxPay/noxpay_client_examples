const express = require('express')
const app = express();
app.listen(3000, () => console.log('listening at 3000'));

// const _importDynamic = new Function('modulePath', 'return import(modulePath)');

// export const fetch = async function (...args: any) {
//     const {default: fetch} = await _importDynamic('node-fetch');
//     return fetch(...args);
// }

// import fetch from 'node-fetch';
const fetch = require('node-fetch');

// Teste com API do Github

// async function getData() {
//     const response = await fetch('https://api.github.com/users/github');
//     const data = await response.json();

//     console.log(data);
// }

// getData();

// Checking APIKEY //
// async function noxPay() {
//     const response = await fetch('https://testnetapigateway.herokuapp.com/test-auth', {
//         headers: {
//             'api-key': '12345678'
//         }
//     });
//     const data = await response.json();

//     console.log(data);
// }

// noxPay();

// Getting account data //
async function checkAccount() {
    const response = await fetch('https://testnetapigateway.herokuapp.com/api/account', {
        headers: {
            'api-key': '12345678'
        }
    });
    const data = await response.json();

    console.log(data);
}

// checkAccount();

// Creating a new customer

// import { v4 as uuidv4 } from 'uuid';
// const uuid = require('uuid.v4')
// const uuid_gen = uuid();
// console.log(crypto.randomUUID());

custid = '0081f93d-2b30-4fe0-a80b-1145e1236c9d'
custdata = {
    "name": `Usuario-${custid}`,
    "document": `${custid}`,
    "document_type": "CPF"
}
// console.log(custdata)
// async function noxPay() {
//     const response = await fetch('https://testnetapigateway.herokuapp.com/api/customer', {
//         method: 'POST',
//         headers: {
//             'api-key': '12345678',
//             'content-type': 'application/json'
//         },
//         body: JSON.stringify(custdata)
//     });

//      const data = await response.json();
//      console.log(data)

// }

// noxPay()

// Getting customer data
// async function noxPay() {
//     const response = await fetch(`https://testnetapigateway.herokuapp.com/api/customer/${custid}`, {
//         method: 'GET',
//         headers: {
//             'api-key': '12345678',
//             'content-type': 'application/json'
//         }
//     });

//     const data = await response.json();
//     console.log(data)

// }

// noxPay()

// Creating new Payment
// payment =
// {
//     "method": "PIX",
//     "code": "123333",
//     "customer_doc": `${custid}`,
//     "items": [
//         {
//             "description": "BTC",
//             "amount": 150000.0,
//             "quantity": 1.02,
//             "code": "cBTC"
//         },
//         {
//             "description": "ADA",
//             "amount": 100.0,
//             "quantity": 10000.02,
//             "code": "cADA"
//         }
//     ]
// }

// async function noxPay() {
//     const response = await fetch('https://testnetapigateway.herokuapp.com/api/payment', {
//         method: 'POST',
//         headers: {
//             'api-key': '12345678',
//             'content-type': 'application/json'
//         },
//         body: JSON.stringify(payment)
//     });

//      const data = await response.json();
//      console.log(data)

// }

// noxPay()

// Get Payment Info
// txid = '4382c207ef22435bb7348fe7d'
// async function noxPay() {
//     const response = await fetch(`https://testnetapigateway.herokuapp.com/api/payment/${txid}`, {
//         method: 'GET',
//         headers: {
//             'api-key': '12345678',
//             'content-type': 'application/json'
//         },

//     });

//     const data = await response.json();
//     console.log(data)

// }

// noxPay()

// // Cash In
// async function cashIn() {
//     const response = await fetch(`https://testnetapigateway.herokuapp.com/api/payment/pay/${txid}`, {
//         method: 'POST',
//         headers: {
//             'api-key': '12345678'
//             // 'content-type': 'application/json'
//         }
//         // body: JSON.stringify(payment)
        
//     });

//     // const data = await response.json();
//     console.log(response.status)

// }

// cashIn()

// CashOut
paymentOut = {
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

async function createPaymentOut() {
    const response = await fetch('https://testnetapigateway.herokuapp.com/api/payment', {
        method: 'POST',
        headers: {
            'api-key': '12345678',
            'content-type': 'application/json'
        },
        body: JSON.stringify(paymentOut)
    });

    //  const data = await response.json();
     console.log(response.status)

}

createPaymentOut()

// Pay Out
const txoutid = 0
async function cashOut() {
    const response = await fetch(`https://testnetapigateway.herokuapp.com/api/payment/pay/${txoutid}`, {
        method: 'POST',
        headers: {
            'api-key': '12345678',
            'content-type': 'application/json'
        }
        // body: JSON.stringify(payment)
        
    });

    // const data = await response.json();
    console.log(response.status)

}

cashOut()

checkAccount()

