from flask import Flask, request, render_template_string

app = Flask(__name__)


@app.get("/vuln")
def vuln():
    return render_template_string("Hello " + request.args.get("name", ""))


@app.get("/fixed")
def fixed():
    return render_template_string("Hello {{name}}", name=request.args.get("name", ""))


app.run(port=5000)
