from flask import Flask, jsonify, request

app = Flask(__name__)
products = {"notebook": {"name": "Proxy Notebook", "price": 25}}


@app.get("/api/products/notebook")
def product():
    return jsonify(products["notebook"])


@app.post("/api/orders")
def order():
    data = request.get_json()
    return jsonify(
        order_id="ORD-100", item=data["item"], charged=data["unit_price"] * data.get("quantity", 1)
    )


app.run(port=5000)
