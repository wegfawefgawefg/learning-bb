from pathlib import Path
from flask import Flask, jsonify, request
from lxml import etree

app = Flask(__name__)
secret = Path(__file__).with_name("supplier-key.txt")
secret.write_text("FLAG{file_boundary}")


@app.post("/api/invoices/import")
def load():
    root = etree.fromstring(
        request.data, etree.XMLParser(load_dtd=True, resolve_entities=True, no_network=True)
    )
    return jsonify(reference=root.findtext("reference"), amount=root.findtext("amount"))


app.run(port=5000)
