from flask import Flask, jsonify, request

app = Flask(__name__)
logos = {"default": "ACME-LOGO", "compact": "ACME"}


@app.post("/api/invoices/logo/import")
def fetch():
    logo = logos.get(request.get_json().get("logo_id"))
    return jsonify(preview=logo) if logo else (jsonify(error="unknown logo"), 400)


app.run(port=5000)
