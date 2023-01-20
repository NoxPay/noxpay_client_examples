// Código que simula o servidor

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

