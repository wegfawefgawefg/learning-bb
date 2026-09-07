from flask import Flask, render_template_string, request

app = Flask(__name__)


@app.get("/vuln")
def vulnerable_search():
    query = request.args.get("q", "")
    return render_template_string(f"<h1>Results for</h1><p>{query}</p>")


@app.get("/fixed")
def fixed_search():
    query = request.args.get("q", "")
    return render_template_string("<h1>Results for</h1><p>{{ query }}</p>", query=query)


app.run(port=5000)
