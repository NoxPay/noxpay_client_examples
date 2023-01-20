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

