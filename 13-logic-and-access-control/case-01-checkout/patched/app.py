from flask import Flask, jsonify, request

app = Flask(__name__)
products = {"notebook": {"name": "Proxy Notebook", "price": 25}}


@app.post("/api/orders")
def order():
    data = request.get_json()
    quantity = data.get("quantity", 1)
    if not isinstance(quantity, int) or not 1 <= quantity <= 10:
        return jsonify(error="quantity"), 400
    product = products.get(data["item"])
    return (
        jsonify(order_id="ORD-100", item=data["item"], charged=product["price"] * quantity)
        if product
        else (jsonify(error="item"), 400)
    )


app.run(port=5000)
