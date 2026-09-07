from pathlib import Path
from flask import Flask,jsonify,request
from lxml import etree
app=Flask(__name__);Path("secret.txt").write_text("FLAG{xxe}")
def parse(resolve):
 p=etree.XMLParser(load_dtd=resolve,resolve_entities=resolve,no_network=True)
 return jsonify(text="".join(etree.fromstring(request.data,p).itertext()))
@app.post("/vuln")
def vuln():return parse(True)
@app.post("/fixed")
def fixed():return parse(False)
app.run(port=5000)

