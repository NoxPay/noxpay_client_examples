// ====== IMPORTS ====== //   

import { v4 as uuidv4 } from 'uuid';
import * as dotenv from 'dotenv'
dotenv.config()

// ====== VARIABLES ====== //   

const signatureKey = process.env.API_KEY_CLIENT
// console.log(signatureKey)

const custid = uuidv4();

const custdata = {
    "name": `Usuario-${custid}`,
    "document": `${custid}`,
    "document_type": "CPF"
}

// ====== FUNCTIONS ====== //   

// Checking APIKEY //

async function checkAPIKEY() {
    const response = await fetch('https://testnetapigateway.herokuapp.com/test-auth', {
        headers: {
            'api-key': signatureKey
        }
    });
    const data = await response.json();

    console.log(data);
}

// Creating customer

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

// Getting customer data

async function getCustomer() {


    console.log('Getting Customer Data')

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

// Updating customer data

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

    console.log(response)
    const data = await response.json();
    console.log(data);

}

// Creating new Payment

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


// Get Payment Info

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

// Cash In

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

// Pix Out

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
// ====== MAIN ====== //   

// Uncomment the functions that You want to run

// await createCustomer()
// await getCustomer()

// const txid = await createPaymentIn()
// await getPaymentInfo(txid)
// await cashIn(txid)

// const txoutid = await createPaymentOut()

