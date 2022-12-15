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
