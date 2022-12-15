"""
    curl -X POST \
        -H 'X-Signature: fJ7Vy72eyUr5F4amcXHnFV5Cg5j+IF0hiM/h6ESAkjg=' \
        -H 'Content-Type: application/json' \
        --data "@webhook_example.json" \
        http://localhost:8080/webhook_endpoint
    """

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
f = open('webhook_example/config.json')

# returns JSON object as a dictionary
data = json.load(f)
signature_key = data['SIGNATURE_KEY']


# Loading Data
with open('webhook_example/webhook_example.json') as f:
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
