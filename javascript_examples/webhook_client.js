// const fetch = require('node-fetch');

const { createHmac } = await import('node:crypto');

const signatureKey = '1234567';
function simpleSign (text, key) {
    const hash = createHmac('sha256', key)
               .update(text)
               .digest('hex');
    // console.log(hash);
    return hash;
}

import file from './webhook_example.json' assert { type: 'json' };
console.log(file);
console.log(JSON.stringify(file))

const hash = simpleSign(JSON.stringify(file), signatureKey)
console.log(hash)

async function send_data(file, signature) {
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
    // .then(response => {
    //     console.log(response)
    // })
    const data = await response.json();
    console.log(data)
}

// fetch('./webhook_example.json')
//     .then((response) => response.json())
//     .then((json) => console.log(json));


send_data(file, hash);

