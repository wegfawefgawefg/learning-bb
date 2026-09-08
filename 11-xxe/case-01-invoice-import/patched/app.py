from flask import Flask, jsonify, request
from lxml import etree

app = Flask(__name__)


@app.post("/api/invoices/import")
def load():
    root = etree.fromstring(
        request.data, etree.XMLParser(load_dtd=False, resolve_entities=False, no_network=True)
    )
    return jsonify(reference=root.findtext("reference"), amount=root.findtext("amount"))


app.run(port=5000)
